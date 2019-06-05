##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c4
## de la tabla tbl1.tsv
## 

# Importar librerias

import pandas as pd

# Cargar datos

datos = pd.read_csv('tbl1.tsv', sep = '\t')

# Ordenar datos por columna _c4

datos = datos.sort_values('_c4')

# Agrupar por variables de interes, y dividir valores de c4 por ,

q10 = datos.groupby('_c0')['_c4'].apply(lambda x: ','.join(map(str, x))).reset_index()

# Renombrar columnas para que coincida con el grade

q10 = q10.rename(index=str, columns={"_c4": "lista"})

# Imprimir resultado final

print(q10)
