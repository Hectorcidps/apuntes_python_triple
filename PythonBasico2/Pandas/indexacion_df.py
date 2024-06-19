'''
Como acceder a datos especificos usando la funcion LOC[primer valor: se especifica por medio de la indexacion la fila, segundo: se escribe el nombre de la columna]
'''
import pandas as pd

df = pd.read_csv('/Users/hectorciddelprado/Desktop/Python/Ejercicios python/TripleTen/Pandas/music_project_en.csv')
#result = df.loc[4, 'genre']
#print(result) # imprime el 5 elemento que corresponde a dance

######## como usar el metodo LOC[]
'''
-- celda ----> .loc[7 fila, 'nombre de la columna'] se extrae la info de la fila 8 de la columna elegida 

-- columna (SE PUEDE ABREVIAR) ----> .loc[:, 'genre'] se extrae la info de TODAS las celdas de la columna genre

-- columnas multiples (SE PUEDE ABREVIAR) ----> .loc[:, ['Day', 'genre']] se extrae la info de TODAS las celdas de las columnas Day y genre. 
IMPORTANTE: SE ENCIERRAN ENTRE CORCHETES LAS DOS COLUMNAS PORQUE NO SON CONSECUTIVAS

-- multiples COLUMNAS consecutivas (slice) ----> .loc[:, 'artist: 'genre'] se extrae la info de TODAS las celdas de las columnas artist y genre
IMPORTANTE: al ser consecutivas se usa : entre cada nombre la columna

-- una fila ----> .loc[1] Se extraen valores de la segunda fila

-- Todas las filas, empezando por la seleccionada (SE PUEDE ABREVIAR) ----> .loc[1:] Se extraen TODOS los valores desde la segunda fila hasta la ultima fila

-- Todas las filas, hasta la fila seleccionada (SE PUEDE ABREVIAR) ----> .loc[:5] Se extraen TODOS los valores de las 4 primeras filas, es decir desde la 0 hasta la 4

-- multiples FILAS consecutivas (slice) (SE PUEDE ABREVIAR) ----> .loc[2:5] Se extraen TODOS los valores de las celdas entre la tercera y quinta fila
'''

# ejemplo CELDA metodo loc 
df = pd.read_csv('/Users/hectorciddelprado/Desktop/Python/Ejercicios python/TripleTen/Pandas/music_project_en.csv')
celda = df.loc[12, 'artist']
print(celda)

# ejemplo COLUMNA metodo loc
columna = df.loc[:, 'artist']
print(columna)
# ejemplo COLUMNA abreviado
columna_abrev = df['artist']
print(columna_abrev)

# ejemplo COLUMNAS MULTIPLES, SIN SER CONTINUAS metodo loc
mult_colum = df.loc[:, ['genre', 'Day']]
print(mult_colum)
# ejemplo COLUMNAS MULTIPLES, SIN SER CONTINUAS abreviado. ###PRECAUCION DEBE DE IR EN ORDER DE ACUERDO AL NOMBRE LAS COLUMNAS###
multiple_col = df[['Track','genre']]
print(multiple_col)

# ejemplo COLUMNAS MULTIPLES CONTINUAS metodo loc
continuas_multiple = df.loc[:, 'genre': 'Day']
print(continuas_multiple)

# ejemplo UNA FILA metodo loc
fila = df.loc[30000]
print(fila)

# ejemplo Todas las filas metodo loc
all_filas = df.loc[1:]
print(all_filas)
# ejemplo Todas las filas abreviado
all_filas_abre = df[1:]
print(all_filas_abre)

# ejemplo Todas las filas consecutivas metodo loc
todas_filas_sli = df.loc[3:6]
print(todas_filas_sli)
# ejemplo Todas las filas consecutivas abreviado
todas_filas_abre = df[50000:50010]
print(todas_filas_abre)









