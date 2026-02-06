# Construir Bases de Datos

> Se recuerda el comportamiento que debemos tener: Llegadas tarde, el aseo de la estación de trabajo, etc...

> 14 de abril finaliza el trimestre

"Estará la tentación a la inteligencia artificial", se recomienda primero realizar el análisis del trabajo antes de directamente delegarlo a la inteligencia artificial.

A continuación viene una serie de apuntes y/o documentación respecto a lo que se va a ver en la construcción de bases de datos con la instructora Angelica Triana en el cuarto de nueve trimestres de la formación.






---










## Tabla de Contenidos

1. [1. Introducción](#introducción)










---










## Introducción

> Clase del 05/02/2026

El bien más valioso de la empresa, uno generalmente diria que los servidores en las salas de tics, computadores, salas y todo tipo de cosas tangibles. Realmente **el bien más valioso es la información útil** que tenga la empresa.

Como por ejemplo:

* Deudas en un banco

* Numero de clientes y su contacto si se ofrecen servicios

¿Cuál es el simbolo de una BD de un sistema?

<img src="https://w7.pngwing.com/pngs/931/769/png-transparent-database-icon-database-free-blue-background-blue-angle-world-thumbnail.png">

*Imagen Tomada De: https://www.pngwing.com/es/search?q=base+de+datos*

¿Cómo interactuan estos elementos entre sí?

Hay un cliente, el cual sería cualquier dispositivo de algún cliente o usuario y este pide una interacción, siendo entonces un servidor web el intermediario. Pues cualquier petición que haga el cliente, el servidor verifica y envia entonces una respuesta a esa petición.

*  Servidor by Wikipedia: https://es.wikipedia.org/wiki/Servidor*

* Servidor by MDN: https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_web_server

> Modelo, Vista, Controlador.

* Actualmente estamos conociendo la tecnología que va del lado del servidor - Vista

* Empezamos a mirar el lado de bases de datos - Modelo

* Nos falta mirar el backend, en lenguajes como PHP, JAVA - Constrolador

**Lecturas Recomendadas:**

* MVC by MDN: https://developer.mozilla.org/en-US/docs/Glossary/MVC

* MVC by Wikipedia: https://es.wikipedia.org/wiki/Modelo%E2%80%93vista%E2%80%93controlador

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/ModelViewControllerDiagram_es.svg/500px-ModelViewControllerDiagram_es.svg.png">

*Imagen Tomada De: https://es.wikipedia.org/wiki/Modelo%E2%80%93vista%E2%80%93controlador*

---

El modelo lógico es como hacer las tablas asi como en el modelo relacional para delimitar qué limites tiene, primero se hace esto antes de hacer el modelo físico el cual guardara la información.

> Me agrada lo que se viene.

**Conocimientos Previos**

La estrategia de aprendizaje es ingresar a la página a continuación y se comparte un código, siendo asi una evaluación de sondeo estilo juego.

* Quizizz | Wayground: https://wayground.com/

**Siendo asi las preguntas:**

1. ¿Qué quiere decir en la cardinalidad N:M o * a *?

Relación de uno a muchos, en donde una entidad A se relaciona de cero a muchos registros de una entidad B se relaciona de cero a muchos registros de la entidad A. Cuando se transforma esta relación del modelo entidad relación a modelo relacional se debe generar una tabla intermedia. Siendo la tabla intermedia un punto intermedio para descansar y cada usuario se lleva lo que necesita.

2. ¿Qué es una entidad?

La intención de una entidad que tenga todas las caracteristicas pertinentes a si misma siendo asi una serie de atributos que los caracterizan. Es como tener una placa de vehiculo en la cedula de ciudadanía. Su función es representar algo del mundo real y debe tener unos atributos.

* El mundo real se refiere a que sea útil en nuestro mundo físico. Y por ende no se debe ser imaginativo 

3. ¿Qué entiende por normalización de una BD?

Organización de tablas y columnas en donde se buscan evitar errores, repeticiones innecesarias y/o datos duplicados, funcionan de esta forma como un conjunto de reglas. La base de datos tiene que ser totalmente trasparente y depende totalmente de nuestro pensamiento porque no hace nada que nosotros no le pedimos. Siendo asi, la forma en la que nosotros podemos evitar errores es haciendo normalización.

---

Para conocimientos previos se tiene una lista de elementos/objetos y se debe determinar si es Entidad, Atributo, Valor

> Una entidad es una entidad dependiendo del contexto.

* Pedido = Entidad (Pensé que era Atributo, pero el pedido por si sólo contiene fecha de entrega y otros atributos.)

* Estrato = Atributo (En una entidad casa, estrato puede ser entonces un atributo el cual puede contener valores que seria estrato 1, 2, 3, etc...)

* Disco = Entidad (Depende del contexto: Pero si miramos dentro de un disco puede haber marca, contenido, musica, video y demás. Aunque tambien puede ser marca del disco, nombre del disco, descripción del disco.)

* Edad = Atributo (Pertenece a una entidad que puede ser animal, mascota, persona, trabajor, etc.. Que contiene de valor 17, 18, 20, 40 y demás valores.)

* Producto = Entidad (Contiene por dentro diferentes elementos que pueden ser atributos como nombre_del_producto, descripcion_producto, etc...)

* Alto = Valor (Para mi fue valor, pero tambien puede ser Atributo pues depende del contexto. Porque podemos pensar en proporciones de rangos bajo, alto y por ese estilo seria entonces el valor, pero podemos pensarlo tambien como Alto en medidas siendo asi un atributo.)

> Las entidades a veces son abstractas porque un producto es un servicio.

* Rojo = Valor (El atributo del rojo es color.)

* Vehiculo = Entidad (Un vehiculo contiene diferentes atributos como marca, color, modelo, kilometraje, etc...)

* Femenino = Valor (Porque si lo pensamos, su atributo es Genero.)

* Matricula = Atributo (Porque va a contener una serie de valores como ABD123, puede ser Entidad si estoy en un colegio.)

> El contexto es muy importante.

* Dependencia = Atributo (Depende del contexto porque se puede referir a el area del trabajador, aunque tambien a un area de trabajo y los atributos que va a tener)

> Asi y muchas otras situaciones más para identificar más. ¿Cómo estamos viendo el mundo real que luego estará en el software?

---

Como programador voy a manipular el diseño y la construcción

la normalización es:


Grafo Relacional - Identificación de claves como ficha que tiene inicio y fin, aprendiz tambien tiene ficha por ende es una llave foranea (El que necesita la información es el que pide prestado)

Modelado de bases de datos: Especificar Tipos de Datos sin el SGBD

MR - Modelo Relacional:

> Hay de MER a MR

---


MER - Modelo Entidad Relación: Se determina un mapa, estilo mapa mental con la entidad representada con un cuadro y su nombre, Atributo con un semi circulo.

**Estudio de Caso:**

Una tienda de mascotas desea implementar una base de datos para administrar su información, teniendo en cuenta que:

* Una mascota es vendida a un cliente y a cada cliente se le pueden vender varias mascotas.

* A cada cliente también se le pueden vender diferentes productos para el cuidado de la mascota.

* A cada mascota se le aplican varias vacunas y cada vacuna se le pueden aplicar a diferentes mascotas.

* De la mascota se puede registrar: su nombre, tipo, genero, raza y un código para identificarla.

* Del cliente se necesita registrar: su cedula, nombres, apellidos, dirección y teléfono.

* De los productos se registrará: el código de barras, nombre del producto, marca y precio.

* De las vacunas se registrará: el nombre de la vacuna, un código, dosis a aplicar y nombre de la enfermedad que trata.

**Razonamiento**

Mascota seria entonces la entidad y sus atributos: Genero, Raza, 

El cliente tambien es una entidad: 

Productos es una entidad:

Vacunas tambien es una entidad:

Relaciones con ventas ¿Qué sucede cuando se vende una mascota? ¿Qué pasa si un cliente compra varias mascotas?

Un cliente puede tener varios productos, mascotas - Uno a muchos

Cada vacuna se puede aplicar a diferentes mascotas y una mascota puede tener muchas vacunas - Muchos a muchos

Hay que evitar salir del alcance lo que más se pueda.

---

SGBD = sISTEMA gESTOR DE bases de datos - En donde se codifica la BD

---

STAR UML

DB Designer

---

**Resumen Formas Normales**

1FN = No filas repetidas, datos atomicos, simples e indivisibles.

Si a veces hay combinaciones de colores, entonces color pasaria de atributo a entidad.

> Los instructores sólo nos buscan guiar porque a la final, sólo somos nosotros quienes conocemos el sistema.

**2FN**

Una vez se cumple 1FN, todos los atributos que no forman de parte de la clave principal (pk) tienen dependencia funcional completa de ella. Verificar si ese atributo pertenece totalmente a la entidad.

**3FN**

La clave principal depende de sólo los datos que estan hay y no pertenece a otra entidad?

Como por ejemplo: Si en una pelicula tenemos los atributos titulo, director, nacionalidad director, duración, puntuaciones, productora. ¿Es pertinente tener los datos del director en esta entidad pelicula?

Otro ejemplo: Si en una tabla de conductores siendo asi codigo conductor, datos del conductor, y datos del vehiculo. Siendo asi los datos del vehiculo se pueden saltar si tenemos el código del conductor y que esta sea una FK en la tabla de vehiculos.

---

Las BD existen desde hace mucho tiempo, en papel, piedra y demás y no de forma digital. Son una colección organizada lógicamente

existen demasiados modelos de bases de datos

como jerarquicas- como modelo conceptual

Muldimensional - como arreglos 

Relacionales, las que usamos nosotros

Bases de Datos en Red

Orientadas a Objetos

Como se estaba buscando no tenerla en papel, piedra o papel. Usamos software, tenemos un SGBD - Sistema de Gestor de Bases de Datos. Anteriormente las empresas estaban creando su propia BD. 

Esto tenia problemas de compatibilidad entre empresas si se iban a compartir BD, el respaldar la información.

**¿Qué caracteriza una BD?**

100% Redudancia

Integridad de datos, con mucho cuidado de tipos de datos.

Se almacena en una maquina | Servidor | Disco

Maneja un diccionario de datos siendo asi un inventario de todos los datos que hay en todas las tablas.

Maneja Usuarios (Informato(yo) que manipula, usuario final (el que accede a traves de la interfaz), Administrador (Da los roles))

Da integridad, Seguridad y Concurrencia.

¿Cuantas personas no interactuan con la BD todo el tiempo? ¿Cómo es NEQUI en su BD? Un servidor usa CPU y por ende sólo hace una solicitud al tiempo, un proceso al tiempo y por ende bloquea a un usuario cuando atiende a otro, pero cuando lo hace: Lo hace tan rápido que da la ilusión que lo hace al mismo tiempo todo.

---

Nosotros vamos a ver Bases de Datos relacionales

Maneja Celdas y Columnas. Salió Edgar Frank Codd creó las BD relacionales y trabajaba en IBM, estaba cansado por problemas de compatibilidad entre empresas. Acordando asi, guardar la información en tablas y que no dependa de lo físico porque anteriormente si no tenias el equipo de microsoft, o el otro OS pues no podias hacer ciertas acciones.

Entonces propuso a IBM la idea, eventualmente fue ORACLE quien acepto esta propuesta.

**Terminalogia MODELO RELACIONAL**

Una tabla es una relación. (Son lo mismo en estas BD), estaran los dominios que es el dato ¿Qué caracteristica tiene? Como un entero de tantos digitos, booleanos, número de caracteres.

A los atributos en estas BD se les llamada Campos.

Duplas = Registros

**Hay varias SGBD Relacionales**

ORACLE

MICROSOFT SERVER

SQLITE

MARIABD = fork derivado de oracle 

Postgre SQL para millones de registros

---

Nosotros estamos usando XAMPP, es un servidor web local siendo un paquete de programas para poder desarrollar software en donde dentro tiene un SGBD:

* x - Cualquier OS

* a - Apache - Servidor Web 

* m - MariaDB = SGBD

* p - PHP - backend

* p - PERL - backend

---

* Se pide instalar MSQL Workbench y XAMPP














---














## 