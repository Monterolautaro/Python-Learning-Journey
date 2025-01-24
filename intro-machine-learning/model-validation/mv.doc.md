# Teoría básica sobre la válidación de modelos de aprendizaje automático

En esta sección estará la teoría vinculada al archivo de práctica: [Model validation](./mv.py)

## Indice

1. [Introducción](#introducción)
2. [The problem with example scores](#the-problem-with-in-sample-scores)
3. [Coding it](#coding-it)

## Introducción

¿Qué es la válidación de modelos?

Vamos a querer evaluar el rendimiento de todos los modelos que construyamos. En la mayoría de aplicaciones (a pesar de que no en todas), la medida relevante para la cálidad del modelo es la precisión de sus predicciones. En otras palabras, si las predicciones del modelo van a ser cercanas a lo que pasa realmente. 

Algunas personas cometen un grabe error cuando miden la precisión de las predicciónes. Hacen predicciónes con sus datos de entrenamiento y comparan esas predicciónes con los valores objetivo en sus datos de entrenamiento. Vamos a ver el problema con este metodo y como resolverlo en un momento, pero primero pensemos sobre cómo hacemos esto.

Primero necesitariamos resumir la cálidad del modelo en una forma entendible. Si comparamos los valores predichos y los valores actuales para los valores de casas por 10,000 casas, seguramente nos encontremos con un mix de buenas y malas predicciones. Mirar a través de una lista de 10,000 valores predichos y actuales sería inútil. Necesitamos resumir esto en una sola metrica.

Hay varias metricas para resumir la cálidad del modelo, pero vamos a empezar con una llamada "Mean Absoulute Error" (También llamada "MAE"). Vamos a descomponer esta metrica empezando con la última palabra, error.

El error de predicción para cada casa es:
```bash
error=actual−predicted
```
Entonces, si una casa cuesta $150,000 y predecimos que cuesta $100,000, el error es $50,000.

Con la metrica MAE, tomamos el valor absoluto de cada error. Esto convierte cada error en un número positivo. Luego, tomamos el promedio de esos errores absolutos. Esta es nuestra medida de la calidad del modelo. 

Para calcular MAE, primeros necesitamos un modelo. Eso se construye en la celda oculta a continuación.
<details>
  <summary>Presiona aquí para ver el contenido oculto</summary>

  ```bash
  # Data Loading Code Hidden Here
import pandas as pd

# Load data
melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 
# Filter rows with missing price values
filtered_melbourne_data = melbourne_data.dropna(axis=0)
# Choose target and features
y = filtered_melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 
                        'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_melbourne_data[melbourne_features]

from sklearn.tree import DecisionTreeRegressor
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(X, y)
```
</details>

<br></br> 

Una vez tengamos el modelo, acá esta cómo podemos calcular el Mean absolute error 
```bash
from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)

# Salida: 434.71594577146544
```

## The problem with 'In-sample' scores
La medida que acabamos de calcular puede ser llamada un puntaje 'in-sample'. Usamos una sola "muestra" de casas tanto para construir el modelo como para evaluarlo. Aquí está el motivo por el cual esto es un problema.

Imaginemos que, en el gran mercado hipotecario real, el color de una puerta no está nada relacionado con el precio de una casa.

Sin embargo, en el ejemplo de datos que usamos para construir el modelo, todas las casas con puertas verdes son muy caras. El trabajo del modelo es encontrar patrones que predigan precios, entonces va a ver este patron, y siempre va a predecir altos precios para casas con puertas verdes.

Desde que este patron fue derivado de los datos de entrenamiento, el modelo va a parecer preciso en los datos de entrenamiento.

Pero si este patrón no se repite cuando el modelo ve datos nuevos, el modelo va a ser muy impreciso cuando lo usamos en la práctica.

Desde que el valor práctico del modelo viene de hacer predicciónes en datos nuevos, medimos la cálidad en datos que no fueron usados para construir el modelo. La forma mas directa de hacer esto, es excluir algunos datos del proceso de construccion del modelo, y luego usarlos para testear la precisión en datos que no fueron visto antes. Estos datos son llamados "Validation data".

## Coding it
La libreria scikit-learn tiene una función ```train_test_split``` para dividir los datos en dos. Vamos a usar uno de estos datos como datos de entrenamiento para el modelo, y los otros datos como datos de validación para calcular ```mean_absolute_error```.

Aca está el código:
```bash
from sklearn.model_selection import train_test_split

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(train_X, train_y)

# get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))

# Salida: 265806.91478373145
```


