class A:
    def __init__(self):
        self._contador = 0  # Este atributo es privado
    def incrementa(self):
        self._contador += 1
    def cuenta(self):
        return self._contador

class B(object):
    def __init__(self):
        self.__contador = 0  # Este atributo es privado
    def incrementa(self):
        self.__contador += 1
    def cuenta(self):
        return self.__contador

# Pruebas con la clase A
a = A()
a.incrementa()
a.incrementa()
a.incrementa()
print(a.cuenta()) # #3
print(a._contador) # #3

# Pruebas con la clase B
b = B()
b.incrementa()
b.incrementa()
print(b.cuenta()) # #2
# print(b.__contador) # Traceback...AttributeError: 'B' object has no attribute '__contador'. Did you mean: '_B__contador'?
print(b._B__contador) # #2