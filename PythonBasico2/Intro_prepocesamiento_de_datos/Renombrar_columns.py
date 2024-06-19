'''
Algunos problemas típicos con los nombres de columna incluyen:

-- Nombres de columna que contienen espacios. Pueden ser fáciles de pasar por alto y crear problemas al intentar acceder a una columna. 
-- Es mejor utilizar snake_case al nombrar columnas y variables.
-- Falta de claridad en los nombres de columna. Puede ser difícil saber qué representan los datos en una columna.
'''

############ Metodo RENAME() ##############

'''
El primer paso es revisar el DataSet para saber si hay un error utilizando el metodo info()
'''

import pandas as pd

df = pd.read_csv('/Users/hectorciddelprado/Desktop/datasets/music_log.csv')
print(df.info())

#### EJEMPLO DEL USO DEL METODO RENAME()

## PASO 1 crear dataframe 

# Creamos una lista con los datos qu vamos a usar en el DataFrame
measurements = [
    ['Sun', 146, 152],
    ['Moon', 0.36 , 0.41],
    ['Mercury', 82 , 217],
    ['Venus',38 , 261],
    ['Mars', 56 , 401],
    ['Jupiter', 588 , 968],
    ['Saturn', 1195 ,1660],
    ['Uranus', 2750 , 3150],
    ['Neptune', 4300 , 4700 ],
    ['Halley\'s comet', 5, 5400]
]
# en una variable nueva colocamos los nombres de las columnas
header = ['Celestian bodies ', 'MIN', 'MAX']
# asignamos el nombre del DF en este caso 'planetas', y lo declaramos como dataframe
planetas = pd.DataFrame(data=measurements, columns=header)# no olvidar usar data y columns agregando la variable donde se almacena cada una de la informacion

### PASO 2, verificar el nombre de las columnas para identificar si hay errores que se deban corregir

print(planetas.columns) # aqui utilizamos el metodo columns para saber con exactitud en nombre de cada columna 

'''
Al imprimir el nombre de las columnas detectamos que Celestian bodies tiene un espacio extra y la primera letra esta en mayuscula, 
ademas MIX Y MAX estan en mayusculas y no son muy explicitas, es decir, 
no sabemos con exactitud a que se refieren los datos contenidos en esas variables
'''

#### PASO 3, usar el metodo rename() utilizando un diccionario para modificar los errores en los nombres de las columnas detectados

# diccionario donde se agrega exactamente igual el nombre de la columna por la que se desea reemplazar
columns_new = {
    "Celestian bodies ": "celestian bodies",
    "MIN": "min_distance",
    "MAX":"max_distance"
}
# llamar a la variable anteriormente usada donde se declara el DF y ahi usar el metodo rename(aqui va columns y el nombre del diccionario donde se modifico los nombres)
planetas = planetas.rename(columns=columns_new)
print(planetas.columns) # se reimprime planetas para ver los cambios hechos

## existe otra forma de hacerlo mediante inplace = 

# Se declara el diccionario como primer paso ..... 

# Despues se hace uso del parametro inplace=
planetas.rename(columns_new, inplace= True)
print(planetas.columns)

## una tercer forma de hacerlo seria mediante un bucle for, esto es AUTOMATIZACION 

# Se crea una lista vacia donde se almacenaran las modificaciones
new_col_name = []
# se inicia el ciclo for
for old_name in planetas.columns:
    name_stripped = old_name.strip() # se eliminan los espacios al principio y al final
    name_lowered = name_stripped.lower() # se convierten todos los caracteres en minusculas
    name_no_spaces = name_lowered.replace(' ', '_') # reemplazamos los espacios entre palabras con _
    new_col_name.append(name_no_spaces) # agregamos a la nueva lista todo lo antes hecho, colocando el ultimo metodo hecho, ya que va de arriba hacia abajo las acciones

planetas.columns = new_col_name # Reasignamos el nombre de las columnas por la lista que hemos modificado es decir new_col_name
print(new_col_name)
