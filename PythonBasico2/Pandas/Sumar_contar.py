'''
media, contar y sumar valores en un dataFrame de pandas

3 metodos
---- > mean
---- > count 
---- > sum
'''

############ METODO MEAN ##############
# Sacar el promedio a algo 

import pandas as pd

df = pd.read_csv('/Users/hectorciddelprado/Desktop/datasets/music_log.csv')

# se declara la variable pop para extraer unicamente las canciones con genre pop a traves de la indexacion booleana
pop_df = df[df['genre'] == 'pop']

'''se crea una nueva variable donde se solicita que de las canciones pop extraidas ateriormente se muestre el tiempo de duracion 
almacenado en la columna total play
'''
pop_duration = pop_df['total play']
# print(pop_duration) 

duration_average = pop_duration.mean()
print(duration_average) # muestra el tiempo promedio de todas las canciones del genero pop 

### ES POSIBLE ESCRIBRIR TODo EL CODIGO EN UNA SOLA LINEA #######
mean_duration = df[df['genre'] =='pop']['total play'].mean()
print(mean_duration)



############ METODO COUNT ##############
## nos permite contar el numero de filas que cumplen con una condicion en especial

# primero se establece la variable, que contenga la infor que vamos a comparar con la columna total play 
duration_threshold = 180
# despues se extraen del DataSet las canciones cuya duracion sea mayor a 180, despues se elige la columna de donde provienen estos datos y se aplica el metodo count() 
long_songs = df[df['total play'] > duration_threshold]['total play'].count()
print(long_songs) # se imprime la variable donde se hicieron todos las condiciones



############ METODO SUM ##############
# permite sumar los valores de una fila en especifico o una columna 

## en este caso elimine los espacios existentes en los nombres de las columnas porque me generaban un error
df.columns = df.columns.str.strip() 

user_sum_dur = df[df['user_id'] == 'BF6EA5AF']['total play'].sum()
print(user_sum_dur)



