# Construcción de Software 

A continuación mis apuntes y/o documentación de los temas vistos en Construcción del Software con la instructora Angelica Triana en el cuarto de nueve trimestres. El enfoque de este área es **git y github**. 










## Tabla de Contenido

[1. Estandarización](#estandarización)

[2. Control de Versiones](#control-de-versiones)

[3. Git y Github](#git-y-github)

[4. Comandos de Git](#comandos-de-git)











---











## Estandarización

Para tener ciertos certificados se debe trabajar con ISO con buenas practicas. 

Para nosotros esto seria la convención o guía de código. ¿Cómo podemos hace un mejor código? Teniendo en cuenta entonces que debe ser limpio, legible. Po rende debemos:

* Tener cuidado con la nomenclatura

* La sangria | Identación

* DRY - Don´t repeat yourself

Tener en cuenta si el lenguaje solicita minusculas como HTML o mayusculas como SQL.

Todo esto es para identificar donde hacer cambios, matenimiento y demás.

**Dentro de las buenas practicas esta el control de versiones**. Anteriormente se hacia el control de versiones mediante comentarios.

El control de versiones permite copias de seguridad, try-cath o agarrar el error para que el programa pueda seguir funcionando, sirve para temas de recuperación.

Es importante dejar comentarios para recordar qué se debe hacer, tienen que ser precisos.

Las buenas prácticas nos llevara a los requerimientos funcionales, porque asi puede ser seguro, comprobable, adaptable, mantenible.

Es importante tener variables bien escritas y no a mitad.

El espaciado es muy agradable para la lectura.

---

Se pide realizar la siguente lectura: https://www.neoguias.com/tipos-notacion-nombres/

Camel case = valorDescuento

valor-descuento = Kebal Case 

valorDescuento = 

valcular_descuento = Snake Case

En las propias páginas de los lenguajes de programación se comenta cuales son los tipos de escritura

Digamos... Veremos entonces diferentes formas de escribir hola mundo

python = print("Hola Mundo")

php = <?php> echo "Hola Mundo" ?>

Java = 

JS = console.log("hola mundo")

C# = using System; namespace Hola Mundo { class {...}}

<img src="">

---

**¿Por qué tener estandares de codificación?**

Nos ahorra dinero, nos ahorra costos en ese sentido para su analisis, diseño, implementación, mantenimiento.

Se nos pide hacer un cuadro comparativo por cada lenguaje de programación verificando que tipo de escritura se maneja. Se debe realizar descripción, y un ejemplo.














---








## Control de Versiones

¿Qué es repositorio?

¿Cómo guardamos?

¿Cómo nombramos el control de versiones?

Debemos pensar de esto como un arbol, el tronco seria lo principal y las ramas sera las otras versiones de esto.

¿Cómo controlamos los cambios?

¿Qué es un control de versiones?

Es gestionar el codigo de fuente, modificar, agregar, eliminar y como tal un rastreo.

Anteriormente el control de versiones.

git fue hecho por linus torvals en tan solo 10 días.

versiones por número en donde el numero menor que seria 1, 2, 3 y demás.

En la nomenclatura si se utiliza 1.2.2 o numeros despues de puntos son pequeñas corecciones.

El numero principal cambia cuando la estructura cambia todo.

---

De ahora en adelante, para mis repositorios voy a redactarlo con 1.2.3, 1.2.4, 1.2,5 y asi para tener un control más elegante y ciudadoso con los temas llevando asi un seguimiento profesional y más exacto teniendo una numeración para cada cambio siendo asi: EN desarrollo web con 180 commits, deberian haber entonces 180 números con esta estructura.

---

En git, se explica el release candidate, RTM = Release to , GA

Versión parche en donde aveces se pueden colocar 4 números. En donde la propia empresa se encuentra de una vulnerabilidad. 

Se puede versión por fechas: 1.2.3.1543 (Año mes día)

El problema del control de versiones es que las empresas tienen su propia estandarización

Es curioso entonces que Android pone un numero y luego el nombre de un dulce.

> Investigar Control de versiones de netflix

> ¿Puedo encontrar el control de versiones de diferentes empresas?

* La funcionalidad de las ramas es principalmente cuando se va a agregar algo nuevo.

---

Se recomienda la siguente lectura: https://medium.com/@jointdeveloper/sistemas-de-control-de-versiones-qu%C3%A9-son-y-por-qu%C3%A9-amarlos-24b6957e716e

**A continuación mis apuntes sobre esta lectura**

> Reconocimiento en que los demás aprendices asi como yo van por ese camino de Ingenieria 

Todo cambia una vez conoces el control de versiones

> Reflexión, cuestionese y preguntese ¿Conozco realmente qué es el control de versiones y que uso le puedo dar?

Vamos a iniciar hablando sobre el antes del control de versiones

<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/0*vjveQSD3TKHoqHc6.jpg">

*Imagen Tomada De: https://medium.com/@jointdeveloper/sistemas-de-control-de-versiones-qu%C3%A9-son-y-por-qu%C3%A9-amarlos-24b6957e716e*

El control de versiones registra cada uno de los cambios que se realiza en un archivo o en un conjunto de archivos. Siendo asi facil recuperar versiones especificas, elementos funcionales del sistema, corregir errores y demás

> La imagen a continuación me agrado bastante, refleja totalmente lo que es un control de versiones en donde cada commit agrega algo nuevo.

<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/0*qhbqSpJTrjqRNRSF.png">

*Imagen Tomada De: https://medium.com/@jointdeveloper/sistemas-de-control-de-versiones-qu%C3%A9-son-y-por-qu%C3%A9-amarlos-24b6957e716e*

Los sistemas de control de versiones han tenido sus propios controles de versiones y su ciclo de vida. Pues han habido programadores más experimentados que estaban trabajando por este proyecto.

> Ingenieros de Software que trabajaron por esto. ¿Existe un modelo de negocio?

Lo que más me gusta de esto, es que tenemos total control de las versiones sin tener que alterar la principal, **the main branch**

> El control de versiones se guarda en una BD, mis repos estan en las BD de github. Este documento está en una BD de github.

Anteriormente se tenian diferentes versiones de los archivos o del conjunto de archivos, pero como archivos aparte, con carpetas con diferente nombre. 

* Habrá gente que tuvo que pensar en como nombrar a su versión del proyecto: "Versión del proyecto final, final, final.", "Proyecto Copia"

De esta forma el control de versionamiento estaba en los computadores de cada persona, siendo de esta forma: Un problema para la compatibilidad, union de contribuciones o aportes al código, por ende era dificil compartirse código.

---

Eventualmente surgieron **los sistemas de control de versiones centralizados**

En donde estos ya no estan en los computadores de cada persona, sino en un servidor.

* Qué es un Servidor by GoDaddy: https://www.godaddy.com/resources/latam/digitalizacion/servidor-que-es-tipos

Esto trajo un nuevo reto: ¿Cómo trabajar en un mismo archivo al mismo tiempo? Pues los usuarios invalidaban los aportes de otros usuarios.

> Yo todavía no he trabajado en un desarrollo de software de algún programa y todavia no he visto como es ese flujo de trabajo. Será interesante mirar cómo se organizan las empresas para esto.

Esto funciono para proyectos con pocas actualizaciones, pero no para proyectos con docenas de contribuyentes activos que realizaban correciones a diario.

Entonces surgió un **control de versiones descentralizado** en donde ya no hay un repositorio centralizado sino a cada desarrollador una copia local del sistema en donde cada dev puede trabajar de manera aislada, pero teniendo un sistema de contribuciones sobre contribuciones y demás resoluciones de conflictos.

Hay diferentes controles de versiones, por ende recomendable investigar:

* [CVS](https://es.wikipedia.org/wiki/CVS "CVS by Wikipedia")

* [Git](https://git-scm.com/ "https://git-scm.com/")

* [Subversion](https://subversion.apache.org/ "Subversion")

* [Mercurial](https://www.mercurial-scm.org/ "https://www.mercurial-scm.org/")

* [Baazar](https://es.wikipedia.org/wiki/Bazaar_(software))

Siempre hay un contexto de interminables cambios.

Muchas personas trabajando de forma simultanea en el código. Puede haber incompatibilidad entre librerias.

Se permite trabajar de forma colaborativa, distribución del trabajo, integrar el trabajo, crear | recuperar versiones, crear ramas, y mucho más.














---














## Git y Github

git es lo local, se tiene que instalar.

github ya es distribución

Hay una competencia directa con GitHub:

* [GitLab](https://about.gitlab.com/ "https://about.gitlab.com/")

* [BitBucket](https://bitbucket.org/product/ "https://bitbucket.org/product/")

Sus principales diferencias es la privatización del repositorio y su integración con flujos de trabajo.

---

En la clase miramos los diferentes comandos que se usaria en la terminal y linea de comandos de bash y por ende:

* git init

* git add .

* git commit 

* git status

* git log

* git checkout

> ¿Realmente entiendes qué hace y el funcionamiento de cada uno de estos comandos?

Nodo = Punto de Guardado en la Línea del tiempo.

Se habla de la instalación de git. La navegación entre la terminal y línea de comandos.



---














## Git y Github

> Clase del 13/02/2026

**Planear actividades de construcción del Software de acuerdo con el diseño establecido**

> Producción y compilación del contenido digital tomado de la Instructora Angelica Triana con sólo fines academicos. Mis apuntes son basados en las guias que ella crea y provee.

* Debe reflexionar: ¿Entiende qué es git?, ¿Entiende qué es github?, ¿Entiende la relación entre git y github?, ¿Entiende qué es un repositorio?

El head es simplemente un puntero o un indicador de posición. El cursor de lectura en un reproductor de musica, pues le dice a usted donde se encuentra en el "mapa". 

Su función es decirte en qué commit (Punto de la historia) estás trabajando actualmente.

Esto apunta a la rama en la que estas trabajando pues cuando haces un commit, el HEAD se mueve automáticamente hacia ese punto.

* Existe el estado **Detached HEAD**: En donde si intentas moverte a un commit antiguo en lugar de a una rama, por lo que git va a mencionar el DETACHED HEAD que esto significa que no esta sujeto a una RAMA sino a un momento fijo en el pasado.

---

**¿Qué es el MAIN?**

Antiguamente llamado MASTER es el nombre por defecto de la rama principal del proyecto. En una línea del tiempo esto significa la historia principal, es la rama que tiene el código limpio y listo para producción. Head es un puntero movil de posición  mientras que main es una referencia de punta que referencia al ultimo commit de esa línea de tiempo especifica.

Cuando inicias un repo al escribir **GIT INIT** automaticamente se crea esta rama para tener un lugar inicial donde construir.

> HEAD: Lugar exacto donde estan tus archivos en el tiempo presente.

> MAIN: Serie cronologica de COMMITS que forman el proyecto (Versión que se lanza a producción)

por medio de GIT LOG se puede identificar cuantos commit se han realizado.

Lectura Recomendada - git log by git documentation: https://git-scm.com/docs/git-log

<img src="https://imgs.search.brave.com/PF7otGsq8H5_4jYdExMLuHOJYkAWG0mL_CQHqLcpaB0/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jb2Rp/bmdub21hZHMuY29t/L2ltYWdlcy84ODMy/MDAyZi02NTBkLTQ0/MTQtMDA4Yi04NDFk/NTczNDg4MDAvcHVi/bGlj">

*Imagen Tomada De: https://codingnomads.com/git-log*

---

**Flujo de trabajo en git**

> El directorio local es una carpeta de nuestro PC en donde nosotros iniciamos el comando git init

Tendremos nuestro working  directory, el lugar donde realizamos el git add, tenemos staging area que es donde tenemos pendiente los guardados y por ende se hace el git commit, tendremos un local repo, en donde si hacemos gitpush se sube al remote repo.

En el remote repo, que sera en nuestro caso el repositorio den github, si pedimos git fetch, para traer todo. Entonces podemos revisar con git chekout o git merge.

> El directorio remoto es un servidor externo.

Todo el tiempo vamos a estar en este proceso.

<img src="https://git-scm.com/book/es/v2/images/benevolent-dictator.png">

*Imagen Tomada De: https://git-scm.com/book/es/v2/Git-en-entornos-distribuidos-Flujos-de-trabajo-distribuidos*

Lectura Recomendada - comparing workflows by atlassian: https://www.atlassian.com/es/git/tutorials/comparing-workflows

* q sirve para salir en tal caso de estar encerrado en alguna función de git

* qw sirve para salir y guardar.

> Línea de comandos: Una terminal es un programa cuyo objetivo principal es leer comandos y ejecutar otros programas.

Instalación de Visual Studio: https://code.visualstudio.com/download 

Se invita a usar la función de BASH TERMINAL en Visual Studio Code.

Se invita a realizar el siguente taller:

---

Taller: 13/02/2026 - Exploración de Comandos GIT

1. Se pide en una carpeta iniciar con git - git init

2. Se pide revisarlo con git status

3. Se pide crear un HTML con una estructura básica

4. Agregar el commit por medio de git add y el nombre del archivo

5. Limpiar la terminal por medio de clear

6. Se pide con las flechas de arriba y abajo, mirar los diferentes 

7. Se pide agregar un commit para hacer una "fotografia"

8. Se pide realizar un cambio y eventualmente repetir el proceso de git add . y git commit

---

Momento #2 

---

Empezamos a hablar de github y el cómo crear un repositorio y sus diferentes elementos: Crear repositorios, publicos, privados, lineas de comando

Se habla de mirar la administración de credenciales en WINDOWS para quitar las cuentas y asi no tener problemas para subir con bash

Esto es un TEST de trabajo.

---

Se pide realizar una infografía de cómo funciona git y 

Se pide investigar desktop github

Se pide realizar un documento en github para señalar un menú, ciertos simbolos, una guia rapida del git y github

Se pide una guia para compartir un repositorio entre un grupo de trabajo










---










## Comandos de Git

En esta sección se describen los comandos fundamentales de **Git**, utilizados para la configuración inicial y el control de versiones en un proyecto de software.

Git es un sistema de control de versiones que permite registrar cambios en archivos, trabajar en equipo y mantener un historial del desarrollo.

Antes de comenzar a trabajar con Git, es necesario configurar el nombre y el correo electrónico del usuario. Esta información quedará registrada en cada commit.

```bash
git config --global --list
```

Muestra la configuración global actual de Git, incluyendo:

- Nombre de usuario  
- Correo electrónico  
- Editor por defecto  
- Otras configuraciones activas  

---

Permite definir el nombre que aparecerá como autor de los commits.

```bash
git config --global user.name "Tu Nombre"
```

Ejemplo:

```bash
git config --global user.name "Juan Perez"
```

---

Configurar correo electrónico

```bash
git config --global user.email "correo@ejemplo.com"
```

Define el correo asociado a los commits realizados.

Ejemplo:

```bash
git config --global user.email "juan@email.com"
```

---

**Concepto de repositorio local**

Un repositorio **local** es el proyecto almacenado en tu computador.

Cuando ejecutas:

```bash
git init
```

Se crea un repositorio Git en la carpeta actual.  
A partir de ese momento, Git comenzará a rastrear los cambios realizados en los archivos.

---

Comando `add`

```bash
git add .
```

Este comando agrega todos los archivos modificados al área de preparación (**staging area**).

* El punto `.` significa: Agregar todos los archivos de la carpeta actual.

El área de preparación es un paso intermedio antes de confirmar los cambios con un commit.

---

Comando `commit`

```bash
git commit -m "Mensaje descriptivo del cambio"
```

El commit guarda oficialmente los cambios en el historial del proyecto.

- `-m` permite agregar un mensaje descriptivo.
- Cada commit representa un punto de guardado del proyecto.
- Permite volver a versiones anteriores si es necesario.

Ejemplo:

```bash
git commit -m "Se agrega formulario de login"
```

---

Flujo básico de trabajo en Git

1. Modificar archivos.
2. Agregar cambios:
   ```bash
   git add .
   ```
3. Confirmar cambios:
   ```bash
   git commit -m "Descripción del cambio"
   ```

Este proceso permite llevar un control ordenado del desarrollo del software.

---

Los comandos básicos de Git permiten:

- Configurar la identidad del desarrollador.
- Crear un repositorio local.
- Preparar archivos para seguimiento.
- Guardar versiones del proyecto mediante commits.
- Mantener un historial organizado del desarrollo.

---

git clone

git log

git log --oneline

git fetch

git pull