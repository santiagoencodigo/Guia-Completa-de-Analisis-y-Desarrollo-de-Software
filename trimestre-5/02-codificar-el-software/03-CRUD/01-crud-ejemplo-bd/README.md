# CRUD

En esta sección se documenta el proceso de creación de un CRUD (Create, Read, Update y Delete) utilizando Python, aplicando conceptos fundamentales de desarrollo de software vistos durante el tecnólogo ADSO. Este documento funciona como una recopilación de apuntes personales y académicos elaborados durante el proceso de aprendizaje, reuniendo ejemplos, estructura del proyecto, manejo de datos, lógica de programación y buenas prácticas utilizadas durante el desarrollo, con el objetivo de reforzar conocimientos, servir como material de apoyo y facilitar la consulta de temas relacionados con Python y las operaciones CRUD dentro de un enfoque completamente educativo y formativo.


## Tabla de Contenido

[1. CRUD - Creación de Ejemplo BD](#1-crud---creación-de-ejemplo-bd)

[2. Complementación de ejemplo_bd: Entidad tareas](#2-complementación-de-ejemplo_bd-entidad-tareas)

> Clase del 6/05/2026 

## 1. CRUD - Creación de Ejemplo BD

Las siglas CRUD significan:

> Me emociona bastante iniciar en este tema despues de tanto tiempo y teniendo en cuenta que el anterior trimestre miramos algo de frontend, en este tambien estamos viendo y ahora que estamos viendo backend... Bien. Posiblemente dentro de poco veamos una interacción entre FRONTEND y BACKEND.

* CREATE

* READ

* UPDATE

* DELETE


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
















## 2. Complementación de ejemplo_bd: Entidad tareas

> Clase del 7/05/2026

Se pide escribir el siguente código SQL:

```sql
    CREATE TABLE tareas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        titulo VARCHAR(100),
        descripcion TEXT,
        usuario_id INT,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    );
```

Se pide en la carpeta models crear el archivo tarea.py y en la carpeta services/tarea_service.py

* **Arquitectura en Capas**: Separando por funciones.

* "Lo que fue con una tabla, asi será con la otra.": Tabla que existe, modelo que se crea. (Se crea dicho objeto.)

> Se recuerda que es importante el uso de mayusculas y minusculas (Sensitive Case)

Tenemos el tema del modelo, en donde tarea.py vamos a ingresar el código:

```py
    class Tarea:
        def __init__(self, titulo, descripcion, usuario_id, id=None):
            self.id = id
            self.titulo = titulo
            self.descripcion = descripcion
            self.usuario_id = usuario_id
        
        def __str__(self):
            return f"{self.id} - {self.titulo} (Usuario ID: {self.usuario_id})"

            # Este modelo tendrá dos funciones entonces: Constructor y el str.
```

Ahora a continuación viene la CRUD/Funciones que tendrá la tarea service en el archivo tarea service.

Será lo mismo o muy similar a lo que hicimos el dia de ayer, se importa de la carpeta modelos, el archivo tarea y la función Tarea, con su propio constructor el cual tendrá como parametros asi msimo y a la conexión con la base de datos.

Activa la conexión y empieza a responder ¿Qué vamos a hacer?

> Ahorita editaremos nuestro MAIN.PY para cuestiones de nuestro menú

```python
    from models.tarea import Tarea

    class TareaService:
        def __init__(self, db):
            self.db = db

        # CREATE
        def crear(self, tarea):
            cursor = self.db.get_cursor()
            cursor.execute(
                "INSERT INTO tareas (titulo, descripcion, usuario_id) VALUES (%s, %s, %s,)",
                (tarea.titulo, tarea.descripcion, tarea.usuario_id)
            )
            self.db.commit()

        # READ
        def listar(self):
            cursor = self.db.get_cursor()
            # Hacemos un JOIN aqui.
            cursor.execute("""
                SELECT t.id, t.titulo, t.descripcion, u.nombre
                FROM tareas t
                JOIN usuario u ON t.usuario_id = u.id
            """
            )
            return cursor.fetchall()

        # UPDATE
        def actualizar(self, tarea):
            cursor = self.db.get_cursor()
            cursor.execute(
                "UPDATE tareas SET titulo=%s, descripcion=%s, usuario_id=%s, WHERE id=%s",
                (tarea.titulo, tarea.descripcion, tarea.usuario_id, tarea.id)
            )
            self.db.commit()

        # DELETE
        def eliminar(self, id):
            cursor = self.db.get_cursor()
            cursor.execute("DELETE FROM tareas WHERE id=%s", (id,))
            # La , solamente se deja, para especificar que habra algo más.
            # Convencion: "Notacion se escribe asi"
            self.db.commit()
```

A continuación vamos a editar MAIN.PY de nuestra carpeta raiz.

Mantendremos nuestro config.db, e importaremos services.tarea y models.tarea agregandolos.

Por lo que:

> Se agrega la nueva función:

```py
# Adición del día 7/05/2026
def menu_tareas(service):
    while True:
        print("\n--- CRUD TAREAS ---")
        print("\n1. Crear tarea")
        print("\n2. Listar tareas")
        print("\n3. Actualizar tarea")
        print("\n4. Eliminar tarea")
        print("\n5. Volver")

        opcion = input("Opción:")

        if opcion == "1":
            titulo = input("Título: ")
            descripcion = input("Descripción: ")
            usuario_id = int(input("ID Usuario: "))
            service.crear(Tarea(titulo, descripcion, usuario_id))

        elif opcion == "2":
            tarea = service.listar()
            for t in tareas:
                print(f"{t[0]} | {t[1]} | {t[2]} | Usuario: {t[3]}")

        elif opcion == "3":
            id = int(input("ID tarea: "))
            titulo = input("Nuevo título: ")
            descripcion = input("Nueva descripción")
            usuario_id = int(input("Nuevo ID usuario: "))
            service.actualizar(Tarea(titulo, descripcion, usuario_id, id))

        elif opcion == "4":
            id = int(input("ID tarea a eliminar: "))
            service.eliminar(id)

        elif opcion == "5":
            break            
```

Y ahora entonces dentro de nuestro main.py vamos a editar nuestra función de main.

```python
    def main():
        # Se crea el objeto DB de la clase Database
        db = Database()
        # Se conecta a la base de datos
        db.connect()

        # service será otro objeto de la clase UsuarioService el cual enviara la variable db como parametro siendo la conexión
        usuario_service = UsuarioService(db)

        #Objeto para tarea service
        tarea_service = TareaService(db)

        # Este ciclo siempre será verdadero hasta que el usuario decida lo contrario
        while True:
            print()
            print("\n--- SISTEMA CRUD ---")
            print("1. Usuario")
            print("2. Tareas")
            print("3. Salir")


            opcion = input("Opción: ")

            # Código Original (Usuarios)
            if opcion == "1":

                while True:
                    print()
                    print("\n--- CRUD Usuarios ---")
                    print("\n1. Crear")
                    print("\n2. Listar")
                    print("\n3. Actualizar")
                    print("\n4. Eliminar")
                    print("\n5. Volver")

                    op = input("Opción:")

                    if op == "1":
                        # Se recoje | input
                        nombre = input("Nombre:")
                        email = input("Email:")
                        usuario = Usuario(nombre, email)

                        # Se invoca la función dandole los parametros
                        
                        usuario_service.crear_usuario(usuario)


                    if op == "2":
                        print()
                        usuarios = usuario_service.listar_usuario()

                        # Como es listar, hacemos un ciclo para imprimir todo el super arreglo. Pasandolo uno por uno.
                        # for u in usuario_service.listar():
                        for u in usuarios:
                            print(u)

                    if op == "3":
                        id = int(input("ID:"))
                        nombre = input("Nuevo Nombre:")
                        email = input("Nuevo email:")
                        usuario = Usuario(nombre, email, id)

                        # Versión Pasada: usuario_service.actualizar(Usuario(nombre, email, id))

                        usuario_service.actualizar_usuario(usuario)

                    if op == "4":
                        id = int(input("ID a eliminar:"))

                        # Versión Pasada: usuario_service.eliminar(id)

                        usuario_service.eliminar_usuario(id)

                    if op == "5":
                        break

            elif opcion == "2":
                menu_tareas(tarea_service)

            elif opcion == "3":
                db.close()
                break            
```

---

### Informe de Depuración y Corrección de Errores

Durante el desarrollo del CRUD en Python con MySQL se presentaron diferentes errores relacionados con constructores, métodos, consultas SQL y representación de objetos. Estos inconvenientes fueron solucionados mediante pruebas, revisión de código y apoyo complementario de herramientas de asistencia como ChatGPT, utilizadas como apoyo técnico y educativo durante el proceso de aprendizaje.

#### Problemas identificados y solucionados:

**Error en constructores (__init__)**

Se utilizó _init_ en lugar de __init__, lo que impedía que las clases recibieran parámetros correctamente.
Métodos inexistentes en servicios

Se intentaron ejecutar métodos como crear_usuario(), obtener_usuarios() y listar() que no existían o tenían nombres diferentes dentro de la clase UsuarioService.

**Representación incorrecta de objetos**

Los usuarios se imprimían como direcciones de memoria (<models.usuario.Usuario object at ...>) debido a que el método __str__() estaba escrito incorrectamente como _str_.

**Envío incorrecto de objetos a MySQL**

Se enviaba un objeto completo Usuario al método eliminar en lugar del ID, generando errores de conversión de tipos en MySQL.

**Errores de sintaxis SQL**

Se detectaron comas sobrantes en consultas INSERT y UPDATE, provocando errores de sintaxis en MariaDB/MySQL.
Tablas inexistentes en la base de datos

El sistema intentó consultar tablas que aún no habían sido creadas, como tareas, o tablas con nombres incorrectos como usuario en vez de usuarios.

**Problemas en consultas JOIN**

Durante el listado de tareas, el JOIN utilizaba un nombre de tabla incorrecto, afectando la relación entre usuarios y tareas.

**Inconsistencias en nombres de variables**

Algunas variables fueron declaradas con nombres diferentes (tarea y tareas), causando errores durante los ciclos de impresión.

**Conclusión**

El proceso de depuración permitió reforzar conocimientos relacionados con arquitectura en capas, conexión a bases de datos, consultas SQL y programación orientada a objetos en Python. Además, evidenció la importancia de mantener coherencia en nombres de métodos, clases, variables y estructuras SQL para garantizar el correcto funcionamiento del sistema CRUD.

---

Ahora se pide realizar de forma autonoma la integración de una tercera tabla llamada categorias y modificar nuestras actuales, por ende:

```sql
    CREATE TABLE categorias (
        id INT AUTO_INCREMENT
        PRIMARY KEY,
        nombre VARCHAR(100)
    );

    -- Modificar Nuestras Tablas

    ALTER TABLE tareas
    ADD categoria_id INT;
    ALTER TABLE tareas
    ADD FOREIGN KEY (categoria_id) REFERENCES categorias(id);    
```

Se pide entonces crear models/categoria.py e insertar el siguente código:

```python
    class Categoria:
        def __init__(self, nombre, id=None):
            self.id = id
            self.nombre = nombre

        def __str__(self):
            return f"{self.id} - {self.nombre}"
```

Se pide tambien crear service/categoria_service.py

```py
    from models.categoria import Categoria

    class CategoriaService:
        def __init__(self, db):
            self.db = db
        
        # CREATE
        def crear(self, categoria):
            cursor = self.db.get_cursor()
            cursor.execute(
                "INSERT INTO categorias (nombre) VALUES (%s)",
                (categoria.nombre,)
            )
            self.db.commit()
        
        # READ
        def listar(self):
            cursor = self.db.get_cursor()
            cursor.execute("SELECT * FROM categorias")
            return cursor.fetchall()
            # UPDATE
        def actualizar(self, categoria):
            cursor = self.db.get_cursor()
            cursor.execute(
            "UPDATE categorias SET nombre=%s WHERE id=%s",
            (categoria.nombre, categoria.id)
            )
            self.db.commit()
        
        # DELETE
        def eliminar(self, id):
            cursor = self.db.get_cursor()
            cursor.execute("DELETE FROM categorias WHERE id=%s", (id,))
            self.db.commit()
```

Se pide actualizar models/tarea.py con:

```py
    class Tarea:
        def __init__(self, titulo, descripcion, usuario_id,
        categoria_id, id=None):
            
            self.id = id
            self.titulo = titulo
            self.descripcion = descripcion
            self.usuario_id = usuario_id
            self.categoria_id = categoria_id #nuevo

        def __str__(self):
            return (
            f"ID: {self.id} | "
            f"Título: {self.titulo} | "
            f"Descripción: {self.descripcion} | "
            f"Usuario ID: {self.usuario_id} | "
            f"Categoría ID: {self.categoria_id}"
            ) 

    # Este modelo tendrá dos funciones entonces: Constructor y el str.
```

Y se pide actualizar service/tarea_service.py con:

```py
    from models.tarea import Tarea

    class TareaService:
        def __init__(self, db):
            self.db = db

        # =========================
        # CREATE
        # =========================
        def crear(self, tarea: Tarea):
            cursor = self.db.get_cursor()
            sql = """
            INSERT INTO tareas (titulo, descripcion, usuario_id, categoria_id)
            VALUES (%s, %s, %s, %s)
            """
            valores = (
                tarea.titulo,
                tarea.descripcion,
                tarea.usuario_id,
                tarea.categoria_id
            )
            cursor.execute(sql, valores)
            self.db.commit()
            print("Tarea creada correctamente")

        # =========================
        # READ (con JOINs)
        # =========================
        def listar(self):
            cursor = self.db.get_cursor()
            sql = """
            SELECT 
                t.id, 
                t.titulo, 
                t.descripcion, 
                u.nombre AS usuario, 
                c.nombre AS categoria
            FROM tareas t
            JOIN usuarios u ON t.usuario_id = u.id
            JOIN categorias c ON t.categoria_id = c.id
            """
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados

        # =========================
        # UPDATE
        # =========================
        def actualizar(self, tarea: Tarea):
            cursor = self.db.get_cursor()
            sql = """
            UPDATE tareas 
            SET titulo=%s, 
                descripcion=%s, 
                usuario_id=%s, 
                categoria_id=%s 
            WHERE id=%s
            """
            valores = (
                tarea.titulo,
                tarea.descripcion,
                tarea.usuario_id,
                tarea.categoria_id,
                tarea.id
            )
            cursor.execute(sql, valores)
            self.db.commit()
            print("Tarea actualizada correctamente")

        # =========================
        # DELETE
        # =========================
        def eliminar(self, id):
            cursor = self.db.get_cursor()
            sql = "DELETE FROM tareas WHERE id=%s"
            cursor.execute(sql, (id,))
            self.db.commit()
            print("Tarea eliminada correctamente")
```

Conclusiones:

    Se utilizaron clases para aplicar programación orientada a objetos, lo que permite
    organizar mejor el código, reutilizar componentes y separar responsabilidades.

    Separar en archivos mejora la escalabilidad y el mantenimiento del sistema,
    evitando código monolítico y facilitando futuras modificaciones.

    La arquitectura permite escalar fácilmente, por ejemplo agregando nuevas
    entidades, servicios o incluso migrando a una API sin afectar la lógica existente.
    
    En conclusión, este CRUD no solo cumple con las operaciones básicas, sino que
    también implementa buenas prácticas de desarrollo como separación de
    responsabilidades, uso de programación orientada a objetos y conexión estructurada
    a base de datos.