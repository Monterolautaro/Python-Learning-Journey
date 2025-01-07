# Teoría sobre listas en python

En esta sección estará la teoría vinculada al archivo de práctica: [listas](./index.py)

# Indice

1. [Listas](#listas)
2. [Indexing](#indexing)
3. [Slicing](#slicing)
4. [Changing lists](#changing-lists)
5. [List functions](#list-functions)
6. [Objects](#pausa-para-hablar-sobre-objects)
7. [List methods](#list-methods)
8. [Searching lists](#searching-lists)

## Listas
- ***Las listas en python representan secuencias de valores ordenadas. Acá hay un ejemplo de como crearlas:***
```bash
primes = [2, 3, 5, 7]
```
- ***Podemos poner otros tipos de datos en las listas:***
```bash
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
```

- ***Podemos incluso crear una lista de listas:***
```bash
hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (Una coma después del último elemento es opcional)
]
# (Podría también haber escrito todo en una línea, pero se vuelve difícil de leer)
hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]
```

- ***Una lista puede contener un mix de diferentes tipos de variables o datos:***
```bash
my_favourite_things = [32, 'raindrops on roses', help]
```
## Indexing

- ***Podemos acceder a elementos individuales en una lista, a través de corchetes:***
```bash
planets[0]
# Salida: Mercury
```
- ***Los elementos al final de una lista, pueden ser accesibles con números negativos, empezando desde el -1:***
```bash
planets[-1]
# Salida: Neptune
```

## Slicing

- ***¿Cuáles son los tres primeros planetas de la lista? Podemos responder a esta pregunta usando slicing***
    - _planets[0:3]_ es nuestra manera de preguntar por elementos de la lista _planets_, empezando por el indice 0 y continuando hasta el indice 3, pero sin incluirlo. 
```bash
planets[0:3]
```

- ***Tanto el índice del comienzo como el del final son opcionales. Si dejo vacío el primer índice, se asume que es 0. Entonces, puedo reescribir la expresión de esta forma:***
```bash
planets[:3]
# Salida: ['Mercury', 'Venus', 'Earth']
```

- ***Si dejo vacío el índice final, se asume que es el length completo de la lista:***
    - la expresión de abajo significa "dame todos los planetas desde el índice 3 en adelante"
```bash
planets[3:]
# Salida: ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
```

- ***Podemos también usar índices negativos cuando hacemos slicing:***
```bash
# Todos los planetas excepto el primero y el ultimo 
planets[1:-1]
# Salida: ['Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus']
```
```bash
# Los ultimos tres planetas
planets[-3:]
# Salida: ['Saturn', 'Uranus', 'Neptune']
```

## Changing lists
Las listas son mutables, pueden ser modificadas (A diferencia de las tuplas).

- ***Una forma de modificar una lista, es asignar un nuevo valor a un índice o expresión slice***
    - Por ejemplo, vamos a decir que queremos modificar a "_Marte_" de la lista de _planets_:
```bash
planets[3] = 'Malacandra'
print(planets)
# Salida: ['Mercury',
#  'Venus',
#  'Earth',
#  'Malacandra',   <--
#  'Jupiter',
#  'Saturn',
#  'Uranus',
#  'Neptune']
```

- ***Usando slicing:***
```bash
planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)
# Salida: ['Mur', 'Vee', 'Ur', 'Malacandra', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
```

- ***Devolvamos a todos los planetas su nombre original:***
```bash
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars',]
# Salida: ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
```

## List functions
Python tiene muchas funciones utiles para trabajar con listas. 

-  len ***nos da el length de una lista:***
```bash
# ¿Cuantos planetas hay en la lista?
len(planets)
# Salida: 8
```

- sorted ***devuelve una versión ordenada de la lista:***
```bash
# Los planetas son ordenados alfabeticamente
sorted(planets)
# Salida: ['Earth', 'Jupiter', 'Mars', 'Mercury', 'Neptune', 'Saturn', 'Uranus', 'Venus']
```

- sum ***hace lo que se puede esperar***
```bash
# Suma los números de una lista
primes = [2, 3, 5, 7]
sum(primes)
# Salida: 17
```

- max ***retorna el número mas alto en una lista:***
```bash
# La función "min" hace lo opuesto
max(primes)
# Salida: 7
```

## Pausa para hablar sobre: Objects
Seguro han leído que todo en Python es un objecto. ¿Qué significa esto?

En resumen, los objetos llevan algunas cosas con ellos. Se puede acceder a ese material, usando la sintáxis por punto de Python

Por ejemplo, ***los números en Python llevan consigo una variable asociada llamada imag que representa su parte imaginaria:***
```bash
x = 12
# x es un número real, entonces su parte imaginaria es 0.
print(x.imag)
# Salida: 0

# Cómo crear un número complejo:
c = 12 + 3j
print(c.imag)
# Salida: 3
```

- Las cosas que un objeto lleva consigo, pueden también incluir funciones. ***Una función adjunta a un objeto es llamada un*** método.
***Por ejemplo, los números tienen un metodo llamado*** bit_length. ***De nuevo, accedemos a él usando sintáxis por punto:***. 
    - Las cosas que no son funciones adjuntas a un objeto, como imag, son llamados atributos.
```bash
# Puedes usar el método bit_length para averiguar cuántos bits son necesarios para representarlo en binario.
x.bit_length
# <function int.bit_length()>
```

- ***Para llamarlo, añadimos párentesis:***
```bash
x.bit_length()
# Salida: 4
```

Diferencia entre imag y bit_lenght:
1. _imag_ es solo un dato asociado a un objeto, no se llama con párentesis.
2. los métodos como _bit_length_ son funciones, por lo que hay que ejecutarlos con párentesis.

## List Methods

- list.append ***modifica una lista añadiendo un elemento al final:***
```bash
planets.append('Pluto')
```
 ### **Nota:**
 append ***es un método que llevan consigo todos los objetos del tipo lista, no solo*** planets, ***asi que podríamos haber llamado a*** help(list.append). ***Además, si intentams llamar a*** help(append), ***Python nos dirá que no existe ningúna variable llamada*** "append". ***El nombre*** "append" ***solo existe entre listas*** , ***no existe un nombre estandarizado en*** funciones builtin **como en** max ***o*** len.

 ```bash
 help(planets.append)
 # Salida: Help on built-in function append:

# append(object, /) method of builtins.list instance
#     Append object to the end of the list.
 ```

 - ***Si miramos el valor de*** planets, ***podemos ver que el método sí lo modifico, aunque no retorne nada:***
 ```bash
 print(planets)
 # Salida: ['Mercury',
#  'Venus',
#  'Earth',
#  'Mars',
#  'Jupiter',
#  'Saturn',
#  'Uranus',
#  'Neptune',
#  'Pluto']   <--
 ```

 - list.pop ***elimina y devuelve el último elemento de una lista:***
```bash
planets.pop()
# Salida: 'Pluto'

print(planets)
# Salida: ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
```

## Searching lists


