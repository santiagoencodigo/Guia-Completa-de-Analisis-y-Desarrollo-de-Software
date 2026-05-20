
# Sesión 3

> Clase del 29/04/2026 | Martes

> A continuación todos los ejercicios que se encuentren en esta sección de este documento markdown, se encontrarán en el documento 2-python-essentials-1.py dentro de la carpeta code.

---

**Variables**

* Se da una situación entonces:

Érase una vez en la Tierra de las Manzanas, John tenía tres manzanas, María tenía cinco manzanas, y Adán tenía seis manzanas. Todos eran muy felices y vivieron por muchísimo tiempo. Fin de la Historia.

* Se solicita lo siguente:

1. Crear las variables: john, mary, y adam;

2. Asignar valores a las variables. El valor debe de ser igual al número de manzanas que cada quien tenía;

3. Una vez almacenados los números en las variables, imprimir las variables en una línea, y separar cada una de ellas con una coma;

4. Después se debe crear una nueva variable llamada total_apples y se debe igualar a la suma de las tres variables anteriores;

5. Imprime el valor almacenado en total_apples en la consola;

6. Experimenta con tu código: crea nuevas variables, asigna diferentes valores a ellas, y realiza varias operaciones aritméticas con ellas (por ejemplo, +, -, *, /, //, etc.). Intenta poner una cadena con un entero juntos en la misma línea, por ejemplo, "Número total de manzanas:" y total_apples.

```py
    john = 3

    print("john tiene", john, "Manzanas")

    mary = 5

    print("mary tiene", mary, "Manzanas")

    adam = 6

    print("Adam tiene", adam, "Manzanas")

    print()

    print(f'La cantidad de manzanas totales entre nuestros tres personas es', john, "+", mary, "+", adam, "=", adam+john+mary)
```

---

**2.4.8 Operadores Abreviados**

Python ofrece soluciones para hacer más facil y rápida la programación por lo que

```python
    x = x * 2
```


Puede ser lo mismo que:

```python
    x *= 2
```

Siendo de esta forma, aplicable con cada una de las operaciones aritmeticas simples

```python
    x += 2
    
    x /= 2
    
    x %= 2

    x **= 2
```

---

**2.4.9 Variables: Un convertidor simple**

Se pide realizar el siguente ejercicio:

> Millas y kilómetros son unidades de longitud o distancia.

* Teniendo en mente que 1 milla equivale aproximadamente a 1.61 kilómetros, complementa el programa en el editor para que convierta de:

* Millas a kilómetros;
* Kilómetros a millas.

> Se da un consejo: Utilizar la función round() para el print() y asi entonces mostrar resultados hexadecimales

> Es interesante como es que dentro del curso se habla bastante de utilizar una SANDBOX para poner a prueba esto.

> Este mismo programa seria el que se utilizaria para hacer diferentes converciones como de temperaturas, USD a EUR.

> La busqueda de esto es implementar operadores y cadenas.

Por lo que:

> Este fue primer intento, aunque contiene errores y no es funcional.

```py
    # Lo primero que pienso es, ¿A cuanto vale un kilometro en metros?
    kilometro = 1000

    # millas = 1.61 kilometros
    millas = 1609


    print("- - - - -")
    print("Inicio de programa - Convertidor de km a millas y de millas a km.")
    print()

    operacion = prompt("Escriba 1 para convertir de KM a Millas, Escriba 2 para convertir de Millas a KM: ")

    print()

    if operacion==1:
        kilometros=prompt("Escriba el número de kilometros que desea convertir a millas: ")
        proceso1 = kilometros / 1.61
        print()
        print(kilometros, "kilómetros son", round(proceso1, 2), "millas")

    else if operacion==2:
        millas=prompt("Escriba el número de millas que desea convertir a km: ")
        proceso2 = millas * 1.61
        print()
        print(millas, "millas son", round(proceso2, 2), "kilómetros")
        
    else :
        print("Opción invalida, vuelve a intentarlo.")
        print("- - - - -")
        print("Fin programa.")
        print("- - - - -")
    
```

Solución:

```py
    kilometers = 12.25
    miles = 7.38

    miles_to_kilometers = miles * 1.61
    kilometers_to_miles = kilometers / 1.61

    print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
    print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")
```

---

Entonces una variable es un espacio de memoria reservada, tiene un identificador (No puede contener espacios, por lo que generalmente en los lenguajes de programación se hacen las diferentes tipos de notaciones como variable_nombre o variable-nombre o variableNombre, etc...), es creada e iniciada una vez se le asigna un valor.

Python es un lenguaje dinamico por lo que no se tiene que especificar que tipo de dato tiene la variable pues solamente se asigna el nombre, el signo = y el valor.

```py
    var = 1+2
```

Existen los operadores de asignación compuesta o tambien conocidos como operadores abreviados.

Por otro lado a las variables se les puede asignar nuevos valores como en:

```py
    var = 2
    print(var)
    var = 3
    print(var)
    var += 1
    print(var)
```

Por otro lado vimos tambien que se puede combinar texto y variables usando el operador +

> Ahora entiendo el problema de mi anterior script para el convertidor, no se usan " + " sino " , "

Y entonces se presentan las siguentes preguntas:

> No dejaré la respuesta, es buena idea intentarlo responder todo el tiempo que se vea para que refuerce la memoria, igualmente es sencillo.

```py
    # Preguntas de Cuestionario:

    # Pregunta 1: ¿Cuál es la salida del siguiente fragmento de código?
    var = 2
    var = 3
    print(var)

    # Pregunta 3: ¿Cuál es el resultado del siguiente fragmento?
    a = '1'
    b = "1"
    print(a + b)

    # Pregunta 4: ¿Cuál es el resultado del siguiente fragmento?
    a = 6
    b = 3
    a /= 2 * b
    print(a)
```

---

**Sección 5 - Comentarios**

> "Te compartiremos algunos comentarios sobre comentarios"

> Es realmente importante documentar el código.

Es importante dejar palabras que sean para otras personas y no para el lenguaje de programación como tal, con el fin de explicar como funciona o tal vez especificar ciertos elementos del código.

Se denomina comentario porque es omitido por el programa y es tomado como que no es parte del código. El comentario será un espacio vacio por más largo que llegue a ser.

Un ejemplo puede ser:

```py
    # Este programa evalúa la hipotenusa c.
    # a y b son las longitudes de los cátetos.
    a = 3.0
    b = 4.0
    c = (a ** 2 + b ** 2) ** 0.5  # Se emplea ** en lugar de una raíz cuadrada.
    print("c =", c)
```

> Los desarrolladores buenos describen cada pieza importante del código.

** Marcar fragmentos de código**

Otro uso que se le pueden dar a los comentarios es marcar pedazos de código que ya no se estan utilizando.

```py
    # Este es un programa de prueba.
    x = 1
    y = 2
    # y = y + x
    print(x + y)
```

> "Si deseas comentar o descomentar rápidamente varias línea(s) de código, selecciona las líneas que deseas modificar y utiliza el siguiente método abreviado de teclado: CTRL + / (Windows) or CMD + / (Mac OS). Es un truco muy útil, ¿no? Ahora experimenta con el código en el editor."

> Yo personalmente para los comentarios uso 'control + }'

* Es buena idea separar el código por pedazos y hacer comentarios por ejemplo: Separando por funciones.

> Por otro lado, recordé que en python no se usa la palabra prompt si no input (Estoy un poco acostumbrado a JS)

---

**2.6 Sección 6 - Interacción con el Usuario**

> Saber cómo hablarle a una computadora

Ahora además de print(), rounded() se introduce una nueva función: **input()**

Ahora... Pensando que print() envia datos a la consola, la importancia de la nueva función que vamos a ver regresa un valor utilizable por lo que es capaz de leer los datos que fueron introducidos en el programa.

> Un programa que no obtiene datos de entrada es un programa sordo

```py
    print("Dime lo que sea...")
    anything = input()
    print("Hmm...", anything, "... ¿en serio?")
```

Una función tipo input, no es necesario que tenga argumentos aunque puede tenerlos, y la función como tal pondrá la consola en modo entrada apareciendo un cursor que parpadea y todos los datos que se ingresen aqui antes de oprimir la tecla enter seran enviados al programa.

Estos datos tienen que ser asignados a una variable sino se perderan.

La función input() con argumentos es algo asi como...:

```py
    anything = input("Dime lo que sea...")
    print("Hmm...", anything, "...¿en serio?") 
```

Por lo que esta función es bastante importante pues simplifica el código.

* Es importante tener en cuenta que todo los datos que sean tomados de la función input es una cadena. Y no seran tomados como datos flotantes ni como enteros. Por ejemplo:

```py
    anything = input("Ingresa un número:")
    something = anything ** 2.0
    print(anything, "al cuadrado es", something)   
```

Debe salir algo asi como:

```bash
    Traceback (most recent call last):
    File ".main.py", line 4, in <module>
    something = anything ** 2.0
    TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'
```

> El mismo texto lo dice y menciona como se intento aplicar el operador ** a str - Esto esta prohibido.

¿Entonces qué se hace en estas situaciones?

Para esto tenemos los **Convertidores de Tipos** en donde python ofrece dos soluciones simples para especificar el tipo de datos.

Siento estos dos:

* **float()**: Toma un argumento e intenta convertirlo a un valor flotante o decimal.

* **int()**: Toma un argumento e intenta convertirlo a un valor entero. 

Un equipo de input(), int(), float() abre entonces nuevas posibilidades.

Eventualmente se tendrá la capacidad de escribir programas completos los cuales serán procesados y mostraran resultados. Por supuesto estos programas son muy primitivos y no muy utilizables debido a que no pueden tomar decisiones y aun no son capaces de actuar de acuerdo a la situación.

Mire el siguente código:

```py
    leg_a = float(input("Ingresa la longitud del primer cateto: "))
    leg_b = float(input("Ingresa la longitud del segundo cateto: "))
    hypo = (leg_a**2 + leg_b**2) ** .5
    print("La longitud de la hipotenusa es:", hypo)
```

> Este programa le preguntó al usuario los dos catetos, calcula la hipotenusa e imprime el resultado. Ejecútalo de nuevo e intenta introducir valores negativos.

---

**Operadores Cadena**

El signo + al ser aplicado en dos cadenas se convierte en un operadores de concatenación en donde:

'string + string'

Concatenar es la acción de juntar dos datos. Esto no es conmutativo debido a que no es lo mismo decir "ab" + "ba" a que "ba" + "ab"

```py
    fnam = input("¿Me puedes dar tu nombre por favor? ")
    lnam = input("¿Me puedes dar tu apellido por favor? ")
    print("Gracias. ")
    print("\nTu nombre es " + fnam + " " + lnam + ".")
```

Ahora por otro lado si el signo **" * "** (asterisco) cuando es aplicado a una cadena se convierte en un operador de replicación por lo que replica la cadena el numero de veces indicado por el numero.

Por ejemplo:

```py
    print("s a n t i a g o e n c o d i g o" * 5)

    print()    
    print()    
    print()    
    print()

    print("+" + 10 * "-" + "+")
    print(("|" + " " * 10 + "|\n") * 5, end="")
    print("+" + 10 * "-" + "+")
```

> Interesante la forma en la que se utilizo el segundo parentesis.

Hay otro tipo de conversión que esta vez ya es con una nueva función la cual seria: str()

> Se puede hacer mucho más que conversiones entre tipos de datos.

Volviendo a cómo hallar la hipotenusa:

```py
    leg_a = float(input("Ingresa la longitud del primer cateto: "))
    leg_b = float(input("Ingresa la longitud del segundo cateto: "))
    print("La longitud de la hipotenusa es " + str((leg_a**2 + leg_b**2) ** .5))
```

Como tal el resultado a esto será: 'La longitud de la hipotenusa es: 5.09313263312...'

* Como tal se paso el resultado entero a una función print como una sola cadena.

Hasta este momento entonces habremos comprendido tres nuevas cosas:

Tipos de datos básicos, conjunto de operadores fundamentales, organizar salida y cómo obtener datos del usuario

* Ya en este momento me siento con bastante retroalimentación respecto a python, hace bastante tiempo no lo habia vuelto a ver y se me habia olvidado algunas cosas.

> Debo tener cuidado con eos porque ya python lo habia manejado anteriormente, ahora entonces debo evitar que me suceda lo mismo con SQL. Que pese a que no es dificil volver a recordar la sintaxis... Pues es mejor mantener una practica constante con varios lenguajes.

```py
name = input("Ingresa tu nombre: ")
print("Hola, " + name + ". ¡Un gusto conocerte!")
```

* Cuando la función input() es llamada o invocada, el flujo del programa se detiene, el símbolo del cursor se mantiene parpadeando (le está indicando al usuario que tome acción ya que la consola está en modo de entrada) hasta que el usuario haya ingresado un dato y/o haya presionado la tecla Enter.

Ejemplo de uso de variables:

```py
    num_1 = input("Ingresa el primer número: ") # Ingresa 12
    num_2 = input("Ingresa el segundo número: ") # Ingresa 21
    
    print(num_1 + num_2) # El programa retorna 1221


    # Y si por otro lado? ....

    my_input = input("Ingresa algo: ") # Entrada de ejemplo: hola
    print(my_input * 3) # Salida Esperada: holahola
```

Hubo entonces otro cuestionario el cual los resultados serian:

```py
    # Pregunta 1: ¿Cuál es el resultado del siguiente fragmento?
    x = int(input("Ingresa un número: ")) # El usuario ingresa un 2
    print(x * "5")

    # Pregunta 2: ¿Cuál es el resultado esperado del siguiente fragmento?
    x = input("Ingresa un número: ") # El usuario ingresa un 2
    print(type(x))

```

Siendo asi, ahora finalizamos PE1: Módulo 2. Tipo de datos, variables, operaciones básicas de entrada y salida, operadores básicos.

---

A continuación entonces iniciamos con **PE1: Módulo 3. Valores Booleanos, Ejecución Condicional, Bucles, Listas y su Procesamiento, Operaciones Lógicas y de Bit a Bit**

> Hasta el momento ha sido muy interesante, al inicio pensaba que habia la posibilidad de que fuera a ser muy básico, pero a medida del tiempo me he dado de cuenta de que esta bastante funcional y realmente estoy aprendiendo nuevos elementos sobre python, fundamentos.

**Sección 3.1 - Cómo tomar decisiones en python**

A continuación estaremos aprendiendo sobre sentencias condicionales y cómo usarlas para la toma de decisiones en python.

Un programador escribe un programa y un programa hace preguntas.

Una computadora ejecuta el programa y proporciona las respuestas. Por lo que el programa debe ser capaz de reaccionar de acuerdo a esas respuestas.

Una computadora solo conoce dos respuestas: 
 
 * Si.
 
 * No.

> No se va a recibir nunca un "Dejeme pensar...", "No lo sé..." etc...

Para hacer preguntas, python utiliza un conjunto de operadores especiales.

Primero: **¿Son dos valores iguales?** para esta pregunta se utiliza **==**, (igual igual)

Entonces podemos pensar en:

* = es un operador de asignación.

* == es una pregunta en donde dice ¿Estos valores son iguales?. Necesita dos argumentos y verifica si son iguales.

Por lo que:

```py
2 == 2

# La respuesta será true.



2 == 2.

# Python puede convertir el valor entero en su equivalente real por lo que la respuesta es True.



1 == 2

# Es evidente que la respuesta es false.
```

Para saber su var == 0 debemos determinar primero cuanto es el valor de var

```py
    var = 0  # Asignando 0 a var
    print(var == 0)

    var = 1  # Asignando 1 a var
    print(var == 0)
```

---

**Desigualdad: Operador no es igual a (!=)**

El operador != compara dos valores, pero esta vez si estos valores son diferentes la respuesta sera true.

Como por ejemplo:

```py
    var = 0  # Asignando 0 a var
    print(var != 0)
    
    var = 1  # Asignando 1 a var
    print(var != 0)   
```

---

**Operador de Comparación: Mayor Qué (>)**

True confirma que un valor es mayor que otro.

Por lo que...

```py
black_sheep > white_sheep 

# La respuesta dependerá totalmente de los valores que tengan estas dos variables.
```

---

**Operadores de Comparación: Mayor o igual que**

Es una variante no estricta en donde hay dos signos subsecuentes en dodne ambos son operadores (Estrictos y no estrictos) 

Siendo asi:

> El siguente ejemplo podría ser muy importante para un sistema de radar

```py
    current_velocity_mph < 85  # Menor que
    current_velocity_mph <= 85  # Menor o igual que
```

---

Ahora finalmente, tenemos varias formas entonces de obtener información, comparar resultados ahora... ¿Cómo podriamos hacer uso de los resultados? 

> "Haciendo uso de las respuestas"

Existen dos posibilidades:

1. Se puede memorizar almacenando la información en una variable y utilizarla más tarde.

La variable arbitraria seria una como:

```py
respuesta = numero_leones >= numero_tigres
```

2. Esta posibilidad es más conveniente y mucho más común en donde se puede utilizar la respuesta que se obtenga para tomar una decisión sobre el futuro del programa.

Ahora entonces miremos nuestra tabla de prioridades:

| Prioridad | Operador | Notas |
| :---: | :--- | :--- |
| 1 | `+`, `-` | unario |
| 2 | `**` | |
| 3 | `*`, `/`, `//`, `%` | |
| 4 | `+`, `-` | binario |
| 5 | `<`, `<=`, `>`, `>=` | |
| 6 | `==`, `!=` | |

> Esta tabla consiste en qué, en una operación que contiene muchos operadores por dentro deben seguir entonces una jerarquia para hacer sus operaciones.

> Unario significa que depende del signo del numero.

> Binario quiere decir que la operación ocurre entre dos numeros

> El nivel más bajo de la tabla consiste en hacer igualdades o diferencias.

Ahora se pide realizar:

Usando uno de los operadores de comparación en Python, escribe un programa simple de dos líneas que tome el parámetro n como entrada, que es un entero, e imprime False si n es menor que 100, y True if n es mayor o igual que 100.

```py
    # Mi respuesta fue: (Exacta a la que se muestra en el curso.)
    n = int(input("Inserte un número"))
    booleano = n >= 100
    print(booleano)
```

---

**Condicionales y Ejecución Condicional**

> Ya se sabe cómo hacer preguntas a python.

Ahora, surge una nueva pregunta: ¿Cómo hacer uso razonable de las respuestas? se debe tener un mecanismo que permita hacer algo si una condición se cumple y si no se cumple no hacerlo.

* Es como pensar en donde si de acuerdo a la lluvia decides salir o no. Podriamos pensar de esto como un booleano y de acuerdo a la respuesta saldremos o no.

Para esto, python ofrece una solución especial que se denomina intrucción condicional o sentencia condicional

Pensemos de esto como:

    if true_or_not:
        do_this_if_true

Entonces tenemos la palabra reservada **IF** en donde con una expresión ya sea pregunta o respuesta podemos interpretarla como true o como false. Unos dos puntos despues de esta condición y finalmente con una sangria una serie de instrucciones o algoritmos. Como tal esta sangria se considera desde un tabulador o desde 4 espacios.

Es importante que todas las sangrias sean exactamente iguales.

* Si la expresión true_or_not representa la verdad (es decir, su valor no es igual a cero), las sentencias con sangría se ejecutarán;

* Si la expresión true_or_not no representa la verdad (es decir, su valor es igual a cero), las sentencias con sangría se omitirán

Esto podemos pensarlo como "Si el clima es bueno, saldré y despues almorzamos."

En otras palabras, las condiciones influyen a nuestro comportamiento.

Podemos tomar de ejemplo funciones que no tienen parametros como:

    if the_weather_is_good:
        go_for_a_walk()
    have_lunch()
    
Entonces nosotros podemos pensar que:

* Podemos pensar esto como que un desarrollador se duerme despues de haber contado 120 ovejas. En donde una vez cumpla la condición ejecutará la función de dormir.

```py
    if sheep_counter >= 120: # Evaluar una expresión condicional
        sleep_and_dream() # Ejecutar si la expresión condicional es verdadera
    
```

> Pienso que esa función descrita será lo que hará la diferencia eventualmente cuando se escriban funciones complejas.   

Es muy importante la sangria en python pues:

Analice el siguente ejemplo:

```py
    if sheep_counter >= 120:
        make_a_bed()
        take_a_shower()
        sleep_and_dream()
    feed_the_sheepdogs()
```

Hay una serie de acciones despues de contar cierta cantidad de ovejas, pero sin embargo el alimentar a los perros no pertenece al bloque if por lo que se ejecutará sin importar si se llegan a contar esa cantidad de ovejas.

---

Ahora tenemos una nueva condicional por presentar: **if-else** En donde, anteriormente nosotros ante un mal clima decidimos no salir, pero entonces ¿Qué podriamos hacer? Solo sabremos que no vamos a salir. Por ende tambien podimos haber planificado algo por hacer en tal caso del mal clima.

Entonces: Si el clima es bueno saldré, sino es asi voy a ver programar en python.

Siendo asi, ahora nosotros sabemos qué sucederá si se cumplen alguna de estas condiciones. En otras palabras "Tendriamos un plan B"

Observe entonces, el siguente pedazo de codigo:

```py
    if true_or_false_condition:
        perform_if_condition_true
    else:
        perform_if_condition_false   
```

Por lo tanto else termina siendo una nueva palabra reservada.

Por lo que tenemos dos opciones:

```py
    if the_weather_is_good:
        go_for_a_walk()
    else:
        go_to_a_theater()
    have_lunch()
    
```

* Si el clima es bueno, saldremos a caminar. De lo contrario, iremos al cine. Y sin importar las condiciones iremos a almorzar.

---

Ahora a continuación Sentencias if-else anidadas

Lee lo que hemos planeado para este Domingo. Si hay buen clima, saldremos a caminar. Si encontramos un buen restaurante, almorzaremos allí. De lo contrario, vamos a comer un sandwich. Si hay mal clima, iremos al cine. Si no hay boletos, iremos de compras al centro comercial más cercano.

```py
if the_weather_is_good:
    if nice_restaurant_is_found:
        have_lunch()
    else:
        eat_a_sandwich()
else:
    if tickets_are_available:
        go_to_the_theater()
    else:
        go_shopping()
```

Este uso de la condicional if se le conoce como anidamiento, debemos tener en cuenta que se debe mirar mucho los niveles de sangria.

---

**La sentencia ELIF**

> Ahora me di cuenta de confundí else if con elif para un ejercicio que fui a realizar.

Este es un caso especial, siendo una nueva palabra clave: **ELIF**

Se usa para verificar más de una condición:

si hay buen clima, saldremos a caminar, de lo contrario, si obtenemos entradas, iremos al cine, de lo contrario, si hay mesas libres en el restaurante, vamos a almorzar; si todo falla, regresaremos a casa y jugaremos ajedrez.

> Podemos pensar de estas palabras como "De lo contrario..."

```py
    if the_weather_is_good:
        go_for_a_walk()
    elif tickets_are_available:
        go_to_the_theater()
    elif table_is_available:
        go_for_lunch()
    else:
        play_chess_at_home()
```

Se le conoce como cascada a la secuencia if-elif-else.

Se debe tener en cuenta que no se puede usar else sin un if.

---

A continuación miraremos algunos programas simples pero completos.

Este por ejemplo: Encuentra el número mayor en una serie de números y lo imprimen.

```py
    # Se leen dos números
    number1 = int(input("Ingresa el primer número: "))
    number2 = int(input("Ingresa el segundo número: "))

    # Elige el número más grande
    if number1 > number2:
        larger_number = number1
    else:
        larger_number = number2

    # Imprime el resultado
    print("El número más grande es:", larger_number)
```

Aunque tambien podemos tener esta forma de organización:

```py
    # Se leen dos números
    number1 = int(input("Ingresa el primer número: "))
    number2 = int(input("Ingresa el segundo número: "))

    # Elige el número más grande
    if number1 > number2: larger_number = number1
    else: larger_number = number2

    # Imprime el resultado
    print("El número más grande es:", larger_number)
```

> Agradable. Pese a verse diferentes y la importancia de la sangria en python, respeto a funcionalidad y a uso de sintaxis esta exactamente igual.

Ahora, ¿Qué pasara si tratamos de comparar 3 numeros?

```py
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
```

---

**Pseudocódigo e introducción a los bucles**

Entonces ahora, debemos tener la capacidad de poder escribir un programa que sea capaz de comparar diez numeros incluso. Ya se conoce el esquema por lo que ampliar el tamaño del problema realmente no es tan complejo.

Ahora. **¿Qué pasaria si se te pide que escribas un programa que compare 200 numeros?** si 200 variables no son complicadas entonces imaginemos un millon.

Imagina un código que contiene 199 sentencias condicionales y doscientas invocaciones a la funión input()

---

Le pedi a gemini que: Haz un código de PYTHON que solamente con condicionales if-elif-else compare 200 numeros para determinar cual es el mayor y cual es el menor.

> gemini 3.1 pro

Respuesta:

Te seré muy honesto: hacer este ejercicio creando 200 variables individuales (n1, n2, n3... n200) y comparándolas a mano puramente con if-elif-else sin usar nada más requeriría escribir miles y miles de líneas de código. Sería un dolor de cabeza gigante, imposible de mantener y va en contra de la regla número uno de la programación: ¡no repetir código innecesariamente!

En el mundo real (y en Python), lo que hacemos para cumplir con tu regla de "solo usar condicionales para determinar el mayor y menor" (es decir, prohibido usar funciones trampa como max() o min()) es guardar esos 200 números en una lista y usar un ciclo for para que le pase los números uno por uno a nuestro bloque de if-elif-else.

Quise hacer la prueba con DEEPSEEK R1 esta vez pidiendole que ignorara que fuera una mala practica o que se pudiera hacer con bucle, que la hiciera igualmente sin importar las líneas de código y lanzo un código:

Algo similar a esto, pero 200 veces y no 10.

```py
    # Lista de 200 números de ejemplo
    numeros = [
        45, 23, 89, 12, 76, 34, 56, 90, 11, 67,
        33, 78, 44, 22, 99, 55, 21, 87, 65, 43,
        32, 68, 91, 10, 77, 54, 38, 29, 85, 46,
        61, 73, 19, 95, 30, 47, 81, 64, 28, 59,
        37, 96, 14, 83, 51, 72, 18, 94, 42, 71,
        27, 86, 53, 66, 35, 98, 13, 79, 50, 62,
        40, 97, 16, 82, 49, 70, 25, 84, 57, 69,
        31, 92, 15, 88, 41, 74, 26, 93, 48, 63,
        36, 100, 17, 80, 52, 75, 20, 99, 58, 60,
        39, 101, 24, 97, 44, 33, 77, 55, 22, 11,
        90, 56, 78, 34, 12, 89, 23, 45, 67, 76,
        43, 65, 87, 21, 54, 98, 46, 29, 85, 38,
        68, 32, 91, 10, 77, 54, 38, 29, 85, 46,
        61, 73, 19, 95, 30, 47, 81, 64, 28, 59,
        37, 96, 14, 83, 51, 72, 18, 94, 42, 71,
        27, 86, 53, 66, 35, 98, 13, 79, 50, 62,
        40, 97, 16, 82, 49, 70, 25, 84, 57, 69,
        31, 92, 15, 88, 41, 74, 26, 93, 48, 63,
        36, 100, 17, 80, 52, 75, 20, 99, 58, 60,
        39, 101, 24, 97, 44, 33, 77, 55, 22, 11
    ]  # Asegurar que tenga 200 números (aquí hay 200)

    # Inicializar mayor y menor con el primer número
    mayor = numeros[0]
    menor = numeros[0]

    # Comparar número por número usando solo if, elif, else
    # Número 1
    if numeros[1] > mayor:
        mayor = numeros[1]
    elif numeros[1] < menor:
        menor = numeros[1]
    else:
        pass

    # Número 2
    if numeros[2] > mayor:
        mayor = numeros[2]
    elif numeros[2] < menor:
        menor = numeros[2]
    else:
        pass

    # Número 3
    if numeros[3] > mayor:
        mayor = numeros[3]
    elif numeros[3] < menor:
        menor = numeros[3]
    else:
        pass

    # Número 4
    if numeros[4] > mayor:
        mayor = numeros[4]
    elif numeros[4] < menor:
        menor = numeros[4]
    else:
        pass

    # Número 5
    if numeros[5] > mayor:
        mayor = numeros[5]
    elif numeros[5] < menor:
        menor = numeros[5]
    else:
        pass

    # Número 6
    if numeros[6] > mayor:
        mayor = numeros[6]
    elif numeros[6] < menor:
        menor = numeros[6]
    else:
        pass

    # Número 7
    if numeros[7] > mayor:
        mayor = numeros[7]
    elif numeros[7] < menor:
        menor = numeros[7]
    else:
        pass

    # Número 8
    if numeros[8] > mayor:
        mayor = numeros[8]
    elif numeros[8] < menor:
        menor = numeros[8]
    else:
        pass

    # Número 9
    if numeros[9] > mayor:
        mayor = numeros[9]
    elif numeros[9] < menor:
        menor = numeros[9]
    else:
        pass

    # Número 10
    if numeros[10] > mayor:
        mayor = numeros[10]
    elif numeros[10] < menor:
        menor = numeros[10]
    else:
        pass
```

Hizo un total de 1600 líneas de código, esta termina siendo la importancia de los ciclos.

---

Por suerte uno no tiene que lidiar con eso.

> Ahora el enfoque será un poco pseudocodigo para todavia no tener que pensar en un lenguaje de programación

Por ahora:

```py
    largest_number = -999999999
    number = int(input())
    if number == -1:
        print(largest_number)
        exit()
    if number > largest_number:
        largest_number = number
    # Ir a la línea 02
```

El proposito de esto es para que el numero más grande, sea efectivamente el más grande para cualquiera de los numeros ingresados.

Nuestro algoritmo no sabrá realmente cuantos números se van a ingresar. Esperaremos a que el usuario entregue todos los numeros que llegue a desear.

El programa funcionara bien con cien, y con mil numeros ¿Cómo hacemos eso?

Haremos un trato con el usuario en donde si escribe -1 será una señal de que no hay más datos y que el programa debe finalizar.

De lo contrario, el programa seguirá leyendo los numeros y asi sucesivamente.

Python contiene muchas funciones integradas que hacen el trabajo por uno, como por ejemplo la función max() para verificar cual es el número más grande y se puede usar con multiples argumentos.

```py
    # Se leen tres números.
    number1 = int(input("Ingresa el primer número: "))
    number2 = int(input("Ingresa el segundo número: "))
    number3 = int(input("Ingresa el tercer número: "))

    # Verifica cuál de los números es el mayor
    # y pásalo a la variable largest_number.

    largest_number = max(number1, number2, number3)

    # Imprime el resultado.
    print("El número más grande es:", largest_number)
```

Asi mismo tambien se puede usar min() para el más chiquito entre todos los argumentos

---

**Fundamentos de la Sentencia if-else**

Se plantea la situación:

Érase una vez una tierra de leche y miel - habitada por gente feliz y próspera. La gente pagaba impuestos, por supuesto - su felicidad tenía límites. El impuesto más importante, denominado Impuesto Personal de Ingresos (IPI, para abreviar) tenía que pagarse una vez al año y se evaluó utilizando la siguiente regla:

* si el ingreso del ciudadano no era superior a 85,528 pesos, el impuesto era igual al 18% del ingreso menos 556 pesos y 2 centavos (esta fue la llamada exención fiscal).

* si el ingreso era superior a esta cantidad, el impuesto era igual a 14,839 pesos y 2 centavos, más el 32% del excedente sobre 85,528 pesos.

Tarea: Escribir una calculadora de impuestos.

```py
salario = float(input("Introduce el ingreso anual: "))

if salario < 85528:
    moneda = salario * 0.18 - 556.02
else:
    moneda = (salario - 85528) * 0.32 + 14839.02

if moneda < 0.0:
    moneda = 0.0

moneda = round(moneda, 0)
print("El impuesto es:", moneda, "pesos")
 
```

Calculo Año bisiesto:

```py
    year = int(input("Introduce un año: "))

    if year < 1582:
        print("No esta dentro del período del calendario Gregoriano")
    else:
        if year % 4 != 0:
            print("Año Común")
        elif year % 100 != 0:
            print("Año Bisiesto")
        elif year % 400 != 0:
            print("Año Común")
        else:
            print("Año Bisiesto")
```

> Se finalizo la sección 1 del modulo 3.

---

**Sección 2 - Bucles en Python**

Se aprenderá a usar ciclo while y for, evitar caer en bucles infinitos y omitir ciertas iteraciones en los bucles.

Podemos pensarlo como:

    mientras haya algo que hacer
        hazlo
    
> registro también declara que, si no hay nada que hacer, nada ocurrirá.

En python se veria algo asi como:

    while
        instruction

* la diferencia sintáctica es solo una: usa la palabra while en lugar de la palabra if.

* if realiza sus sentencias sólo una vez; while repite la ejecución siempre que la condición se evalúe como True.

Podemos pensarlo como:

    while conditional_expression:
        instruction_one
        instruction_two
        instruction_three
        :
        :
        instruction_n
 
* una instrucción o conjunto de instrucciones ejecutadas dentro del while se llama el cuerpo del bucle.

* Si la condición es false, no habrá bucle.

* Si la condición siempre es true, el bucle podría continuar hasta el infinito.

A continuación un ejemplo de un BUCLE SIN FIN.

```py
    while True:
        print("Estoy atrapado dentro de un bucle.")
```

---

