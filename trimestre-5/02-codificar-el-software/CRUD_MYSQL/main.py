from config.db import Database
from service.usuario_service import UsuarioService
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
    
if __name__ == "__main__":
    main()
