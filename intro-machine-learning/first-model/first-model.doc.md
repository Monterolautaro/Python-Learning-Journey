# Teoría para crear el primer modelo de aprendizaje automático

En esta sección estará la teoría vinculada al archivo de práctica: [First model](./first-model.py)

# Indice

1. [Selecting data for modeling](#selecting-data-for-modeling)
2. [Selecting The prediction target](#selecting-the-prediction-target)
3. [Choosing features](#choosing-features)
4. [Building your model](#building-your-model)

## Selecting data for modeling
Nuestro set de datos tenía muchas variables para mirarlo, o inclúso para mostrarlo en consola correctamente. Cómo podemos reducir esta gran cantidad de datos a algo que podamos entender?

Vamos a empezar tomando un par de variables usando nuestra intuición. En archivos posteriores vamos a usar tecnias estadísticas para priorizar varibales automáticamente.

Para elegir variables/columnas, vamos a necesitar mirar una lista de todas las columnas en el set de datos. Esto se hace con la propiedad colums del DataFrame (la parte de abajo del código).
```python
import pandas as pd

melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 
melbourne_data.columns

# Salida: Index(['Suburb', 'Address', 'Rooms', 'Type', 'Price', 'Method', 'SellerG',
    #    'Date', 'Distance', 'Postcode', 'Bedroom2', 'Bathroom', 'Car',
    #    'Landsize', 'BuildingArea', 'YearBuilt', 'CouncilArea', 'Lattitude',
    #    'Longtitude', 'Regionname', 'Propertycount'],
    #   dtype='object')
```
Hay varias maneras para seleccionar un subconjunto de las columnas de un DataFrame. El curso de pandas de Kaggle las cubre mas en detalle, pero por ahora vamos a enfocarnos en dos maneras de hacerlo.

1. Dot notation, la cual usamos para seleccionar el "objetivo de predicción" (prediction target).

2. Seleccionando con una lista de columnas, la cual usamos para seleccionar las "caracteristicas".

## Selecting The Prediction Target
Podemos obtener una variable con dot-notation (notación por punto). La única columna es guardada en una Series, que es como un DataFrame con solo una columna de datos.

Vamos a usar dot-notation para seleccionar la columna que queremos predecir, que es llamado el "prediction target". Por convención, el prediction target es llamado ```y```. Asi que el codigo que necesitamos para guardar los precios de la casa en los datos de Melbourne es 
```bash
y = melbourne_data.Price
```

## Choosing "Features"
Las columnas que son escritas en el input en nuestro modelo (y después usados para hacer predicciones) son llamadas "features" (caracteristicas). En nuestro caso, esas van a ser las columnas usadas para determinar el precio de la casa. A veces, vamos a usar todas las columnas, con excepción del objetivo, como cáracteristicas. Otras veces, vamos a estar mejor usando menos de ellas.

Por ahora, vamos a construir un modelo con solo unas pocas features. Luego veremos como iterar y comparar modelos construidos con diferentes features.

Seleccionamos múltiples features brindando una lista de nombres de columnas entre corchetes. Cada item en esa lista debe ser un string (con comillas). 

Acá hay un ejemplo:
```bash
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
```
Por convención, estos datos son llamados ```X```
```bash
X = melbourne_data[melbourne_features]
```
Revisemos rápidamente los datos que vamos a estar usando para predecir precios de casas usando el método ```describe()``` y el método ```head()```, que muestra las primeras filas.
```bash
X.describe()

# Salida: 	Rooms	Bathroom	Landsize	Lattitude	Longtitude
# count	6196.000000	6196.000000	6196.000000	6196.000000	6196.000000
# mean	2.931407	1.576340	471.006940	-37.807904	144.990201
# std	0.971079	0.711362	897.449881	0.075850	0.099165
# min	1.000000	1.000000	0.000000	-38.164920	144.542370
# 25%	2.000000	1.000000	152.000000	-37.855438	144.926198
# 50%	3.000000	1.000000	373.000000	-37.802250	144.995800
# 75%	4.000000	2.000000	628.000000	-37.758200	145.052700
# max	8.000000	8.000000	37000.000000	-37.457090	145.526350

X.head()

# Salida: 	Rooms	Bathroom	Landsize	Lattitude	Longtitude
            # 1	2	1.0	156.0	-37.8079	144.9934
            # 2	3	2.0	134.0	-37.8093	144.9944
            # 4	4	1.0	120.0	-37.8072	144.9941
            # 6	3	2.0	245.0	-37.8024	144.9993
            # 7	2	1.0	256.0	-37.8060	144.9954
```
Visualmente checkear nuestros datos con estos comando es una parte importante en el trabajo de un cientifico de datos. Frecuentemente vamos a encontrarnos sorpresas en los set de datos que merecen ser inspeccionadas. 


## Building your model
Vamos a usar la libreria scikit-learn para crear los modelos. Cuando codeamos, esta libreria es escrita como sklearn, como vamos ver en el código de ejemplo. Scikit-learn es facilmente la libreria mas popular para modelado de tipos de datos tipicamente guardados en DataFrames.

Los pasos para construir y usar un modelo son:

- Define: ¿Qué tipo de modelo va a ser? ¿Un decision tree? ¿Algún otro tipo de modelo? Algúnos otros parametros del tipo de modelo son especificados también.
- Fit: Capturar patrones de los datos brindados. Este es el corazon del modeling.
- Predict: Predecir, justo como suena.
- Evaluate: Determinar qué tan precisas son las prediciones de nuestro modelo.

Acá hay un ejemplo de como definir un modelo decision tree con scikit-learn y entrenandolo con las features y la target variable.
```bash
from sklearn.tree import DecisionTreeRegressor

# Definir el modelo. Especificar el número para random_state para asegurar los mismos resultados en cada ejecución
melbourne_model = DecisionTreeRegressor(random_state=1)

# Entrenar el modelo (Fit)
melbourne_model.fit(X, y)
```
Varios modelos de aprendizaje automatico permiten algo de aleatoriedad en el entrenamiento del modelo. Especificando un numero para ```random_state``` asegura que obtengamos los mismos resultados en cada ejecución. Esto es considerado una buena práctica. Podemos usar cualquier número, y la calidad del modelo no va a depender significativamente de exactamente el valor que elegimos. 

Ahora tenemos el modelo entrenado que podemos usar para hacer predicciónes. 

En la práctica, vamos a querer hacer predicciónes para nuevas casas que lleguen al mercado por sobre casas que ya tenemos los precios. Pero vamos a hacer predicciones por las primeras filas de los datos de entrenamiento para ver como funciona la función de predicción.
```bash
print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))

# Salida: Making predictions for the following 5 houses:
#      Rooms  Bathroom  Landsize  Lattitude  Longtitude
# 1      2       1.0     156.0   -37.8079    144.9934
# 2      3       2.0     134.0   -37.8093    144.9944
# 4      4       1.0     120.0   -37.8072    144.9941
# 6      3       2.0     245.0   -37.8024    144.9993
# 7      2       1.0     256.0   -37.8060    144.9954
# The predictions are

# [1035000. 1465000. 1600000. 1876000. 1636000.]
```