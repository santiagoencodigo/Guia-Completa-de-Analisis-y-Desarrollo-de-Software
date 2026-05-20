# Sesión 4

> Clase del 30/04/2026

> A medida del tiempo aprender en este curso ha sido bastante interesante. 

El día de hoy continuaremos entonces con bucles.

> A continuación mis apuntes de 3.2 Sección 2 - Bucles en Python.

* Para finalizar bucles infinitos en un programa nosotros oprimimos las teclas control c o control break en algunas computadora, asi provocando una KeyboardInterrumpt y permitirá que el programa salga del bucle.

Entonces analicemos el siguente código:

```py
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
```

Veamos otro ejemplo:

```py
    # Un programa que lee una secuencia de números
    # y cuenta cuántos números son pares y cuántos son impares.
    # El programa termina cuando se ingresa un cero.

    odd_numbers = 0
    even_numbers = 0

    # Lee el primer número.
    number = int(input("Introduce un número o escribe 0 para detener: "))

    # 0 termina la ejecución.
    while number != 0:
        # Verificar si el número es impar.
        if number % 2 == 1:
            # Incrementar el contador de números impares odd_numbers.
            odd_numbers += 1
        else:
            # Incrementar el contador de números pares even_numbers.
            even_numbers += 1
        # Leer el siguiente número.
        number = int(input("Introduce un número o escribe 0 para detener: "))

    # Imprimir resultados.
    print("Conteo de números impares:", odd_numbers)
    print("Conteo de números pares:", even_numbers)
```

A continuación estos dos ejemplos de código hacen lo mismo respecto a funcionalidad

```py
    while number != 0:

    # Es equivalente a:

    while number:


    # Y la condición que verifica si un numero es impar:

    if number % 2 == 1:


    # Es equivalente a:

    if number % 2:
```

---

Ahora empleando una variable counter para salir de un bucle.

```py
    counter = 5
    while counter != 0:
        print("Dentro del bucle.", counter)
        counter -= 1
    print("Fuera del bucle.", counter)
```

* Es código esta destinado a imprimir la cadena "Dentro del bucle" y va guardando un valor en counter y una vez se halla cumplido la condición. Es decir que la variable counter halla llegado a 0.

> Recordemos que la legibilidad puede ser un factor más importante. El código debe estar listo para un nuevo programador.

---

Ahora continuaremos con un escenario.

    Un mago junior ha elegido un número secreto. Lo ha escondido en una variable llamada secret_number. Quiere que todos los que ejecutan su programa jueguen el juego Adivina el número secreto, y adivina qué número ha elegido para ellos. ¡Quiénes no adivinen el número quedarán atrapados en un bucle sin fin para siempre! Desafortunadamente, él no sabe cómo completar el código.

Entonces, ¿Qué se debe hacer?

> Todavia no lo haré, pero es sencillo ya que es asignarle una variable a un número y mientras el input no sea igual a esa variable, repetir el print sino felicitar al usuario y dejarlo libre.

El código:

    1. pedirá al usuario que ingrese un número entero;

    2. utilizará un bucle while;

    3. comprobará si el número ingresado por el usuario es el mismo que el número escogido por el mago. Si el número elegido por el usuario es diferente al número secreto del mago, el usuario debería ver el mensaje "¡Ja, ja! ¡Estás atrapado en mi bucle!" y se le solicitará que ingrese un número nuevamente.

    4. Si el número ingresado por el usuario coincide con el número escogido por el mago, el número debe imprimirse en la pantalla, y el mago debe decir las siguientes palabras: "¡Bien hecho, muggle! Eres libre ahora."

>  Se pueden usar comillas triples para hacer un print de multiples líneas de código.

```py
    secret_number = 777

    print(
    """
    +================================+
    | ¡Bienvenido a mi juego, muggle!|
    | Introduce un número entero     |
    | y adivina qué número he        |
    | elegido para ti.               |
    |¿Cuál es el número secreto?     |
    +================================+
    """)
```

---


**Bucles en tu código con for**

