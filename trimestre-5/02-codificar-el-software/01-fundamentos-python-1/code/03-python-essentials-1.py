# Archivo creado el 30/04/2026
# santiagoencodigo
# Apuntes - Fundamentos de Python 1

print()
print()
print()
print(
"""
+================================+
| Este es mi documento python    |
| Introduce un número entero     |
| y selecciona un ejercicio      |
|                                |
|¿Cuál eliges tú??               |
|                                |
|s a n t i a g o e n c o d i g o |
|                                |
+================================+
""")
print()
print()
print()









# |  Fundamentos de Python 1.  |


print("- 3171608 - \n  - A D S O -  \n  - CDM - ")

print()

# Inicio de Menú

print("---")
print("  |  Menú - Fundamentos Python 1 - Sesión 4 | ")
print("---")


print()
print()
print()
print()

# Lista de Ejercicios:

print()
print("Primera Sesión")
print()

print("1. Ejercicio: Bucle Infinito")
print("2. Ejercicio: The largest Number - Bucle infinito.")
print("3. Ejercicio: Contador para terminar bucle.")
print('4. Ejercicio: Ciclo for hecho con while, "¿En qué número vamos?"')
print('5. Ejercicio: Demostración RANGE() con 2 (dos) argumentos')
print('6. Ejercicio: Demostración RANGE() con (tres) argumentos')
print("7. Ejercicio: for expo in range(16)")
print("8. Ejercicio: break and continue en un bucle.")
print("9. Ejercicio: The largest number with break en un bucle.")
print("10. Ejercicio: The largest number with continue en un bucle.")
print("11. Ejercicio: Uso de ELSE en un ciclo.")
print("12. cantidad de cajas")






print()
print()
print()
print()

print("---")
print("Fin Menú")
print("---")

print()
print()
print()
print()

seleccion_pregunta = int(input("¿Qué número de ejercicio desea ver?: "))

# Fin de Menú.









# Ejercicios: De la clase del 22/04/2026

    # A continuación estos ejercicios son del 2.1.6 La función print() y su efecto, argumentos, y valores retornados





if seleccion_pregunta == 1:

    print()    
    print("1. Ejercicio: Bucle Infinito")
    
    while True:
        print("Estoy atrapado dentro de un bucle.")
        
        
        
elif seleccion_pregunta == 2:
    
    print()    
    print("2. Ejercicio: The largest Number")
    
    # Almacena el actual número más grande aquí.
    largest_number = -999999999

    # Ingresa el primer valor.
    number = int(input("Introduce un número o escribe -1 para detener: "))

    # Si el número no es igual a -1, continuaremos
    while number != -1:
        # ¿Es el número más grande que el valor de largest_number?
        if number > largest_number:
            # Sí si, se actualiza largest_number.
            largest_number = number
        # Ingresa el siguiente número.
        number = int(input("Introduce un número o escribe -1 para detener: "))

    # Imprime el número más grande.
    print("El número más grande es:", largest_number)


elif seleccion_pregunta ==3:
    while counter != 0:
        print("Dentro del bucle.", counter)
        counter -= 1
    print("Fuera del bucle.", counter)
    
elif seleccion_pregunta ==4:
    print("Seleccionaste un ejercicio que va a imprimir lo mismo 100 veces.")
    i = 0
    while i < 100:
        print("Ciclo for hecho con while, ¿En qué número vamos?")
        print(i)
        i += 1    
        
elif seleccion_pregunta ==5:
    for i in range(2, 8):
        print("El valor de i es", i)
        
elif seleccion_pregunta ==6:
    for i in range(2, 8, 3):
        print("El valor de i es", i)
        
elif seleccion_pregunta ==7:
    power = 1
    for expo in range(16):
        print("2 a la potencia de", expo, "es", power)
        power *= 2
        
elif seleccion_pregunta ==8:
    # break - ejemplo

    print("La instrucción break:")
    for i in range(1, 6):
        if i == 3:
            break
        print("Dentro del bucle.", i)
    print("Fuera del bucle.")


    # continue - ejemplo

    print("\nLa instrucción continue:")
    for i in range(1, 6):
        if i == 3:
            continue
        print("Dentro del bucle.", i)
    print("Fuera del bucle.")
    
elif seleccion_pregunta ==9:
    largest_number = -99999999
    counter = 0

    # Como while True, siempre se repetira y nunca va a parar. Solamente parara si el number = -1 por el break en la condicional.
    while True:
        number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
        if number == -1:
            break
        counter += 1
        if number > largest_number:
            largest_number = number

    if counter != 0:
        print("El número más grande es", largest_number)
    else:
        print("No has ingresado ningún número.")

elif seleccion_pregunta ==10:
    largest_number = -99999999
    counter = 0

    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

    while number != -1:
        if number == -1:
            continue
        counter += 1

        if number > largest_number:
            largest_number = number
        number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

    if counter:
        print("El número más grande es", largest_number)
    else:
        print("No has ingresado ningún número.")

elif seleccion_pregunta ==11:
    i = 1
    while i < 5:
        print(i)
        i += 1
    else:
        print("else:", i)
        
    print()
    print()
    print()
    
    print("Y si I valiera 5 desde un inicio?")
    
    i = 5
    while i < 5:
        print(i)
        i += 1
    else:
        print("else:", i)
        
    print()
    print()
    print()
    
    print("¿Y con un for?")  
    # Cuando el cuerpo del bucle no se ejecuta, la variable de control conserva el valor que tenía antes del bucle.      

        
    i = 111
    for i in range(2, 1):
        print(i)
    else:
        print("else:", i)

elif seleccion_pregunta ==12:
    contador_filas = 0
    bloques_necesarios = 1

    cantidad_cajas = int(input("Ingrese la cantidad de cajas: "))

    while cantidad_cajas >= bloques_necesarios:
        cantidad_cajas -= bloques_necesarios
        contador_filas += 1
        bloques_necesarios += 1

    print("Altura de la pirámide:", contador_filas)
    
    
elif seleccion_pregunta ==13:
    print("a")