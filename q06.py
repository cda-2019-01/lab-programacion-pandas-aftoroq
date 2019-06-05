##
## Imprima la suma de la _c2 por cada letra de la _c1 
## de la tabla tbl0
## 

# Importamos librerias

import pandas as pd

# Cargar datos

datos = pd.read_csv('tbl0.tsv', sep = '\t')

# Crear solucion al ejercicio

q06 = datos.groupby('_c1')['_c2'].sum()

# Imprimimos en formato necesario

print(q06)