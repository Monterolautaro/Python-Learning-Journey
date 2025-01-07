# **Documentación del sistema de clasificación de imágenes**
```bash
Este documento detalla el funcionamiento del sistema de clasificación de imágenes,
con teoría sobre todo acerca del funcionamiento de cada metodo utilizado, cada tupla, número,
etc.

En index.py habrán comentarios que empiecen con ### 
los cuales van a decir en que número va a estar la explicación
de esas lineas de código en esta documentación
```

## 1. Cargar el conjunto de datos

```bash
 datos, metadatos = tfds.load('fashion_mnist', as_supervised=True, with_info=True)
```

### **¿Qué hace tfds.load?**

- *tfds.load*: descarga el conjunto de datos especificado (en este caso, fashion_mnist), lo descomprime y
  lo prepara para su uso.

- *'fashion_mnist'*: Es un conjunto de datos de imágenes en escala de grises de 28x28 píxeles,ß
   donde cada imagen representa una prenda de ropa (camisetas, zapatos, etc.) asociada con una
   etiqueta numérica (0–9). Es un Dataset elegido para la clasificatoria (se puede elegir
   cualquier dataset disponible en tensorflow_datasets)

- *as_supervised=True*: Significa que los datos serán devueltos en un formato (input, label). En este caso, (imagen, etiqueta):
    - input es una imagen (tensor 28x28x1).
    - label es la categoría de ropa (un número entre 0 y 9).

- *with_info=True*: Devuelve un objeto adicional llamado metadatos, que contiene información sobre los datos, como la cantidad
  de ejemplos o los nombres de las clases.

### **Salida**
*datos* contiene dos subconjuntos principales:

- *datos['train']*: Para entrenar el modelo.
- *datos['test']*: Para evaluar el modelo.
- *metadatos* incluye información como la cantidad de ejemplos y los nombres de las etiquetas.

## 2. Separar entrenamiento y pruebas

```bash
    datos_entrenamiento, datos_pruebas = datos['train'], datos['test']
```

### **¿Qué pasa aquí?**
Se usa **desempaquetamiento de tuplas** para asignar los subconjuntos de entrenamiento y prueba a variables separadas.

- *datos['train']*: Contiene las imágenes y etiquetas para entrenar.
- *datos['test']*: Contiene las imágenes y etiquetas para evaluar.

## 3. Obtener nombres de las clases

```bash
 nombres_clases = metadatos.features['label'].names
```

### ¿Qué hace esta línea?
- *metadatos.features* es un diccionario que describe las características de los datos.
- *'label'* se refiere a las etiquetas asociadas a las imágenes.
- *.names* devuelve una lista de nombres legibles para humanos, como "Camiseta", "Zapato", etc.

Ejemplo:
```bash
nombres_clases = ['Camiseta', 'Pantalón', 'Suéter', 'Vestido', ...]
```

## 4. Normalizar las imagenes
```bash
def normalizar(imagen, etiquetas):
    imagenes = tf.cast(imagen, tf.float32)
    imagenes /= 255
    return imagenes, etiquetas
```

### ¿Qué es la normalización?

La normalización convierte los valores de los píxeles de las imágenes (originalmente entre 0 y 255) a un rango de 0 a 1. Esto mejora la eficiencia del entrenamiento porque los modelos de aprendizaje automático funcionan mejor con valores pequeños y consistentes.

**Paso a paso**

1. *tf.cast(imagen, tf.float32)*: Convierte la imagen a tipo float32. Por defecto, los valores de píxeles están en enteros (int), lo que no permite cálculos precisos.

2. *imagenes /= 255*: Divide cada valor de píxel por 255 para llevarlo al rango [0, 1].

3. **Devuelve** *(imagenes, etiquetas)*: Regresa la imagen normalizada y su etiqueta asociada.

## 5. Aplicar normalización
```bash
datos_entrenamiento = datos_entrenamiento.map(normalizar)
datos_pruebas = datos_pruebas.map(normalizar)
```

### ¿Qué es _.map()_?
_.map()_ aplica una función (en este caso, _normalizar_) a cada elemento de un conjunto de datos.

- Entrada: _(imagen, etiqueta)_.
- Salida: _(imagen normalizada, etiqueta)_.

## 6. Cachear los datos
```bash
datos_entrenamiento = datos_entrenamiento.cache()
datos_pruebas = datos_pruebas.cache()
```

### ¿Qué hace _.cache()_?

Almacena el conjunto de datos en memoria para acelerar el entrenamiento. Sin esto, TensorFlow leería cada imagen desde el disco en cada iteración, lo que es más lento.

