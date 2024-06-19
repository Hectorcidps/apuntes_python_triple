'''
INDEXACION LOGICA O BOOLENA 
filtrar con operaciones logicas, que arrojan como resultado un(os) dato(s) boolean(os), es decir True o False
'''

### 1. encontrar todas las filas que cumplan cierta condicion 

import pandas as pd

df = pd.read_csv('/Users/hectorciddelprado/Desktop/Python/Ejercicios python/TripleTen/Pandas/music_project_en.csv')
print(df['genre'] == 'pop' ) ## filtrar con abreviacion 
print(df.loc[:, 'genre'] == 'pop') # filtrar con metodo loc 

### 2. Usar el resultado obtenido en el paso previo para filtrar el DataFrame original 

''' 3 formas de obtener el resultado usando la indexacion logica. Arroja TODAS las columnas pero unicamente las que cumplan
    con la condicion POP en GENRE 
'''
print(df.loc[df.loc[:, 'genre'] == 'pop']) # usando metodo loc
print(df.loc[df['genre'] == 'pop']) # combinando metodo log y abreviacion 
print(df[df['genre']== 'pop']) # usando la abreviacion 


'''
EJEMPLO DE LA PLATAFORMA 
obtener todas las filas en la que la columna 'Day' contengan unicamente valores 'Friday'
'''
df = pd.read_csv('/Users/hectorciddelprado/Desktop/Python/Ejercicios python/TripleTen/Pandas/music_project_en.csv')
print(df.loc[:, 'Day'] == 'Friday')
print(df.loc[df.loc[:,'Day'] == 'Friday']) # NO OLVIDAR EL :, ANTES DEL NOMBRE DE LA COLUMNA
print(df[df['Day'] == 'Friday']) # notacion abreviada
print(df.loc[df['Day']=='Friday']) # solo en el filtrado con dos metodos loc, se usa el :, y despues el nombre de la columna 


''' 
La tabla resultante solo debe contener filas con 'genre' igual a 'jazz'. 
Almacena la tabla filtrada en la variable jazz_df y muéstrala.
'''
import pandas as pd

df = pd.read_csv('/Users/hectorciddelprado/Desktop/datasets/music_log.csv')

jazz_df = (df[df['genre'] =='jazz']) # SE ALMACENA CON LA NOTACION ABREVIADA
print(jazz_df)


'''

Filtra la tabla original para incluir solamente las canciones que tengan 'total play' mayor que 90 segundos. 
Almacena la tabla filtrada en la variable high_total_play_df y muéstrala.

'''
import pandas as pd

df = pd.read_csv('/Users/hectorciddelprado/Desktop/datasets/music_log.csv')

high_total_play_df = (df.loc[df.loc[:, 'total play'] > 90]) ## filtrado con DOS metodos loc

print(high_total_play_df)


'''
para aplicar varias condiciones, primero podemos aplicar la primera condición y almacenar el resultado. 
Luego, podemos llamar a la indexación lógica con la segunda condición. 
MULTIPLES CONDICIONES del DataSet  selecciona las filas en las que el género es el jazz y el tiempo total de reproducción oscila entre 80 y 130
'''
import pandas as pd

df = pd.read_csv('/Users/hectorciddelprado/Desktop/datasets/music_log.csv')

# selecciona las filas en las que el género es el jazz y el tiempo total de reproducción oscila entre 80 y 130
df = df[df['total play'] >= 80]
df = df[df['total play'] <= 130]
df = df[df['genre'] == 'jazz']

print(df)
