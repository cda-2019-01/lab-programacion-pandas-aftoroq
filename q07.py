##
## Agregue una columna  con la suma de _c0 y _c2 a la tabla tbl0.tsv 
## 

# Importamos librerias

import pandas as pd

# Cargar datos

datos = pd.read_csv('tbl0.tsv', sep = '\t')

# Crear columna adicional de suma

datos['suma'] = datos['_c0'] + datos['_c2']

# Imprimir toda la base de datos

print(datos)