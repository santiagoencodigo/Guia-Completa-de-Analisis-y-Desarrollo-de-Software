# Normas APA (7ª edición) para informes de investigación

> Este documento presenta una guía práctica sobre las Normas APA (7ª edición) aplicadas a la elaboración de informes de investigación en el contexto del desarrollo de software. Las normas APA (American Psychological Association) son un estándar ampliamente utilizado para la presentación de trabajos académicos y científicos, que garantiza uniformidad, claridad y credibilidad en la comunicación de resultados de investigación.

> Este documento contiene "Cositas por recordar."

---

## Tabla de contenido

- [1. Formato general del documento](#1-formato-general-del-documento)
- [2. Estilos de títulos y niveles](#2-estilos-de-títulos-y-niveles)
- [3. Citas y referencias](#3-citas-y-referencias)
- [4. Tablas y figuras](#4-tablas-y-figuras)
- [5. Lista de referencias bibliográficas](#5-lista-de-referencias-bibliográficas)
- [6. Uso de ChatGPT e inteligencia artificial en investigaciones](#6-uso-de-chatgpt-e-inteligencia-artificial-en-investigaciones)

---

## 1. Formato general del documento

### 1.1. Papel y márgenes

| **Elemento** | **Especificación** |
|--------------|-------------------|
| **Tamaño de papel** | Carta (21.59 cm × 27.94 cm) |
| **Márgenes** | 2.54 cm en todos los lados (superior, inferior, derecho, izquierdo) |

### 1.2. Tipografía

La 7ª edición de las normas APA permite varias fuentes. Para este contexto, se recomienda:

| **Fuente** | **Tamaño** |
|------------|------------|
| Times New Roman | 12 puntos |
| Calibri | 11 puntos |
| Arial | 11 puntos |
| Lucida Sans Unicode | 10 puntos |
| Georgia | 11 puntos |

> **Recomendación:** Para informes de investigación en el ámbito del desarrollo de software, se sugiere utilizar **Times New Roman de 12 puntos** por su legibilidad y aceptación académica.

### 1.3. Espaciado y alineación

- **Interlineado:** 2.0 (doble espacio) en todo el documento, sin espacios adicionales entre párrafos.
- **Alineación:** Texto alineado a la izquierda (no justificado).
- **Sangría:** Primera línea de cada párrafo con sangría de 1.27 cm (½ pulgada). **No usar la barra espaciadora** para crear sangrías; utilizar la función de sangría del procesador de texto.
- **Citas largas:** Las citas de más de 40 palabras se pueden dejar a espacio y medio (1.5).

### 1.4. Numeración de páginas

- Todas las páginas deben numerarse, incluyendo la portada.
- Los números arábigos se colocan en la **esquina superior derecha**.
- La portada se numera como página 1, aunque el número no siempre se muestra en la portada según el estilo.

### 1.5. Portada

La portada debe incluir:

```
Título del trabajo (minúsculas, negrita, centrado)
(Solo va en mayúscula la inicial de nombres propios, ciudades y siglas)

Nombres y Apellidos del Estudiante
Nombres y Apellidos del Asesor o Instructor

Institución / Programa de Formación
```

**Reglas importantes:**
- No se deben colocar logos, bordes, marcas de agua ni elementos decorativos.
- No se deben utilizar plantillas de guías o cursos.
- No se deben resaltar títulos o párrafos con color.
- No deben quedar páginas en blanco.

---

## 2. Estilos de títulos y niveles

Las normas APA definen cinco niveles de títulos. Cada nivel tiene un formato específico que indica la jerarquía de la información.

### Tabla resumen de niveles

| **Nivel** | **Formato** | **Alineación** | **Negrita** | **Cursiva** | **Sangría** | **Punto final** | **Texto** |
|-----------|-------------|----------------|-------------|-------------|-------------|-----------------|-----------|
| **1** | Cada palabra inicia en mayúscula | Centrado | Sí | No | No | No | Nuevo párrafo |
| **2** | Cada palabra inicia en mayúscula | Izquierda | Sí | No | No | No | Nuevo párrafo |
| **3** | Cada palabra inicia en mayúscula | Izquierda | Sí | Sí | No | No | Nuevo párrafo |
| **4** | Cada palabra inicia en mayúscula | Izquierda | Sí | No | 1.27 cm | Sí | Misma línea |
| **5** | Cada palabra inicia en mayúscula | Izquierda | Sí | Sí | 1.27 cm | Sí | Misma línea |

> **Nota:** Los conectores (como "y", "de", "para", etc.) no deben llevar mayúscula en los títulos. Cada título de nivel 1 da comienzo a una nueva página.

---

## 3. Citas y referencias

### 3.1. Citas en el texto

Las citas pueden ser de dos tipos:

| **Tipo** | **Formato** | **Ejemplo** |
|----------|-------------|-------------|
| **Cita narrativa** | El autor se menciona en la oración, seguido del año entre paréntesis. | *Según Pérez (2023), la transformación digital...* |
| **Cita parentética** | El autor y el año se colocan entre paréntesis al final de la oración. | *La transformación digital ha revolucionado la educación (Pérez, 2023).* |

### 3.2. Citas textuales

| **Tipo** | **Formato** |
|----------|-------------|
| **Cita corta (menos de 40 palabras)** | Se integra en el texto entre comillas dobles. |
| **Cita larga (40 palabras o más)** | Se escribe en un bloque independiente, sin comillas, con sangría de 1.27 cm y a espacio y medio (1.5). |

---

## 4. Tablas y figuras

### 4.1. Tablas

**Formato general:**
- Número de tabla en negrita (ej. *Tabla 1*).
- Título de la tabla en cursiva y mayúsculas capitalizadas.
- Nota al pie de la tabla (si aplica), precedida por la palabra *Nota.* en cursiva.

**Ejemplo de tabla en Markdown:**

```markdown
*Tabla 1*
*Ejemplo de tabla corta o con poca información*

| **Intervalo de edades** | **F** | **M** | **Total** |
|-------------------------|-------|-------|-----------|
| 1 a 2 años              | 23    | 19    | 42        |
| 3 a 4 años              | 31    | 27    | 58        |
| 5 a 6 años              | 38    | 33    | 71        |
| 7 a 8 años              | 51    | 48    | 99        |

*Nota.* Esta tabla muestra el intervalo de años y géneros encontrados en el estudio de caso. Fuente: Autoría propia.
```

**Recomendaciones:**
- Utilizar bordes horizontales para separar los datos; no utilizar bordes verticales.
- Los títulos dentro de las tablas deben escribirse en mayúsculas y sin negrita.

### 4.2. Figuras

**Formato general:**
- Número de figura (ej. *Figura 1*).
- Título de la figura.
- Nota explicativa y fuente, si es necesario.

**Ejemplo:**

```markdown
*Figura 1*
*Formas y descripción de las formas*

[Representación gráfica de las formas]

*Fuente.* Autoría propia.
```

---

## 5. Lista de referencias bibliográficas

La lista de referencias debe aparecer al final del documento, en una página separada, con el título **Referencias** (centrado, en negrita).

**Formato general:**
- Orden alfabético por apellido del autor.
- Sangría francesa (primera línea al margen, líneas siguientes con sangría de 1.27 cm).
- Cada referencia debe incluir: autor, fecha, título y fuente.

### Ejemplos de referencias

**Libro:**
```
Apellido, A. A. (Año). *Título del libro*. Editorial.
```

**Artículo de revista:**
```
Apellido, A. A. (Año). Título del artículo. *Nombre de la Revista*, *volumen*(número), páginas.
```

**Recurso en línea:**
```
Apellido, A. A. (Año). *Título del recurso*. Recuperado de https://www.ejemplo.com
```

**Documento institucional (sin autor):**
```
Nombre de la Institución. (Año). *Título del documento*. Recuperado de https://www.ejemplo.com
```

---

## 6. Uso de ChatGPT e inteligencia artificial en investigaciones

### 6.1. La IA como herramienta de apoyo

La inteligencia artificial, como ChatGPT, debe ser utilizada como una **herramienta de apoyo** en el proceso de investigación, no como un sustituto del pensamiento crítico y el análisis personal.

> A continuación me gusto mucho entender de la IA como forma de nuevo conocimiento validado y enriquecido.

**Modelo de uso de ChatGPT:**

```
+-------------------+     +-------------------+     +-------------------+
|                   |     |                   |     |                   |
|   Redacción       |     |    Lectura        |     |   Verificación    |
|   generada por    | --> |    (revisión,     | --> |   Fundamentación  |
|   ChatGPT         |     |    análisis,      |     |   Ampliación      |
|                   |     |    edición)       |     |   Profundización  |
+-------------------+     +-------------------+     +-------------------+
                                                           |
                                                           v
                                               +-------------------+
                                               |                   |
                                               |   Nuevo           |
                                               |   conocimiento    |
                                               |   validado y      |
                                               |   enriquecido     |
                                               +-------------------+
```

### 6.2. Cómo citar ChatGPT

Cuando se utiliza texto generado por ChatGPT en un trabajo académico, se debe citar adecuadamente.

**Cita en el texto:**
> *"El texto generado por ChatGPT indicó que, se trata de una pregunta clásica, sin una respuesta definitiva, 'Desde un punto de vista biológico, se argumenta que las aves modernas evolucionaron a partir de animales que no eran exactamente gallinas...' (OpenAI, 2023)."*

**Referencia:**
```
OpenAI. (2023). ChatGPT (versión del 15 de julio) [Modelo de lenguaje de gran tamaño]. 
https://chat.openai.com/chat
```

**Elementos clave:**
- **Autor:** El autor del modelo es OpenAI.
- **Fecha:** El año de la versión utilizada.
- **Título:** El nombre del modelo es "ChatGPT", en cursiva.
- **Versión:** Se incluye entre paréntesis después del título.
- **Corchetes:** Se utilizan para descripciones adicionales (ej. "[Modelo de lenguaje de gran tamaño]").
- **URL:** Cuando el nombre del editor y el autor son iguales, no se repite el editor.

### 6.3. Buenas prácticas con IA

- **Contrastar fuentes:** Verificar la información generada por IA con fuentes confiables.
- **Análisis crítico:** Evaluar críticamente las respuestas antes de incorporarlas.
- **Solicitudes concretas:** Formular preguntas específicas para obtener respuestas más precisas.
- **Inspiración, no competencia:** Utilizar los generadores como fuente de inspiración y apoyo, no como reemplazo del trabajo propio.

---

Se recomienda mucho la lectura:

- [Manual de Normas APA 7ª edición - Pontificia Universidad Javeriana Cali](https://www.javerianacali.edu.co/sites/default/files/2022-06/Manual%20de%20Normas%20APA%207ma%20edicio%CC%81n.pdf)

---

> Gracias por leer.