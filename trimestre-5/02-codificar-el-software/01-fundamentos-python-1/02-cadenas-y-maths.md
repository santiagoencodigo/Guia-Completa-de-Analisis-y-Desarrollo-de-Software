> Clase del 23/04/2026

## Sesión 2 - Codificar el Software - Fundamentos de Python 1

* Ahora ya finalizamos PE1: Módulo 1. Introducción a Python y a la Programación Informática.

* Ahora iniciamos PE1: Módulo 2. Tipos de Datos, Variables, Operaciones Básicas de Entrada y Salida, Operadores Básicos.

> 2.2.1 Literales - los datos en sí mismos

Ahora ya tenemos conocimientos sobre el uso de print. 

> Al parecer el print es con lo que uno deberia iniciar generalmente al momento de programar.

* Un literal es el que se da valor asi mismo como kmh = 64

Ya conocemos que es una cadena y qué es un número entero.

> Una computadora todo el tiempo esta haciendo operaciones matemáticas.

Para los números nosotros podemos pensar de dos formas:

* Enteros: No tienen parte fraccionaria

* Punto - Flotantes: Contienen partes fraccionarias

---

**Numeros Octales y Hexadecimales** 

Se habla de un uso de números en representación de un octal en donde si un número esta precedido por un "0o" El numero será tratado como valor octal. Esto quiere decir que tiene digitos en un rango de [0 ... 7]

Es como intentar:

```py
print(0o123)
```

La segunda convención nos permite utilizar números hexadecimales. Dichos números deben ser precedidos por el prefijo 0x por lo que:


```py
print(0x123)
```

---

**2.2.3 Flotantes**

Es el tipo de literales que estan designadas para representar y almacenar datos que no tienen parte decimal vacia. Tienen o pueden tener una parte fraccionaria despues del punto decimal.

Números como 2.5, -0.4 son números punto flotantes.

> Con . se determina el punto flotante.

> .4 = 0.4

> 4 = 4.0

* 4 Es un numero entero.

* 4.0 Es un numero flotante.

---

**Notación Cientifica**

Recordando la notación cientifica, por ejemplo la velocidad de la luz se escribe directamente: 300000000. Y para evitar escribir tantos ceros. Se utiliza de forma abreviada: '3 x 108.' *(tres por diez elevado a la octava potencia.)*

* Podemos usar la letra e como exponente por lo que:

```py
    print(3E8)
```

Ahora para seguir codificando flotante... ¿Cómo se expresa La constante de Planck? denotada como h. De acuerdo con los libros de texto tiene un valor de 6.62607 * 10 en exponente de -34

Si esto se quisiera programar seria:

```py
    print(6.62607E-34)
```

---

**Cadena**

Las cadenas requieren comillas : **" "**

```py
    print("Esto es una cadena")
```

Si se desea imprimir una cadena que tenga comillas por dentro tenemos que usar comillas simples '' o tambien se puede usar empleando la diagonal invertida **/**

```py
    print('Esto es una "cadena"')
    print("Estoy aprendiendo \"python"\"")
```

Ahora para mostrar un apóstrofe ' en una cadena, se puede hacer:

```py
    print('I\'m santiagoencodigo')
```

---

**2.2.5 Valores Booleanos**

Se emplean para representar un valor muy abstracto: **Veracidad**.

Cada vez que se le pregunta a python si un número es más grande que otro, el resultado es la creación de un tipo de dato muy especifico: Un valor booleano.

> El nombre proviene de George Boole(1815-1864) que es autor de las leyes del pensamiento, las cuales definen algebra Booleana. Una parte del algebra que hace uso de los valores: True y False denotados como: 1 y 0.

Un programador escribe un programa, y el programa hace preguntas. Python ejecuta el programa y provee las respuestas. El programa debe ser capaz de responder acorde a las respuestas recibidas.

Afortunadamente las computadoras entienden:

* Esto es verdad.

* Esto es falso.

> Nunca habrá una respuesta como no lo sé, probablemente sí, pero no estoy seguro.

Piense, ¿Cual será el resultado del siguente código?

```py
    print(True > False)
    print(True < False) 
```

Mire el siguente código:

```py
    print("\"I'm\"\n\"\"learning\"\"\n\"\"\"Python\"\"\"")  
```

---

* Finalizamos 2.2 Sección 2 - Literales en Python.

**2.3 Sección: Operadores - Herramienta de manipulación de datos**

> Ahora empiezo a mirar a cualquier lenguaje de scripts distinto. No habia reflexionado aun pese a usar JS y PY en el pasado... Todos los operadores funcionan bastante para la manipulación de datos en verdad.

> Podemos pensar de python como una calculadora.

```py
    print(2+2)
```

Hay una serie de operadores básicos:

* **+**: suma

* **-**: resta

* *: multiplicacion
 
* **/**: division

* **//**: Divisón Exacta

* **%**: MOD/Residuo

* **: Exponente

---

Exponenciación

```py
    print(2 ** 3)
    print(2 ** 3.)
    print(2. ** 3)
    print(2. ** 3.)
```

Multiplicación

```py
    print(2 * 3)
    print(2 * 3.)
    print(2. * 3)
    print(2. * 3.)
```

