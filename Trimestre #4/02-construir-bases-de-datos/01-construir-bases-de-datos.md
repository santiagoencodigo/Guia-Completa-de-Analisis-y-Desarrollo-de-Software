# Construir Bases de Datos

> Se recuerda el comportamiento que debemos tener: Llegadas tarde, el aseo de la estación de trabajo, etc...

> 14 de abril finaliza el trimestre

"Estará la tentación a la inteligencia artificial", se recomienda primero realizar el análisis del trabajo antes de directamente delegarlo a la inteligencia artificial.

A continuación viene una serie de apuntes y/o documentación respecto a lo que se va a ver en la construcción de bases de datos con la instructora Angelica Triana en el cuarto de nueve trimestres de la formación.






---










## Tabla de Contenidos

[1. Introducción](#introducción)

[2. Bases de Datos](#bases-de-datos)










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












##