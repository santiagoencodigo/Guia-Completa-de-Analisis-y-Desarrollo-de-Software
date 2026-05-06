
## Tabla de Contenido

[1. Sesión 1 - Inicio Fundamentos de Python 1](#primera-sesión---inicio-fundamentos-de-python-1)

[ 2. Sesión 2 - Codificar el Software - Fundamentos de Python 1](#sesión-2---codificar-el-software---fundamentos-de-python-1)

[3. Sesión 3](#3-sesión-3)

[4. Sesión 4](#sesión-4)

[5. Sesión 5 - ]()


---









> Clase del día 22/04/2026 (Miercoles) (Tercera Clase - Quinto Trimestre)

## Primera Sesión - Inicio Fundamentos de Python 1

Entregables:

* Conexion de BD

* CRUD

* Inicio de Sesion

* Backend con interfaz (frontend)

Nosotros vamos a ir por el camino de python: Vamos a ir en una ruta de aprendizaje enfocada a la web, utilizaremos VSCODE, python necesita una maquina virtual (¿Del propio lenguaje?) Es una interpretación en codigo maquina.

Debemos aprender otras funcionalidades de Xampp y aunque la p sea de php, vamos a utilizar python para este proyecto y xampp al mismo tiempo.

Nos presenta:

Codeium: Ai Coding Autocomplete and Chat for Python.

¿Qué es Windsurf Plugin?

Windsurf pyright?

---

> Se invita a aprovechar el tiempo en las clases.

**Entregables de aqui a 2 meses.**

* Haremos curso de python 1. 

* Haremos curso de python 2.

* Cuestionario de Python orientado al desarrollo de CRUD para Junio.

* Solicitud vs Entrega de SCRUM. (Entregables de acuerdo a los requisitos.)

* Entrega proyecto (Conexión a BD, CRUD, inicio sesión, descarga de archivos)

---

<img src="https://imgs.search.brave.com/v1r_2ujP29wZINhHP97e2uPIH93tW-BHaVYUEbvBg8w/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly93d3cu/dWNlbm1hbmNoZXN0/ZXIuYWMudWsvbWVk/aWEvZmlsZXJfcHVi/bGljX3RodW1ibmFp/bHMvZmlsZXJfcHVi/bGljLzI2L2JjLzI2/YmNiNzFkLTdmNWEt/NDRjZC1hY2NjLTUx/ZmNjZmZmNGJjMi9j/aXNjby1uZXR3b3Jr/aW5nLWFjYWRlbXkt/aGVhZGVyLWJhbm5l/ci5qcGdfXzEyOTh4/NDAzX3N1YmplY3Rf/bG9jYXRpb24tNjQ5/LDIwMV9zdWJzYW1w/bGluZy0yLndlYnA">

Vamos a usar a cisco networking academy como plataforma de aprendizaje cisco

https://www.netacad.com/

> Entonces se pide que desarrollemos el curso Fundamentos de Python 1 | Python Essentials 1

A continuación mis apuntes de Python Essentials 1 - Programa de Cisco Networking Academy

---

**PE1: Module 1. Introduction to Python and Computer Programming**

> Me parece curioso lo de "Python Institute | PI"

* Le dicen "Lenguaje de hoy y el de mañana."

* Diseñar, escribir, ejecutar, depurar y mejorar programas python a nivel básico.

> Prepara para el curso PCEP - Programador Python certificado nivel básico - Examen de certificación del instituto python.

* Fue desarrollado por: https://pythoninstitute.org/ en colaboración con la academia cisco.

> Soy parte del publico objetivo del curso.

Habran materiales de práctica, laboratorios, cuestionarios, evaluaciones, pruebas.

¿Qué se va a aprender?

Conceptos universales, sintaxis y semántica del lenguaje Python, utilizar elementos importantes de bibliotecas de python, instalar entorno de ejecución, diseño, desarrollo, probar y depurar programas python.

Se divide en:

1. **Modulo 1:** Introducción a python y programas de informática

2. **Modulo 2:** Tipos de datos, variables, operaciones básicas de entrada-salida y operadores básicos.

3. **Modulo 3:**: Valores booleanos, ejecución condicional, bucles, listas y procesamiento de listas, operaciones lógicas y bit a bit.

4. **Modulo 4:**: Funciones, tuplas, diccionarios, excepciones y procesamiento de datos.

Va a haber un examen PCEP-30x: https://pythoninstitute.org/pcep

> Tal vez esa sea la parte de pago que menciona la instructora.

<img src="https://imgs.search.brave.com/YJyxp1cdvFBL2TV4AanKRfPG9Ucdq918e-pKdntbtzs/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly90b29s/c3FhLmNvbS9nYWxs/ZXJ5L1B5dGhvbi8x/LnBjZXAuanBn">

---

**Section 1: Introduction to Programming**

Vamos a mirar conceptos clave de programación:

* Listas de Instrucciones

* Archivo fuente

* Elementos del Lenguaje

* Compilación e Interpretación

¿Cómo funciona un programa informático?

Un programa hace que una computadora sea funcionable. Un piano no es más que una caja de madera. Un ordenador aunque sea el más potente, es solo un objeto. Sin programa no funciona.

Una computadora solo puede ejecutar operaciones extremadamente simples, por lo que puede evaluar los resultados de operacion fundamentales, como sumar, restar, dividir y hacerlo muy rápido y repetir estas acciones practicamente cualquier numero de veces.

Si se le pide a una computadora saber la velocidad que se ha alcanzado durante un viaje largo:

La computadora no es consciente de cosas como la distancia, la velocidad o el tiempo.

Por lo tanto hay que indicarle a la computadora que acepte un numero que represente la distancia, otro numero que represente el tiempo de viaje, dividir el primer valor por el segundo y almacenar el resultado en la memoria, muestre el resultado en un formato legible.

Estas cuatro acciones forman un programa.

---

Lenguajes naturales vs lenguajes de programación

El lenguaje es un medio y herramienta para expresar y registrar pensamientos.

Hay muchos idiomas alrededor de nosotros pero alguno de ellos no se requieren hablar o escribir como el lenguaje corporal.

> Es posible expresarse con mucha precisión sin decir una palabra.

Las computadoras tienen su propio lenguaje - Codigo Maquina

Una computadora carece de algún rastro de inteligencia: "Es un perro bien entrenado" Responde a un conjunto predeterminado de ordenes conocidas.

Un conjunto completo de comandos se les conoce como lista de instrucciones.

Los diferentes tipos de computadora pueden variar de acuerdo al tamaño de su lista de instrucciones.

> El lenguaje maquina fue desarrollado por el ser humano.

* Actualmente ninguna computadora es capaz de crear un nuevo lenguaje. Sin embargo eso podria cambiar dentro de poco.

* El lenguaje del ser humano se desarrollo de forma natural.

* Se le conoce como lenguaje natural a las palabras nuevas que se crean y a las palabras viejas que se olvidan.

---

¿Qué hace que un lenguaje sea?

Contiene las siguentes caracteristicas:

1. Alfabeto: Conjunto de Simbolos

2. Lexis: Diccionario - Conjunto de palabras que el idioma ofrece.

3. Sintaxis: Conjunto de reglas formales o informales que determinan si una cadena de palabras forma una oración valida.

4. Semántica: Conjunto de reglas que determinan si una frase tiene sentido.

---

Lenguaje Maquina vs Lenguaje de Alto Nivel

El alfabeto de un lenguaje maquina, es el conjunto de simbolos que podemos usar para dar comandos a la computadora... Desafortunadamente esta lenguaje es diferente a la humana, por lo que necesitamos hacer un puente entre los dos lenguajes (Humano y Maquina).

El puente tiene que ser un lenguaje en el que los humanos puedan escribir sus programas, y que sea a su vez un lenguaje que las computadoras puedan ejecutar.

>Debe ser un lenguaje más complejo que lenguaje maquina y que sea lenguaje más simple que lenguaje natural.

Entre más similares al lenguaje natural es Lenguaje de Alto nivel.

Entre más similar al lenguaje maquina es Lenguaje de Bajo Nivel.

* Código Fuente.

* Archivo Fuente.

---

Compilación vs Interpretación

La programación informática es el acto de componer los elementos del lenguaje de programación seleccionado en el orden que provacará el efecto deseado.

Esto depende de la imaginación, el conocimiento y la experiencia del programador.

Por lo que debe ser una composición correcta en:

* alfabéticamente: escritura reconocible

* lexicalmente: cada lenguaje tiene su diccionario

* sintácticamente: reglas

* semánticamente: tiene sentido

Desafortunadamente un programador puede tener un problema con alguno de estos elementos. Cada uno de ellos puede provocar que el lenguaje sea inutil.

Afortunadamente la traducción puede ser realizada por el propio computador lo que hace que todo sea más rápido y eficiente.

Diferencias entre Compilación e Interpretación

<img src="https://www.netacad.com/authoring-resources/courses/c97034f8-d6b9-463c-a281-51d5ed1bd109/23b514e0-d2b4-5b19-8219-dc8952cbbcca/en-US/assets/651b38c773b0415eb31f87b048d13656.png">

Por razones fundamentales un lenguaje de alto nivel esta diseñado para caer en alguna de estas dos categorías.

Hay muy pocos idiomas que puedan compilarse e interpretarse.

---

¿Qué hace el intérprete? 

Suponiendo que ahora exista un archivo de computadora: En realidad un fragmento de texto. Es texto puro sin fuentes, colores, imagines inscrustadas u otros medios. El interprete lee el código fuente de una manera común en la cultura occidental: de arriba a abajo, y de izquierda a derecha. Aunque existen excepciones.

Si el compilador encuentra un error finaliza su trabajo y lanza un mensaje de error.

Capaz el interprete incluso avise donde fue el error, pero esto puede ser engañoso debido a que el interprete no puede seguir las intenciones del usuario programador.

---

Compilación: La ejecución del código es muy rápida, sólo el usuario debe tener el compilador, el usuario final puede usar su codigo sin el. El traducido se almacena en lenguaje maquina y como es dificil de entender puede que tus propios inventos y trucos de programación sigan siendo tu secreto. <br> Pero este proceso requiere mucho tiempo, es posible que no se pueda usar inmediatamente despues de una enmienda, se debe tener tantos compiladores como plataformas de hardware quieras que ejecuten el codigo.

Interpretación: Puedes ejecutar el código tan pronto lo completes, no hay fases adicionales de traducción, el codigo se almacena en un lenguaje de programación <br> No hay una interpretación del código rapida, tanto usted como el usuario final deberan tener el interprete.

---

Python es un lenguaje interpretado. Si se quiere programar python se debe contar con el interprete y no se podrá usar el código sin él. Afortunadamente esto es gratis.

Python se le conoce como un lenguaje de Script.

<img src="https://imgs.search.brave.com/B_BW-Q9CL45vBccsICidafIgHESIlvwm8gVmFc5VLr4/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly8xMDAw/bWFyY2FzLm5ldC93/cC1jb250ZW50L3Vw/bG9hZHMvMjAyMC8x/MS9QeXRob24tbG9n/by5wbmc">

*Imagen Tomada De: https://byspel.com/que-significa-que-python-sea-un-lenguaje-interpretado/*

---

**Sección 2 - Introducción a Python**

Python es un lenguaje de programación ampliamente utilizado, interpretado, orientado a objetos y de alto nivel con semántica dinámica, utilizado para programación con propósito general.

> El nombre python viene de una serie de comedia de la BBC llamada El circo volador de Monty Python

> Monty python y una pizza son los nutrientes principales de un programador

¿Quien creo python?

Una caracteristica sorprendente de python es fue hecho con el trabajo de una sola persona.

Por lo general los lenguajes de programación son desarrollados y publicados por grandes empresas.

Python fue creado por Guido Van Rossum nacido en Harleem.

La velocidad con la que python se ha extendido por el mundo es el resultado continuo del trabajo de miles de programadores muy a menudo anónimos

> Las circunstancias en las que se creó Python son un poco desconcertantes.

Según Guido van Rossum:

*En diciembre de 1989, estaba buscando un proyecto de programación "hobby" que me mantuviera ocupado durante la semana cercana a Navidad. Mi oficina (...) estaría cerrada, pero tenía una computadora en casa y no tenía mucho más en mis manos. Decidí escribir un intérprete para el nuevo lenguaje de programación en el que había estado pensando últimamente: un descendiente de ABC que atrajera a los hackers de Unix/C. Elegí Python como título provisional para el proyecto, ya que estaba de un humor un poco irreverente (y era un gran admirador de Monty Python's Flying Circus). Guido van Rossum*

Los objetos de Guido fueron

* Lenguaje poderoso como el de los competidores.

* código abierto.

* código comprensible como inglés sencillo.

* adecuado para tareas cotidianas.

Interesante mirar:

1. [https://github.com/python/cpython](https://github.com/python/cpython "https://github.com/python/cpython")

2. [https://github.com/gvanrossum](https://gvanrossum.github.io// "https://gvanrossum.github.io//")

3. [https://gvanrossum.github.io//](https://gvanrossum.github.io// "https://gvanrossum.github.io//")

4. [https://pypl.github.io/PYPL.html](https://pypl.github.io/PYPL.html "https://pypl.github.io/PYPL.html")

5. [tiobe.com/tiobe-index/](tiobe.com/tiobe-index/ "tiobe.com/tiobe-index/")

> Un proyecto de código abierto puede ser una estrategia muy fuerte.

"Python is easy to learn, teach, use, understand, obtain"

Python tiene dos competidores directos: 

* PERL lenguaje escrito por Larry Wall - [https://www.wall.org/~larry/](https://www.wall.org/~larry/ "https://www.wall.org/~larry/") Se parece a C.

* RUBI lenguaje escrito por Yukihiro Matsumoto - [https://github.com/matz](https://github.com/matz "https://github.com/matz") Lleno de ideas nuevas.

---

¿Donde podemos ver a python en acción?

* Implementación de Servicios de Internet

* Motores de Busqueda

* Herramientas de la Nube

* Redes Sociales

* Desarrollo de Herramientas

* Aplicaciones de Uso Diario

* Cientificos

* Proyectos TI probadores

> Programación de bajo nivel | "Cerca al Metal"

Python rara vez se ve en un controlador, motor gráfico, aplicaciones para dispositivos moviles.

Existen python 2 y python 3 (Lenguajes muy diferentes) en donde se tocaria incluso reescribir algunos elementos del código para ejecutar un codigo de una versión de python a un entorno de otra versión de python.

* El tradicional implementación de python, llamada CPYTHON es la versión de referencia de Guido Van Rossum

Existen versiones de python como:

* CPYTHON

* jyton

* pypy

* Micropython

---

**Sección 3 - Descarga e Instalación de Python**

2. Escribi python3 en la terminal BASH y empezó a instalar python.

1. De igual forma se puede instalar aqui: [python.org/downloads/](python.org/downloads/ "python.org/downloads/")

> Ya entiendo un poco más lo de "Looking for a specific release?"

¿Cómo empezar a trabajar con python?

Al instalar Python3 habrá una aplicación que es una IDLE de python, esto se puede remplazar con un editor de codigo, ya que es un espacio para escribir el código.

> IDLE: Entorno integrado de Desarrollo y Aprendizaje

La consola será para insertar el código una vez finalizado y depurarlo, detenerlo a la fuerza

Ahora es momento de escribir y ejecutar un programa python que como tal esto conciste en crear un archivo fuente y llenarlo con codigo.

A continuación sigue un examen: Consiste en 10 preguntas (Finaliza modulo 1) - 100% scored en la primera vez.

---

**Modulo 2**

Se explica la estructura:

1. Palabra print (Función)
2. Parentesis de Apertura
3. Una línea de texto entre comillas.
4. Un parentesis de Cierre

```py
print("Hola, Mundo!")
```

Una función puede causar algún efecto, evaluar un valor, devolver resultados.

La función puede provenir directamente de python, pueden venir por modulos pues hay funciones que pueden venir con una instalación por separada. Y por otro lado, uno mismo puede crear una función.

El nombre de una función debe ser evidente.

Una función debe tener un efecto y un resultado.

Una función tambien puede tener un tercer componente que este es el de los argumentos. Una función puede aceptar cualquier cantidad de argumentos, tantas como sea necesarias para su tarea. Para esto las funciones de python demandan la presencia de un par de paréntesis, el de apertura y el de cierre.

Una cadena está delimitada por comillas.

Cualquier cosa dentro de comillas se tomara de manera literal y no como código.

Para invocar funciones, se tiene que nombrar la función y el uso de parentesis con o sin sus argumentos.

```py
    function_name(argument)
    print("Hola, python!")
    print("greg")
    print(greg)
    print('greg')
```

> Python explora sus datos internos para encontrar una función existente del nombre, si esta busqueda falla python abortará el código.

Generalmente print se usa para enviar o mostrar datos resultantes al dispositivo de salida.

Ahora entendiendo que la invocación de una función es uno de los otros muchos tipos posibles de instrucciones de Python.

Ahora, ¿Cómo se acopla más de una instrucción en un código python? Por esto es muy importante la sintaxis pues python solicita que no halla más de una instrucción por línea

Se comenta entonces el uso de \

> La \ se puede hacer con alt + 92 

```py
    print("La witsi Witsi Araña\nSubió a su teleraña")
    print()
    print("Vino la lluvia\nY se la llevó")
```

La barra invertida \ tiene un significado muy especial cuando se usa dentro de cadenas, se llama carácter de escape y la palabra n tiene el significado de newline o un caracter de nueva linea

Ahora usando multiples argumentos:

> Los argumentos se separaron por comas.

```py
    print("La witsi Witsi Araña", "Subió", "a su telaraña")
```

Existe el mecanismo que se llama argumentos de palabras clave. El nombre proviene de el hecho que el significado de estos argumentos no se toma de su ubicación sino de la palabra especial

```py
    print("Mi nombre es", "Santiago.", end=" ")
    print("Santiago Python.")

    print("Mi", "nombre", "es", sep="_", end="*")
    print("Monty", "Python.", sep="*", end="*\n")
```

Se pide hacer un ejercicio si si se llego a entender este tema.

Busque como output Programming***Essentials***in...Python

```py
    print("Programming", "Essentials", "in", sep="***", end="...")
    print("Python")
```

Y entonces hubo una secuencia de preguntas:

```py
    # Resultado Esperado?
    print("Mi\nnombre\nes\nBond.", end=" ")
    print("James Bond.")

    # Resultado Esperado?
    print(sep="&", "fish", "chips")

    # ¿Cual generaria una sintax error?:
    print('Greg\'s book.')
    print("'Greg's book.'")
    print('"Greg\'s book."')
    print("Greg\'s book.")
    print('"Greg's book."')
```

---

**Sección 2 - Literales en Python**

Los literales son los datos en si mismos.

Si miramos el numero 123 podemos afirmar que su valor es ciento veintritrés, pero si miramos la letra c ¿Qué valor tiene? Tal vez... pueda representar la constante de una integración, la longitud de la hipotenusa, existen muchas posibilidades.

123 Es un literal.

C No es literal.

```py
    # Entero
    print(123)
    # Cadena
    print("123")
```

> La memoria de una computadora almacena los datos en una serie de bits.

> Un nuevo concepto importante: Sistemas numericos posicionales.

Los tipos de datos se guardan de forma muy distinta unos con los otros.

Python no acepta 11 111 111 por lo que tocaria escribir 11_111_111 o 1111111












---












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











---













## 3. Sesión 3

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



















---

















## Sesión 4

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

---

Ahora finalmente














---













## Sesión 5 - 

> Clase del 6/05/2025

> Se pide entregar bastante rapido los certificados de estos dos cursos por lo que en consecuencia no me haré otro documento python para reforzar los aprendizajes, mejor lo haré en otra ocasión para retroalimentar y reforzar conocimientos.

**¿Cómo tratar con bits individuales?**

Pregunta importante: ¿Para qué puedes usar los operadores de bit a bit?

Entonces se nos da un escenario:

1. Imagina que eres un desarrollador obligado a escribir una pieza importante de un sistema operativo. 

2. Se te ha dicho que puedes usar una variable asignada de la siguiente forma:

```python
    flag_register = 0x1234
```

Es posible que tengas que hacer frente a las siguientes tareas:

* Comprobar el estado de tu bit - deseas averiguar el valor de su bit; comparar la variable completa con cero no hará nada, porque los bits restantes pueden tener valores completamente impredecibles, pero puedes usar la siguiente propiedad de conjunción:

```python
    x & 1 = x
    x & 0 = 0
```

Se nos da el ejemplo:

```python
    the_mask = 8

    if flag_register & the_mask:
        # Mi bit se estableció en 1.
    else:
        # Mi bit se restableció a 0.

```

* Reinicia tu bit - asigna un cero al bit, mientras que todos los otros bits deben permanecer sin cambios; usemos la misma propiedad de la conjunción que antes, pero usemos una máscara ligeramente diferente - exactamente como se muestra a continuación:

11111111111111111111111111110111

Toma en cuenta que la máscara se creó como resultado de la negación de todos los bits de la variable the_mask. Restablecer el bit es simple, y se ve así (elige el que más te guste):

```python
    the_mask = 8

    flag_register = flag_register & ~the_mask
    flag_register &= ~the_mask
```
 
* Establece tu bit - asigna un 1 a tu bit, mientras que todos los bits restantes deben permanecer sin cambios; usa la siguiente propiedad de disyunción:


```python
    x | 1 = 1
    x | 0 = x

    # Equivale a 

    flag_register = flag_register | the_mask
    flag_register |= the_mask
```

Niega tu bit - reemplaza un 1 con un 0 y un 0 con un 1. Puedes utilizar una propiedad interesante del operador ~x:

```python
    x ^ 1 = ~x
    x ^ 0 = x

    # Esto equivale:

    flag_register = flag_register ^ the_mask
    flag_register ^= the_mask
```

---

**Desplazamiento binario a la izquierda y desplazamiento binario a la derecha**

Python ofrece otra operación relacionada con los bits individuales: shifting. Esto se aplica solo a los valores de número entero, y no debe usar flotantes como argumentos para ello

¿Cómo multiplicas cualquier número por diez? 

Como puede ver, multiplicar por diez es de hecho un desplazamiento de todos los dígitos a la izquierda y llenar el vacío resultante con cero.

> 12345 × 10 = 123450

¿División entre diez? Echa un vistazo:

12340 ÷ 10 = 1234

Dividir entre diez no es más que desplazar los dígitos a la derecha.

desplazar un valor un bit a la izquierda corresponde a multiplicarlo por dos; respectivamente, desplazar un bit a la derecha es como dividir entre dos (observa que se pierde el bit más a la derecha).

    Por ejemplo: 

    valor << bits
    valor >> bits
 
    El argumento izquierdo de estos operadores es un valor entero cuyos bits se desplazan. El argumento correcto determina el tamaño del desplazamiento.

Entonces por dar otro ejemplo:

```python
    var = 17
    var_right = var >> 1
    var_left = var << 2
    print(var, var_left, var_right)

    # Resultado: 17 68 8
```