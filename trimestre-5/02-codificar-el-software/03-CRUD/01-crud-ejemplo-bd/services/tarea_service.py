from models.tarea import Tarea

class TareaService:
    def __init__(self, db):
        self.db = db

    # CREATE
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

    # READ (con JOINs)
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
        
        # Convertir a objetos Tarea para mantener consistencia
        tareas = []
        for r in resultados:
            tarea = Tarea(r[1], r[2], None, None, r[0])
            tarea.usuario_nombre = r[3]
            tarea.categoria_nombre = r[4]
            tareas.append(tarea)
        return tareas

    # UPDATE
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

    # DELETE
    def eliminar(self, id):
        cursor = self.db.get_cursor()
        sql = "DELETE FROM tareas WHERE id=%s"
        cursor.execute(sql, (id,))
        self.db.commit()
        print("Tarea eliminada correctamente")