# Conceptos adicionales: Bucle for, in, y otros conceptos relevantes

## Bucle for
    - Un bucle for se utiliza para iterar sobre una secuencia (como listas, tuplas, cadenas de texto o rangos de números). Permite ejecutar un bloque de código repetidamente para cada elemento de la secuencia.

**Estructura básica:**
```bash
for elemento in secuencia:
    # Código que se ejecuta para cada elemento
```
### Ejemplo práctico
```bash
numeros = [1, 2, 3, 4]
for numero in numeros:
    print(numero)
# Salida: 
# 1
# 2
# 3
# 4
```
## Uso del operador in
    - El operador in verifica si un elemento está presente en una secuencia (lista, cadena, tupla, etc.).

### Ejemplo:
```bash
frutas = ["manzana", "banana", "cereza"]
if "banana" in frutas:
    print("Sí, 'banana' está en la lista de frutas")
```

## Enumerar elementos con enumerate
    - enumerate permite iterar sobre una secuencia obteniendo tanto el índice como el valor del elemento actual.

### Ejemplo:
```bash
frutas = ["manzana", "banana", "cereza"]
for indice, fruta in enumerate(frutas):
    print(indice, fruta)
# Salida:
# 0 manzana
# 1 banana
# 2 cereza
```

## Rango de números con range
    - range genera una secuencia de números, útil para iterar un número fijo de veces.

### Ejemplo:
```bash
for i in range(5):
    print(i)
# Salida:
# 0
# 1
# 2
# 3
# 4
```
### Uso avanzado de range:
```bash
range(start, stop, step):
start: Número inicial (por defecto, 0).
stop: Número final (no incluido).
step: Incremento entre números (por defecto, 1).
for i in range(1, 10, 2):
    print(i)
# Salida:
# 1
# 3
# 5
# 7
# 9
```
## Bucle while
    - Un bucle while repite un bloque de código mientras una condición sea verdadera.

***Estructura básica:***
```bash
while condición:
    # Código a ejecutar
```
```bash
Ejemplo práctico:

contador = 0
while contador < 5:
    print(contador)
    contador += 1
# Salida:
# 0
# 1
# 2
# 3
# 4
```
## Condicional if-else
    - Permite ejecutar un bloque de código dependiendo de una condición.

***Estructura básica:***
```bash
if condición:
    # Código si la condición es verdadera
else:
    # Código si la condición es falsa
```
### Ejemplo:
```bash
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

Estos conceptos son fundamentales para comprender y trabajar con el código en Python, incluidos los ejemplos relacionados con el procesamiento de imágenes y el uso de bibliotecas como TensorFlow y Matplotlib.