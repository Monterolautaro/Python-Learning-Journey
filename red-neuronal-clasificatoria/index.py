import tensorflow as tf
import numpy as np
import tensorflow_datasets as tfds

### 1. Cargar el conjunto de datos
datos, metadatos = tfds.load('fashion_mnist', as_supervised=True, with_info=True)


### 2. Separar entrenamiento y pruebas
datos_entrenamiento, datos_pruebas = datos['train'], datos['test']

# 3. Obtener nombres de las clases
nombres_clases = metadatos.features['label'].names


## 4. Normalizar los datos (pasar de 0-255 a 0-1)
def normalizar(imagen, etiquetas):
    imagenes = tf.cast(imagen, tf.float32)
    imagenes /= 255 # Aca lo pasa de 0-255 a 0-1
    return imagenes, etiquetas


# 5. Normalizar los datos de entrenamiento y pruebas con la funcion normalizar
datos_entrenamiento = datos_entrenamiento.map(normalizar)
datos_pruebas = datos_pruebas.map(normalizar)

# 6. Agregar a caché (usar memoria en lugar de disco, entrenamiento mas rapido)
datos_entrenamiento = datos_entrenamiento.cache()
datos_pruebas = datos_pruebas.cache()


# 7. Mostrar una imagen de los datos de pruebas
for imagen, etiqueta in datos_entrenamiento.take(1):
    break
imagen = imagen.numpy().reshape((28,28)) # Redimensionar, cosas de tensores

# 8. Graficar una imagen 
import matplotlib.pyplot as plt
#Dibujar
plt.figure()
plt.imshow(imagen, cmap=plt.cm.binary)
plt.colorbar()
plt.grid(False)
plt.show


# 13. Graficar múltiples imágenes con etiquetas:

plt.figure(figsize=(10,10))
for i, (imagen, etiqueta) in enumerate(datos_entrenamiento.take(25)):
    imagen = imagen.numpy().reshape((28,28))
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(imagen, cmap=plt.cm.binary)
    plt.xlabel(nombres_clases[etiqueta])
    plt.show


# 14. Creación del modelo
modelo = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28,1)), #1 - blanco y negro
    tf.keras.layers.Dense(50, activation=tf.nn.relu),
    tf.keras.layers.Dense(50, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax) #Para redes de clasificación
])
# Flatten: Convierte la matriz 2D (28x28) en un vector 1D.
# Dense: Capas totalmente conectadas con 50 neuronas y activación ReLU.
# Softmax: Devuelve probabilidades (usado en clasificación).


modelo.compile(
    optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),
    metrics=['accuracy']
)

num_ej_entrenamiento = metadatos.splits['train'].num_examples
num_ej_pruebas = metadatos.splits['test'].num_examples

TAMANO_LOTE = 32

datos_entrenamiento = datos_entrenamiento.repeat().shuffle(num_ej_entrenamiento).batch(TAMANO_LOTE)
datos_pruebas = datos_pruebas.batch(TAMANO_LOTE)

# batch: Divide los datos en lotes de tamaño 32.
# shuffle: Baraja los datos de entrenamiento.
# repeat: Hace que el dataset sea infinito (útil para varias épocas).

## Entrenar el modelo
import math

historial = modelo.fit(
    datos_entrenamiento, 
    epochs=5,
    steps_per_epoch=math.ceil(num_ej_entrenamiento/TAMANO_LOTE),
    validation_data=datos_pruebas,
    validation_steps=math.ceil(num_ej_pruebas/TAMANO_LOTE)
)
# epochs=5: Realiza 5 pasadas completas por los datos de entrenamiento.
# validation_data: Evalúa el modelo con datos de prueba después de cada época.


# Resultado de la función de perdida
plt.xlabel("# Epoca")
plt.ylabel("Magnitud de perdida")
# Graficar pérdida por época:
plt.plot(historial.history['loss'])
plt.show()


# Generar predicciones:
for imagenes_prueba, etiquetas_prueba in datos_pruebas.take(1):
    imagenes_prueba = imagenes_prueba.numpy()
    etiquetas_pruebas = etiquetas_prueba.numpy()
    predicciones = modelo.predict(imagenes_prueba)

# Funciones para graficar predicciones:
def graficar_imagen(i, arr_predicciones, etiquetas_reales, imagenes):
    arr_predicciones, etiqueta_real = arr_predicciones[i], etiquetas_reales[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(imagenes[i], cmap=plt.cm.binary)

    etiqueta_prediccion = np.argmax(arr_predicciones)

    if etiqueta_prediccion == etiqueta_real:
        color = 'blue' # Si es correcto
    else:
        color = 'red' # Si es incorrecto

    plt.xlabel("{} {:2.0f}% ({})".format(
        nombres_clases[etiqueta_prediccion],
                                100*np.max(arr_predicciones),
                                nombres_clases[etiqueta_real],
                                color=color))
    
    
def graficar_valor_arreglo(i, arr_predicciones, etiqueta_real):
    arr_predicciones, etiqueta_real = arr_predicciones[i], etiqueta_real[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    grafica = plt.bar(range(10), arr_predicciones, color="#777777")
    plt.ylim([0, 1])
    etiqueta_prediccion = np.argmax(arr_predicciones)
    
    grafica[etiqueta_prediccion].set_color('red')
    grafica[etiqueta_real].set_color('blue')
    
    filas = 5
    columnas = 5
    num_imagenes = filas*columnas
    plt.figure(figsize=(2*columnas, 2*filas))
    for i in range(num_imagenes):
        plt.subplot(filas, columnas, 2*i+1)
        graficar_valor_arreglo(i, predicciones, etiquetas_pruebas)
        
# Tomar cualquier indice del set de pruebas para ver su prediccion
imagen = imagenes_prueba[5]
imagen = np.array([imagen])
prediccion = modelo.predict(imagen)

print("Prediccion: ", nombres_clases[np.argmax(prediccion[0])])