##
## Imprima la cantidad de registros por cada letra 
## de la columna _c1 de la tabla tbl0
## 

# Importar librerias

import pandas as pd
import numpy as np

# Lectura de archivos

datos = pd.read_csv('tbl0.tsv', sep='\t')

# Solucion de ejercicio

q01 = datos.groupby('_c1')['_c0'].count()

# Imprimimos en formato necesario

print(q01)