Este es otro tipo de bucle en python en donde es importante contar los "giros" o "vueltas" del bucle para verificar las condiciones, como un bucle que debe ejecutarse exactamente 100 veces.

Esto en un ciclo while se veria algo asi:

```py
    i = 0
    while i < 100:
        # do_something()
        i += 1    
```

* FOR esta diseñado para realizar tareas más complicadas en donde explora grandes colecciones de datos

```py
    for i in range(100):
        # do_something()
        pass   
```

La palabra reservada **for**, no contiene condición despues de eso pues se verifican internamente sin ninguna intervención.

cualquier variable despues de la palabra reservada for es la variable de control del bucle, cuenta los giros y lo hace automaticamente.

La palabra reservada **in** describe un rango de valores en el cual se podrá hacer el bucle asignandoseles a una variable de control.

La función **range()** es responsable de generar todos los valores deseados de una variable de control. Pues alimentara nuestro bucle con números del 0 al número que se le asigne.

La palabra clave **pass** dentro del cuerpo del bucle no hace nada y es una instrucción vacia (Para saltar o pasar si no se hace o sucede algo.)

Observe el siguente còdigo:

```py
    # Este código se ejecutará 10 veces.

    # Algo a tener en cuenta es que este rango de 10, va realmente de 0 a 9.
    for i in range(10):
        print("El valor de i es", i)
```

Por otro lado nuestra función **range()** puede contener hasta dos argumentos

```py
    for i in range(2, 8):
        print("El valor de i es", i)
```

En donde el primer argumento determina el valor inicial de la variable de control, el ultimo argumento muestra el valor que no se le asignara a la variable de control.

* RANGE solo acepta enteros como argumentos

La función RANGE tambien puede aceptar tres argumentos, mira.

```py
    for i in range(2, 8, 3):
        print("El valor de i es", i)
```

El tercer argumento es un incremento el cual es un valor agregado para controlar la variable en cada giro del bucle en donde el valor de incrementado por defecto es 1.

Entonces teniendo un incremento de 5, saltandose el número ocho, lo que saldra en consola es:

```bash
    El valor de i es 2
    El valor de i es 5
```

Entonces:

* 2 (número inicial) → 5

* 2 incremento por 3 es igual a 5 

* el número está dentro del rango de 2 a 8 → 8 

* 5 incremento por 3 es igual a 8

* el número no está dentro del rango de 2 a 8, porque el parámetro de parada no está incluido en la secuencia de números generados por la función.

En el siguente ejemplo no hay output:

```py
    for i in range(1, 1):
        print("El valor de i es", i)
 ```

Los argumentos de RANGE deben organizarse de forma ascendente por lo que si es igual o menor no va a funcionar.

```py
    power = 1
    for expo in range(16):
        print("2 a la potencia de", expo, "es", power)
        power *= 2
```

* La variable expo se utiliza como una variable de control para el bucle e indica el valor actual del exponente.

--- 

**Sentencias break y continue**

Hemos tratado a un bucle como algo indivisible e inseparable de instrucciones que realizan completamente luego de cada giro. Sin embargo como desarrollador a veces no es necesario avanzar con un bucle en su totalidad.

Python proporciona dos instrucciones especiales para esto, pues simplifican el trabajo del desarrollador:

Estas dos instrucciones son (Dos palabras clave | Reservadas):

* break: Sale del bucle inmediatamente

* continue: Se comporta como si el programa ya hubiera llegado al final del cuerpo.

```py
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
```

---

Por otro lado, podemos usar la función .upper() para poner en mayusculas el texto.

Entonces por ejemplo:

```py
    user_word = user_word.upper()
```

---

El bucle while y el bucle else: Tanto el bucle while como for pueden tener la palabra reservada else

```py
    i = 1
    while i < 5:
        print(i)
        i += 1
    else:
        print("else:", i)
```

