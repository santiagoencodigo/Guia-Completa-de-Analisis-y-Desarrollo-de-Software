# Modelado de Artefactos de Software

# Bases de datos

### ¿Qué es una base de datos?

Es una colección organizada y estructurada de información que se almacena electrónicamente para facilitar su acceso, gestión y actualización. (Permiten almacenar grandes volúmenes de datos)

Su desarrollo es de forma lineal (waterfall) se realizan los siguentes procesos:

1. Requerimientos Funcionales
2. Casos de Uso
3. Modelo Entidad Relación (MER) = DFD

<img src = "https://imgs.search.brave.com/1mJ17W7EwQcYGb7OMSnHDzEKooUD8cpd_iAawSWSkZo/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9zdC5k/ZXBvc2l0cGhvdG9z/LmNvbS8xMDUwMjY3/LzIzMjgvaS80NTAv/ZGVwb3NpdHBob3Rv/c18yMzI4NzQ4OC1z/dG9jay1waG90by1k/YXRhYmFzZS1jb25j/ZXB0LXdpdGgtbGFw/dG9wLXRhYmxldC5q/cGc">

*Imagen Tomada de: https://depositphotos.com/es/photos/base-de-datos.html*

### Motor de Bases de Datos

#### Los 6 Motores de Bases de Datos más reconocidos en el mercado

Oracle: Es el motor relacional más antiguo, comenzó el negocio de las bases de datos. En ese entonces no era un negocio sino un proyecto cientifico, fue entonces que [Larry Ellison](https://www.forbes.com/profile/larry-ellison/) vio potencial y fundo la empresa. (Hoy en día es de los 10 hombres más ricos en el mundo)
  
Microsoft SQL Server: Es la respuesta de Microsoft hacia Oracle, paso muchos años sólo funcionando para windows, fue desde 2017 que ha sido multiplataforma. (Son lideres en Business Intelligence)

My SQL: Es el motor más usado por los desarrolladores

SQlite: Es una base de datos pequeña, es muy usada para hacer persistencia local en aplicaciones móviles

PostgreSQL: Inicio como un proyecto universitario llamado INGRES, inspirado en Oracle e incluyó funciones avanzadas y tiggers que MySQL no tuvo por años.

MariaBD:

### Gestor de bases de datos


### Un objeto en BD

Hay dos tipos de bases de datos (relacionales y no relacionales) 

## Tipos de Bases de Datos


### BD Relacional

Relacional SQL: Son datos estructurados con relaciones entre tablas y se usa en ERP, ventas, RRHH y generalmente utiliza los motores MySQL, SQL, PostgreSQL, Oracle

Los objetos estan relacionados entre sí


### BD No Relacional

No Relacional NoSQL

Datos no estruturados o semiestructurados (documentos, grafos, etc..) un ejemplo claro con las redes sociales, loT, big data y generalmente tiene los motores MongoDB, Cassandra, Redis

Se necesitan los documentos entidad, relación y los casos de uso para determinar que tablas y atributos se necesitan.

Se plantea utilizar XAMPP (mysql)

primero fue SQL (Structured Query Language), que en español significa **Lenguaje de Consulta Estructurada** 


### BD Orientada a objetos

Almacena datos como objetos del lenguaje de programación, generalmente se ve en aplicaciones java, C#, y utiliza los motores db4o, objetctDB


### BD Distribuida

bases de datos replicada en varios servidores o ubicaciones, se ve en sistemas de alta disponibilida y tiene los motores cockroachDB y Cassandra

arquitectura modelo servidor


### BD en Memoria

Datos almacenados en RAM para alta velocidad, 

---

### Tenemos:

* SQL que cuesta dinero y generalmente es usado por las empresas
* MySQL es FREE y pertenece a oracle y sirve para un proyecto pequeño y local.

  Los dos funcionan de una forma muy similar

>https://www.w3schools.com/sql/sql_select.asp

>https://sqliteonline.com/
 

### Herramientas:

* [Xampp](https://www.apachefriends.org/ "apachefriends.org")
  
* [Visual Studio Code](https://code.visualstudio.com/ "Visual Studio")
  
* [SQL Sever Mangement Studio](https://www.microsoft.com/es-es/sql-server/sql-server-downloads "Microsoft - SQL")


Una tabla se representa como una cuadricula (Entonces usaremos c# o draw.io) 


### Ejemplo de aplicación

Como buenas Prácticas Los nombres deben ser estilo entidad y especificación, debe ser corto y simple, es decir:

* Entidad_Tabla_Atributo
  
* usuario_Crear

En un requerimiento funcional donde su caso de uso es "CREAR USUARIO" 

Por lo que la fila en esta tabla puede ser: Cedula, Cod_Usuario, Nom_Usuario, Ape_Usuario, Correo_Usuario, Tipo_Usuario



---



## Modelo Entidad Relación (MER)

Entidades: Un objeto en la base de datos = Tabla






# Casos de Uso

## ¿Qué es un Caso de Uso?

Salen de los requerimientos y son los casos de uso

Se inicia con la pregunta ¿Quien va a usar el sistema?

Generalmente en el sistema el usuario pide información, por lo que... ¿Cómo accede a esta información?


---
