from models.categoria import Categoria

class CategoriaService:
    def __init__(self, db):
        self.db = db
    
    # CREATE
    def crear(self, categoria: Categoria):
        cursor = self.db.get_cursor()
        cursor.execute(
            "INSERT INTO categorias (nombre) VALUES (%s)",
            (categoria.nombre,)
        )
        self.db.commit()
        print("Categoría creada correctamente")
    
    # READ
    def listar(self):
        cursor = self.db.get_cursor()
        cursor.execute("SELECT * FROM categorias")
        datos = cursor.fetchall()
        
        categorias = []
        for d in datos:
            categorias.append(Categoria(d[1], d[0]))
        return categorias
    
    # UPDATE
    def actualizar(self, categoria: Categoria):
        cursor = self.db.get_cursor()
        cursor.execute(
            "UPDATE categorias SET nombre=%s WHERE id=%s",
            (categoria.nombre, categoria.id)
        )
        self.db.commit()
        print("Categoría actualizada correctamente")
    
    # DELETE
    def eliminar(self, id):
        cursor = self.db.get_cursor()
        cursor.execute("DELETE FROM categorias WHERE id=%s", (id,))
        self.db.commit()
        print("Categoría eliminada correctamente")