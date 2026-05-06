# CRUD

> Clase del 6/05/2026 


CREATE
READE
UPDATE
DELETE

No vamos a usar frameworks en este momento.

Lo más importante es el codigo en si mismo

Vamos a hacer un CRUD que se conecte con MYSQL.


---

**Caso**

Este proyecto consiste en el desarrollo de un CRUD en Python conectado a una base de datos MySQL, sin interfaz gráfica, utilizando una arquitectura en capas.

El objetivo es gestionar la tabla usuarios mediante operaciones básicas: crear, leer, actualizar y eliminar registros desde consola.

Se utilizará MySQL como sistema gestor de base de datos. Se creará una base de datos llamada ejemplo_db* y una tabla usuarios con tres campos: id como clave primaria autoincremental, nombre y email.

El proyecto está organizado en una arquitectura por capas, separando responsabilidades para mejorar la mantenibilidad del código.

> Entre más separado el código, más escalable por que es más facil es.

Entonces se pide hacer este paso a paso-

En la terminal:

    mkdir CRUD_MYSQL

    cd CRUD_MYSQL

    touch main.py

    mkdir config - touch db.py

    mkdir models - touch usuario.py

    mkdir services - usuario_service.py 

Primero, como vamos a conectar python con MYSQL tenemos que instalar una dependencia.

Entonces hay que escribir el siguente comando en la terminal:

    Muchas veces en python toca instalar dependencias y dependencias.

    **pip install mysql-connector-python**

    Y si no funciona: **py -m pip install mysql-connector-python**

Y se pide insertar en phpmyadmin de XAMPP:

```sql
    CREATE DATABASE ejemplo_db;

    USE ejemplo_db;

    CREATE TABLE usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100),
        email VARCHAR(100)
    );
```

En el caso de python se tienen que descargar muchas instancias y librerias como tal, vamos a importar y en python escribimos en el archivo config/db.py:

```python
    # Importamos la dependencia de MYSQL
    import mysql.connector

    class Database:
        # Creamos nuestro constructor sin parametros
        def _init_(self):
            # Atributo con el valor none porque inicialmente no tiene nada.
            self.connection = None
        
        # Ahora creamos entonces nuestro metodo (Contexto de Clases)/funcion (Contexto General) connect de la clase Database
        # No tiene otros parametros más que si mismo.        
        # ¿Cual será la misión de este metodo? - Conectar la base de datos.
        def connect(self):
            # Conectamos esta función con nuestra importación de la dependencia
            self.connection = mysql.connector.connect(
                host="localhost", # Estamos en el equipo asi que sí, localhost.
                user="root", # user por defecto
                password="", # Comillas vacias porque no tenemos contraseña.
                database="ejemplo_db"
            )
            print("Conectado") # Si las cosas bien, vamos a imprimirlo!

        def get_cursor(self):
            return self.connection.cursor()

        # Para guardar.
        def commit(self):
            self.connection.commit()
                
        # Si ya terminé de hacer lo que tenia que hacer, esta función quitará la conexión con la BD.
        def close(self):
            self.connection.close
```

El archivo db.py se encarga exclusiamente de la conexión a la base de datos. Centraliza la configuración y permite reutilizar la conexión en todo el sistema.

> Cuando finalicemos esta primera parte.

Ahora vamos a modificar models/usuarios.py

```py
    # Como esto es una clase, tiene su constructor.
    # Pensemos en que cada registro en la tabla, será entonces un objeto.
    # Cada registro tendrá los mismos campos que nuestro objeto.
    class Usuario:
        # Cada uno de los datos van a viajar a estos parametros.
        def _init_ (self, nombre, email, id="None"):
            # Se van a almacenar en estas variables:
            self.id = id
            self.nombre = nombre
            self.email = email
        
        # Esta es una función especial, que se llama str o "string". 
        # Es importante para temas de impresión: id, nombre, email.
        # Ahora vamos a modelar la base de datos aqui:
        def _str_ (self):
            return f"{self.id} - {self.nombre} - {self.email}"
```

Ahora entonces vamos a la logica o acciones, como tal vamos a crear el servicio de la CRUD. Entonces toda la información que se guarden van a tomar acciones.

Entonces ahora vamos a editar services/usuario_service.py

