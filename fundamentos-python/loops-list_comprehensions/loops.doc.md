# Teoría sobre búcles y listas por comprensión en python

En esta sección estará la teoría vinculada al archivo de práctica: [loops](./loops.py)

# Indice

1. [Loops](#loops)
2. [While loops](#while-loops)
3. [List comprehensions](#list-comprehensions)

## Loops
**Los búcles son una manera de ejecutar código repetidamente. Acá hay un ejemplo:**
```bash
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ') # Muestra todo en la misma línea

# Salida: Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune 
```

***El búcle*** _for_ ***especifica:***

- _El nombre de la variable a utilizar (en este caso, planet)_
- _el set de valores para que el búcle finalice (en este caso, planets)_
- _Se usa la palabra reservada "_in_" para conectarlos entre si._

- ***El objeto a la derecha del*** "_in_" ***puede ser cualquier objeto que soporte una iteración. Basicamente, si puede ser pensado como un grupo de cosas, probablemente puedas iterar sobre él. Además de las*** _listas_, ***podemos iterar sobre los elementos de una*** _tupla_:
```bash
multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
product

# Salida: 360
```

- ***Podemos incluso iterar sobre cada cáracter en un string:***
```bash
s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# Muestra todas las mayusculas en s, una en cada vez. 
for char in s:
    if char.isupper():
        print(char, end='') 

# Salida: HELLO
```


### range()

_range()_ **es una funcion que devuelve una secuencia de números. Resulta ser muy útil para escribir búcles.**

- ***Por ejemplo, si queremos repetir una acción 5 veces:***
```bash
for i in range(5):
    print("Doing important work. i =", i)

# Salida: Doing important work. i = 0
        # Doing important work. i = 1
        # Doing important work. i = 2
        # Doing important work. i = 3
        # Doing important work. i = 4
```

## While loops

**El otro tipo de búcle en Python es el búcle** _while_, **el cual itera siempre y cuando se cumpla la condición:**
```bash
i = 0
while i < 10:
    print(i, end=' ')
    i += 1 # Incrementa el valor de i en 1

# Salida: 0 1 2 3 4 5 6 7 8 9 
```

**El argumento del búcle** _while_ **es evaluado como una declaración booleana, y el búcle es ejecutado hasta que la declaración sea evaluada a** _False_.

## List comprehensions

_List comprehensions_ **son una de las funciones mas amadas y únicas de Python. La forma mas sencilla de entenderlas, es probablemente solo mirar un par de ejemplos:**
```bash
squares = [n**2 for n in range(10)]
squares

# Salida: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

- ***Aquí está como haríamos lo mismo pero sin una*** list comprehension:
```bash
squares = []
for n in range(10):
    squares.append(n**2)
squares

# Salida: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

- ***Podemos incluso añadir un condicional:***
```bash
short_planets = [planet for planet in planets if len(planet) < 6]
short_planets

# Salida: ['Venus', 'Earth', 'Mars']
```

**(Si estás familiarizado con SQL, podrías pensarlo siendo como un operador "WHERE")**

- ***Aca hay un ejemplo filtrando con un condicional y aplicando un poco de transformación a la variable del búcle:***
```bash
# str.upper() devuelve todas las letras de un string convertidas en mayuscula
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
loud_short_planets

# Salida: ['VENUS!', 'EARTH!', 'MARS!']
```

- ***La gente generalmente lo escribe en una línea, pero podrías encontrar la estructura mas limpia cuando está dividida en 3 partes:***
```bash
[
    planet.upper() + '!' 
    for planet in planets 
    if len(planet) < 6
]

# Salida: ['VENUS!', 'EARTH!', 'MARS!']
```

(Continuando con la analogía de SQL, podrías pensar a estas tres lineas como SELECT, FROM, y WHERE)

- ***La expresión a la izquierda técnicamente no tiene que envolver a la variable del búcle (a pesar de que sería bastante inusual)***
```bash
[32 for planet in planets]

# Salida: [32, 32, 32, 32, 32, 32, 32, 32]
```

- ***las*** _list comprehensions_ ***combinadas con funciones como*** _min, max,_ ***y*** _sum_ ***pueden liderarnos a soluciones de una línea impresionantes, que de otra manera, necesitariamos de varias lineas para resolverlos.***
    - ***Por ejemplo, compara las siguientes 2 celdas de código que hacen exactamente lo mismo.***
```bash
def count_negatives(nums):
    """Return the number of negative numbers in the given list.
    
    >>> count_negatives([5, -1, -2, 0, 3])
    2
    """
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative
```
- ***Solución usando una list comprehension:***
```bash
def count_negatives(nums):
    return len([num for num in nums if num < 0])
```

- ***Si lo único que nos interesara fuera minimizar las lineas de código, esta tercer solución es todavía mejor!***
```bash
def count_negatives(nums):
    # Recordatorio: En los ejercicios "booleans and conditionals", aprendimos un truco de 
    # Python donde calculando algo como True + True + False + True va a ser igual a 3.
    return sum([num < 0 for num in nums])
```

- Cual de estas soluciones es la "mejor" es totalmente subjetivo. Resolver un problema escribiendo menos código siempre está bueno, pero vale la pena tener en mente las siguientes líneas de [The zen of python](../docs/python's_zen.md):
```
    La legibilidad cuenta.
    Explícito es mejor que ímplicito.
```
**Asi que, usemos estas herramientas para hacer programas compactos y legibles. Pero cuando haya que elegir, por favor escribamos código que sea fácil de entender para otros.**