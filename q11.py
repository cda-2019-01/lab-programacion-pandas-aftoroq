##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c5a
## y _c5b (unidos por ':') de la tabla tbl2.tsv
## 

# Importar librerias

import pandas as pd

# Cargar datos

datos = pd.read_csv('tbl2.tsv', sep = '\t')

# Creamos variable auxiliar que concatene las columnas _c5a y _c5b separados por : .. La denominamos lista para que funcione en la visualizacion final

datos['lista'] = datos[['_c5a','_c5b']].apply(lambda x: ':'.join(map(str,x)), axis=1)

# Ordenamos la base de datos con la nueva columna

datos = datos.sort_values('lista')

# Agrupamos por las columnas _c0 y lista  separando los valores por ,

q11 = datos.groupby('_c0')['lista'].apply(lambda x: ','.join(map(str, x))).reset_index()

# Imprimimos resultado final

print(q11)