Se pide programar lo siguente:

    Escucha esta historia: Un niño y su padre, un programador de computadoras, juegan con bloques de madera. Están construyendo una pirámide.

    Su pirámide es un poco rara, ya que en realidad es una pared en forma de pirámide - es plana. La pirámide se apila de acuerdo con un principio simple: cada capa inferior contiene un bloque más que la capa superior.

    Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la altura de la pirámide que se puede construir utilizando estos bloques.

```py
    contador_filas = 0
    bloques_necesarios = 1

    cantidad_cajas = int(input("Ingrese la cantidad de cajas: "))

    while cantidad_cajas >= bloques_necesarios:
        cantidad_cajas -= bloques_necesarios
        contador_filas += 1
        bloques_necesarios += 1

    print("Altura de la pirámide:", contador_filas)
```

---

**Resumen de Sección**

* Un bucle while ejecuta una sentencia o un conjunto de sentencias siempre que se cumpla una condición booleana.

* Un bucle for ejecuta un conjunto de sentencias muchas veces, se usa para iterar sobre una secuencia como por ejemplo una lista, un diccionario, un conjunto u otros objetos iterables.

* Existen las sentencias break y continue para cambiar el flujo de un bucle (break para salir), (continue para omitir la iteración.)

* Los bucles while y for tambien pueden usar else.

* La función range genera una secuencia de números en donde acepta enteros y devuelve objetos de rango y tiene la siguente secuencia: 1. start: parametro que afirma inicio de secuencia, 2. stop: final de secuencia generada, 3. step: diferencia entre los números por secuencia.

---

**Quiz**

```py
    # Pregunta 1: Crea un bucle for que cuente de 0 a 10, e imprima números impares en la pantalla.

    for i in range(1, 11):
        # Línea de código.
            # Línea de código.


    
    # Pregunta 2: Crea un bucle while que cuente de 0 a 10, e imprima números impares en la pantalla.



    # Pregunta 3: Crea un programa con un bucle for y una sentencia break. El programa debe iterar sobre los caracteres en una dirección de correo electrónico, salir del bucle cuando llegue al símbolo @ e imprimir la parte antes de @ en una línea.

    for ch in "www.munetonsantiago@gmail.com":
    if ch == "@":
        # Línea de código.
    # Línea de código.

    
    
    # Pregunta 4: Crea un programa con un bucle for y una sentencia continue. El programa debe iterar sobre una cadena de dígitos, reemplazar cada 0 con x, e imprimir la cadena modificada en la pantalla. 
    


    # Pregunta 5: ¿Cuál es la output del siguiente código?

    n = 3
    
    while n > 0:
        print(n + 1)
        n -= 1
    else:
        print(n)
    


    # Pregunta 6: ¿Cuál es la output del siguiente código?

    n = range(4)
    
    for num in n:
        print(num - 1)
    else:
        print(num)
    


    # Pregunta 7: ¿Cuál es la output del siguiente código?

    for i in range(0, 6, 3):
        print(i)
```

> Aqui habria terminado entonces 3.2 - Sección 2 - Bucles en python.

---

> Aqui inicia 3.3 Sección 3 Operadores Lógicos y Operaciones bit a bit en Python.

> ¿Entiendes qué son tablas de verdad?

> ¿Entiendes qué es desplazamiento de bits?

> ¿Entiendes qué es operaciones bit a bit?

> ¿Sabes qué son Operadores Lógicos?

**Lógica de Computadoras**

Las condiciones que hemos usado hasta ahora han sido muy primitivas, las condiciones que utilizamos en la vida real son mucho más complejas. 

Pues piense en este enunciado: 

    'Si tenemos tiempo libre, y el clima es bueno, saldremos a caminar.'

Usamos entonces la conjunción and (y) lo que significa que salir a caminar depende de dos condiciones.

Podemos pensar tambien en el siguente enunciado:

    Si tu estás en el centro comercial o yo estoy en el centro comercial, uno de nosotros le comprará un regalo a mamá.

Entonces aqui usamos la palabra OR en donde para que esto ocurra debe suceder por lo menos una de las condiciones. A esto se le conoce como disyunción.

