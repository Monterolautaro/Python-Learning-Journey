# Teoría sobre cadenas y diccionarios en python

En esta sección estará la teoría vinculada al archivo de práctica: [dictionaries](./dictionaries.py)

# Indice

1. [Strings syntax](#string-syntax)
2. [Strings are sequences](#strings-are-sequences)
3. [String methods](#string-methods)
4. [Dictionaries](#dictionaries)

## Strings

Un lugar donde el lenguaje de Python realmente brilla es en la manipulación de strings. En esta sección vamos a cubrir algúnos de los métodos de cadena y las operaciones de formateo.

Estos patrones de manipulación de cadenas se ven muy frecuentemente en el contexto de la ciencia de datos.

### String syntax
Ya has visto muchas strings en ejemplos durante las lecciones anteriores, pero para recordar, strings en Python se definen con comillas simples o comillas dobles. Son funcionalmente equivalentes.
```bash
x = 'Pluto is a planet'
y = "Pluto is a planet"
x == y

# Salida: True
```

Las comillas dobles son convenientes si tu string contiene una comilla simple (e.g. representando una comilla doble).
Similarmente, es fácil crear un string que contenga comillas dobles si la envuelves en comillas simples:
```bash
print("Pluto's a planet!")
print('My dog is named "Pluto"')
# Salida: Pluto's a planet!
#         My dog is named "Pluto"
```

Si intentamos poner un comilla simple dentro de un string con comillas simples, Python se confundirá
```bash
'Pluto's a planet!'

# Salida:
  File "/tmp/ipykernel_19/1561186517.py", line 1
    'Pluto's a planet!'
           ^
SyntaxError: invalid syntax
```
Podemos arreglar esto poniendo una barra invertida antes de la comilla simple.
```bash
'Pluto\'s a planet!'
```

La tabla de abajo enfatiza algunos de los usos importante de la barra invertida.

| What you type... | What you get |           example       | print(example)      |
|------------------|--------------|-------------------------|---------------------|
| \'               | '            | 'What\'s up?'           | What's up?          |
| \"               | "            | "That's \"cool\""       | That's "cool"       |
| \\               | \            | "Look, a mountain: /\\" | Look, a mountain: /\|
| \n               |              | "1\n2 3"                | 1                   |
|                  |              |                         | 2 3                 |

La última secuencia, \n, representa el carácter de nueva línea. Esto causa que Python comience una nueva línea.
```bash
hello = "hello\nworld"
print(hello)

# Salida: Hello
#         World
```

Además, las sintaxis de triple comilla de Pythom para string nos deja incluír nuevas lineas literalmente (Solo pulsando 'Enter' en nuestro teclado, en lugar de usar la secuencia '\n'). Ya hemos visto esto en las docstrings que usamos para documentar nuestras funciones, pero podemos usarlos cualquier lugar queremos definir un string.
```bash
triplequoted_hello = """hello
world"""
print(triplequoted_hello)
triplequoted_hello == hello

# Salida: hello
#         world
#         True
```
La función print() automaticametne agrega una nueva línea de caracteres a menos que especifiquemos un valor para la palabra clave del argumento _end_ otro que el valor predeterminado de '\n': 
```bash
print("hello")
print("world")
print("hello", end='')
print("pluto", end='')

# Salida: hello
#         world
#         hellopluto
```

## Strings are sequences

Las strings pueden ser pensadas como secuencias de caracteres. Todo lo que hemos visto que podemos hacerle a una lista, podemos también hacerlo a un string.

```bash
# Indexing
planet = 'Pluto'
planet[0]

# Salida: 'P'

# Slicing
planet[-3:]

# Salida: 'uto'

# Cual es la longitud del string?
len(planet)

# Salida: 5

# Si, incluso podemos iterar sobre ellas
[char+'! ' for char in planet]

# Salida: ['P! ', 'l! ', 'u! ', 't! ', 'o! ']
```

- ***Pero una myor diferencia en como se diferencias de las listas es que los strings son inmutables. No podemos modificarlos.***
```bash
planet[0] = 'B'
# planet.append tampoco funciona.

# Salida: TypeError: 'str' object does not support item assignment
```

## String methods

- ***Como*** list, ***el tipo string tiene muchos métodos útiles. Te mostraré solo algúnos ejemplos aquí.***
```bash
# TODO MAYUSCULAS
claim = "Pluto is a planet!"
claim.upper()

# Salida: 'PLUTO IS A PLANET!'
```
```bash
# todo minusculas
claim.lower()

# Salida: 'pluto is a planet!'
```
```bash
# Buscando por el primer index de un substring
claim.index('plan')

# Salida: 11
```
```bash
# Empieza con
claim.startswith(planet)

# Salida: False
```
```bash
# false por la falta del signo de exclamación
claim.endswith('planet')

# Salida: False
```

***Yendo entre strings y lists:*** .split() ***y*** .join()

- str.split() ***vuelve a un string en una lista de cosas mas pequeñas, dividiendose en los espacios por default. Esto es muy útil para ir de una cadena de strings muy grande, a una lista de palabras.***
```bash
words = claim.split()
words

# Salida: ['Pluto', 'is', 'a', 'planet!']
```

- ***Ocasionalmente vas a querer dividir en algo diferente a los espacios en blanco.***
```bash
datestr = '1956-01-31'
year, month, day = datestr.split('-')
```

- str.join() nos toma en la otra dirección, uniendo una lista de strings en un solo string, usando el string que queremos como separador.
```bash
'/'.join([month, day, year])

# Salida: '01/31/1956'
```
- ***Si, podemos poner carácteres unicode dentro de nuestras cadenas de strings:***
```bash 
' 👏 '.join([word.upper() for word in words])

# Salida: 'PLUTO 👏 IS 👏 A 👏 PLANET!
```

- ***Building strings with*** .format()
    - ***Python nos deja concatenar strings con el operador ***+ .
```bash
planet + ', we miss you.'

# Salida: 'Pluto, we miss you.'
```

- ***Si queremos lanzar con algún objeto que no sea string, tenemos que convertirlo primero a string con*** str()
```bash
position = 9
planet + ", you'll always be the " + position + "th planet to me."

# Salida: TypeError: can only concatenate str (not "int") to str
```

```bash
planet + ", you'll always be the " + str(position) + "th planet to me."

# Salida: "Pluto, you'll always be the 9th planet to me."
```

- ***Esto se está volviendo difícil de leer y de escribir.*** str.format() ***al rescate.***
```bash
"{}, you'll always be the {}th planet to me.".format(planet, position)

# Salida: "Pluto, you'll always be the 9th planet to me."
```
Así es mas limpio, llamamos al método .format() en un string, donde los valores de Python que queremos insertar, son representador conlos placeholders de llaves {}.

Si eso fuuera todo lo que el método format() puede hacer, sería todavía increíblemente útil. Pero como no lo es, puede hacer mucho mas.
Aca hay un poco de lo que puede hacer:
```bash
pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 puntos decimales   3 puntos decimales, format como %     separado por comas
"{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
)

# Salida: "Pluto weighs about 1.3e+22 kilograms (0.218% of Earth's mass). It is home to 52,910,390 Plutonians."
```
```bash
# Refiriendose a format() argumentos por indice, empezando desde el 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)

# Salida: Pluto's a planet.
#         No, it's a dwarf planet.
#         planet!
#         dwarf planet!
```

## Dictionaries
Los diccionarios en Python son estructuras de datos para mapear llaves a valores.
```bash
numbers = {'one':1, 'two':2, 'three':3}
```
***En este caso 'one', 'two', and 'three' son las llaves, y 1, 2 and 3 son sus correspondientes valores.***
***Los valores son accesibles con la sintaxis de corchetes (Bracket syntax) similar a la indexación en listas y strings.***

```bash
numbers['one']

# Salida: 1
```
- ***Podemos usar la misma sintaxis para añadir otro par de clave y valor.***
```bash
numbers['eleven'] = 11
numbers

# Salida: {'one': 1, 'two': 2, 'three': 3, 'eleven': 11}
```

- ***O para cambiar el valor asociado a una clave existente***
```bash
numbers['one'] = 'Pluto'
numbers

# Salida: {'one': 'Pluto', 'two': 2, 'three': 3, 'eleven': 11}
```
- ***Python tiene comprensión por diccionarios*** (diccionary comprehensions) ***con una sintaxis similar a la de las comprensiónes por listas*** (list comprehensions) ***que vimos anteriormente.***
```bash
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
planet_to_initial

# Salida: {'Mercury': 'M',
        # 'Venus': 'V',
        # 'Earth': 'E',
        # 'Mars': 'M',
        # 'Jupiter': 'J',
        # 'Saturn': 'S',
        # 'Uranus': 'U',
        # 'Neptune': 'N'}
```
***El operador*** in ***nos dice cuando algo es una clave en un diccionario.***
```bash
'Saturn' in planet_to_initial

# Salida: True


'Betelgeuse' in planet_to_initial

# Salida: False
```
- ***Un búcle sobre un diccionario va a recorrer sus claves.***
```bash
for k in numbers:
    print("{} = {}".format(k, numbers[k]))

    # Salida: one = Pluto
            # two = 2
            # three = 3
            # eleven = 11
```
- ***Podemos acceder a una colección de todas las llaves o de todos los valores con*** dict.keys() ***y*** dict.values(), ***respectivamente.***
```bash
# Obten todas las iniciales, ordenalas alfabeticamente, y ponlas en una string separada por espacios.
' '.join(sorted(planet_to_initial.values()))

# Salida: E J M M N S U V
```
- ***El muy útil método*** dict.items() ***nos deja iterar sobre las llaves y los valores de un diccionario simultaneamente. (En python jargon, un item se refiere a un par de clave, valor)***
```bash
for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))
# Salida: Mercury begins with "M"
    #     Venus begins with "V"
    #     Earth begins with "E"
    #     Mars begins with "M"
    #     Jupiter begins with "J"
    #     Saturn begins with "S"
    #     Uranus begins with "U"
    #     Neptune begins with "N"
```
