# Reglas de 

<!-- REGLAS DE CONSISTENCIA ENTRE DIAGRAMAS DE CLASE Y DIAGRAMAS DE CASOS DE USO -->

## ESPECIFICACIÓN FORMAL EN OCL DE REGLAS DE CONSISTENCIA ENTRE LOS DIAGRAMAS DE CLASES Y CASOS DE USO DE UML Y EL MODELO DE INTERFACES

Las reglas de concistencia nos permite la planeación para la construción de nuestro Software

> OCL: 

    Para entender las reglas utilizaremos de ejemplo un requerimiento funcional

    Modulo: Facturación

    RF1: El sistema debe permitir generar la factura con la información del cliente y el producto a facturar

### REGLA 1

El nombre de un caso de uso debe incluir un verbo y un sustantivo, el sustantivo debe corresponder al nombre de una clase en el diagrama de clases (Cada elemento esta relacionado)

> Verbo: El verbo debe corresponder a una operación de una clase del diagrama de clases: Registrar

> Sustantivo: Siempre será candidato a ser clase - es Nombre del objeto o opersona: Cliente

Caso de uso: Registrar Cliente

<p style="color:green;">El diagrama de clase debe dar solución al diagrama de casos de uso.</p>

### Diagrama de Casos de Uso

<img src="https://cms.boardmix.com/images/es/articles/examples/sistema-de-restaurante.png" width="450px" height="300px">

### Diagrama de Clases

<img src="https://d2slcw3kip6qmk.cloudfront.net/marketing/pages/chart/class-diagram-for-ATM-system-UML/Class-Diagram-ATM-system-750x660.png"  width="450px" height="300px">


### REGLA 2

que cada clase en el modelo UML tenga que ser implementada como una clase en Java

### REGLA 3

Una interfaz grafica tiene un titulo, verbo y un sustantivo, dicho verbo tiene que a una clase identificada. Como que si hay una interfaz llamada "Registrar Cliente", debe haber una clase llamada "Cliente"

Ese verbo, debe corresponder a una operación, metodo o función que tenga el diagrama de clase.

Video Recomendado: https://www.youtube.com/watch?v=nysy7qnpe30

Web Site recomendado: http://www.scielo.org.co/scielo.php?script=sci_arttext&pid=S1692-33242008000100010

### REGLA 4


<!-- Diagramas de Flujo de Datos  -  DFD --->

---

## Diagramas de flujo de datos

El diagrama de flujo o flujograma o diagrama de actividades es la representación gráfica de un algoritmo o proceso. Se utiliza en disciplinas como programación, economía, procesos industriales y psicología cognitiva.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/LampFlowchart_es.svg/250px-LampFlowchart_es.svg.png"/>

DFD: Descposición por Niveles, un diagrama de contexto es el primer nivel, lueg ovrios DFd EN NIVELES INTERMEDIOS. Hay 5 niveles de DFD

Una entidad es cualquier cosa que pueda tener sus datos propios. Como una silla (Numero de patas, color, altura, ancho) El mundo entero esta lleno de entidades.

El color rojo puede ser una caracteristica de una entidad tipo (Mesa, Silla, Carro) por lo que los nombres deben tener significado tanto para los procesos como para los flujo de datos

Hay que tener mucho cuidado con redes desconectadas debido a que todas deben estar relacionadas.

Es importante pensar quien es fuente de infromación y qué proceso ocurre y quien es destino de información. 

Es fundamental ser lo más general posible.

> Procesos:
> Flujos de Datos:

## Diagrama de nivel 0 = Diagrama de contexto

Un diagrama de contexto, también conocido como diagrama de contexto de sistema o diagrama de flujo de datos de nivel 0, es una representación visual que define los límites entre un sistema, o parte del sistema, y su entorno, mostrando las entidades que interactúan con él.

<img src = "https://cmapsconverted.ihmc.us/rid=1J4Y48BKX-28V41ZN-QW6/DIAGRAMA%20DE%20CONTEXTO.cmap?rid=1J4Y48BKX-28V41ZN-QW6&partName=htmljpeg"/>

[Diagrama de contexto](https://imgs.search.brave.com/8gAFA4pGj65_-qB5eULVoia3z40Lzdvce0lX0Pa9UE8/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZXMuZWRyYXdtYXgu/Y29tL2ltYWdlcy9r/bm93bGVkZ2Uvd2hh/dC1pcy1jb250ZXh0/LWRpYWdyYW0uanBn "Imagen diagrama de contexto") en estas, lo que vemos son los inputs y outputs

### Software para Diagramas

+ [Star UML](https://staruml.io/ "Website: Star UML")
+ [Dia UML](http://dia-installer.de/shapes/UML/index.html.en "dia UML")

Esto representa el MVC (Modelo Vista Controlador)


<!-- Conexiones DFD -->


### Conexiones permitidas entre los componentes de un DFD

Una entidad externa no puede conectarse directamente a un almacen.

### Tipos de Datos

### Tipos de flujo de datos

Flujo de dialogo: Representa una interacción entre un proceso y un almacén de datos, específicamente una consulta seguida de una actualización

Flujo de consulta:
Flujo de acualización:

## Diagrama de nivel 1 = Diagrama de contexto

