### Ejercicio 1

import pandas as pd

# Importo kaggle para descargar el dataset
import kagglehub as kh
# kh.login()

## descargo el dataset usando la libreria de kaggle
path = kh.dataset_download("dansbecker/home-data-for-ml-course")

home_data = pd.read_csv(path)

home_data.describe()