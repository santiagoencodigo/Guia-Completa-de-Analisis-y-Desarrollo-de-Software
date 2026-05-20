

## Sesión 5

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