División

```py
    print(6 / 3)
    print(6 / 3.)
    print(6. / 3)
    print(6. / 3.)
```

División Entera

```py
    print(6 // 3)
    print(6 // 3.)
    print(6. // 3)
    print(6. // 3.)
```

Mod/Residuo

```py
    print(4 % 2)
```

Operaciones:

```py
    print(-4 - 4)
    print(4. - 8)
    print(-1.1)
```

* unario: un solo operador - +5

* binario contiene dos operadoreS - 5 + 4

> Por otro lado es importante recordar el uso de Operadores y Parentesis lo cual cambiara el orden.

---

> En este momento ya hemos terminado 3 secciones y vamos para la cuarta.

**Sección 4 - Variables**

> Es curioso preguntarse... pese a saberlo, qué es una variable, cómo usar una variable, qué reglas gobiernan una variable.

Se les conoce como cajas con forma de datos.

Python nos permite codificar literales las cuales contengan valores númericos y de cadenas.

Es normal pensar que en un programa siempre ocurren operaciones matemáticas. 

Ahora puede surgir una nueva pregunta: ¿Cómo se pueden almacenar los datos de estas operaciones, para poder emplearlas en más operaciones sucesivamente?

Python nos ayuda con eso, mediante cajas o contenedores especiales para ese propósito. El contenido de estos contenedores puede variar de casi cualquier forma.

Lo que compone una variable son principalmente dos cosas:

* Un nombre

* Un valor (Contenido del contenedor)

> Es de recordarse que las variables no aparecen de forma automática y que como desarrollador yo soy quien debe decidir cuantas variables deseo utilizar en mi programa.

¿Cómo nombrar una variable?

1. Puede contener: mayusculas, minusculas, dígitos, y el carácter _ 

2. El nombre de la variable debe iniciar con una letra.

3. El guion bajo es considerado una letra.

4. Tener cuidado con las mayusculas debido a que aunque sean la misma secuencia.

5. No hay limites con la longitud de la variable.

6. Es de recordar que el nombre de la variable no puede tener espacio, no puede iniciar con un caracter como ! ni con un número como 1..9

---

Para asignar una variable se puede:

Para crear una variable se le debe asignar un valor a algo.

* Insertar cualquier dato, este valor se puede variar tanto como se quiera.

Un ejemplo:

```py
    var = 1
    account_balance = 1000.0
    client_name = 'John Doe'
    print(var, account_balance, client_name)
    print(var)
```

---

> A continuación mis apuntes sobre: 2.4.6 Resolviendo problemas matemáticos simples.

En teoria ahora por los conocimientos de operadores, print y variables. Ahora tengo las habilidades para construir un programa que resuelva problemas matemáticos simples como el teoerema de pitágoras.

* El cuadrado de la hipotenusa es igual a la suma de los cuadrados de los catetos.

```py
    a = 3.0 
    b = 4.0
    c = (a ** 2 + b ** 2) ** 0.5
    print("c =", c)   
```

---

**2.4.7 - LAB - Variables Escenario**

A continuación una historia:

Érase una vez en la Tierra de las Manzanas, Juan tenía tres manzanas, María tenía cinco manzanas, y Adán tenía seis manzanas. Todos eran muy felices y vivieron por muchísimo tiempo. Fin de la Historia.

Tu tarea es:

1. Crear las variables: john, mary, y adam;

2. Asignar valores a las variables. El valor debe de ser igual al número de manzanas que cada quien tenía;

Una vez almacenados los números en las variables, imprimir las variables en una línea, y separar cada una de ellas con una coma;

Después se debe crear una nueva variable llamada total_apples y se debe igualar a la suma de las tres variables anteriores;

Imprime el valor almacenado en total_apples en la consola;

Experimenta con tu código: crea nuevas variables, asigna diferentes valores a ellas, y realiza varias operaciones aritméticas con ellas (por ejemplo, +, -, *, /, //, etc.).

Intenta poner una cadena con un entero juntos en la misma línea, por ejemplo, "Número total de manzanas:" y total_apples.

```py
    john = 3
    mary = 5
    adam = 6

    print(john, mary, adam, sep=',')

    total_apples = john + mary + adam
    print(total_apples)

    # peter = 12.5
    # suzy = 2
    # print(peter / suzy)
    # print("Total number of apples:", total_apples)
```

---

**2.4.8 Operadores Abreviados**

Hay operaciones como:

```py
    x = x * 2
```

python ofrece una forma más corta de escribirlo:

```py
    x *=2
```

Y por ende:

```py
    i = i + 2 * j
    
    # Es lo mismo que:

    i += 2 * j
```

o por otro lado:

```py
    var = var / 2

    # Es lo mismo que:

    var /= 2
```

o por otro lado:

```py
    rem = rem % 10

    # Es lo mismo que:

    rem = %= 10
```

> Se pide tener finalizado el curso de Fundamentos de python 1 para el siguente miercoles. (29 de Abril).

> El ultimo cuestionario no se realiza siendo Fundamentos de Python 1 (PE1) Examen Final del Curso y no se va a realizar Examen de Certificación PCEP - Certified Entry-Level Python Programmer.









