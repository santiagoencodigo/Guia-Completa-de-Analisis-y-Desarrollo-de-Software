# Como esto es una clase, tiene su constructor.
# Pensemos en que cada registro en la tabla, será entonces un objeto.
# Cada registro tendrá los mismos campos que nuestro objeto. 
class Usuario:
    # Cada uno de los datos van a viajar a estos parametros.
    def __init__ (self, nombre, email, id="None"):
        # Se van a almacenar en estas variables:
        self.id = id
        self.nombre = nombre
        self.email = email
    
    # Esta es una función especial, que se llama str o "string". 
    # Es importante para temas de impresión: id, nombre, email.
    # Ahora vamos a modelar la base de datos aqui:
    def __str__ (self):
        return f"{self.id} - {self.nombre} - {self.email}"