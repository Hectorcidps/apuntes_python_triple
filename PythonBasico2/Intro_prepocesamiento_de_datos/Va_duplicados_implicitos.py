import pandas as pd

###### -- Como encontrar valores duplicados explicitos e implicitos con el metodo DUPLICATED() #########

df = pd.read_csv('/Users/hectorciddelprado/Desktop/datasets/music_log.csv')

## metodo duplicated() para conocer si existen valores duplicados, arroja True o False
print(df.duplicated())
print(df.duplicated().sum()) # usando el metodo sum() sumamos todos los valores duplicados y arroja la suma total


###### -- Como eliminar duplicados explicitos usando el metodo DROP_DUPLICATES() ########
'''
Para eliminar filas completamente duplicadas usamos el metodo DROP_DUPLICATES(), si no queremos hacer reasignacion de variables
usamos el parametro inplace=True
'''
# reasignando la variable df
#df = df.drop_duplicates()
# usando el parametro inplace
df.drop_duplicates(inplace=True)
print(df.duplicated().sum()) # al imprimir muestra 0 ya que los valores duplicados han sido eliminados

# print(df.head()) Al imprimir, los indices o index han cambiado del 1 se pasa al 3 ya que la fila fue eliminada, por lo cual hay que usar:
# el metodo rest_index()

#df = df.drop_duplicates().reset_index() 
# al aplicar este metodo reaorganiza los indices para que vyaan en orden ademas que crea una nueva columna llamada index, donde se muestran los valores antiguos
#print(df.head())

## para borrar la columna INDEX usamos el siguiente metodo:

df = df.drop_duplicates().reset_index(drop=True)
print(df.head())
## esto imprime el DataSet sin duplicados y sin columna index 



'''
Los duplicados implicitos se refieren a que si bien los valores no son identicos, el lenguaje puede transmitir algo similiar por ejemplo:
Ortografia --- behaviour(britanico) / behavior (USA) el idioma usa diferentes palabras segun su ortografia pero significan lo mismo
Errores ortograficos --- Jazz / Jazzz, al tener 3 'Z' esta mal
Uso de mayusculas --- American / american 
'''

## metodo UNIQUE() muestra los duplicados implicitos en una columna 

print(df['genre'].unique()) #Asi se usa la funcion.

#### Si solo queremos saber cuantos duplicados unicos teemos basta con usar el metodo NUNIQUE() arroja la suma de datos unicos
print(df['genre'].nunique())

##### -- Como eliminar duplicados implicitos usando el metodo replace() ########

### si existieran datos duplicados implicitos se usa el metodo replace() para modificarlos, en este caso lo implemente con 'conjazz'

# se pasa primero el valor incorrecto de la tabla y se pone el valor correcto despues
df['genre'] = df['genre'].replace('conjazz', 'jazz')
# Se tiene que pasar en CADA UNO de los valores duplicados
# tambien se puede usar el parametro inplace= para evitar reasignar la variable 
# df['genre'].replace('conjazz', 'jazz', inplace=True) en este caso usare la opcion donde se reasigna la variable 
print(df['genre'].unique())

#### se puede crear una funcion que permita AUTOMATIZAR el cambio de valores duplicados implicitos, esta es la plantilla a usar

'''
def replace_wrong_values(df, column, wrong_values(puede ser una lista), correct_value):
    for wrong_value in wrong_values:
        df[column] = df[column].replace(wrong_value, correct_value)
    return df
'''

rating = ['date', 'name', 'points']
players = [
        ['2018.01.01',  'Rafael Nadal', 10645],
                ['2018.01.08',  'Rafael Nadal', 10600],
                ['2018.01.29',  'Rafael Nadal', 9760],
                ['2018.02.19',  'Roger Federer', 10105], 
                ['2018.03.05',  'Roger Federer', 10060],
                ['2018.03.19',  'Roger Federerr', 9660],
                ['2018.04.02',  'Rafael Nadal Parera', 8770],
                ['2018.06.18',  'Roger Fedrer', 8920],
                ['2018.06.25',  'Rafael Nadal Parera', 8770],
                ['2018.07.16',  'Rafael Nadal Parera', 9310],
                ['2018.08.13',  'Rafael Nadal Parera', 10220],
                ['2018.08.20',  'Rafael Nadal Parera', 10040],
                ['2018.09.10',  'Rafael Nadal Parera', 8760],
                ['2018.10.08',  'Rafael Nadal Parera', 8260],
                ['2018.10.15',  'Rafael Nadal Parera', 7660],
                ['2018.11.05',  'Novak Djokovic', 8045],
                ['2018.11.19',  'Novak Djokovic', 9045]
]
tennis = pd.DataFrame(data=players, columns=rating)
print(tennis)

tennis['name'] = tennis['name'].replace('Roger Federerr', 'Roger Federer')
tennis['name'] = tennis['name'].replace('Roger Fedrer', 'Roger Federer')
tennis['name'] = tennis['name'].replace('Rafael Nadal', 'Rafael Nadal Parera')

print(tennis)

'''
USANDO EL PARAMETRO INPLACE=

tennis['name'].replace('Roger Federerr', 'Roger Federer', inplace = True)
tennis['name'].replace('Roger Fedrer', 'Roger Federer', inplace = True)
tennis['name'].replace('Rafael Nadal', 'Rafael Nadal Parera', inplace = True)

print(tennis)
'''

'''
USANDO UNA FUNCION 

duplicates = ['Roger Federerr', 'Roger Fedrer'] # una lista de nombres mal escritos
name = 'Roger Federer' # el nombre correcto
tennis = replace_wrong_values(tennis, 'name', duplicates, name) # llamar a la función, replace() se llamará dos veces
print(tennis)
'''