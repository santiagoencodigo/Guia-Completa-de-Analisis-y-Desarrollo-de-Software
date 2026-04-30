# Archivo creado el 22/04/2026
# santiagoencodigo
# Apuntes - Fundamentos de Python 1

print()
print()
print()









# |  Fundamentos de Python 1.  |


print(" - santiagoencodigo - \n - 3171608 - \n  - A D S O -  \n  - CDM - ")

print()

# Inicio de Menú

print("---")
print("  |  Menú - Fundamentos Python 1  | Sesión 3 ")
print("---")


print()
print()
print()
print()

# Lista de Ejercicios:

print()
print("Tercera Sesión")
print()

print("1. Ejercicio: Primera Aplicación de Variables")
print("2. Ejercicio: Conversión de KM a Millas")
print("3. Ejercicio: Mal uso de input | (Esta opción lanzara un error.3)")
print("4. Ejercicio: Calculo de hipotenusa.")
print("5. Ejercicio: Concatenación de Cadenas.")
print("6. Ejercicio: Replicación de Cadenas.")
print("7. Ejercicio: Uso de Función str().")
print("8. Ejercicio: Operación")
print("9. Ejercicio: Calculo de duración de tiempo.")
print('10. Ejercicio: print(x * "5")')
print('11. Ejercicio: Comparación entre 3 numeros mediante condicionales.')
print('12. Ejercicio: ESPATIFILIO o espatifilo - Uso de Condicionales.')








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
    print("Ejercicio 1. Primera Aplicación de Variables")

    john = 3

    print("john tiene", john, "Manzanas")

    mary = 5

    print("mary tiene", mary, "Manzanas")

    adam = 6

    print("Adam tiene", adam, "Manzanas")

    print()

    print(f'La cantidad de manzanas totales entre nuestros tres personas es', john, "+", mary, "+", adam, "=", adam+john+mary)





elif seleccion_pregunta == 2: 
    kilometers = 12.25
    miles = 7.38

    miles_to_kilometers = miles * 1.61
    kilometers_to_miles = kilometers / 1.61

    print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
    print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")

    print("A")

    x = int(input())
    y = int(input())

    x = x // y
    y = y // x

    print(y)







elif seleccion_pregunta == 3:
    anything = input("Ingresa un número:")
    something = anything ** 2.0
    print(anything, "al cuadrado es", something)





elif seleccion_pregunta == 4:

    leg_a = float(input("Ingresa la longitud del primer cateto: "))
    leg_b = float(input("Ingresa la longitud del segundo cateto: "))
    hypo = (leg_a**2 + leg_b**2) ** .5
    print("La longitud de la hipotenusa es:", hypo)



elif seleccion_pregunta == 5:

    fnam = input("¿Me puedes dar tu nombre por favor? ")
    lnam = input("¿Me puedes dar tu apellido por favor? ")
    print("Gracias. ")
    print("\nTu nombre es " + fnam + " " + lnam + ".")



elif seleccion_pregunta == 6:
    print("s a n t i a g o e n c o d i g o" * 15)

    print()
    print()
    print()
    print()
    print()
    print()
    print()

    print("+" + 10 * "-" + "+")
    print(("|" + " " * 10 + "|\n") * 5, end="")
    print("+" + 10 * "-" + "+")


elif seleccion_pregunta ==7:
    leg_a = float(input("Ingresa la longitud del primer cateto: "))
    leg_b = float(input("Ingresa la longitud del segundo cateto: "))
    print("La longitud de la hipotenusa es " + str((leg_a**2 + leg_b**2) ** .5))

elif seleccion_pregunta ==8:
    x = float(input("Ingresa el valor para x: "))
    y = 1./(x + 1./(x + 1./(x + 1./x)))
    print("y =", y)

elif seleccion_pregunta ==9:
    hour = int(input("Hora de inicio (horas): "))
    mins = int(input("Minuto de inicio (minutos): "))
    dura = int(input("Duración del evento (minutos): "))
    mins = mins + dura 
    hour = hour + mins // 60 # encuentra el número de horas ocultas en los minutos y actualiza las horas
    mins = mins % 60 # corrige los minutos para que estén en un rango de (0..59)
    hour = hour % 24 # corrige las horas para que estén en un rango de (0..23) 
    print(hour, ":", mins, sep='')

elif seleccion_pregunta==10:
    x = int(input("Ingresa un número: ")) # El usuario ingresa un 2

    # Como tal esto no es una operación matemática sino que python interpreta la linea de abajo como multiplicar la cadena de texto por 2.

    print(x * "5")
 
elif seleccion_pregunta==11:
    # Se leen tres números
    number1 = int(input("Ingresa el primer número: "))
    number2 = int(input("Ingresa el segundo número: "))
    number3 = int(input("Ingresa el tercer número: "))

    # Asumimos temporalmente que el primer número
    # es el más grande.
    # Lo verificaremos pronto.
    largest_number = number1

    # Comprobamos si el segundo número es más grande que el mayor número actual
    # y actualiza el número más grande si es necesario.
    if number2 > largest_number:
        largest_number = number2

    # Comprobamos si el tercer número es más grande que el mayor número actual
    # y actualiza el número más grande si es necesario.
    if number3 > largest_number:
        largest_number = number3

    # Imprime el resultado.
    print("El número más grande es:", largest_number)


elif seleccion_pregunta == 12:
    print("ESPATIFILIO o espatifilo")
    name = input("Introduce el nombre de la flor: ")

    if name == "ESPATIFILIO":
        print("Si, ¡El ESPATIFILIO es la mejor planta de todos los tiempos!")
    elif name == "espatifilo":
        print("No, ¡quiero un gran ESPATIFILIO!")
    else:
        print("¡ESPATIFILIO!, ¡No", name + "!")

else:
    print("a")