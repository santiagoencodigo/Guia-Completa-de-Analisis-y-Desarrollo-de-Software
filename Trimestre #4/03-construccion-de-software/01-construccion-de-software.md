# Construcción de Software 

A continuación mis apuntes y/o documentación de los temas vistos en Construcción del Software con la instructora Angelica Triana en el cuarto de nueve trimestres. El enfoque de este área es **git y github**. 










## Tabla de Contenido

[1. Estandarización](#estandarización)

[2. Control de Versiones](#control-de-versiones)











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
