##
## Imprima el maximo de la _c2 por cada letra de la _c1 
## de la tabla tbl0
## 

# Importar librerias

import pandas as pd

# Carga de datos

datos = pd.read_csv('tbl0.tsv', sep = '\t')

# Crear calculo del ejercicio

q03 = datos.groupby('_c1')['_c2'].max()

# Imprimir en formato necesario

print(q03)