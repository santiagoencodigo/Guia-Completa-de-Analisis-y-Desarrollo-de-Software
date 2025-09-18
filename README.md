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



### REGLA 5



### REGLA 6
