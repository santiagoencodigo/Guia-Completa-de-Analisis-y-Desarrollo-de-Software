#nombre/identificador de la clase
#class es palabra reservada
class Coche:
    """Docstring: Esta clase define el estado y el 
    comportamiento de un coche"""
    #atributos de clase
    ruedas=4
    #constructor
    def __init__(self, color, aceleracion):
        #atributos de instancia
        self.color= color
        self.acceleracion=aceleracion
        self.velocidad=0
    #métodos
    def acelera(self):
        self.velocidad=self.velocidad+self.aceleracion
    def frena(self):
        v=self.velocidad - self.aceleracion
        if v<0:
            v=0
        self.velocidad=v


        # 1. Crear objeto
        # mi_coche = Coche("rojo", 10)

        # 2. Hacer uso de funciones

        # mi_coche.acelera()
        # mi_coche.velocidad()


c1 = Coche('rojo', 20)
c2 = Coche('azul', 20)

print(c1.color) #rojo
print(c2.color) #azul

print(c1.ruedas) # Atributo de clase, resultado 4
print(c2.ruedas) # Atributo de clase, resultado 4

Coche.ruedas = 6 # Atributo de clase, resultado 6

print(c1.ruedas) # Atributo de clase, resultado 6
print(c2.ruedas) # Atributo de clase, resultado 6








class CocheVolador(Coche):
    ruedas = 6
    def __init__(self, color, aceleracion, esta_volando=False):
        # la función super(). Esta función devuelve un objeto 
        # temporal de la superclase que permite invocar a los métodos 
        # definidos en la misma.
        super().__init__(color, aceleracion)
        #se crea el atributo de instancia esta_volando solo para 
        # objetos de la clase CocheVolador.
        self.esta_volando = esta_volando

    def vuela(self):
        self.esta_volando = True

    def aterriza(self):
        self.esta_volando = False

c = Coche('azul', 10)
cv1 = CocheVolador('rojo', 60)

print(cv1.color) #resultado rojo
print(cv1.esta_volando) #resultado False

cv1.acelera()

print(cv1.velocidad) #resultado 60
print(CocheVolador.ruedas) #resultado 6
# print(c.esta_volando) #resultado Traceback (most recent call last)...