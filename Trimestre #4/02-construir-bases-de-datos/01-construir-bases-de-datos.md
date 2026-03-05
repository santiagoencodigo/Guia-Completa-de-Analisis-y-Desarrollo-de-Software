# Construir Bases de Datos

> Se recuerda el comportamiento que debemos tener: Llegadas tarde, el aseo de la estación de trabajo, etc...

> 14 de abril finaliza el trimestre

"Estará la tentación a la inteligencia artificial", se recomienda primero realizar el análisis del trabajo antes de directamente delegarlo a la inteligencia artificial.

A continuación viene una serie de apuntes y/o documentación respecto a lo que se va a ver en la construcción de bases de datos con la instructora Angelica Triana en el cuarto de nueve trimestres de la formación.






---










## Tabla de Contenidos

[1. Introducción](#introducción)

[2. Bases de Datos](#bases-de-datos)

[3. Consultas en Base de Datos](#consultas-en-base-de-datos)

[4. Introducción a INNER JOIN, LEFT JOIN, RIGHT JOIN](#introducción-a-inner-join-left-join-right-join)

[5. Importación de Archivos CSV - Taller: Biblioteca SQL](#importación-de-archivos-csv---taller-biblioteca-sql)

[6. Procedimientos, Funciones, Triggers](#procedimientos-funciones-triggers)

[7. Procedimientos y Funciones Aplicadas en Biblioteca BD](#procedimientos-y-funciones-aplicadas-en-biblioteca-bd)

[8. Triggers]()










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














## Bases de Datos

> A continuación tendremos una explicación

SQL es un lenguaje estándar de programación para el acceso a bases de datos. Este nacio de una idea de alguien que trabajaba en IBM y se paso a ORACLE.

Hay tres grandes grupos para aprender a programar.

1. DDL - Lenguaje de Definición de Datos (Palabras Reservadas: Create (crear), Alter (modificar), Drop(Eliminar))

2. DML - Lenguaje de Manipulación de Datos: Create, Update, Delete, Select (CRUD: 4 acciones básicas que nuestro sistema deberia tener)

3. DCL - Lenguaje de Control de Datos (Se administra quien puede en el grupo de devs hacer ciertas cosas: Como por ejemplo "Si usted es JR no puede hacer DROP en la BD.") - Grant Revoke, Deny

---

**Tipos de Datos Cadena**

Como hablamos de gestionar una base de datos, tenemos muchos tipos de datos por lo que como debemos tener control sobre nuestra estructura de datos tenemos muchos tipos de datos.

    Letras

* CHAR - 255 Caracteres

* VARCHAR - 65535 Caracteres

    Peso en Bytes

* Binary - 255 

* VARBINARY 2^16

    Multimedia

* TINYBLOB 255 bytes

* TINYTEXT 255 Caracteres

* BLOB

* TEXT

* MEDIUM BLOB

* MEDIUM TEXT

* LONGBLOB

* LONGTEXT

* ENUM(v1, v2)

* SET(v1, v2)

---

**Tipos de Datos Númericos**

* INT-INTERGER  - 32 bits

* BIT - 1 bit

* TINYINT - 8 bits

* SMALLINT

* MEDIUMINT

* BIGINT 64 bits

> Size = Cantidad de Números

* FLOAT (size, d) - 32 bits

* DOUBLE(Size, d) - 64 bits

---

**Tipos de Datos Númericos - Booleanos**

> Son booleanos porque al final son 1 y 0

* BOOL - TINYINT(1) - 

* BOOLEAN TINYINT(1) - 

* SERIAL 

* DEC (size, d) - decimal

* FIXED - decimal

* DOUBLE_PRECISION - DOUBLE

* REAL - DOUBLE

---

**Tipo de Datos - Fecha**

> Nosotros tenemos la costumbre de que es AÑO - MES - DÍA

* DATE - 1000-01-01

* DATETIME - 1000-01-01 00:00:01.00000

* TIMESTAMP - Zona Horaria - UTC

> FSP - Fracciones per Second

* TIME - Sólo la hora - FSP

* YEAR - Año

---

**Tipos de Datos - Geoespaciales**

> Se debe hacer de cuenta que es un plano cartesiano

* POINT (X, Y)

* LINESTRING

* POLYGON

* MULTIPOINT

**JSON**

JavaScript

---

**Cojetamiento**

Juego de caracteres que va a haber en las BD, pues no todas las BD no van a estar en español o en ingles. Pues muchas veces las formas de almacenamiento va a cambiar. Muchas vees a esto se le puedeconocer como:

* CHARSET COLLECTION

> El de nosotros será latin.

---

**XAMPP**

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/XAMPP_Windows_10.PNG/330px-XAMPP_Windows_10.PNG">

*Imagen Tomada De: https://es.wikipedia.org/wiki/XAMPP*

Es un conjunto de herramientas para tener una zona de trabajo para testear y hacer trabajos básicos.

Tiene un emparejamient con PHP para la comunicación con la BD.

Apache se conecta con la interfaz en el navegador.

MySQL - Sintaxis para la BD

* Los puertos que aparee al lado de Start en Actions: 80,44 -81 - 3306 - 3307 - 3308. Es porque muchas veces las herramientas que uno usa, aplicaciones utilizan ciertos puertos.

Si no funciona XAMPP, se puede usar onecompiler.com/mysql: https://onecompiler.com/mysql

* Cuando se deja de usar XAMPP, es mejor apagarlo. Porque muchas veces se empieza a trabajar con los archivos internos de XAMPP

> Interesante leer a profundidad y entender cada uno de los elementos de la interfaz del http://localhost/phpmyadmin/ una vez inicias XAMPP.

---

**Pasos para Crear una BD**

1. Necesito determinar mi espacio de atrabajo por lo que se usara DDL. Creación de la base de datos: Escribir en el SQL - CREATE DATABASE.
Se habria creado asi entonces la BD y necesitamos ahora tablas/entidades

2. CREATE TABLE 

3. Incorporar Elementos de Integridad: not null, primary key, UNIQUE, CHECK, DEFAULT. Por medio de PK y FK hacer conección entre tablas.

    Ya aqui tenemos la BD, pero es una BD vacia.

Ahora nosotros gestionamos la BD, por lo que somos responsables de pedirle a los usuarios como insertar la información y por eso se generan Restricciones o constrain

* NOT NULL - Garantiza que la columna no este vacia.

* UNIQUE: Dato unico e irrepetible. - Como el correo.

* Primary Key: Dato que quiero que sea una llave, una combinación de NOT NULL y UNIQUE que identiifca de forma exclusiva una tabla. - La que tenga esta, se le conoce como tabla maestra.

* Foreing Key: Llave que pide pretada, la tabla que tenga esta tiene una relación tiene una muchos

    CREATE TABLE persons (
        ID int NOT NULL,
        LastName varchar(255) NOT NULL,
        FirstName varchar(255),
        Age int,
        UNIQUE (ID)
    )

* CHECK: ¿se cumple el dato antes de registrarlo?

    CREATE TABLE persons(
        Age int
        CHECK(18<0)
    )

* DEFAULT: Establece un valor por defect, como registrar automaticamente que una persona es de bogotá

* INDEX: Se utiliza para crear y recuperar datos de la base de datos muy rapidamente.

* Campo AUTO INCREMENT: Importante para la tabla maestra, sólo funciona para llaves primarias. 

    CREATE TABLE persons (
        Personid int NOT NULL AUTO_INCREMENT
    )

* Si quiero que inicie desde ciert número.

    ALTER TABLE persons AUTO_INCREMENT=100;

XAMPP nos puede ayudar con esto, pero si fueramos a usar la consola para hacer esto. Generalmente con un servidor:

* show database;

* use nombreBD;

* show tables;

* describe table;

---

en **XAMPP** esta la interfaz para crear la Base de Datos, pero esto no es tan buena practica porque la interfaz puede cambiar, mas no el código.

Para hacer la BD, primero tenemos que haber hecho el diseño.

> Interesante hacerme una ecommerce como proyecto en github, que tenga todo este apartado de diseño y bases de datos.

La miga de pan: Es la ruta. - Por ejemplo: Servidor: 127.0.0.1:3307

¿Qué relación tiene una tabla de ventas con una tabla de productos? - Muchos a muchos - Pueden hacer muchos productos en muchas ventas y muchas ventas con muchos productos

¿Qué relación puede tener una tabla de Clientes y tabla Ventas? - Un cliente puede tener muchas ventas y por ende - Uno a muchos.

> La instructora empieza a Diagramar las tablas para explicar.

---

A continuación vamos con el proceso de la creación de nuestra tabla una vez ya escribimos CREATE DATABASE nombre;

Preguntas para Reflexionar antes de Crearla.

* ¿Qué datos puede tener una cliente?

* ¿Qué datos puede tener Ventas?

* ¿Qué datos puede tener Productos?

* ¿Cual es la primera tabla que se crea?

    Se crea tabla: CREATE TABLE CLIENTE;

* DOCUMENTO: Puede VARCHAR ¿Pero y si tambien alguien agrega letras?, por ende debe ser int, ahora ¿Cuantos caracteres?, Debe ser Obligatorio y por ende NOT NULL.

* NOMBRE: Será un VARCHAR con 45 caracteres, deben ser NOT NULL porque no pueden quedar vacios.

> Despues de crear cada uno de los campos es importante insertar la ,

* CORREO: Será un VARCHAR de 100 caracteres, deben ser NOT NULL porque no pueden quedar vacios.

> Es importante establecer que se quiere NULL y que se quiere NOT NULL

* Restricciones - PRIMARY KEY () - ¿Qué dato es menos probable que se repita y me pueda permitir identificar a un usuario? Dentro de los parametros del PK insertamos el nombre de nuestro campo.

> Al final, ya no se inserta una ,

    CREATE TABLE CLIENTE(
        DOCUMENTO INT NOT NULL,
        NOMBRE_COMPLETO VARCHAR(45),
        CORREO VARCHAR(100),
        PRIMARY KEY (DOCUMENTO)
    );

Ahora si queremos mirar en la barra lateral donde se encuentran las BD en XAMPP, podemos encontrar y darle click a nuestra BD ya existente, podemos abrirla y por dentro estará nuestra tabla CLIENTE.

---

**Vamos a crear la tabla VENTA**

* Queremos un ID que se pueda identificar y por ende ID_VENTA

* Queremos una fecha para identificar esta venta y que sea NOT NULL

* Queremos un precio que sea entero y NOT NULL

* Un primary key para identificar y que sea una llave maestra.

* Vamos a establecer una FOREING KEY para hacer la conexión con la tabla CLIENTES:

        1. Ahora quiero que se conecte con la otra tabla ya existente (CLIENTE), por ende necesito una FK. La instructora sugiere pensarlo como pedir prestado o copiar, hay que copiar la PK de la otra tabla principal. Copiando asi entonces, tambien el tipo de dato de nuestra PK de CLIENTE.

        2. Se tiene que definir como si fuera uno de los tipos de datos de la tabla venta común y corriente. Y luego establecemos entonces COPIA_DOCUMENTO como FOREIGN KEY.

        3. Finalmente hay que agregar la referencia de donde vamos a tomar nuestra y por ende será la tabla CLIENTE y su dato DOCUMENTO

por ende:

    CREATE TABLE VENTA(
        ID_VENTA INT AUTO_INCREMENT,
        FECHA DATE NOT NULL,
        PRECIO INT NOT NULL,
        COPIA_DOCUMENTO INT NOT NULL,
        PRIMARY KEY(ID_VENTA),
        FOREIGN KEY(COPIA_DOCUMENTO) REFERENCES CLIENTE(DOCUMENTO)
    );

Ya entones nosotros podemos clickaer en la barra lateral estas tablas y poder observar cada uno de nuestros campos de nuestra tablas.

Si seleccionamos nuestra tabla, podemos mirar en el apartado de DISEÑADOR para poder mirar la relación entre nuestras tablas.

> Es muy importante tener en cuenta en donde realizamos nuestro ultimo click pues será eso lo que tengamos seleccionados, si nosotros dimos click a una tabla, pues se tendrá que hacer click a la BD.

---

**Vamos a crear una tabla productos**

Es importante nombrar el atributo, luego un _ y finalmente el nombre de nuestra tabla. Entonces para esta tabla: **atributo_PRODUCTO**

Necesitamos:

* ID

* NOMBRE

* PRECIO

* CANTIDAD

> Esta no tiene una FK debido a que esta exista por si misma.

Se le crea entonces una PK para identificarla, pues esta es otra tabla maestra.

Entonces:

    CREATE TABLE PRODUCTO(
        ID_PRODUCTO INT UNIQUE AUTO_INCREMENT,
        NOMBRE_PRODUCTO VARCHAR(55) NOT NULL,
        PRECIO_PRODUCTO INT NOT NULL,
        CANTIDAD INT NOT NULL,
        PRIMARY KEY(ID_PRODUCTO)
    );

---

Ya tenemos 3 tablas maestras, ahora vamos a crear una tabla intermedia que hace una union. Debemos pensar en un nombre que sea unico, que no se pueda repetir, tenemos que bautizarla de una forma que no interfiera con el futuro de desarrollo para que sea sostenible. **No podemos repetir nombres!** Y a su vez debemos llegar a una identificación exacta.

*   Se tiene que empezar a documentar el código en este momento, se puede hacer por medio de #COMENTARIO

A esta tabla, generalmente las nombran como la UNION del nombre de las dos tablas que se van a unir. Por ende si tenemos VENTAS y PRODUCTOS, puede ser **VENPRO**.

**¿Por qué creamos esta tabla?:** Porque nos interesa realizar la union de dos tablas diferentes.

> No entendí, ¿Cual es el funcionamiento de esta tabla en el mundo real? - Respaldos.

**¿Qué datos necesitamos de esta tabla?**

* Como será la union: necesitamos la copia de venta, la copia de pro

* Esta tabla puede tener PK si lo amerita.

* Debemos recordar la estructura de una FK copiando el atributo, y agregando una referencia.

Por ejemplo:

    CREATE TABLE VENPRO(
        COPIA_PRODUCTO INT NOT NULL,
        COPIA_VENTA INT NOT NULL,
        FOREIGN KEY (COPIA_PRODUCTO) REFERENCES PRODUCTO(ID_PRODUCTO),
        FOREIGN KEY (COPIA_VENTA) REFERENCES VENTA(ID_VENTA)
    );

---

Una vez creamos las 3 tablas principales y la intermedia, vamos a exportarla. Esta en las funciones de arriba.

* Es importante tener en cuenta: ¿Sabes eliminar una BD? ¿Sabes exportarla e importarla?

---

**ALTER**

* Para cambiar el nombre de una tabla es ALTER TABLE nombreAnterior RENAME nombreNuevo;

* Si me equivoque y me toca borrar la FK, cuando se une una tabla con otra tabla y esto no corresponde.

**DROP**

DROP DATABASE nombredelatabla;

DROP TABLE table_name;

Para eliminar la BD: TRUNCATE TABLE table_name;

---

De ahora en adelante continua entonces DML

Si entonces todo es estable y vamos a empezar con un lenguaje de manipulación de datos, esto quiere decir que vamos a insertar datos

> Se debe tener cuidado donde se esta seleccionado, para editar esto se debe hacer en las tablas:

    INSERT INTO `cliente`(`DOCUMENTO`, `NOMBRE_COMPLETO`, `CORREO`) VALUES ('[value-1]','[value-2]','[value-3]')

Si entonces deseamos **MOSTRAR DATOS**

Esto es donde nosotros más vamos a estar, para realizar consultas

    SELECT * FROM Customers;

    SELECT CustomerName, City FROM Customer;

---

El DELETE se usa para eliminar registros existentes

    DELECT FROM Customers; (NOUUUUUUUUUUUUUUUUUUUUUUUUUUU)      

Es importante definir qué se va a borrar de forma especifica:

    DELECT FROM Customers WHERE CustomerName='Alfreds Futterkiste'

---

Por otro lado si se va a actualizar

    UPDATE Customers
    SET ContactName = 'Alfred Schidt', City='Frankfurt'
    Where CustomerID = 1;

---

**Llave Compuesta**

Se define una clave compuesta cuando ningún campo por si sólo cumple.

Lo más común es un parqueadero. En un parqueadero un registro no puede repetirse, digamos... Si tenemos una PK no podrá ser entonces no se podrá repetir, pero y si ¿El carro vuelve al parqueadero? Para esto entonces, se debe ingresar otra llave. Siendo asi PK la placa y PK el TIME

> Entonces en un parqueadero una horallegada puede ser PK.

Entonces el sistema puede dejar 4 PK, pero por normalización no esta tan bien.

---

A continuación vamos entonces con el ejercicio:

Se nos muestra un Modelo Relacional y surgen unas preguntas

¿Cual es la primera tabla que se debe crear?

1. ¿Cuales son las llaves maestras?

> Sigue luego, la que tienen FK pero entre más pocas van primero.

2. ¿Cual tiene más llaves foraneas?

> Si tienen muchas, son intermedias y por ende van en la ultima jerarquia de creación.

Entonces:

Tenemos varias tablas, la primera que realizamos es CLIENTE, voy a hacerlo con la misma BD. Por ende le haré unas modificaciones de acuerdo a lo que se aprendió.

Debe haber una tabla cliente, en la que mi BD actualmente tiene realice un DROP TABLE CLIENTE;

y entonces escribí:

    CREATE TABLE CLIENTE(
        ID_CLIENTE INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        NOMBRE VARCHAR(50) NOT NULL,
        APELLIDO VARCHAR(50) NOT NULL,
        DIRECCION VARCHAR(150) NOT NULL,
        FECHA_NACIMIENTO DATETIME NOT NULL,
        TELEFONO INT NOT NULL,
        EMAIL VARCHAR(50) NOT NULL
    );

Luego entonces otra tabla Maestra MODO_PAGO 

    CREATE TABLE MODO_PAGO(
        NUMERO_PAGO INT NOT NULL PRIMARY KEY,
        NOMBRE_PAGO VARCHAR(50) NOT NULL,
        OTROS_DETALLES VARCHAR(50) NOT NULL
    );

Luego sigo con FACTURA que contiene FK de CLIENTE y MODO_PAGO

    CREATE TABLE FACTURA(
        NUM_FACTURA INT NOT NULL PRIMARY KEY,
        ID_CLIENTE INT NOT NULL,
        FECHA DATE NOT NULL,
        NUMERO_PAGO INT NOT NULL,
        FOREIGN KEY (ID_CLIENTE) REFERENCES CLIENTE(ID_CLIENTE),
        FOREIGN KEY (NUMERO_PAGO) REFERENCES MODO_PAGO(NUMERO_PAGO)
    );

---

**Operadores Aritmeticos**

Hay diferentes operadores,

los operadores relacionales

hay operadores que se usan para las consultas, por ejemplo

    SELECT * FROM Producs 
    WHERE Price = 18

* = - Quiere decir IGUAL 

* <> - No Igual - SELECT * FROM Products WHERE price <> 18;

---

**Valores Inválidos**

Valores que estan malos, y no se representaran de forma correcta

* Un valor es inválido por tener un tipo de dato incorrecto por estar fuera de rango. Esto incluye espacios. 

* Se presenta el concepto de truncar.

* Un numero entero puede generar problemas por espacio si se cuenta como numero y por eso muchas veces se deja como varchar-

* La fecha - Si el formato no esta bien todo va a aparecer como 0

---

**Valores NULL**

NULL es que no podemos decir si existe o no existe. Como si es desconocido.

En donde 0/empty string - Null: Reconozco su existencia y no se define que si estuvo o no estuvo pues no se sabe. Un valor NULL es diferene a un 0.

Si estoy insertando datos.

    INSERT INTO LIBROS (TITULO, AUTOR, EDITORIAL, PRECIO)
    VALUES('ELBAFH' 'AKIRA', 'TOEIA' 'PLANEAT' 'NULL')

Los datos que esten nulos se van a ignorar y despues podrian actualizarse.

    SELECT * FROM LIBROS
    WHERE PRECIO IS NULL;

> Busqueda de libros que se desconoce el precio

    SELECT * FROM LIBROS
    WHERE PRECIO = 0;

No va a aparecer nada.

---

**Campos Calculados**

Con los datos para operaciones matematicas, empezamos a jugar con eso: En donde por ejemplo si tengo una tabla de libros la cual contiene precio, cantidad. Y me interesa entonces verificar su valor dependiendo de la cantidad de libros totales y su precio unitario (Se representa como una columna aparte.)

Este numero no se guarda sino que se encuentra como una operación aritmetica temporal.

    # En caso de querer comparar precios con precios con descuento
    SELECT TITULO, PRECOI, PRECIO*01, PRECIO-(PRECIO*0.1)
    
---

Se pide Transcribir y ejecutar el SCRIPT

> Cuando se va a agregar nombre a un campo, es buena practica agregar las iniciales y luego su atributo como: de la tabla producto los elementos pro_id, pro_nombre

    CREATE TABLE PRODUCTO(
        PRO_ID INT AUTO_INCREMENT,
        PRO_NOMBRE VARCHAR(20) NOT NULL,
        PRO_PRECIO INT NOT NULL CHECK (PRO_PRECIO>=1),
        PRO_CANTIDAD INT NOT NULL CHECK(PRO_CANTIDAD>=0),

        # Tynyblob guarda una dirección que se consulta y representa el archivo multimedia

        PRO_FOTO TINYBLOB,
        PRO_DESCRIPCION VARCHAR(20),
        PRIMARY KEY(PRO_ID)
    );

> CHECK es una restricción que verifica la condición que esta dentro de sus parametros.

    INSERT INTO PRODUCTO (PRO_NOMBRE, PRO_PRECIO, PRO_CANTIDAD, PRO_FOTO, PRO_DESCRIPCION)
    VALUES 
    ('Silla Deco', 250000, 7, null, 'Mesa Noche 45x45' ),

    # Si el numero esta negativo, no se puede permitir
    ('Mesa Auxiliar', 310000, 1, null, 'Para la Sala' ),
    ('Mesa Auxiliar 2', 350000, 0, null, 'Para la Sala' );

> No es obligatorio agregar foto, descripción.

Una vez hecho este código se pueden hacer las consultas:

    SELECT * FROM PRODUCTO
    WHERE PRO_FOTO IS NOT NULL;

    SELECT * FROM PRODUCTO
    WHERE PRO_DESCRIPCION = '';










---











---












## Consultas en Base de Datos

> Clase del 16/02/2026

> Anteriormente hubo una clase de explicación sobre las diferentes tipos de consultas que se podian realizar.

**Estudio de Caso: Veterinaria**

Se nos presenta una situación de un proceso de diseño a construcción, por lo que se mira diferentes trabajos para la normalización de una BD y por ende MER (Modelo Entidad Relación), Grafo Relacional, Especificación de tipos de datos, MR (Modelo Relacional con el SGBD)

> El objetivo de esta actividad es la construcción con SQL

Entonces se pide realizar código SQL a partir de un modelo relacional y por ende:

```sql

    --  Creación de Base de Datos
    CREATE DATABASE VETERINARIA;

        -- Comando para usar la BD y editarla.
        USE VETERINARIA;

    -- Creación de Tablas (Tabla Maestra)
    CREATE TABLE CLIENTE (
        CEDULA VARCHAR(25) PRIMARY KEY,
        NOMBRES VARCHAR (50) NOT NULL,
        APELLIDOS VARCHAR (50) NOT NULL,
        DIRECCION VARCHAR (255) NOT NULL,
        TELEFONO VARCHAR (15) NOT NULL
    );
    
    -- Creación de Tabla Maestra
    CREATE TABLE PRODUCTO (
        CODIGOBARRAS BIGINT(20) PRIMARY KEY,
        NOMBRE VARCHAR(25) NOT NULL,
        MARCA VARCHAR(25) NOT NULL,
        PRECIO INT(11) NOT NULL
    );

        -- Creación de Tablas (Contienen FK)
        CREATE TABLE VENTA (
            ID_VENTA INT(11) PRIMARY KEY,
            COPIACEDULAVENTA VARCHAR(25) NOT NULL,
            CODIGOBARRAS BIGINT(20) NOT NULL,

            -- Es muy importante verificar los parentesis.
            FOREIGN KEY (COPIACEDULAVENTA) REFERENCES CLIENTE (CEDULA),
            FOREIGN KEY (CODIGOBARRAS) REFERENCES PRODUCTO (CODIGOBARRAS)
        );

    CREATE TABLE VACUNA (
        CODIGOVACUNA VARCHAR(50) PRIMARY KEY,
        NOMBREVACUNA VARCHAR(50) NOT NULL,
        DOSIS TINYINT(4) NOT NULL,
        ENFERMEDADTRATADA VARCHAR(100) NOT NULL
    );

    CREATE TABLE MASCOTA (
        CODIGOMASCOTA INT(11) PRIMARY KEY,
        NOMBREMASCOTA VARCHAR(25) NOT NULL,
        TIPOMASCOTA VARCHAR(25) NOT NULL,
        RAZA VARCHAR(25) NOT NULL,
        GENERO ENUM('MACHO','HEMBRA','N/A'),
        COPIACEDULACLIENTE VARCHAR(25) NOT NULL,
        FOREIGN KEY (COPIACEDULACLIENTE) REFERENCES CLIENTE (CEDULA)
    );

        -- Tabla Intermedia
        CREATE TABLE APLICACION (
            COPIACODIGOMASCOTA INT(11) NOT NULL,
            COPIACODIGOVACUNA VARCHAR(50) NOT NULL,
            FOREIGN KEY (COPIACODIGOMASCOTA) REFERENCES MASCOTA(CODIGOMASCOTA),
            FOREIGN KEY (COPIACODIGOVACUNA)  REFERENCES VACUNA(CODIGOVACUNA)
        );

```

> Me agrada bastante practicar con esto, aprendí entonces a realizar un nuevo elemento en: GENERO ENUM('MACHO','HEMBRA','N/A')

**Pasamos a una nueva sección de práctica: Sentencias SQL**

1. Una vez creada la base de datos, se pide insertar por lo menos 5 registros en cada tabla y relacionar algunos registros.

2. Consultar cada una de las tablas

3. Modificar un registro de la tabla mascota

4. Eliminar un registro de la tabla mascota

> Ahora me surge una nueva pregunta, ¿Donde inserto los nuevos registros?

```sql
    -- Cliente solo contiene primary key por lo que será el primero en tener registros
        INSERT INTO CLIENTE (CEDULA, NOMBRES, APELLIDOS, DIRECCION, TELEFONO)
        VALUES
        ('12334567890', 'Santiago', 'Hernandez', 'CR 77 e', '1414141414'),
        ('22334567890', 'Samuel', 'Perez', 'CR 78 a', '1212121212'),
        ('32334567890', 'Calamardo', 'Ochoa', 'CR 79 b', '1111111111'),
        ('42334567890', 'Cristian', 'Sanchez', 'CR 80 c', '1616161616'),
        ('52334567890', 'Luisa', 'Hernandez', 'CR 81 d', '1818181818');


    -- Luego sigue producto por ser tambien tabla maestra.
        INSERT INTO PRODUCTO (CODIGOBARRAS, NOMBRE, MARCA, PRECIO)
        VALUES
        (555551, 'Portatil', 'HP', 2000000),
        (555552, 'Mouse', 'Logitech', 80000),
        (555553, 'Teclado', 'Genius', 120000),
        (555554, 'Monitor', 'Samsung', 750000),
        (555555, 'Impresora', 'Epson', 650000);


            -- Una vez creada las tablas CLIENTE y PRODUCTO, pasamos con VENTAS. Pero como es Intermediaria la dejaré comentada.
                -- INSERT INTO VENTA (ID_VENTA, COPIACEDULAVENTA, CODIGOBARRAS)
                -- VALUES
                -- (1, '12334567890', 555551),
                -- (2, '22334567890', 555552),
                -- (3, '32334567890', 555553),
                -- (4, '42334567890', 555554),
                -- (5, '52334567890', 555555);


    -- Ahora surgimos con VACUNA: Estos registros se los pedí a chatgpt con datos reales.
        INSERT INTO VACUNA (CODIGOVACUNA, NOMBREVACUNA, DOSIS, ENFERMEDADTRATADA)
        VALUES
        ('VAC001', 'BCG', 1, 'Tuberculosis'),
        ('VAC002', 'Hepatitis B', 3, 'Hepatitis B'),
        ('VAC003', 'Pentavalente', 3, 'Difteria, Tétanos, Tosferina, Hepatitis B, Haemophilus influenzae tipo b'),
        ('VAC004', 'Polio (IPV)', 4, 'Poliomielitis'),
        ('VAC005', 'SRP', 2, 'Sarampión, Rubéola y Paperas'),
        ('VAC006', 'Influenza', 1, 'Influenza estacional'),
        ('VAC007', 'Varicela', 2, 'Varicela'),
        ('VAC008', 'COVID-19', 2, 'COVID-19'),
        ('VAC009', 'Neumococo', 3, 'Infecciones por neumococo'),
        ('VAC010', 'Rotavirus', 2, 'Gastroenteritis por rotavirus');


    -- Continuamos con Mascota
        INSERT INTO MASCOTA
        (CODIGOMASCOTA, NOMBREMASCOTA, TIPOMASCOTA, RAZA, GENERO, COPIACEDULACLIENTE)
        VALUES
        (1, 'Max', 'Perro', 'Labrador', 'MACHO', '12334567890'),
        (2, 'Luna', 'Gato', 'Siames', 'HEMBRA', '22334567890'),
        (3, 'Rocky', 'Perro', 'Bulldog', 'MACHO', '32334567890'),
        (4, 'Mia', 'Gato', 'Persa', 'HEMBRA', '42334567890'),
        (5, 'Toby', 'Perro', 'Poodle', 'MACHO', '52334567890'),
        (6, 'Nala', 'Perro', 'Pastor Aleman', 'HEMBRA', '12334567890'),
        (7, 'Simba', 'Gato', 'Mestizo', 'MACHO', '22334567890'),
        (8, 'Kira', 'Conejo', 'Cabeza de Leon', 'HEMBRA', '32334567890'),
        (9, 'Thor', 'Perro', 'Rottweiler', 'MACHO', '42334567890'),
        (10, 'Coco', 'Ave', 'Canario', 'N/A', '52334567890');
```

Ahora a continuación voy a consultar cada una de las tablas por lo que:

* select * from cliente

* select * from producto

* select * from vacuna

* select * from mascota

Al hacer esto, me parece interesante que puedo editar, eliminar y copiar desde la interfaz de XAMPP.

A continuación voy a modificar un registro de la tabla mascota.

```sql

    -- Si quiero modificar un sólo campo.
    UPDATE MASCOTA
    SET RAZA = 'Golden Retriever'
    WHERE CODIGOMASCOTA = 1;

```

y para eliminar una tabla:

```sql
    DELETE FROM MASCOTA
    WHERE CODIGOMASCOTA = 1;
```

Y entonces se pide realizar las siguentes consultas:

5. Mostrar los productos que sean igual o mayores en el precio a 2000

```sql
    SELECT *
    FROM PRODUCTO
    WHERE PRECIO >= 2000;
```

6. Hacer una consulta que utilice un apodo –alias

```sql
    SELECT 
        NOMBRE AS Producto,
        MARCA AS Marca_Comercial,
        PRECIO AS Precio_Unitario
    FROM PRODUCTO;
```

7. Una consulta que sume el total de los precios de todos los productos

```sql
    -- para eso se usa la función de agregación SUM().
    SELECT SUM(PRECIO) AS Total_Precios
    FROM PRODUCTO;
```

8. Una consulta que ordene de forma descendente los apellidos de los
clientes

```sql
    SELECT *
    FROM CLIENTE
    ORDER BY APELLIDOS DESC;
```

9. Una consulta que muestre que mascotas tienen los clientes

> Esta todavia no la entiendo del todo, por lo que debo entender.

Reflexione: Los c.(CAMPO) como por ejemplo c.NOMBRES, c.APELLIDOS es porque directamente se define en FROM CLIENTE c que CLIENTE es c. Eso quiere decir que su selección dice "Tome de la entidad CLIENTE, el campo NOMBRES"

```sql
    SELECT
        -- CLIENTE -> NOMBRES
        c.NOMBRES,
        c.APELLIDOS,
        COUNT(m.CODIGOMASCOTA) AS Cantidad_Mascotas
    FROM CLIENTE c
    LEFT JOIN MASCOTA m
        ON c.CEDULA = m.COPIACEDULACLIENTE
    GROUP BY c.CEDULA, c.NOMBRES, c.APELLIDOS;
```

10. Una consulta que muestre que vacunas tiene una mascota

```sql
    SELECT NOMBREVACUNA, ENFERMEDADTRATADA
        FROM VACUNA
        WHERE CODIGOVACUNA IN (
            SELECT COPIACODIGOVACUNA
            FROM APLICACION
            WHERE COPIACODIGOMASCOTA = 1
    );
```

11. Una consulta que muestre las mascotas que empiecen con la letra C.

```sql
    SELECT *
    FROM MASCOTA
    WHERE NOMBREMASCOTA LIKE 'C%';
```

12. Una consulta que agrupe cuantas vacunas tiene cada mascota.

```sql
    SELECT 
        NOMBREMASCOTA,
        (
            SELECT COUNT(*)
            FROM APLICACION a
            WHERE a.COPIACODIGOMASCOTA = m.CODIGOMASCOTA
        ) AS Cantidad_Vacunas
    FROM MASCOTA m;
```

13. Una consulta que muestre el calculo del 3% de descuento en un producto seleccionado en la consulta.

```sql
    SELECT 
        NOMBRE,
        PRECIO,
        (PRECIO * 0.03) AS Descuento_3_Por_Ciento,
        (PRECIO - (PRECIO * 0.03)) AS Precio_Con_Descuento
    FROM PRODUCTO
    -- WHERE CODIGOBARRAS = 555551;
```

14. Una consulta que muestre la consulta de que productos han comprado los clientes.

```sql
    SELECT NOMBRE, MARCA, PRECIO
    FROM PRODUCTO
    WHERE CODIGOBARRAS IN (
        SELECT CODIGOBARRAS
        FROM VENTA
    );
```

15. Una consulta que muestre cuantas mascotas tiene un cliente y solo muestre a los que tengan igual o mayor a 2 mascotas.

```sql
    SELECT 
    NOMBRES,
    APELLIDOS,
    (SELECT COUNT(*)
    FROM MASCOTA m
    WHERE m.COPIACEDULACLIENTE = c.CEDULA) AS Cantidad_Mascotas
    FROM CLIENTE c;
```











---











## Introducción a INNER JOIN, LEFT JOIN, RIGHT JOIN

> Clase del 19/02/2026

Explicación del JOIN y sus diferentes aspectos.

Se pide insertar el siguente código:

```sql
    -- El atributo if not exists es muy funcional si tenemos un backup, pero ya hay ciertas tablas para no tener errores.
    create database if not exists lugar;

    create table if not exists Regiones(
        idRegion int(2) primary key,
        Region varchar(20) not null);

    create table if not exists Provincias(
        idProvincia int(2) primary key,
        Provincia varchar(20) not null,
        idRegion int(2) not null,
        foreign key (idRegion) references Regiones(idRegion));

    create table if not exists Comunas(
        idComuna int(2) primary key,
        Comuna varchar(20) not null,
        idProvincia int(2) not null,
        foreign key (idProvincia) references Provincias(idProvincia));
```

Datos:

```sql
    insert into Regiones (idRegion, Region)
    values (1, 'Andina'),(2, 'Pacifica'),(3,'Caribe');

    insert into Provincias(idProvincia, Provincia,
    idRegion) values (1, 'Cundinamarca', 1), (2,'Choco',2),(3,'Antioquia',1); 

    insert into Comunas(idComuna, Comuna, idProvincia)
    values (1,'Bogotá',1),(2,'Medellín',3),(3, 'Facatativa',1);
```

Consultas:

```sql
    select Regiones.idRegion, Region, Provincia, Comuna
    from ((Provincias
    inner join Regiones on 
    Provincias.idRegion=Regiones.idRegion)
    inner join Comunas on 
    Comunas.idProvincia=Provincias.idProvincia); 
    
    select Regiones.idRegion, Region, Provincia, Comuna
    from ((Provincias
    left join regiones on 
    Provincias.idRegion=Regiones.idRegion)

    left join Comunas on 
    Comunas.idProvincia=Provincias.idProvincia); 

    select Regiones.idRegion, Region, Provincia, Comuna
    from ((regiones
    left join Provincias on 
    Provincias.idRegion=Regiones.idRegion)
    left join Comunas on 
    Comunas.idProvincia=Provincias.idProvincia);
```

---

Teniendo en cuenta el siguente código:

    ```sql
    create database Hospital_SMH;

    use Hospital_SMH;

    create table paciente(
    num_historial char(3) not null,
    nombre_paciente varchar(50) not null,
    primary key(num_historial)
    );

    insert into paciente(num_historial,nombre_paciente)
    values('p20','Juan Marín'),('p40','Luisa Peralta'),('p22','Andrés López');

    create table medico(
    cod_identificacion int not null,
    nombre_medico varchar(50) not null,
    primary key(cod_identificacion)
    );

    insert into medico(cod_identificacion,nombre_medico)
    values (123,'Andrea Luna'),(456,'Eli Salinas'),(890,'Andrés M. Cruz');

    select * from medico;

    create table ingreso(
    num_ingreso int auto_increment not null,
    fechayhora datetime not null,
    pac_ingreso char(3) not null,
    med_ingreso int not null,
    primary key(num_ingreso),
    foreign key (pac_ingreso) references paciente(num_historial),
    foreign key(med_ingreso) references medico(cod_identificacion)
    );

    insert into ingreso(fechayhora,pac_ingreso,med_ingreso)
    values ('2023-12-04 10:40:00','p40',456);

    insert into ingreso(fechayhora,pac_ingreso,med_ingreso)
    values ('2023-12-04 10:50:00','p40',123);

    insert into ingreso(fechayhora,pac_ingreso,med_ingreso)
    values ('2023-12-04 10:40:00','p20',123);

    select * from ingreso;
```

Luego se pide realizar una serie de consultas para practicar el concepto de JOINs:

1. Un right join entre las tablas medico e ingreso, donde la tabla de la derecha es médico.

```sql
    -- RIGHT JOIN
    SELECT * FROM
    INGRESO
    RIGHT JOIN MEDICO
    ON INGRESO.med_ingreso = MEDICO.cod_identificacion;
```

2. Un left join entre las tablas paciente e ingreso, donde la tabla de la izquierda es paciente.

```sql
    -- LEFT JOIN
    SELECT * FROM
    PACIENTE
    LEFT JOIN INGRESO
    ON PACIENTE.num_historial = INGRESO.pac_ingreso;
```

3. Un inner join entre las tres tablas.

```sql
    -- INNER JOIN
    SELECT * FROM
    PACIENTE
    INNER JOIN INGRESO
    ON PACIENTE.num_historial = INGRESO.pac_ingreso
    INNER JOIN MEDICO ON INGRESO.med_ingreso=medico.cod_identificacion
```

> ¿Realmente entiendes qué es un INNER JOIN, LEFT JOIN, RIGHT JOIN?

> ¿Si entendió los temas de Group by, Order By, count, Operaciones matemáticas en BD?

**Lecturas Recomendadas:**

* Qué es INNER JOIN by IONOS: https://www.ionos.com/es-us/digitalguide/hosting/cuestiones-tecnicas/inner-join/

* INNER JOIN, LEFT JOIN, RIGHT JOIN by Microsoft: https://support.microsoft.com/es-es/topic/operaciones-left-join-right-join-ebb18b36-7976-4c6e-9ea1-c701e9f7f5fb

Primero debo revisar el código que tengo. Es agradable mirar como en XAMPP, una vez terminado cada **;** en tu código puedes observar como finaliza una **consulta** y te muestra un resultado si has consultado por algo en especifico.

---

**Existen otros JOIN**

> Clausula LIMIT para limitar registros

En SQL existen diferentes formas de combinar tablas además del JOIN tradicional con ON. A continuación se describen algunos tipos:

**JOIN UTILIZANDO USING:** La cláusula USING se utiliza cuando las columnas que relacionan tienen ambas tablas que tienen el mismo nombre.

**NATURAL JOIN:** Une automáticamente las tablas usando las columnas  que tengan el mismo nombre en ambas tablas. (Es de cuidado porque une todas las tablas que tengan el mismo nombre.)

**CROSS JOIN:** Realiza un plano cartesiano combinando todos los registros de la primera tabla

> Se menciona un examen/cuestionario para la siguente semana el cual es calificable: Tube 1 respuesta incorrecta - Confundiendo left con right.

---

Se pide seguir las instrucciones de la instructora

```sql
    -- Se pide crear una base de datos
    CREATE DATABASE Practica_19feb26;

    USE Practica_19feb26;
```

Se pide crear un EXCEL con los campos documento, nombreCliente, Direccion    

Se pide ingresar por lo menos tres registos

Se pide que una vez se tengan diferentes registros en una tabla al momento de guardar el excel debe ser con CSV y entonces se explica la función de importar de XAMPP siendo asi este archivo CSV.

¿Qué pasa si mi tabla depende de otra tabla? 

```sql
CREATE TABLE PEDIDOS (
	ID_PEDIDO INT PRIMARY KEY,
    NOMBRE_ENCARGADO VARCHAR(20) NOT NULL,
    CLIENTE INT NOT NULL,
    FOREING KEY (COPIA_CLIENTE) REFERENCES CLIENTE(DOCUMENTO)   
);
```

> Se recomienda mucho repasar











---











## Importación de Archivos CSV - Taller: Biblioteca SQL

> Clase del 23/02/26

Se pide insertar el siguente código SQL:

```sql
    CREATE DATABASE 23FebreroDB;

    USE 23FebreroDB;

    CREATE TABLE SOLICITUD (
        ID INT(11) NOT NULL,
        FECHA DATE NOT NULL,
        TIPOSOLICITUD ENUM('QUEJA', 'FELICITACION', 'RECLAMO') NOT NULL,
        PRIMARY KEY (ID)
    );
```

Y entonces se pide abrir un documento EXCEL con los titulos id, fecha, solicitud con registros insertados. Se comenta que en EXCEL una vez se inserta fechas hay un choque entre formatos por lo que hay que cambiarle el formato de la celda de las fechas. (Debe ser YYYY-MM-DD)

* El formato de exportación es CSV UTF-8

Y se pide guardar el archivo EXCEL como CSV y se pide importarlo en Xampp. (Antes de importarlo, debe estar seleccionada la tabla en la que vamos a insertar los datos y antes de importarlo se debe especificar que estan separados por ;)

Video Recomendado: https://www.youtube.com/watch?v=mObLsAU6Cr4

---

<imgs src="https://dev.mysql.com/img/banners/MySQLInstallerBannerV5.png">

Lectura Recomendada y Descarga de Workbench: https://www.mysql.com/products/workbench/

Se pide realizar un trabajo de forma individual siendo un modelo relacional hecho con MYSQL WORKBENCH explicandose:

* Las llaves doradas son PK

* Los rombos color azul celeste con NOT NULL

* Los rombos de color rojo con FK

Por lo que por medio de la SGBD debemos crear la BD.

> Por esta ocasión pensaba usar workbench para el trabajo, pero por temas de contraseña de administrador no se puede debido a que este trabajo y estos apuntes los realizos en los dispositivos de las instalacioens que generalmente a uno le ofrecen al momento de estudiar en los ambientes de aprendizaje.

Documento Practica 1. Biblioteca en MYSQL

```sql
    -- Lo normal es crear la BD
    CREATE DATABASE BIBLIOTECA_SANTIAGOENCODIGO;

    -- Importante usarla despues para no tener problemas con las siguentes consultas
    USE BIBLIOTECA_SANTIAGOENCODIGO;

    -- Creación de Tablas Maestras

        CREATE TABLE TABLA_SOCIO (
            SOC_NUMERO INT(11) PRIMARY KEY,
            SOC_NOMBRE VARCHAR(45) NOT NULL,
            SOC_APELLIDO VARCHAR(45) NOT NULL,
            SOC_DIRECCION VARCHAR(255) NOT NULL,
            SOC_TELEFONO VARCHAR(10) NOT NULL
        );

        CREATE TABLE TABLA_LIBRO (
            LIB_ISBN BIGINT(20) PRIMARY KEY,
            LIB_TITULO VARCHAR(255) NOT NULL,
            LIB_GENERO VARCHAR(20) NOT NULL,
            LIB_NUM_PAGINAS INT(11) NOT NULL, 
            LIB_DIAS_PRESTAMO TINYINT(4)
        );

            -- Teniendo estas dos tablas ya se puede crear:

            CREATE TABLE TABLA_PRESTAMO (
                PRES_ID VARCHAR(20) PRIMARY KEY,
                PRES_FECHA_PRESTAMO DATE NOT NULL,
                PRES_FECHA_DEVOLUCION DATE NOT NULL,

                -- FK
                SOC_COPIA_NUMERO INT(11) NOT NULL,
                LIB_COPIA_ISBN BIGINT(20) NOT NULL,

                FOREIGN KEY (SOC_COPIA_NUMERO) REFERENCES TABLA_SOCIO (SOC_NUMERO),
                FOREIGN KEY (LIB_COPIA_ISBN) REFERENCES TABLA_LIBRO (LIB_ISBN)                
            );

        -- Ultima Tabla Maestra

        CREATE TABLE TABLA_AUTOR (
            AUT_CODIGO INT(11) PRIMARY KEY,
            AUT_APELLIDO VARCHAR(45) NOT NULL,
            AUT_NACIMIENTO DATE NOT NULL,
            AUT_MUERTE DATE NOT NULL
        );

            -- Ultima Tabla Intermedia

            CREATE TABLE TABLA_TIPOAUTORES (
                -- FK
                COPIA_ISBN BIGINT(20) NOT NULL,
                COPIA_AUTOR INT(11) NOT NULL,
                 
                --  ATRIBUTO PROPIO DE ESTA TABLA
                TIPO_AUTOR VARCHAR(20) NOT NULL,

                    -- Definición de FK

                    FOREIGN KEY (COPIA_ISBN) REFERENCES TABLA_LIBRO (LIB_ISBN),
                    FOREIGN KEY (COPIA_AUTOR) REFERENCES TABLA_AUTOR (AUT_CODIGO)
            );

```

> En esta práctica aprendí a tener más cuidado con el uso de las , por cada atributo o campo nuevo que ingrese en una tabla y por otro lado, tener cuidado con escribir bien la sintaxis al CREATE TABLE.

> Me gusta bastante tambien mirar el modo diseñador.

> Debo repasar la cardinalidad y ¿Qué significa realmente uno a muchos, uno a uno, muchos a muchos?

Ya entonces, le pedí a CHATGPT que realizará los registros. Personalmente no le dedico tiempo porque considero que es muy mecanico y realmente no aprenderia mucho ya sabiendo la estructura para insertar datos.

**Registros - Tabla Socios**

```sql
    INSERT INTO TABLA_SOCIO 
    (SOC_NUMERO, SOC_NOMBRE, SOC_APELLIDO, SOC_DIRECCION, SOC_TELEFONO) 
    VALUES
    (1, 'Ana', 'Ruiz', 'Calle Primavera 123, Ciudad Jardin, Barcelona', '912345678'),
    (2, 'Andrés Felipe', 'Galindo Luna', 'Avenida del Sol 456, Pueblo Nuevo, Madrid', '2123456789'),
    (3, 'Juan', 'González', 'Calle Principal 789, Villa Flores, Valencia', '2012345678'),
    (4, 'María', 'Rodríguez', 'Carrera del Río 321, El Pueblo, Sevilla', '3012345678'),
    (5, 'Pedro', 'Martínez', 'Calle del Bosque 654, Los Pinos, Málaga', '1234567812'),
    (6, 'Ana', 'López', 'Avenida Central 987, Villa Hermosa, Bilbao', '6123456781'),
    (7, 'Carlos', 'Sánchez', 'Calle de la Luna 234, El Prado, Alicante', '1123456781'),
    (8, 'Laura', 'Ramírez', 'Carrera del Mar 567, Playa Azul, Palma de Mallorca', '1312345678'),
    (9, 'Luis', 'Hernández', 'Avenida de la Montaña 890, Monte Verde, Granada', '6101234567'),
    (10, 'Andrea', 'García', 'Calle del Sol 432, La Colina, Zaragoza', '1112345678'),
    (11, 'Alejandro', 'Torres', 'Carrera del Oeste 765, Ciudad Nueva, Murcia', '4951234567'),
    (12, 'Sofía', 'Morales', 'Avenida del Mar 098, Costa Brava, Gijón', '5512345678');
```

Realice lo mismo, pero con GEMINI (Considero que me dio una respuesta mucho más rápida, tube cuidado con el contexto del código SQL que le envie.)

**Registros - Tabla Libro**

```sql
    USE BIBLIOTECA_SANTIAGOENCODIGO;

    INSERT INTO TABLA_LIBRO (LIB_ISBN, LIB_TITULO, LIB_GENERO, LIB_NUM_PAGINAS, LIB_DIAS_PRESTAMO) VALUES
    (1234567890, 'El Sueño de los Susurros', 'novela', 275, 7),
    (9876543210, 'El Laberinto de los Recuerdos', 'cuento', 412, 7),
    (2468135790, 'La Melodía de la Oscuridad', 'romance', 189, 7),
    (1357924680, 'El Jardín de las Mariposas Perdidas', 'novela', 536, 7),
    (8642097531, 'El Reloj de Arena Infinito', 'novela', 321, 7),
    (9517530862, 'Las Crónicas del Eco Silencioso', 'fantasía', 448, 7),
    (3141592653, 'El Secreto de las Estrellas Olvidadas', 'Misterio', 203, 7),
    (2718281828, 'El Bosque de los Suspiros', 'novela', 387, 2),
    (8888888888, 'La Ciudad de los Susurros', 'Misterio', 274, 1),
    (5555555555, 'La Última Llave del Destino', 'cuento', 503, 7),
    (9999999999, 'El Enigma de los Espejos Rotos', 'romance', 156, 7),
    (7777777777, 'El Misterio de la Luna Plateada', 'Misterio', 422, 7);
```

> Al usar GEMINI es necesario tener que especificar que realice el código SQL sino realiza una imagen.

**Registros - Tabla Prestamo**

```sql
    USE BIBLIOTECA_SANTIAGOENCODIGO;

    INSERT INTO TABLA_PRESTAMO (PRES_ID, PRES_FECHA_PRESTAMO, PRES_FECHA_DEVOLUCION, SOC_COPIA_NUMERO, LIB_COPIA_ISBN) VALUES
    ('pres1', '2023-01-15', '2023-01-20', 1, 1234567890),
    ('pres2', '2023-02-03', '2023-02-04', 2, 9999999999),
    ('pres3', '2023-04-09', '2023-04-11', 6, 2718281828),
    ('pres4', '2023-06-14', '2023-06-15', 9, 8888888888),
    ('pres5', '2023-07-02', '2023-07-09', 10, 5555555555),
    ('pres6', '2023-08-19', '2023-08-26', 12, 5555555555),
    ('pres7', '2023-10-24', '2023-10-27', 3, 1357924680),
    ('pres8', '2023-11-11', '2023-11-12', 4, 9999999999),
    ('pres9', '2023-12-29', '2023-12-30', 8, 5555555555);
```

**Registros - Tabla Autor**

```sql
    USE BIBLIOTECA_SANTIAGOENCODIGO;

    INSERT INTO TABLA_AUTOR (AUT_CODIGO, AUT_APELLIDO, AUT_NACIMIENTO, AUT_MUERTE) VALUES
    (123, 'Taylor', '1980-04-15', NULL),
    (456, 'García', '1978-09-27', '2021-12-09'),
    (789, 'Rodríguez', '1985-12-10', NULL),
    (234, 'Medina', '1977-06-21', '2005-09-12'),
    (567, 'Davis', '1983-03-04', '2010-03-28'),
    (890, 'Brown', '1982-11-17', NULL),
    (345, 'Wilson', '1975-08-29', NULL),
    (678, 'Silva', '1986-02-02', NULL),
    (901, 'Soto', '1979-05-13', '2015-11-05'),
    (432, 'Miller', '1981-10-26', NULL),
    (765, 'López', '1976-07-08', NULL),
    (98, 'Smith', '1974-12-21', '2018-07-21');
```

> Es chevere que el XAMPP de la advertencia de que no sea nula.

**Registros - Tabla Tipo Autor**

```sql
    USE BIBLIOTECA_SANTIAGOENCODIGO;

    INSERT INTO TABLA_TIPOAUTORES (COPIA_ISBN, COPIA_AUTOR, TIPO_AUTOR) VALUES
    (1357924680, 123, 'Traductor'),
    (1234567890, 123, 'Autor'),
    (1234567890, 456, 'Coautor'),
    (2718281828, 789, 'Traductor'),
    (8888888888, 234, 'Autor'),
    (2468135790, 234, 'Autor'),
    (9876543210, 567, 'Autor'),
    (1234567890, 890, 'Autor'),
    (8642097531, 345, 'Autor'),
    (8888888888, 345, 'Coautor'),
    (5555555555, 678, 'Autor'),
    (3141592653, 901, 'Autor'),
    (9517530862, 432, 'Autor'),
    (7777777777, 765, 'Autor'),
    (9999999999, 98, 'Autor');
```

De esta forma ya tenemos todos nuestros registros entonces. Se recomienda entonces hacer una selección general de cada una de las tablas.

Y ahora entonces, se pide realizar la siguente consulta:

> Me alegra ahora mirar este código y entenderlo, saber que lo ejecutaré en la consulta y va a funcionar.

> Interesante como se utilizan los apodos para esto.    

```sql
    SELECT AUT_APELLIDO, LIB_ISBN, LIB_TITULO, TIPO_AUTOR
    FROM TABLA_AUTOR A, TABLA_LIBRO L, TABLA_TIPOAUTORES T
    WHERE T.COPIA_AUTOR=AUT_CODIGO AND T.COPIA_ISBN = L.LIB_ISBN
```

Me parece muy agradable cómo se pueden juntar diferentes tablas. Y entonces es interesante tambien mirar por medio del WHERE la conexión entre la PK y la FK pues se comparan igualdades. Y entonces lo relaciono directamente con la situación real de una empresa, en donde muy probablemente esta consulta tendrá un apodo para no tener que escribir este código como tal.

Se pide desarrollar entonces una serie de scripts.

> Me parece interesante como practica lo siguente.

> De ahora en adelante, le recomiendo totalmente: PROHIBIDO TRANSCRIBIR, busque entender el por qué cada palabra en la sintaxis de SQL por cada QUERY que se realice.

1. Modifique el registro 765 de la tabla autor y agréguele una fecha de muerte.

Es interesante el comando `SHOW COLUMNS FROM TABLA_AUTOR;` para mirar qué tablas hay y cómo estan escritas o compuestas.

```sql
    -- Se dice donde será el cambio, ¿En qué tabla?
    UPDATE TABLA_AUTOR  
    -- ¿Cual es el campo que vamos a actualizar?
    SET AUT_MUERTE = '2020-05-10'
    -- ¿Donde vamos a hacer el cambio?
    WHERE AUT_CODIGO = 765;
```

2. Elimine el registro pres9 de la tabla préstamos.

```sql
    -- ¿Donde será el cambio?
    DELETE FROM TABLA_PRESTAMO
    WHERE PRES_ID = 'pres9';
```

3. Realice un query que consulte todos los autores que hayan fallecido.

Recordemos que una QUERY es una consulta, por otro lado en nuestros registros o lo tenemos en 0000-00-00 o directamente la fecha de muerte por lo que podemos asignar la consulta que nos seleccione las que sea diferente a ese valor y por ende:

```sql
    SELECT * FROM TABLA_AUTOR
    WHERE AUT_MUERTE <> '0000-00-00';
```

4. Realice una consulta donde utilice un LIKE y busque los libros que tienen la palabra “susurros”.

> Se entiende realmente qué quiere decir LIKE en SQL?

Recordemos que LIKE se utiliza especialmente para busquedas de texto especificas y por ende:

```sql
    SELECT * FROM TABLA_LIBRO
    -- Me parece interesante que la busqueda es antes y despues que se busca susurros por el % al inicio y al final.
    WHERE LIB_TITULO LIKE '%susurros%';

```

5. Realice una consulta que utilice un BETWEEN que encuentre los autores que nacieron entre 1970-01-01 y 1979-01-01.

> ¿Realmente entiende qué hace BETWEEN en SQL?

Recordemos que BETWEEN es para tener un rango de busqueda

```sql
    SELECT * FROM TABLA_AUTOR
    -- Entonces se utiliza la condicional AND y el BETWEEN para poder tener entonces un rango, en un ambiente empresarial me gustaria verlo.
    WHERE AUT_NACIMIENTO BETWEEN '1970-01-01' AND '1979-01-01'
```

6. Realice una consulta donde utilice las tablas necesarias que permitan mostrar que socios tienen préstamos -sin uso de join

> Recordemos entonces que tenemos una tabla de prestamos con FK de los socios/clientes y de los libros con su codigo ISBN.

Si no usamos JOIN, entonces debemos usar IN o EXISTS para esto.

```sql
    -- Un lugar para comparar.
    SELECT * FROM TABLA_SOCIO 
    
    -- Es como buscar "Estas PK concuerdan con estas FK?"
    WHERE SOC_NUMERO IN (
        SELECT SOC_COPIA_NUMERO FROM TABLA_PRESTAMO
    );
```


7. Realice una consulta donde se muestre el siguiente resultado:

> Tuve que hacer un esfuerzo buscando cada una de las PK Y FK, pero al mirar el de prestamos todo cambio.

```sql
    SELECT LIB_TITULO, SOC_NOMBRE, PRES_FECHA_PRESTAMO, PRES_FECHA_DEVOLUCION
    FROM TABLA_LIBRO L, TABLA_SOCIO S, TABLA_PRESTAMO P
    WHERE S.SOC_NUMERO = P.SOC_COPIA_NUMERO AND L.LIB_ISBN = P.LIB_COPIA_ISBN;
```

8. Realice una consulta donde utilice las tablas necesarias que permitan mostrar que autores tienen libros en calidad de ‘traductor’- sin uso de JOIN

Anteriormente habia realizado estas consultas mirando de acuerdo a lo que realizaba CHATGPT, despues aqui ya teniendo idea, lo intenté.

Primer Resultado (No funcionó): 

```sql
    SELECT * TABLA_TIPOAUTORES WHERE TIPO_AUTOR 'TRADUCTOR', AUTOR_APELLIDO
    FROM TABLA_TIPOAUTORES T, TABLA_AUTOR A
    WHERE T.COPIA_AUTOR = A.AUT_CODIGO
```

Se debia implementar IN para esta consulta en donde:

```sql
    SELECT * FROM TABLA_AUTOR
    -- Comparamos la PK con la FK
    WHERE AUT_CODIGO IN (
        SELECT COPIA_AUTOR
        FROM TABLA_TIPOAUTORES
        -- Se le agrega su condición
        WHERE TIPO_AUTOR = 'Traductor'
    );
```

9. Realizar una consulta donde utilice las tablas necesarias que permitan mostrar que socios tienen préstamos y los ordene por apellido de forma descendente – use JOIN

> ¿Entiende realmente qué es un JOIN?: YO, actualmente no realmente. Pero siento que es muy similar a la solución del punto 7

> La solución de este punto sin INNER JOIN se encuentra en el punto 6.

```sql
    -- Se usa DISTINCT para tener diferentes valores
    SELECT DISTINCT S.SOC_NUMERO, S.SOC_NOMBRE, S.SOC_APELLIDO
    -- Es importante definir el APODO
    FROM TABLA_SOCIO S
    -- Uso de INNER JOIN para mirar cuales concuerdan (pk - fk).
    INNER JOIN TABLA_PRESTAMO P
        ON S.SOC_NUMERO = P.SOC_COPIA_NUMERO
    -- Ahora solo falta definir el ORDEN:
    ORDER BY S.SOC_APELLIDO DESC;
```

10. Realice un LEFT JOIN, entre las tablas préstamo y socio, donde la tabla de la izquierda es socio.

> Entiende realmente qué quiere decir un LEFT JOIN en SQL?

> Reflexione ¿Para qué es esta consulta?: Aparecen todos los registros de la tabla de la izquierda (SOCIO), en donde los prestamos si existen y si no tienen prestamos estos van a aparecer como NULL

> Para hacer este código para esta query, realmente se me dificulta.

```sql
    -- La selección
    SELECT S.SOC_NUMERO, S.SOC_NOMBRE. S.SOC_APELLIDO, P.PRES_ID
        -- Interesante mirar los APODOS por cada tabla.
    FROM TABLA_SOCIO S
    LEFT JOIN TABLA_PRESTAMO P
        -- Comparación entre PK y FK
        ON S.SOC_NUMERO = P.SOC_COPIA_NUMERO;
```










---










## Procedimientos, Funciones, Triggers

> Clase del 02/03/2026

* DML

* DCL

* DDL

* Consulta de Datos

* Productos Cartesiano: INNER JOIN, LEFT JOIN, RIGHT JOIN

* Funciones de Agregado: SUM, MIN, MAX, AVG, COUNT

* Clausulas:

**Lenguaje Transaccional SQL**: son miniprogramas porque es algo especifico que se hacen por medio de funciones, triggers, procedimientos almacenados. En donde hay registros, borrados, consultas y demás procedimientos que pueden ser con parametros o sin parametros en donde depende si necesito esos datos o no.
Existe parametros de entrada y de salida como: IN, IN-OUT, OUT

Funciones: Siempre deben retornar y esta compuesto por sentencias SQL

Triggers: Los disparadores se ejecutan sin necesidad de llamarlos (Como un programa en segundo plano) en donde puede auditar [hacerle seguimiento a los datos | Historial], no hace seguimiento a las consultas, pero sí a todo lo que hace un cambio.

---

**Procedimiento Almacenado**

Esto consume memoria, por ende necesitamos que sea algo que el usuario siempre utilice porque si empezamos a crear un procedimiento por cada consulta esto puede ser muy pesado.

No hay problema si tenemos pocos registros o pocas tablas, pero si tenemos miles de millones.

```sql
    USE CITAS;

    -- Se informa que se debe crear el procedimiento
    CREATE PROCEDURE LISTAPACIENTES()
    SELECT PAC_ID, PAC_NOM, PAC_FECHANACIMIENTO
    FROM PACIENTES;

    -- Invocar Procedimiento
    CALL LISTAPACIENTES()
```

---

**Función**

```sql
    create trigger auditoria_modificacionpacientes before update on pacientes

    for each row 
    -- cada vez que se ejecute el update
    insert into auditoria_pacientes #tabla creadra para la auditoria
    (audi_nombreAnterior,audi_apellidoAnterior,audi_FechaAnterior,
    audi_generoAnterior,audi_nombreNuevo,audi_apellidoNuevo,
    audi_fechaNueva,audi_pacIdentificacion,audi_accion)
    values
    /*Todos los campos de la tabla auditada "pacientes" llevan la palabra old,
    para conservar los datos iniciales*/
    /*Todos los campos de la tabla auditada "pacientes" llevan la palabra new,
    para guardar los nuevos datos*/
    (old.pacNombres,old.pacApellidos,old.pacFechaNacimiento,old.pacGenero,
    new.pacNombres,new.pacApellidos,new.pacFechaNacimiento,new.pacGenero,
    now(),current_user(),new.pacIdentificacion,'Actualización');
```

---

**Procedimientos Almacenados**

Depende de qué gestor uses, pero en phpmyadmin DELIMITER$$, pero en WORKBENCH es DELIMITER//

```sql
    -- Cambiamos el delimitador y lo llamamos desde el inicio

    -- Se usa el signo pesos
    DELIMITER $$ 
    CREATE PROCEDURE get_customer() 
    
    -- minuscula, que hace, y 
    -- el nombre de la tabla de la cual se obtiene los datos y 
    -- finaliza con paréntesis
    BEGIN
        SELECT * FROM CUSTOMER; /*el begin y el end
        significa que esta sentencia hace parte del procedure,
        dejar el delimitador ;*/

    END $$
    DELIMITER ;
    -- y lo dejamos como estaba antes con ;
    -- estos cambios son para mysql, en sql server no se hace.

    -- forma de ejecutar el store procedure
    call sakila.get_customer();
    -- si estamos dentro de la base de datos solo call
    get_customer();
```

Otro ejemplo de un Procedimiento Almanceado:

```sql
    -- ejemplo
    -- cambiamos el delimitador y lo llamamos desde el inicio
    DELIMITER $$ 
    -- se usa el signo pesos
    CREATE PROCEDURE get_customer() 
    -- minuscula, que hace, y 
    -- el nombre de la tabla de la cual se obtiene los datos y 
    -- finaliza con paréntesis
    BEGIN
        SELECT * FROM CUSTOMER; 
        /*el begin y el end
        significa que esta sentencia hace parte del procedure,
        dejar el delimitador ;*/
    END $$
    DELIMITER ;
    -- y lo dejamos como estaba antes con ;
    -- estos cambios son para mysql, en sql server no se hace.

    -- forma de ejecutar el store procedure
    call sakila.get_customer();
    -- Si estamos dentro de la base de datos solo call
    get_customer();
```

Vamos a mirar otro ejemplo por ende creamos una BD:

```sql
    CREATE DATABASE VENTAS;
    USE VENTAS;

    CREATE TABLE CLIENTES (
        ID_CLIENTE INT NOT NULL AUTO_INCREMENT,
        NOMBRE_CLIENTE VARCHAR(20) NOT NULL,
        TELEFONO_CLIENTE BIGINT NOT NULL,
        CORREO_CLIENTE VARCHAR(255) NOT NULL,
        PRIMARY KEY(ID_CLIENTE)
    );

    INSERT INTO CLIENTE (ID_CLIENTE, NOMBRE_CLIENTE, TELEFONO_CLIENTE, CORREO_CLIENTE)
    VALUES 
    (1, 'Ana García', '555-0101', 'ana.garcia@email.com'),
    (2, 'Carlos López', '555-0202', 'carlos.lopez@email.com'),
    (3, 'María Rodríguez', '555-0303', 'maria.rod@email.com'),
    (4, 'Juan Pérez', '555-0404', 'juan.perez@email.com'),
    (5, 'Elena Beltrán', '555-0505', 'elena.b@email.com');
```

Digamos que yo siempre llamo a los clientes y por ende necesito su nombre y numero celular. Será una consulta sencilla

> Esto ya no se puede poner en servidores gratuitos porque ya cobran.

```sql
    CREATE PROCEDURE LISTA_CLIENTES()
    SELECT NOMBRE_CLIENTE, TELEFONO_CLIENTE
    FROM CLIENTES;
```

Para llamar al procedimiento podemos usar:

```sql
    CALL LISTA_CLIENTES();
```

Se menciona que ahora vamos a hacer uso de IN para el parametro NOM siendo asi un procedimiento que usa datos de entrada

```sql
    CREATE PROCEDURE GET_NOMBRE_CLIENTE(IN NOM VARCHAR(20))
    SELECT * FROM CLIENTES
    WHERE NOMBRE_CLIENTE = NOM;

    -- LLamamos a nuestro procedimiento

    CALL GET_NOMBRE_CLIENTE('Elena Beltrán')
```

> Existen tambien parametros por defecto.

**Procedimiento de salida**

Un ejemplo:

```sql
    CREATE PROCEDURE contarProductosPorEstado(
        IN nombre_estado VARCHAR(25),

        -- Numero es la variable que me dirá qué productos estan disponibles
        OUT numero INT)
    -- COUNT va a contar
    SELECT count(id)

    -- Guarda el valor en la variable numero
    INTO numero
    FROM productos
    WHERE estado = nombre_estado;
```

Aplicado a nuestra BD:

```sql
    CREATE PROCEDURE GET_CONTAR_NOMBRE(IN NOM VARCHAR(20), OUT CUENTA INT)
    SELECT COUNT(NOMBRE_CLIENTE)
    INTO CUENTA
    FROM CLIENTES    
    WHERE NOMBRE_CLIENTE = NOM;

    -- LLamamos a nuestro procedimiento

    CALL GET_CONTAR_NOMBRE  ('Elena Beltrán', @CUENTA);
    SELECT @NOMBRE AS 'Cantidad Nombres Seleccionados'
```

Siendo esto variables de salida, muy util en temas de inventarios de salida.

**Variables de Usuario | @**

Solo estan activas mientras mi sesión este activa y podré usar esa variable mientras siga. Estas nos permiten almacenar un valor

```sql
    -- # 1. Declaramos la variable y llamamos al procedimiento
    -- # Usamos el procedimiento de la imagen 3 que tiene un parámetro OUT
    CALL contarProductosPorEstado('activo', @total_activos);

    -- # 2. Consultamos el valor almacenado en la variable de usuario
    SELECT @total_activos AS 'Total de Productos Activos';

    -- # Ejemplo de uso de variable de usuario en una operación simple
    SET @descuento = 0.10;
    SELECT nombre_cliente, (precio * @descuento) AS ahorro 
    FROM CLIENTE;
```

Ahora para temas más de inventario:

```sql
    DELIMITER $$
    CREATE PROCEDURE venderProducto(
        INOUT beneficio FLOAT,
        IN id_producto INT)
    BEGIN
        -- SELECT @incremento_precio = precio
        SELECT precio INTO @incremento_precio
        FROM productos
        WHERE id = id_producto;
        SET beneficio = beneficio + @incremento_precio;
    END $$
    DELIMITER ;

    -- # Ejemplo de ejecución con variables de usuario:
    SET @beneficio=0;

    -- #beneficio=0 id=1 beneficio sería 0+8=8
    CALL venderProducto(@beneficio,1); 
    --  #beneficio=8 id=2 beneficio sería 8+1.5=9.5
    CALL venderProducto(@beneficio,2);
    --  #beneficio=9.5 id=2 beneficio sería 9.5+1.5=11
    CALL venderProducto(@beneficio,2);

    -- Selección del Beneficio total
    SELECT @beneficio;
    SELECT @incremento_precio;
```

---

Se comparte el siguente código para revisar:

```sql
    CREATE TABLE if NOT EXISTS productos (
        id INT NOT NULL AUTO_INCREMENT,
        nombre VARCHAR(20) NOT NULL,
        estado VARCHAR(20) NOT NULL DEFAULT 'disponible',
        precio FLOAT NOT NULL DEFAULT 0.0,
        PRIMARY KEY(id)
    );
    INSERT INTO productos (nombre, estado, precio) 
    VALUES 
    ('Producto A','disponible', 8), ('Producto B', 'disponible', 1.5),('Producto C', 'agotado', 80);
    CREATE PROCEDURE obtenerProductosPorEstado(IN nombre_estado VARCHAR(255))
        SELECT * 
        FROM productos
        WHERE estado = nombre_estado;
    CALL obtenerProductosPorEstado('disponible');
    DELIMITER $$
    CREATE PROCEDURE contarProductosPorEstado(
        IN nombre_estado VARCHAR(25),
        OUT numero INT)
    BEGIN
        SELECT count(id) 
        INTO numero
        FROM productos
        WHERE estado = nombre_estado;
    END$$
    DELIMITER ;
    CALL contarProductosPorEstado('disponible',@numero);
    SELECT @numero AS disponibles;
```

y se pide hacer el siguente procedimiento:

```sql
    DELIMITER $$
    CREATE PROCEDURE venderProducto(
        INOUT beneficio FLOAT,
        IN id_producto INT)
    BEGIN
        #SELECT @incremento_precio = precio
        SELECT precio INTO @incremento_precio
        FROM productos
        WHERE id = id_producto;
        SET beneficio = beneficio + @incremento_precio;
    END $$
    DELIMITER ;

    -- Ejemplo de ejecución:
    SET @beneficio=0;

    CALL venderProducto(@beneficio,1); #beneficio=0 id=1 beneficio sería 0+8=8
    CALL venderProducto(@beneficio,2); #beneficio=8 id=2 beneficio sería 8+1.5=9.5
    CALL venderProducto(@beneficio,2); #beneficio=9.5 id=2 beneficio sería 9.5+1.5=11

    SELECT @beneficio;
    SELECT @incremento_precio;
```

**A continuación un procedimiento para sumar**

```sql
    DROP PROCEDURE IF EXISTS pa_sumar;
    DELIMITER $$
    CREATE PROCEDURE pa_sumar(
        IN V1 INT,
        IN V2 INT)
        BEGIN
            DECLARE suma INT;
            SET suma=V1+V2;/*para modificar una variable utilizamos la palabra set 
    set suma=V1+V2; */
            SELECT suma;
        END$$
    DELIMITER ;

    CALL pa_sumar(1,5);
```

---

Se pide insertar:

```sql
    SELECT CONCAT('Ma', 'ria', 'DB');
    SELECT CONCAT(nombre, estado);
    SELECT SUBSTRING('Knowledgebase', 3, 7);
    SELECT UPPER("SQL Tutorial is FUN!");

    -- La respuesta es 4 elevado a la 2.
    SELECT POW(4, 2);

    SELECT ROUND(135.375, 2);
```

```sql  
    SET lc_time_names = 'es_ES'; #quede en el españo 
    SELECT DATE_FORMAT('1997-10-04 22:23:00', '%d %M %Y') AS 'Nuevo formato';

    -- Para mirar diferencia entre días
    SELECT DATEDIFF('2007-12-31 23:59:59','2007-12-30');
```

---

En convenciones se comenta que es necesario al escribir en SQL:

* fn_nombre: Si es una función

* proc_nombre: Si es un procedimiento











---










## Procedimientos y Funciones Aplicadas en Biblioteca BD

Ahora iremos a el codigo de la biblioteca para poner en practica lo aprendido:

* Para ingresar a este código, puede observar: [03-biblioteca_santiagoencodigo.sql](https://github.com/santiagoencodigo/Guia-Completa-de-Analisis-y-Desarrollo-de-Software/blob/main/Trimestre%20%234/02-construir-bases-de-datos/sql/03-biblioteca_santiagoencodigo.sql)

**Procedimientos Almacenados:**

```sql
    -- Procedimiento sin parametros con una consulta
    DROP PROCEDURE IF EXISTS GET_LISTA_AUTORES;
    CREATE PROCEDURE GET_LISTA_AUTORES()
    SELECT AUT_CODIGO, AUT_APELLIDO
    FROM TABLA_AUTOR
    ORDER BY AUT_APELLIDO DESC;

    CALL GET_LISTA_AUTORES();

    -- Procedimiento con parametro de entrada IN con consulta JOIN
    DROP PROCEDURE IF EXISTS GET_TIPO_AUTOR;

    CREATE PROCEDURE GET_TIPO_AUTOR(VARIABLE VARCHAR(20))
        SELECT AUT_APELLIDO AS 'Autor', TIPO_AUTOR
        FROM TABLA_AUTOR
        INNER JOIN TABLA_TIPOAUTORES
        ON AUT_CODIGO = COPIA_AUTOR
        WHERE TIPO_AUTOR = VARIABLE;

    CALL GET_TIPO_AUTOR('Traductor');

    -- Procedimiento para Insertar
    DROP PROCEDURE IF EXISTS INSERT_LIBRO;

    CREATE PROCEDURE INSERT_LIBRO(C1_ISBN BIGINT(20), C2_TITULO VARCHAR(255), C3_GENERO VARCHAR(20), C4_PAGINAS INT(11), C5_DIASPRES TINYINT(4))
    
        INSERT INTO TABLA_LIBRO (LIB_ISBN, LIB_TITULO, LIB_GENERO, LIB_NUM_PAGINAS, LIB_DIAS_PRESTAMO)

        VALUES (C1_ISBN, C2_TITULO, C3_GENERO, C4_PAGINAS, C5_DIASPRES);

    CALL INSERT_LIBRO(9788426721006,'sql','ingenieria',384,15);

    SELECT * FROM TABLA_LIBRO;
```

Se pide entonces:

1. Hacer un procedimiento con un LEFT JOIN entre las tablas socio y préstamo,
donde la prioridad es la tabla socio.

> Debo estudiar este tema, porque realmente no podría solucionarlo.

```sql
    -- Es buena practica eliminar si existe.
    DROP PROCEDURE IF EXISTS GET_SOCIOS_PRESTAMOS;

    DELIMITER $$

    CREATE PROCEDURE GET_SOCIOS_PRESTAMOS()
    BEGIN
        SELECT S.SOC_NUMERO, S.SOC_NOMBRE, S.SOC_APELLIDO, P.PRES_ID
        FROM TABLA_SOCIO S
        LEFT JOIN TABLA_PRESTAMO P
            ON S.SOC_NUMERO = P.SOC_COPIA_NUMERO
        ORDER BY S.SOC_APELLIDO;
    END $$

    -- Es importante que halla un espacio entre DELIMITER y ;
    DELIMITER ;

    -- Ejecución del Procedimiento para observar el LEFT JOIN

    CALL GET_SOCIOS_PRESTAMOS();
```

2. Hacer procedimiento para listar los libros que están en préstamo con su
correspondiente socio con un INNER JOIN

> Debo estudiar este tema, porque tampoco podria solucionarlo... Aunque tengo idea pues entiendo que estoy escribiendo. Pero no podría escribirlo de la nada, me falta práctica

```sql
    DROP PROCEDURE IF EXISTS GET_LIBRO_EN_PRESTAMO;

    DELIMITER $$

    CREATE PROCEDURE GET_LIBRO_EN_PRESTAMO()
    BEGIN  
        SELECT L.LIB_ISBN, L.LIB_TITULO, S.SOC_NUMERO, S.SOC_NOMBRE, S.SOC_APELLIDO, P.PRES_ID

        FROM TABLA_PRESTAMO P
        INNER JOIN TABLA_LIBRO L
            ON L.LIB_ISBN = P.LIB_COPIA_ISBN
        INNER JOIN TABLA_SOCIO S
            ON S.SOC_NUMERO = P.SOC_COPIA_NUMERO
        ORDER BY S.SOC_APELLIDO;
    END $$

    DELIMITER ;

    CALL GET_LIBRO_EN_PRESTAMO();

```

3. Hacer un procedimiento para insertar un socio

```sql
    DROP PROCEDURE IF EXISTS INSERT_SOCIO;

    DELIMITER $$

    CREATE PROCEDURE INSERT_SOCIO(
        P_SOC_NUMERO int(11),
        P_SOC_NOMBRE varchar(45),
        P_SOC_APELLIDO varchar(45),
        P_SOC_DIRECCION varchar(255),
        P_SOC_TELEFONO varchar(10)
    )

    BEGIN
        INSERT INTO TABLA_SOCIO (
            SOC_NUMERO,
            SOC_NOMBRE,
            SOC_APELLIDO,
            SOC_DIRECCION,
            SOC_TELEFONO
        )

        VALUES (
            P_SOC_NUMERO,
            P_SOC_NOMBRE,
            P_SOC_APELLIDO,
            P_SOC_DIRECCION,
            P_SOC_TELEFONO
        );
    END $$

    DELIMITER ;

    CALL INSERT_SOCIO(13, 'Cristian', 'Ruiz', 'Calle San Bernardino, Ciudad Jardin, Bogotá', '912342638');

```

4. Hacer un procedimiento para buscar por nombre del libro.

```sql
    DROP PROCEDURE IF EXISTS BUSCAR_LIBRO_POR_NOMBRE;

    DELIMITER $$
    CREATE PROCEDURE BUSCAR_LIBRO_POR_NOMBRE ( 
        IN P_TITULO VARCHAR(255))
    BEGIN
        SELECT LIB_ISBN, LIB_TITULO, LIB_GENERO, LIB_NUM_PAGINAS
        FROM TABLA_LIBRO
        -- Los % deben ir en comillas.
        WHERE LIB_TITULO LIKE CONCAT('%', P_TITULO, '%');
    END $$

    DELIMITER ;

    CALL BUSCAR_LIBRO_POR_NOMBRE('sql');
```

5. Hacer un procedimiento para actualizar el teléfono y dirección de un socio.

> Para estos es bueno pensar en ¿Qué debe hacer?

```sql
    DROP PROCEDURE IF EXISTS ACTUALIZAR_DATOS_SOCIO;

    DELIMITER $$

    CREATE PROCEDURE  ACTUALIZAR_DATOS_SOCIO(
        IN P_SOC_NUMERO INT,
        IN P_SOC_NUEVA_DIRECCION VARCHAR(255),
        IN P_SOC_NUEVO_TELEFONO VARCHAR(10)
    )

    BEGIN 
        UPDATE TABLA_SOCIO
        SET  
            SOC_DIRECCION = P_SOC_NUEVA_DIRECCION,
            SOC_TELEFONO = P_SOC_NUEVO_TELEFONO
        WHERE SOC_NUMERO = P_SOC_NUMERO;
    END $$

    DELIMITER ;

    CALL ACTUALIZAR_DATOS_SOCIO(10, 'Avenida Bosa - Las Margaritas', 43144314)

```

6. Hacer un procedimiento para eliminar un libro (cuidado: no debe tener
dependencias)

> No se puede eliminar si está relacionado en TABLA_PRESTAMO.

```sql
    DROP PROCEDURE IF EXISTS ELIMINAR_LIBRO;

    DELIMITER $$

    CREATE PROCEDURE ELIMINAR_LIBRO(
        IN P_LIB_ISBN BIGINT 
    )
    BEGIN 
        -- Con esto verificamos si el libro tiene prestamos asociados.
        IF NOT EXISTS (
            SELECT 1
            FROM TABLA_PRESTAMO
            WHERE LIB_COPIA_ISBN = P_LIB_ISBN
        ) THEN 
            DELETE FROM TABLA_LIBRO
            WHERE LIB_ISBN = P_LIB_ISBN;
        -- END IF contiene ; al final.
        END IF;
    END $$

    DELIMITER ;

    CALL ELIMINAR_LIBRO(9788426721006);
```

7. Hacer una función que devuelva cuantos socios hay registrados.

> Ya una función usa RETURN

```sql
    DROP FUNCTION IF EXISTS CONTAR_SOCIOS;

    DELIMITER $$
    
    CREATE FUNCTION CONTAR_SOCIOS()

    -- Se especifica que retorne un número
    RETURNS INT DETERMINISTIC
    BEGIN 
        -- Nuestra variable | Guardará el valor de los socios
        DECLARE TOTAL INT;

        SELECT COUNT(*)
        INTO TOTAL 
        FROM TABLA_SOCIO;

        RETURN TOTAL;
    END $$
    
    DELIMITER ;

    SELECT CONTAR_SOCIOS() AS TOTAL_SOCIOS;
```

8. Hacer una función que devuelve cuantos días ha estado en préstamo ese
libro. Parámetros (idlibro), usar la función integrada DATEDIFF.

```sql
    DROP FUNCTION IF EXISTS DIAS_EN_PRESTAMO;

    DELIMITER $$

    CREATE FUNCTION DIAS_EN_PRESTAMO(
        P_LIB_ISBN BIGINT
    )
    -- RETURNS solo se usa para definir el tipo de dato
    RETURNS INT DETERMINISTIC

    BEGIN 
        DECLARE DIAS INT;

        SELECT DATEDIFF(CURDATE(), PRES_FECHA_PRESTAMO)
        INTO DIAS
        FROM TABLA_PRESTAMO
        WHERE LIB_COPIA_ISBN = P_LIB_ISBN
        LIMIT 1;

        RETURN DIAS;
    END $$

    DELIMITER ;

    SELECT DIAS_EN_PRESTAMO(7777777777) AS DIAS;
```










---










## Triggers

> Clase del 5/03/2026

Un uso común de los triggers es para la auditoria. Uno no deberia borrar los datos "Asi como asi", generalmente se pasa a otra tabla.

Si retiras tu cuenta bancaria, el banco no te elimina sino que hace un backup de como estuvo la historia contigo y generalmente se retiene esta información en un periodo de 10 años dependiendo de las politicas de datos de la empresa.

La auditoria crea una tabla nueva si o si.

1. Primero se tiene que crear la tabla de respaldo.

2. Despues se crea el trigger.

> Podemos pensar de un trigger como el "Lo q    ue habia antes, lo que hay ahora."

Se pide escribir el siguente código sql de un trigger de procedimiento.

```sql

    CREATE DATABASE Productos_santiagoencodigo;
    USE Productos_santiagoencodigo;

    CREATE TABLE Producto(
        productoID INT PRIMARY KEY,
        nombrePro VARCHAR(30) NOT NULL,
        precioPro INT NOT NULL,
        cantidadTotalPro INT NOT NULL);
        
    CREATE TABLE Entrada(
        entradaID INT PRIMARY KEY,
        fechaEntrada DATE NOT NULL,
        cantidadEntrada INT NOT NULL,
        productoID INT NOT NULL,
        FOREIGN KEY (productoID) REFERENCES Producto(productoID));
        
    INSERT INTO Producto(productoID,nombrePro, precioPro, cantidadTotalPro)
    VALUES (1,'Panela',200,0),(2,'Pastas doria familiar',3500,0);

    DROP TRIGGER IF EXISTS entrada_producto;
    DELIMITER $$
        CREATE TRIGGER entrada_producto BEFORE INSERT
        ON Entrada FOR EACH ROW
        BEGIN
            UPDATE Producto 
            SET cantidadTotalPro=Producto.cantidadTotalPro+new.cantidadEntrada
            WHERE new.productoID=Producto.productoID;
        END$$
    DELIMITER ;

    INSERT INTO entrada(entradaID, fechaEntrada, cantidadEntrada, productoID) 
    VALUES (001,'2020-10-06',10,1);

    SELECT * FROM Producto;

    -- detalle los cambios en la tabla producto
    INSERT INTO entrada(entradaID, fechaEntrada, cantidadEntrada, productoID) 
    VALUES (002,'2020-10-06',13,1);
    INSERT INTO entrada(entradaID, fechaEntrada, cantidadEntrada, productoID) 
    VALUES (003,'2020-10-06',50,2);
    SELECT * FROM Producto;
```

Se nos pide volver a la base de datos de nuesrta biblioteca e insertar el nuevo trigger que servira de auditoria en la tabla socios sino quiero que se pierda nada.

```sql
    CREATE TABLE AUDI_SOCIO(
        ID_AUDI INT(10) AUTO_INCREMENT,
        SOC_NUMERO_AUDI INT(11),
        SOC_NOMBRE_ANTERIOR VARCHAR(45),
        SOC_APELLIDO_ANTERIOR VARCHAR(45),
        SOC_DIRECCION_ANTERIOR VARCHAR(255),
        SOC_TELEFONO_ANTERIOR VARCHAR(10),
        
        SOC_NOMBRE_NUEVO VARCHAR(45),
        SOC_APELLIDO_NUEVO VARCHAR(45),
        SOC_DIRECCION_NUEVO VARCHAR(255),
        SOC_TELEFONO_NUEVO VARCHAR(10),

        -- En qué fecha se modifico?
        AUDI_FECHA_MODIFICACION DATETIME,

        -- ¿Cual fue el usuario que modifico?
        AUDI_USUARIO VARCHAR(10),

        -- ¿Qué hizo el usuario?
        AUDI_ACCION VARCHAR(45),
        PRIMARY KEY(ID_AUDI)
    );
```

Una vez teniendo esa tabla se pide escribir el trigger.

```sql
    DROP TRIGGER IF EXISTS SOCIOS_BEFORE_INSERT;

    DELIMITER $$

    CREATE TRIGGER SOCIOS_BEFORE_INSERT
    BEFORE INSERT ON TABLA_SOCIO
    FOR EACH ROW
    BEGIN

    INSERT INTO AUDI_SOCIO(

        SOC_NUMERO_AUDI,

        SOC_NOMBRE_NUEVO,
        SOC_APELLIDO_NUEVO,
        SOC_DIRECCION_NUEVO,
        SOC_TELEFONO_NUEVO,

        AUDI_FECHA_MODIFICACION,
        AUDI_USUARIO,
        AUDI_ACCION

    )

    VALUES(

        NEW.SOC_NUMERO,
        NEW.SOC_NOMBRE,
        NEW.SOC_APELLIDO,
        NEW.SOC_DIRECCION,
        NEW.SOC_TELEFONO,

        NOW(),
        CURRENT_USER(),
        'INSERT'

    );

    END $$

    DELIMITER ;
```

Entonces si se actualiza, si se borra y demás acciones. Esto va a aparecer en una nueva tabla que mostrara tanto los viejos como los nuevos.

Despues entonces se pide que hagamos un trigger por si se borran datos.

```sql
    DROP TRIGGER IF EXISTS SOCIOS_BEFORE_UPDATE;

    DELIMITER $$

    CREATE TRIGGER SOCIOS_BEFORE_UPDATE
    BEFORE UPDATE ON TABLA_SOCIO
    FOR EACH ROW
    BEGIN

    INSERT INTO AUDI_SOCIO(

        SOC_NUMERO_AUDI,

        SOC_NOMBRE_ANTERIOR,
        SOC_APELLIDO_ANTERIOR,
        SOC_DIRECCION_ANTERIOR,
        SOC_TELEFONO_ANTERIOR,

        SOC_NOMBRE_NUEVO,
        SOC_APELLIDO_NUEVO,
        SOC_DIRECCION_NUEVO,
        SOC_TELEFONO_NUEVO,

        AUDI_FECHA_MODIFICACION,
        AUDI_USUARIO,
        AUDI_ACCION

    )

    VALUES(

        OLD.SOC_NUMERO,
        OLD.SOC_NOMBRE,
        OLD.SOC_APELLIDO,
        OLD.SOC_DIRECCION,
        OLD.SOC_TELEFONO,

        NEW.SOC_NOMBRE,
        NEW.SOC_APELLIDO,
        NEW.SOC_DIRECCION,
        NEW.SOC_TELEFONO,

        NOW(),
        CURRENT_USER(),
        'UPDATE'

    );

    END $$

    DELIMITER ;
```

```sql
    -- ojo no se puede eliminar un registro que tenga FK
    -- registros asociados a otras tablas
    DELETE FROM tbl_socio
    WHERE soc_numero=123456;

    -- consultar tabla de auditoria
    SELECT * FROM audi_socio;
```

---

**Actividad de la Sesión, se pide generar los siguentes triggers:**

+ Un trigger de auditoria para un insert.

+ Un trigger de auditoria para un update.

+ Un trigger de auditoria para un delete en la tabla libro.

Si queremos hacer esto, primero debemos crear nuestra tabla para auditorias:

```sql
    CREATE TABLE AUDI_LIBRO(
        ID_AUDI INT AUTO_INCREMENT,

        LIB_ISBN_AUDI BIGINT,

        LIB_TITULO_ANTERIOR VARCHAR(255),
        LIB_GENERO_ANTERIOR VARCHAR(50),
        LIB_NUM_PAGINAS_ANTERIOR INT,

        LIB_TITULO_NUEVO VARCHAR(255),
        LIB_GENERO_NUEVO VARCHAR(50),
        LIB_NUM_PAGINAS_NUEVO INT,

        AUDI_FECHA_MODIFICACION DATETIME,
        AUDI_USUARIO VARCHAR(50),
        AUDI_ACCION VARCHAR(20),

        PRIMARY KEY(ID_AUDI)
    );
```

Y luego hay si se crea el Trigger de Auditoria para INSERT:

```sql
    DROP TRIGGER IF EXISTS LIBRO_BEFORE_INSERT;

    DELIMITER $$

    CREATE TRIGGER LIBRO_BEFORE_INSERT
    BEFORE INSERT ON TABLA_LIBRO
    FOR EACH ROW
    BEGIN

    INSERT INTO AUDI_LIBRO(

        LIB_ISBN_AUDI,

        LIB_TITULO_NUEVO,
        LIB_GENERO_NUEVO,
        LIB_NUM_PAGINAS_NUEVO,

        AUDI_FECHA_MODIFICACION,
        AUDI_USUARIO,
        AUDI_ACCION

    )

    VALUES(

        NEW.LIB_ISBN,
        NEW.LIB_TITULO,
        NEW.LIB_GENERO,
        NEW.LIB_NUM_PAGINAS,

        NOW(),
        CURRENT_USER(),
        'INSERT'

    );

    END $$

    DELIMITER ;
```

Y entonces se crea el Trigger Auditoria Update:

```sql
    DROP TRIGGER IF EXISTS LIBRO_BEFORE_UPDATE;

    DELIMITER $$

    CREATE TRIGGER LIBRO_BEFORE_UPDATE
    BEFORE UPDATE ON TABLA_LIBRO
    FOR EACH ROW
    BEGIN

    INSERT INTO AUDI_LIBRO(

        LIB_ISBN_AUDI,

        LIB_TITULO_ANTERIOR,
        LIB_GENERO_ANTERIOR,
        LIB_NUM_PAGINAS_ANTERIOR,

        LIB_TITULO_NUEVO,
        LIB_GENERO_NUEVO,
        LIB_NUM_PAGINAS_NUEVO,

        AUDI_FECHA_MODIFICACION,
        AUDI_USUARIO,
        AUDI_ACCION

    )

    VALUES(

        OLD.LIB_ISBN,

        OLD.LIB_TITULO,
        OLD.LIB_GENERO,
        OLD.LIB_NUM_PAGINAS,

        NEW.LIB_TITULO,
        NEW.LIB_GENERO,
        NEW.LIB_NUM_PAGINAS,

        NOW(),
        CURRENT_USER(),
        'UPDATE'

    );

    END $$

    DELIMITER ;
```

Y finalmente un trigger de auditoria para DELETE:

```sql
    DROP TRIGGER IF EXISTS LIBRO_BEFORE_DELETE;

    DELIMITER $$

    CREATE TRIGGER LIBRO_BEFORE_DELETE
    BEFORE DELETE ON TABLA_LIBRO
    FOR EACH ROW
    BEGIN

    INSERT INTO AUDI_LIBRO(

        LIB_ISBN_AUDI,

        LIB_TITULO_ANTERIOR,
        LIB_GENERO_ANTERIOR,
        LIB_NUM_PAGINAS_ANTERIOR,

        AUDI_FECHA_MODIFICACION,
        AUDI_USUARIO,
        AUDI_ACCION

    )

    VALUES(

        OLD.LIB_ISBN,
        OLD.LIB_TITULO,
        OLD.LIB_GENERO,
        OLD.LIB_NUM_PAGINAS,

        NOW(),
        CURRENT_USER(),
        'DELETE'

    );

    END $$

    DELIMITER ;
```

---
