from config.db import Database
from services.usuario_service import UsuarioService
from services.tarea_service import TareaService
from services.categoria_service import CategoriaService
from models.usuario import Usuario
from models.tarea import Tarea
from models.categoria import Categoria

# =========================
# CRUD USUARIOS
# =========================
def menu_usuarios(service):
    while True:
        print("\n--- CRUD USUARIOS ---")
        print("1. Crear")
        print("2. Listar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Volver")
        op = input("Opción: ")
        
        if op == "1":
            nombre = input("Nombre: ")
            email = input("Email: ")
            service.crear_usuario(Usuario(nombre, email))
        elif op == "2":
            for u in service.obtener_usuario():
                print(u)
        elif op == "3":
            id = int(input("ID: "))
            nombre = input("Nuevo nombre: ")
            email = input("Nuevo email: ")
            service.actualizar_usuario(Usuario(nombre, email, id))
        elif op == "4":
            id = int(input("ID: "))
            service.eliminar_usuario(id)
        elif op == "5":
            break

# =========================
# CRUD CATEGORÍAS
# =========================
def menu_categorias(service):
    while True:
        print("\n--- CRUD CATEGORÍAS ---")
        print("1. Crear")
        print("2. Listar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Volver")
        op = input("Opción: ")
        
        if op == "1":
            nombre = input("Nombre: ")
            service.crear(Categoria(nombre))
        elif op == "2":
            for c in service.listar():
                print(c)
        elif op == "3":
            id = int(input("ID: "))
            nombre = input("Nuevo nombre: ")
            service.actualizar(Categoria(nombre, id))
        elif op == "4":
            id = int(input("ID: "))
            service.eliminar(id)
        elif op == "5":
            break

# =========================
# CRUD TAREAS
# =========================
def menu_tareas(service):
    while True:
        print("\n--- CRUD TAREAS ---")
        print("1. Crear")
        print("2. Listar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Volver")
        op = input("Opción: ")
        
        if op == "1":
            titulo = input("Título: ")
            descripcion = input("Descripción: ")
            usuario_id = int(input("ID Usuario: "))
            categoria_id = int(input("ID Categoría: "))
            service.crear(Tarea(titulo, descripcion, usuario_id, categoria_id))
        elif op == "2":
            for t in service.listar():
                print(t)
        elif op == "3":
            id = int(input("ID tarea: "))
            titulo = input("Nuevo título: ")
            descripcion = input("Nueva descripción: ")
            usuario_id = int(input("Nuevo ID usuario: "))
            categoria_id = int(input("Nuevo ID categoría: "))
            service.actualizar(Tarea(titulo, descripcion, usuario_id, categoria_id, id))
        elif op == "4":
            id = int(input("ID tarea: "))
            service.eliminar(id)
        elif op == "5":
            break

# =========================
# MAIN GENERAL
# =========================
def main():
    db = Database()
    db.connect()
    usuario_service = UsuarioService(db)
    tarea_service = TareaService(db)
    categoria_service = CategoriaService(db)
    
    while True:
        print("\n=== SISTEMA CRUD COMPLETO ===")
        print("1. Usuarios")
        print("2. Tareas")
        print("3. Categorías")
        print("4. Salir")
        op = input("Opción: ")
        
        if op == "1":
            menu_usuarios(usuario_service)
        elif op == "2":
            menu_tareas(tarea_service)
        elif op == "3":
            menu_categorias(categoria_service)
        elif op == "4":
            db.close()
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()