##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
## 

# Importar librerias

import pandas as pd 

# Cargar datos

datos = pd.read_csv('tbl1.tsv', sep = '\t')

q04_aux = [x.upper() for x in datos['_c4']]

# Crear solucion al ejercicio

q04 = set([x for x in q04_aux])
q04 = list(q04)
q04.sort()

# Imprimirmos en formato necesario

print(q04)





