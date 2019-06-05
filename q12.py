##
## Si la columna _c0 es la clave en las tablas tbl0.tsv
## y tbl2.tsv, compute la suma de tbl2._c5b por cada
## valor en tbl0._c1.
## 

# Importar librerias

import pandas as pd
import numpy as np

# Cargar datos

datos0 = pd.read_csv('tbl0.tsv', sep = '\t')
datos2 = pd.read_csv('tbl2.tsv', sep = '\t')

# Unir las dos bases de datos por la columna _c0

union =  pd.merge(datos0, datos2, on='_c0')

# Agrupar datos por _c5a y sumar los datos de _c5b correspondiente a cada valor de _c5a

q12 = union.groupby('_c5a').agg({'_c5b': np.sum})

# Imprimir resultado

print(q12.iloc[:,0])