## 7. Mostrar una imagen
```bash
for imagen, etiqueta in datos_entrenamiento.take(1):
    break
imagen = imagen.numpy().reshape((28,28))
```
### Paso a paso

1. _datos_entrenamiento.take(1)_: Toma el primer elemento del conjunto (una tupla (imagen, etiqueta)).
2. _imagen.numpy()_: Convierte la imagen de un tensor (objeto nativo de TensorFlow) a un array de NumPy para manipulación más sencilla.
3. _.reshape((28,28))_: Redimensiona el array a una matriz de 28x28 (representación de la imagen en escala de grises).

## 8. Graficar una imagen
```bash
import matplotlib.pyplot as plt

plt.imshow(imagen, cmap=plt.cm.binary)
plt.colorbar()
plt.show()
```

### ¿Qué es matplotlib?
_matplotlib_ es una biblioteca en Python para crear visualizaciones gráficas. Aquí usamos su submódulo _pyplot_ (con el alias _plt_) para mostrar imágenes y gráficos.

_Desglose línea por línea_:

1. _plt.imshow(imagen, cmap=plt.cm.binary)_:
    - imshow: Muestra una imagen 2D como un gráfico. Recibe como entrada un array o matriz que representa los valores de los píxeles.
    - cmap=plt.cm.binary: Define el mapa de colores. En este caso, binary muestra la imagen en blanco y negro, lo cual es apropiado para imágenes en escala de grises.

### Teoría:
    - Los mapas de colores _(colormaps)_ son maneras de asignar colores a valores numéricos. En aprendizaje automático, usar escalas como blanco y negro puede ser útil para visualizar datos de entrada en redes neuronales.

2. _plt.colorbar()_:
    - Muestra una barra de colores al lado de la imagen para representar la escala de valores (por ejemplo, de 0 a 1 en imágenes normalizadas).

3. _plt.show()_:
    - Renderiza y muestra el gráfico en pantalla. Sin esta línea, la imagen no aparecería.


## 9. Configuración del tamaño de la figura
```bash
plt.figure(figsize=(6,6))
```
### ¿Qué es plt.figure()?

_plt.figure()_: 
    - Este método de matplotlib se utiliza para crear una nueva figura (gráfico) o cambiar las propiedades de una figura ya existente.

### Parámetros más comunes de plt.figure:

1. ***figsize (tuple)***:

    - Determina el tamaño de la figura en pulgadas (ancho, alto).

    - Por ejemplo, (6,6) crea un gráfico cuadrado con 6 pulgadas de ancho y alto.

    - **Importante: El tamaño afecta la claridad y la resolución al guardar o mostrar las figuras.**

2. ***dpi (int)***:

    - Define los "dots per inch" (puntos por pulgada) de la figura. Un valor mayor resulta en una imagen más detallada.

3. ***facecolor (color)***:

    - Establece el color de fondo de la figura.

4. ***num (int o str)***:

    - Asigna un identificador único a la figura, útil para manipular varias figuras simultáneamente.

**Salida**

Crea o modifica una figura que puede ser usada para graficar datos.

## 10. Mostrar una imagen dentro de la figura
```bash
plt.imshow(imagen, cmap=plt.cm.binary)
``` 

### ¿Qué es plt.imshow()?

_plt.imshow()_:
    - Se utiliza para visualizar datos bidimensionales (como imágenes o mapas de calor) en forma de gráfico.

**Parámetros principales de plt.imshow:**

1. ***X (array-like)***:

    - Datos que se van a visualizar.

    - En este caso, imagen es un array de 28x28 que representa una imagen en escala de grises.

2. ***cmap (str o Colormap)***:

    - Define el mapa de colores. Ejemplo: plt.cm.binary muestra la imagen en escala de grises.

3. ***interpolation (str)***:

    - Define cómo se interpola entre valores de píxeles. Opciones comunes:

    - 'nearest': Usa el valor del píxel más cercano.

    - 'bicubic': Genera una transición suave entre valores.

4. ***aspect (str o float)***:

    - Relación de aspecto del gráfico. Opciones:

    - 'auto': Ajusta automáticamente el aspecto según los datos.

    - 'equal': Mantiene proporciones iguales entre ancho y alto.

**Salida**
Muestra la imagen en la figura actual.

## 11. Agregar una barra de colores
```bash
plt.colorbar()
```
### ¿Qué es plt.colorbar()?

_plt.colorbar()_: 
    - Agrega una barra de colores a la figura actual.

**Uso:**

    - Te permite visualizar la escala de valores representada por los colores en el gráfico.

    - En el caso de imágenes normalizadas, muestra un rango de 0 a 1.

