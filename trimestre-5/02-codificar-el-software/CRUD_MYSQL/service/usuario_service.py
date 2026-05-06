# Necesitamos importar del código de la carpeta models el archivo usuario y de ahí la clase Usuario
from models.usuario import Usuario

# Clase constructora UsuarioService
class UsuarioService:
    # Vemos en el parametro DB: Eso quiere decir que ahora va a esperar un parametro en nuestro objeto, esto para la interacción de la BD
    def __init__ (self, db):
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