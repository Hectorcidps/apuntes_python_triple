'''
Pre-procesamiento de los valores ausentes: los logaritmos no funcionan adecuadamente con valores faltantes, ademas los logaritmos estadisticos
padecen lo mismo  
'''
import pandas as pd

df = pd.read_csv('/Users/hectorciddelprado/Desktop/datasets/music_log.csv')
#print(df.columns)
print(df.head(8))

'''
valores ausentes pueden faltar porque el usuario no inserto la informacion necesaria, o el sistema automatizado fallo

Los valores ausentes tiene dos formas esperadas: None o NaN

---- None es una instancia del objeto NoneType que significa ausencia de un valor o nulo
---- NaN se trata como un tipo float, son aquellos valores que no estan definidos o no se puede presentar

Las formas inesperadas son: 
--- 0
--- ?
--- NN
--- n/a
--- si aparece un caracter especial puede tratarse de un None o NaN 
'''

'''
################ METODO ISNA() o ISNULL() ############

isna() o isnull() ----> que columnas tienen valores ausentes, se recomienda usar ISNA() es el mas usado en el mercado. 
por si solo arroja TRUE(si hay valores ausentes) o FALSE(si NO hay valores ausentes), se debe usar con el metodo sum() si se desea saber cuantos
valores ausentes existen en una columna 
'''
print(df.isna()) # imprime TODAS las columnas con True o False
print(df.isna().sum()) # imprime TODAS las columnas con el total de valores ausentes

# print(df.isnull()) Imprime lo mismo que los metodos de arriba pero es menos usado 
# print(df.isnull().sum())


'''
################# Metodo Fillan ############
Los valores ausentes se pueden reemplazar con otros valores, ya que las demas columnas de una fila pueden contener datos valiosos
por lo cual podemos usar el metodo: 
fillan() ----> completar valores ausentes

Sustituir valores NaN con 0, al usar el metodo fill devolvera
una copia de la columna original con todos los valores NaN reemplazados por un valor especificado
'''
# df['total play'] = df['total play'].fillna(0)
df['total play'].fillna(0, inplace=True) # esta es una forma MAS sencilla de hacerlo utiliando el parametro inplace=
#print(df)
print(df.isna().sum())

## hacerlo mediante un bucle for, esta FORMA ES CUANDO SE TIENEN MULTIPLES COLUMNAS LAS CUALES DESEAN SER CAMBIADAS 

# se crea la lista donde contenga todos los valores total play
'''columns_to_replace = ['total play']
for col in columns_to_replace:
    df[col].fillna(0, inplace=True)
'''


'''
############### Metodo dropna ##############
dropna() ----> eliminar filas o columnas con valores ausentes
Este metodo elimina las filas que les falta al menos 1 valor 
'''
#df = df.dropna(subset=['genre', 'track']) # subset es un parametro para que solo elimine las filas con valores nulos, y solo en las columnas elegidas
#print(df)
#print(df.isna().sum())

# Ahora para eliminar las COLUMNAS con valores nulos usaremos lo siguiente:
## ARGUMENTO AXIS, nos permite elegir entre columnas y filas

df =df.dropna(axis='columns')
print(df) # imprime solo las columnas que no tengan valores nulos, ya que las que si tenian fueron ELIMINADAS