**Parámetros comunes:**

1. ***mappable:***

    - Objeto gráfico (como el devuelto por plt.imshow()) al cual está asociada la barra de colores.

2. ***orientation (str):***

    - Dirección de la barra: 'vertical' (predeterminada) o 'horizontal'.

**Salida**
    Renderiza una barra que muestra la escala de colores usada en el gráfico.

## 12. Mostrar el gráfico final
```bash
plt.show()
```
### ¿Qué es plt.show()?

_plt.show():_
    - Renderiza y muestra la figura creada con los comandos anteriores.

***Detalles importantes:***

- Sin esta línea, el gráfico no se visualizará en pantalla.

-   Solo se necesita una vez por figura.

**Salida**

Muestra la figura en pantalla.

## 13. Mostrar múltiples imagenes con etiqueta 

```bash
plt.figure(figsize=(10,10))
for i, (imagen, etiqueta) in enumerate(datos_entrenamiento.take(25)):
    imagen = imagen.numpy().reshape((28,28))
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(imagen, cmap=plt.cm.binary)
    plt.xlabel(nombres_clases[etiqueta])
plt.show()
```
### Explicación teórica y práctica del código:

[Conceptos fundamentales de tensores](./docs/tensores.md)

1. ***Creación de la figura:***

    - plt.figure(figsize=(10,10))

- Utiliza el método plt.figure() para definir una figura cuadrada de 10x10 pulgadas.

2. ***Bucle for con enumerate:***

    - for i, (imagen, etiqueta) in enumerate(datos_entrenamiento.take(25)):

- for: Iterador que recorre los primeros 25 elementos de datos_entrenamiento.

- enumerate: Genera índices (desde 0) y elementos al iterar, útil para numerar automáticamente las imágenes.

**Ejemplo**
[Conceptos fundamentales de búcles](./)
```bash
for i, valor in enumerate(["a", "b", "c"]):
    print(i, valor)
# Salida: 0 a
#         1 b
#         2 c
```
3. ***Transformación de la imagen:***
```bash
imagen = imagen.numpy().reshape((28,28))
```
- Convierte un tensor en un array de Numpy con .numpy().

- Cambia su forma a una matriz de 28x28 píxeles usando .reshape().

4. ***subplots para la grilla:***
```bash
plt.subplot(5,5,i+1)
```
- Divide la figura en una cuadrícula de 5x5 subgráficos.
- i+1: Selecciona la posición del subplot (1 a 25).

### Ejemplo
```bash
plt.subplot(2,2,1)  # Gráfica en el primer cuadrante de una grilla 2x2
```

5. ***Personalización del gráfico:***
```bash
plt.xticks([])
plt.yticks([])
plt.grid(False)
```
- plt.xticks([]), plt.yticks([]): Elimina las marcas de los ejes X e Y.
- plt.grid(False): Desactiva las líneas

# 14. Creación del modelo 
El modelo es creado utilizando tf.keras.Sequential, una API de alto nivel de TensorFlow que permite definir y entrenar redes neuronales de forma sencilla. A continuación, se desglosa cada parte del código:

## Definición del modelo
```bash
modelo = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28,1)), #1 - blanco y negro
    tf.keras.layers.Dense(50, activation=tf.nn.relu),
    tf.keras.layers.Dense(50, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax) #Para redes de clasificación
])
```

1. **tf.keras.Sequential**
- ***Descripción:*** tf.keras.Sequential es una forma de construir modelos donde las capas son apiladas secuencialmente.
- ***Uso:*** Útil para arquitecturas simples, donde cada capa tiene exactamente una entrada y una salida.

**Parámetros del constructor:**

- ***layers (list):*** Lista de capas de la red. Se agregan en el orden en que se ejecutarán durante el entrenamiento y la inferencia.

**Salida:**
Crea un modelo secuencial con las capas definidas.

2. **tf.keras.layers.Flatten**
```bash
tf.keras.layers.Flatten(input_shape=(28,28,1))
```
**Descripción:**

- Convierte una entrada multidimensional en un vector unidimensional.
- En este caso, las imágenes de entrada tienen forma (28,28,1) (altura, ancho, canales). Este formato es común en imágenes en escala de grises.

**Parámetros del constructor:**
- ***input_shape (tuple):*** Forma esperada de la entrada.
    - (28,28,1) representa imágenes de 28x28 píxeles con un solo canal (blanco y negro).

**Ejemplo práctico**
Si la entrada es:
```bash
[[[1], [2]],
 [[3], [4]]]
```

La salida será:
```bash
[1, 2, 3, 4]
```

