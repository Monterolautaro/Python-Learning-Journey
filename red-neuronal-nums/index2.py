## Un algoritmo que me permita pasar de grados Celsius a Grados Fahrenheit

## Con programación regular, lo haría de la siguiente manera:
def convert(c):
    f = c * 1.8 + 32
    return f

print(convert(12))



## El aprendizaje automatico, me sirve cuando no se la formula u algoritmo con el cual llegar al resultado

import tensorflow as tf
## Es una biblioteca de aprendizaje automático que permite
# crear, entrenar y evaluar modelos de redes neuronales.

import numpy as np
# Es una biblioteca para realizar operaciones matemáticas
# rápidas y eficientes con matrices y arrays multidimensionales.

## Los arrays de numpy son mucho mas rápidos y permiten hacer operaciones matematicas directamente 
## en el array, sin tener que recorrer los valores uno por uno.

celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)   
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)


# capa = tf.keras.layers.Dense(units=1, input_shape=[1]) ## 1 capa, 1 entrada
# modelo = tf.keras.Sequential([capa]) ## Un modelo con una capa

            # Keras, qué es?
# Keras: Es una biblioteca de alto nivel integrada en TensorFlow que permite construir 
# y entrenar modelos de redes neuronales de forma sencilla y modular.

# Proporciona abstracciones fáciles de usar para trabajar con redes neuronales sin preocuparse
# demasiado por los detalles matemáticos o la implementación subyacente.

## Luego de acceder a keras de tensorflow (tf.keras) definimos las capas (layer)
## que vamos a utilizar

## Es una capa densa (o completamente conectada),
# donde cada neurona está conectada con todas las neuronas de la capa anterior.


## Sequential: Es un contenedor que permite apilar capas en secuencia.
# Las capas se ejecutan en el orden en que se definen.
# Es ideal para modelos en los que los datos fluyen linealmente, de una capa a la siguiente.

## Documentación de keras:
# https://keras.io/getting_started/intro_to_keras_for_engineers/

oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1]) # Dense(units=3): Crea una capa totalmente conectada con 3 neuronas.
                                                         # input_shape=[1]: Define que la entrada tendrá una única característica
                                                         # (un número, el grado Celsius).

oculta2 = tf.keras.layers.Dense(units=3)                # Dense(units=3): Otra capa con 3 neuronas.
                                                        # No requiere especificar input_shape porque 
                                                        # ya se hereda de la salida de la capa anterior.

salida = tf.keras.layers.Dense(units=1)                 # Dense(units=1): Tiene una sola neurona porque queremos
                                                        # un único valor de salida (el grado Fahrenheit).


modelo = tf.keras.Sequential([oculta1, oculta2, salida])  # tf.keras.Sequential: Es una forma de agrupar las capas en un modelo que
                                                          # se puede entrenar y evaluar. Elas ejecuta en el orden en que se definen.

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
# Se utiliza el optimizador Adam con una tasa de aprendizaje (learning rate) de 0.1.
# Este algoritmo ajusta los pesos de la red para minimizar el error.

    loss='mean_squared_error'
# Calcula el promedio de los errores al cuadrado entre las predicciones y los valores reales.
# Es adecuada para problemas de regresión.
)

print('Empezando el entrenamiento...')
historial = modelo.fit(celsius, fahrenheit, epochs=1000, verbose=False)
# fit: Entrena el modelo usando los datos de entrada (celsius) y salida (fahrenheit).
# epochs=1000: El modelo pasa por los datos 1000 veces para ajustar los pesos.
# verbose=False: Suprime la salida detallada durante el entrenamiento.
print('Modelo entrenado!')

import matplotlib.pyplot as plt
plt.xlabel("# Epoca")
plt.ylabel("Magnitud de pérdida")
plt.plot(historial.history['loss'])
plt.show()
# Se utiliza matplotlib para graficar cómo disminuye el error a medida que avanza el entrenamiento.

print("Hagamos una predicción!")
resultado = modelo.predict(np.array([100.0]))
print('El resultado es ' + str(resultado) + ' fahrenheit!')


## Para mirar los pesos y sesgos de la red neuronal
print("Variables internas del modelo")  
# print(capa.get_weights())
print(oculta1.get_weights())
print(oculta2.get_weights())
print(salida.get_weights())