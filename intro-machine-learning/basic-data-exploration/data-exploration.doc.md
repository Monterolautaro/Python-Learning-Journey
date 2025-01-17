# Teoría básica sobre exploración de datos

En esta sección estará la teoría vinculada al archivo de práctica: [Basic data exploration](./)

# Indice

1. [Introducción](#introducción)
2. [Interpreting data description](#interpreting-data-description)

## Introducción
El primer paso en cualquier proyecto de aprendizaje automático es familiarizarte con los datos. Vamos a usar la librería ```pandas``` para esto. Pandas es la herramienta principal que los cientificos de datos usan para explorar y manipular los datos. La mayoría de las personas abrevian pandas en su código como ```pd```
```bash
import pandas as pd
```
Lo mas importante de la librería Pandas es el DataFrame. Un DataFrame almacena el tipo de datos, podemos pensarlo como una tabla. Esto es similar a una sheet en Excel, o una tabla en una base de datos SQL.

Pandas tiene poderosos metodos para la mayoría de cosas que vamos a querer hacer con estos tipos de datos.

Como un ejemplo, miramos los [datos sobre precios de casas](https://www.kaggle.com/datasets/dansbecker/melbourne-housing-snapshot) en Melbourne, Australia. En la practica, vamos a aplicar los mismos procesos a un nuevo set de datos (dataset), el cual tiene precios en Iowa.

El ejemplo de datos de (Melbourne) está en el path: **../input/melbourne-housing-snapshot/melb_data.csv.**

Cargamos y exploramos los datos con los siguientes comandos:
```python
# guardamos los datos en una variable para un acceso mas sencillo
melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
# Leemos y guardamos los datos en un DataFrame titulado melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path) 
# mostramos un resúmen de los datos alojados en Melbourne data
melbourne_data.describe()
```

<body>
    <table>
        <thead>
            <tr>
                <th>Metric</th>
                <th>Rooms</th>
                <th>Price</th>
                <th>Distance</th>
                <th>Postcode</th>
                <th>Bedroom2</th>
                <th>Bathroom</th>
                <th>Car</th>
                <th>Landsize</th>
                <th>BuildingArea</th>
                <th>YearBuilt</th>
                <th>Lattitude</th>
                <th>Longitude</th>
                <th>Propertycount</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Count</td>
                <td>13580.000000</td>
                <td>1.358000e+04</td>
                <td>13580.000000</td>
                <td>13580.000000</td>
                <td>13580.000000</td>
                <td>13580.000000</td>
                <td>13518.000000</td>
                <td>13580.000000</td>
                <td>7130.000000</td>
                <td>8205.000000</td>
                <td>13580.000000</td>
                <td>13580.000000</td>
                <td>13580.000000</td>
            </tr>
            <tr>
                <td>Mean</td>
                <td>2.937997</td>
                <td>1.075684e+06</td>
                <td>10.137776</td>
                <td>3105.301915</td>
                <td>2.914728</td>
                <td>1.534242</td>
                <td>1.610075</td>
                <td>558.416127</td>
                <td>151.967650</td>
                <td>1964.684217</td>
                <td>-37.809203</td>
                <td>144.995216</td>
                <td>7454.417378</td>
            </tr>
            <tr>
                <td>Std</td>
                <td>0.955748</td>
                <td>6.393107e+05</td>
                <td>5.868725</td>
                <td>90.676964</td>
                <td>0.965921</td>
                <td>0.691712</td>
                <td>0.962634</td>
                <td>3990.669241</td>
                <td>541.014538</td>
                <td>37.273762</td>
                <td>0.079260</td>
                <td>0.103916</td>
                <td>4378.581772</td>
            </tr>
            <tr>
                <td>Min</td>
                <td>1.000000</td>
                <td>8.500000e+04</td>
                <td>0.000000</td>
                <td>3000.000000</td>
                <td>0.000000</td>
                <td>0.000000</td>
                <td>0.000000</td>
                <td>0.000000</td>
                <td>0.000000</td>
                <td>1196.000000</td>
                <td>-38.182550</td>
                <td>144.431810</td>
                <td>249.000000</td>
            </tr>
            <tr>
                <td>25%</td>
                <td>2.000000</td>
                <td>6.500000e+05</td>
                <td>6.100000</td>
                <td>3044.000000</td>
                <td>2.000000</td>
                <td>1.000000</td>
                <td>1.000000</td>
                <td>177.000000</td>
                <td>93.000000</td>
                <td>1940.000000</td>
                <td>-37.856822</td>
                <td>144.929600</td>
                <td>4380.000000</td>
            </tr>
            <tr>
                <td>50%</td>
                <td>3.000000</td>
                <td>9.030000e+05</td>
                <td>9.200000</td>
                <td>3084.000000</td>
                <td>3.000000</td>
                <td>1.000000</td>
                <td>2.000000</td>
                <td>440.000000</td>
                <td>126.000000</td>
                <td>1970.000000</td>
                <td>-37.802355</td>
                <td>145.000100</td>
                <td>6555.000000</td>
            </tr>
            <tr>
                <td>75%</td>
                <td>3.000000</td>
                <td>1.330000e+06</td>
                <td>13.000000</td>
                <td>3148.000000</td>
                <td>3.000000</td>
                <td>2.000000</td>
                <td>2.000000</td>
                <td>651.000000</td>
                <td>174.000000</td>
                <td>1999.000000</td>
                <td>-37.756400</td>
                <td>145.058305</td>
                <td>10331.000000</td>
            </tr>
            <tr>
                <td>Max</td>
                <td>10.000000</td>
                <td>9.000000e+06</td>
                <td>48.100000</td>
                <td>3977.000000</td>
                <td>20.000000</td>
                <td>8.000000</td>
                <td>10.000000</td>
                <td>433014.000000</td>
                <td>44515.000000</td>
                <td>2018.000000</td>
                <td>-37.408530</td>
                <td>145.526350</td>
                <td>21650.000000</td>
            </tr>
        </tbody>
    </table>
</body>

## Interpreting data description
Los resultados muestran 8 números por cada columna en tu set de datos original. El primer número, la cuenta, muestra cuántas filas tienen valores no faltantes.

Los valores faltantes surgen por varias razónes. Por ejemplo, el tamaño de la segunda cama podría no ser recopilado cuando encuestan a una casa de 1 dormitorio. Luego vamos a volver a ver los datos faltantes.

El segundo valor es el promedio (mean), que representa la media. Debajo de este, 'std' es la desviación estándar, que mide qué tan dispersos están los valores numéricamente.

Para interpretar el minimo, 25%, 50%, 75% y los valores máximos, imagina acomodar cada columna desde el valor mas bajo al mas alto. El primer valor (el mas bajo) es el min. Si avanzamos un cuarto en la lista, vamos a encontrar un número que es mayor que el 25% de los valores y menor que el 75% de ellos. eSE ES EL 25% value (pronunciado "25th percentil"). El 50th y 75th percentiles son definidos analogamente, y el max es el valor más grande.

