from models.usuario import Usuario

class UsuarioService:
    def __init__(self, db):
        self.db = db
    
    # CREATE
    def crear_usuario(self, usuario: Usuario):
        cursor = self.db.get_cursor()
        cursor.execute(
            "INSERT INTO usuarios (nombre, email) VALUES (%s, %s)",
            (usuario.nombre, usuario.email)
        )
        self.db.commit()
        print("Usuario creado correctamente")
    
    # READ
    def obtener_usuario(self):
        cursor = self.db.get_cursor()
        cursor.execute("SELECT * FROM usuarios")
        datos = cursor.fetchall()
        
        usuarios = []
        for d in datos:
            usuarios.append(Usuario(d[1], d[2], d[0]))
        return usuarios
    
    # UPDATE
    def actualizar_usuario(self, usuario: Usuario):
        cursor = self.db.get_cursor()
        cursor.execute(
            "UPDATE usuarios SET nombre=%s, email=%s WHERE id=%s",
            (usuario.nombre, usuario.email, usuario.id)
        )
        self.db.commit()
        print("Usuario actualizado correctamente")
    
    # DELETE
    def eliminar_usuario(self, id):
        cursor = self.db.get_cursor()
        cursor.execute("DELETE FROM usuarios WHERE id=%s", (id,))
        self.db.commit()
        print("Usuario eliminado correctamente")