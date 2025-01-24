# Teoría básica sobre el modelo Random Forest

En esta sección estará la teoría vinculada al archivo de práctica: [Random Forest](./rf.py)

## Indice

1. [Introducción](#introducción)
2. [Ejemplo](#example)
3. [Conclusión](#conclusión)

## Introducción
Los arboles de decisión nos dejaron una dificil decisión. Un arbol profundo con muchas hojas, va a sobreentrenar porque cada predicción viene de datos históricos de solo unas pocas casas en su hoja. Pero un arbol superficial con pocas hojas va a funcionar mal porque falla en capturar las distinciones en los datos crudos.

Incluso las técnicas de modelado mas sofisticadas de hoy en dia enfrentan esta tension entre underfitting y overfitting. Pero, algunos modelos tienen ideas mas inteligentes que pueden llevar a un mejor funcionamiento. Vamos a mirar a los Random Forest como un ejemplo.

El Random Forest usa algunos arboles, y hace una predicción promediando las predicciónes de cada componente del arbol. Generalmente tiene mucha mejor precisión predictiva que un solo arbol de decisión y funciona bien con parámetros por default. Si continuamos modelando, podemos aprender más modelos con incluso mejor funcionamiento, pero algunos de esos son sensibles en encontrar los parametros adecuados. 

## Example

Ya hemos visto el código para cargar datos un par de veces. Al final de la carga de datos, tenemos las siguientes variables:

- train_X
- val_X
- train_y
- val_y

<details>
  <summary>Presiona aquí para ver el código de carga de datos</summary>

  ```bash
import pandas as pd
    
# Cargar datos
melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 
# Filtrar columnas con datos faltantes
melbourne_data = melbourne_data.dropna(axis=0)
# Elegir objetivo y valores
y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 
                        'YearBuilt', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]

from sklearn.model_selection import train_test_split

# dividir los datos en datos de entrenamiento y de validación, para ambos, features y target
# La división es basada en un número random generado. Brindandole un valor número a
# el argumento random_state garantiza que obtengamos la misma división cada vez que
# corremos este script.
train_X, val_X, train_y, val_y = train_test_split(X, y,random_state = 0)
```
</details>
<br></br>

Construimos un modelo random forest similarmente a como construiamos un decision tree en scikit-learn - Esta vez usando la clase ```RandomForestRegressor``` en vez de la ```DecisionTreeRegressor```

```bash
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
melb_preds = forest_model.predict(val_X)
print(mean_absolute_error(val_y, melb_preds))

# Salida: 191669.7536453626
```

## Conclusión

Probablemente haya espacio para un mejor funcionamiento, pero este es una gran mejora en comparación con el error del mejor arbol de decisión que era de 250,000. Hay parametros que nos permiten cambiar el funcionamiento del Random Forest de manera similar a como cambiamos la profundidad máxima de un solo arbol de decisión. Pero una de las mejores características de los modelos Random Forest es que generalmente funcionan razonablemente bien incluso sin este ajuste. 
