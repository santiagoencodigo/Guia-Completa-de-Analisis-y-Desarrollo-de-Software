# Definición de clases.

class Perro:
    def sonido(self):
        print("wofff wofff")

class Gato:
    def sonido(self):
        print("Miauuuuuuuuuuu")

class Vaca:
    def sonido(self):
        print("Muuuuuuuuuuu")

# Función que recibe una lista de objetos
# y llama al método "sonido" de cada uno
def a_cantar(animales):
    for animal in animales:
        animal.sonido()  # aquí ocurre el polimorfismo

# Punto de entrada del programa
if __name__ == '__main__':
    perro = Perro()
    gato = Gato()
    gato_2 = Gato()
    vaca = Vaca()
    perro_2 = Perro()

    # Lista con diferentes tipos de objetos
    granja = [perro, gato, vaca, gato_2, perro_2]

    # Ejecuta la función
    a_cantar(granja)