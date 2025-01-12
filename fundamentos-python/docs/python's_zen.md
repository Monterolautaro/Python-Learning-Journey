# Zen of python

# Index
1. [About](#about-zen-of-python)
2. [Principles](#principles)
3. [Being Pythonic](#being-pythonic)
4. [In practice](#in-practice)

## About Zen of Python
El zen de Python es una colección de 19 "principios de guía" para escribir programas
de computación que influencia el diseño del lenguaje de programación Python.
El código de Python que se alinea a estos principios, es usualmente llamado "Pythonic".

- El ingeniero de software Tim Peters escribió este set de principios y los posteo en la lista de mail de Python en 1999. Su lista deja abierto un vigésimo principio "for Guido to fill in", refiriendose a Guido van Rossum, el autor original del lenguaje de Python. La vacante por un vigésimo principio aún no ha sido llenada. 

- El Zen of Python de Peter incluyó como número de entrada 20 en los propósitos de mejora oficiales del lenguaje de Python y fue lanzado al dominio público. ***Fué también incluido como un Easter egg en el interprete de Python, donde puede ser mostrado en consola de la siguiente manera:***
```bash
import this

print(this)

# Salida: The Zen of Python, by Tim Peters

        # Beautiful is better than ugly.
        # Explicit is better than implicit.
        # Simple is better than complex.
        # Complex is better than complicated.
        # Flat is better than nested.
        # Sparse is better than dense.
        # Readability counts.
        # Special cases aren't special enough to break the rules.
        # Although practicality beats purity.
        # Errors should never pass silently.
        # Unless explicitly silenced.
        # In the face of ambiguity, refuse the temptation to guess.
        # There should be one-- and preferably only one --obvious way to do it.
        # Although that way may not be obvious at first unless you're Dutch.
        # Now is better than never.
        # Although never is often better than *right* now.
        # If the implementation is hard to explain, it's a bad idea.
        # If the implementation is easy to explain, it may be a good idea.
        # Namespaces are one honking great idea -- let's do more of those!
        # <module 'this' from '/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/this.py'>
```

## Principles

### Los principios están listados acá:
- Lindo es mejor que feo.
- Explícito es mejor que implícito.
- Simple es mejor que complejo.
- Complejo es mejor que complicado.
- Plano es mejor que anidado.
- Disperso es mejor que denso.
- La legibilidad cuenta.
- Los casos especiales no son lo suficientemente especiales como para romper las reglas.
- A pesar que la practicidad vence a la perfección.
- Los errores no deberían pasar silenciosamente.
- A menos que sean explícitamente silenciados.
- En cara de la ambigüedad, rechaza la tentación a adivinar.
- Debería haber una -y preferiblemente solo una- manera obvia de hacer las cosas. 
- A pesar de que esa manera no sea obvia al principio, a menos de que seas alemán.
- Ahora es mejor que nunca.
- A pesar que nunca es a veces mejor que _justo ahora._
- Si la implementación es difícil de explicar, es una mala idea.
- Si la implementación es fácil de explicar, podría ser una buena idea.
- Los _Namespaces_ son una idea impresionante - hagamos mas de ellos!

## Being Pythonic
Uno de los principios, "Debería haber una -y preferiblemente solo una- manera obvia de hacer las cosas. ", puede ser referenciado como la forma "Pythonic" de hacer las cosas. La definición oficial de "Pythonic" es:

- ***Una buena idea o pieza de código que está sigue muy de cerca los dichos más comúnes del lenguaje Python, mejor que implementar codigo usando conceptos comúnes a otro lenguaje. Por ejemplo, un dicho común en Python es hacer un búcle sobre todos los elementos de un iterable usando un búcle*** _for._ ***Muchos otros lenguajes no tienen este tipo de construcción, entonces la gente desfamiliarizada con Python a veces usa un contador número como:***
```bash
for i in range(len(food)):
    print(food[i])
```
- ***Como opuesto al limpio, metodo Pythonic:***
```bash
for piece in food:
    print(piece)
```
El código que es difícil de entender o leer como una cruda transcripción de otro lenguaje de programación, es llamado **_Unpythonic._**


## In practice

Desde el lanzamiento del Zen of Python, han habido investigaciones hechas en su efectividad y uso actual entre los desarrolladores. A pesar de que la diferencia en interpretación entre desarrolladores de Python principiantes y experimentados, entrevistas entre 13 desarrolladores con diferentes habilidades muestran que el Zen of Python "Influencia positivamente la forma en que los desarrolladores escriben y hablan sobre el código". Los investigadores extendieron este caso de estudio para explorar el uso de los dichos de Python en los repositorios de GitHub, y encontraron que el uso de "Python Idioms" incrementó en el tiempo. Escribiendo código de Python que se alinea con el Zen of Python puede guardar memoría y correr tiempo de programas de Python. El deseo de escribir en un código Pythonic, ha llevado a refactorizar herramientas que ayudan a desarrolladores a alcanzar esta meta.

[Articulo original de wikipedia](https://en.wikipedia.org/wiki/Zen_of_Python)