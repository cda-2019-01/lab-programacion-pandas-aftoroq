##
## Imprima el promedio de la _c2 por cada letra de la _c1 
## de la tabla tbl0
## 

# Importamos librerias

import pandas as pd

# Creamos archivo con datos

datos = pd.read_csv('tbl0.tsv', sep = '\t')

# Solucion ejercicio

q02 = datos.groupby('_c1')['_c2'].mean()

# Imprimirmos en formato necesario

print(q02)