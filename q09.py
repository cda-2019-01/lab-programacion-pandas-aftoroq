##
## Construya una tabla que contenga _c1 y una lista
## separada por ':' de los valores de la columna _c2
## para el archivo tbl0.tsv
## 

# Importar librerias

import pandas as pd

# Cargar datos

datos = pd.read_csv('tbl0.tsv', sep = '\t')

# Ordenar datos por columna _c2

datos = datos.sort_values('_c2')

# Agrupar por variables de interes, y dividir valores de c2 por :

q09 = datos.groupby('_c1')['_c2'].apply(lambda x: ':'.join(map(str, x))).reset_index()

# Renombrar columnas para que coincida con el grade

q09 = q09.rename(index=str, columns={"_c2": "lista","_c1": "_c0"})

# Imprimir resultado final

print(q09)


