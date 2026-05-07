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