Python entonces tiene operadores para construir conjunciones y disyunciones pues sin estos el poder expresivo del lenguaje se debilitaria sustancialmente. Estos son operadores lógicos.

---

**Operador AND**

Es un operador binario con una prioridad inferior a la expresada por los operadores de comparación. Nos permite codificar condiciones complejas sin uso de parentesis como:

```py
    counter > 0 and value == 100
```

| A     | B     | A and B |
|-------|-------|---------|
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

**Operador OR** 

Es un operador binario con una prioridad más baja que and (al igual que + en comparación con *)

| A     | B     | A or B |
|-------|-------|--------|
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

**Operador NOT**

Es un operador unario que realiza la negación lógica, su funcionamiento es convertir lo falso en verdad y la verdad en lo falso

| A     | not A |
|-------|-------|
| True  | False |
| False | True  |

---

**Expresiones Lógicas**

```py
    # Ejemplo 1:
    print(var > 0)
    print(not (var <= 0))
    
    
    # Ejemplo 2:
    print(var != 0)
    print(not (var == 0))    
```

* La negación de una conjunción es la separación de las negaciones.

* La negación de una disyunción es la conjunción de las negaciones.

```py
    not (p and q) == (not p) or (not q)
    not (p or q) == (not p) and (not q)
```

---

**Valores Lógicos vs Bits Individuales**

Los operadores lógicos toman sus argumentos como un todo independientemente de cuantos bits contengan. Los operadores solo conocen el valor: *Ningún bit = 0 = False | Almenos un bit = 1 = True*

**Operadores bit a bit**

Hay cuatro operadores que permiten manipular bits de forma individual, denominados operadores bit a bit. Que estos mismos terminan cubriendo a todas las operaciones que mencionamos anteriormente solo que ya no tendriamos que escribir tal cual 'and', 'not' o 'or' Y además tenemos un operador adicional.

* *&* (ampersand) ‒ conjunción a nivel de bits

* *|* (barra vertical) - disyunción a nivel de bits

* *~* (tilde) - negación a nivel de bits

* *^* (signo de intercalación) - o exclusivo a nivel de bits (xor). (No se pueden cumplir las dos condiciones al mismo tiempo.)

> Se debe tener en cuenta que los argumentos entre operadores deben ser enteros.

Hay una diferencia importante entre los operadores lógicos y los de bit a bit: **Los operadores lógicos no penetran en nivel de bits de argumento.** Solo les interesa el valor final como tal.

Esto quiere decir que los operadores bit a bit son más estrictos, tratan con cada bit por separado. Por lo que si asumimos que una variable ocupa 64 bits, podemos pensar de una operación a nivel de bits como una evaluación de 64 de veces de un operador lógico para cada par de bits de los argumentos.

```py
    i = 15
    j = 22
```

Es equivalente a:

```bash
    i: 00000000000000000000000000001111
    j: 00000000000000000000000000010110
```

Lo que seria una conjunción lógica

```py
    log = i and j
    
    # La operación bit a bit seria:

    bit = i & j
```

Ahora veamos entonces operadores de negación:

```py
    # Primero el lógico:

    logneg = not i

    # La variable logneg se establecerá en False - no es necesario hacer nada más.




    # La negación a nivel de bits es así:

    bitneg = ~i 

```

---

Antes de continuar, ¿Entiende realmente qué es esto?

Las operaciones de bit (bitwise) son importantes porque permiten trabajar directamente con los bits (0 y 1) que componen los datos en un computador. Esto las hace muy eficientes, rápidas y fundamentales en muchos contextos de programación.

Operar a nivel de bits es más rápido que usar operaciones tradicionales, porque el procesador trabaja directamente en binario.

Se usan mucho en:

* sistemas embebidos

* videojuegos

* procesamiento de datos

> En vez de usar varias variables, usas un solo valor.

---

Si asumimos que los enteros se almacenan con 32 bits, la imagen a nivel de bits de las dos variables será la siguiente:

* i: 00000000000000000000000000001111

* j: 00000000000000000000000000010110