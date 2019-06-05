##
## Agregue el año como una columna a la tabla tbl0.tsv 
## 

# Importar librerias

import pandas as pd 
import numpy as np

# Cargar datos

datos = pd.read_csv('tbl0.tsv', sep = '\t')

# Archivo copia para no afectar original

q08 = datos.copy()

# Crear solucion al ejercicio

q08['ano'] = q08['_c3'].replace('-[0-9][0-9]-[0-9][0-9]','', regex=True).astype(object)

# Imprimirmos en formato necesario

print(q08)