```py
    # Necesitamos importar del código de la carpeta models el archivo usuario y de ahí la clase Usuario
    from models.usuario import Usuario

    # Clase constructora UsuarioService
    class UsuarioService:
        # Vemos en el parametro DB: Eso quiere decir que ahora va a esperar un parametro en nuestro objeto, esto para la interacción de la BD
        def _init_ (self, db):
            # Almacenamos el valor aqui:
            self.db = db
        
        # Como aqui estan las acciones que podrá hacer usuario, viene todo el CRUD. En donde el usuario se puede crear, eliminar y actualizar.

        # Iniciamos con el metodo crear.

        def crear(self, usuario): # Empieza a pedir parametro usuario
            # Esto va al constructor y busca el metodo get_cursor, esto viene de mysql y por ende de la importación que hicimos.
            cursor = self.db.get_cursor()
            # Al traer la función, va a ejecutar esta query:

            # Tenemos interacción con la BD desde el backend.
            cursor.execute(
                # %s significa: NO LO SÉ
                "INSERT INTO usuarios (nombre, email) VALUES (%s, %s)",
                # Nos representa estos valores:
                (usuario.nombre, usuario.email)
            )
            # Para guardar.
            self.db.commit()



        # Como no afecta la tabla por eso no tiene parametros
        def listar(self):
            # Me permite ir a la consulta
            cursor = self.db.get_cursor()

            # Ejecuta la query:
            cursor.execute("SELECT * FROM usuarios") 
            
            # La intención es ver la consulta completa
            # Entonces tenemos la variable datos
            # Tenemos la función fetchall() que trae toda la información y la guardará en datos. Esto es para imprimir registro por registro.

            # DATOS SERIA UN SUPER ARREGLO
            datos = cursor.fetchall()

            # Por esa razón nos creamos el array:
            usuarios = []
            # d no es importante, pudo ser cualquier cosa.
            # 
            for d in datos:
                # Esto agregará las filas:
                usuarios.append(Usuario(d[1], d[2], d[0]))
            # Va a retornar el arreglo que hizo uno por uno.
            # Esto mostraria en pantalla.
            return usuarios


        # Ahora para actualizar:
        def actualizar(self, usuario):
            cursor = self.db.get_cursor()
            cursor.execute(
                "UPDATE usuarios SET nombre=%s, email=%s WHERE id=%s",
                (usuario.nombre, usuario.email, usuario.id)
            )
            # Como es una actualización, que guarde.
            self.db.commit()


        # Ahora para eliminar usaremos el ID
        def eliminar(self, id):
            cursor = self.db.get_cursor()
            cursor.execute("DELETE FROM usuarios WHERE id=%s",(id,))
            self.db.commit()
```         

Ahora vamos a editar nuestro ARBITRO, será el que nos organiza todo y por ende a continuación editaremos main.py, archivo en nuestra carpeta raiz de CRUD_MYSQL

```py
    from config.db import Database
    from services.usuario_service import UsuarioService
    from models.usuario import Usuario

    def main():
        # Se crea el objeto DB de la clase Database
        db = Database()
        # Se conecta a la base de datos
        db.connect()

        # service será otro objeto de la clase UsuarioService el cual enviara la variable db como parametro siendo la conexión
        service = UsuarioService(db)

        # Este ciclo siempre será verdadero hasta que el usuario decida lo contrario
        while True:
            print("\n1. Crear")
            print("\n2. Listar")
            print("\n3. Actualizar")
            print("\n4. Eliminar")
            print("\n5. Salir")

            op = input("Opción:")

            if op == "1":
                # Se recoje | input
                nombre = input("Nombre:")
                email = input("Email:")

                # Se invoca la función dandole los parametros
                service.crear(Usuario(nombre, email))


            if op == "2":
                # Como es listar, hacemos un ciclo para imprimir todo el super arreglo. Pasandolo uno por uno.
                for u in service.listar():
                    print(u)

            if op == "3":
                id = int(input("ID:"))
                nombre = input("Nuevo Nombre:")
                email = input("Nuevo email:")
                service.actualizar(Usuario(nombre, email, id))

            if op == "4":
                id = int(input("ID:"))
                service.eliminar(id)

            if op == "5":
                db.close()
                break
        
        if _name_ == "_main_":
            main()

```

> La razón de los cursos es para no explicar los diferentes atributos.

Entonces ahora habremos finalizado la creación de nuestra CRUD

Entonces en teoria hicimos seguimiento a el siguente orden de reación:

1. Base de datos
2. Conexión (db.py)
3. Modelo (Usuario)
4. Servicio (CRUD)
6. Main (menú)

Alguno de los problemas que podrian presentarse:

* No crear la BD y por ende falló la conexión
* Mal password que podria que error de MYSQL
* Ejecutar fuera de la carpeta - error imports
* No instalar libreria - No module named mysql

---