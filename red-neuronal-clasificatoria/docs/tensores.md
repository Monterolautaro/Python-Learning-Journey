# Conceptos básicos previos

## ¿Qué es un tensor?

    - Un tensor es una estructura de datos fundamental utilizada en el aprendizaje automático y la computación numérica. Es similar a un array multidimensional de Numpy, pero está diseñado para aprovechar la aceleración de hardware, como GPU y TPU, mediante librerías como TensorFlow y PyTorch.

***Características principales de los tensores:***

1. **Dimensiones: Un tensor puede tener diferentes dimensiones:**

- **Escalar** (0D): Un solo valor, como un número (3 o -7.5).

- **Vector** (1D): Una lista de valores, como [1, 2, 3].

- **Matriz** (2D): Una tabla de valores con filas y columnas, como:
    -    [[1, 2, 3],
    -    [4, 5, 6]]

- **Tensor 3D o superior:** Una colección de matrices, por ejemplo, imágenes representadas como (altura, ancho, canales).

2. **Compatibilidad con hardware:**
- Los tensores están optimizados para realizar cálculos en paralelo, aprovechando el hardware especializado.

3. **Propiedades:**

- **Forma (shape):** Describe el tamaño del tensor en cada dimensión.

- **Tipo de dato:** Define el tipo de datos que contiene (por ejemplo, float32 o int64).

### Ejemplo en TensorFlow:
```bash
import tensorflow as tf
# Crear un tensor escalar
escalar = tf.constant(5)

# Crear un tensor 1D (vector)
vector = tf.constant([1, 2, 3])

# Crear un tensor 2D (matriz)
matriz = tf.constant([[1, 2], [3, 4]])

print(escalar.shape)  # Salida: ()
print(vector.shape)   # Salida: (3,)
print(matriz.shape)   # Salida: (2, 2)
```

***Relación con arrays de Numpy:***

Aunque los tensores y los arrays de Numpy son similares, los tensores tienen soporte nativo para operaciones que se ejecutan en GPU. Se pueden convertir de un tipo a otro usando:

- **De tensor a array de Numpy:**
```bash
numpy_array = tensor.numpy()
```

- **De array de Numpy a tensor:**
```bash
tensor = tf.convert_to_tensor(numpy_array)
```