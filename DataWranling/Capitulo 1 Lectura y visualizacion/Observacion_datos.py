'''
############ Atributo SHAPE ##########

Si se desea almacenar el numero de filas y columnas como variables, se puede utilizar el atributo shape, este atributo devuelve el numero de filas 
y el numero de columnas dentro de un data set.

Al usar SHAPE en un DataFrame, este siempre arroja primero el numero de filas y luego el numero de columnas  

'''

import pandas as pd 
data = pd.read_excel('/Users/hectorciddelprado/Desktop/datasets/Housing Index Data editable.xlsx')

n_rows, n_columns = data.shape

print(f'EL numero de filas es: {n_rows}, el numero de columnas es: {n_columns}')

'''
La función data.shape devuelve una tupla como salida. Una tupla es un tipo de datos en Python,
al igual que las listas y otros tipos. En palabras sencillas, una tupla es una colección de objetos separados por comas.

Una tupla es similar a una lista de Python en términos de indexación, objetos anidados y repetición.
Sin embargo, la principal diferencia entre ambas es que una tupla Python es INMUTABLE (no puede modificarse),
mientras que una lista Python es mutable.
'''

############### METODO SAMPLE() ###############

'''
El método SAMPLE() selecciona filas aleatorias del DataFrame en lugar de filas consecutivas del principio o del final del DataFrame.

SAMPLE() a diferencia de head() y tail() selecciona 1 fila por defecto, por lo cual es necesario espeficicar el numero de filas que queremos
observar. Ademas, cada vez que se ejecute dara un(os) nuevo(s) numero(s) al azar

para obtener el mismo resultado cada vez que se ejecute el codigo,
necesitas usar el parametro ramdom_state= y establecer algun numero entero de tu eleccion, esto funciona como un "ID" de los numeros
que te arrojo. 
'''

print(data.sample(6, random_state=1000))
print(data.sample(6))
print(data.sample(6, random_state=1000))


###### metodo DESCRIBE() ########

'''
Es un método muy práctico para obtener información sobre las columnas numéricas de tus datos como son:
#### count, mean, min, max, cuartil 1 (25%), mediana (%50), tercer cuartil (%75) y desviacion standard.####
Puedes llamar a describe() en un DataFrame o en un Series; devuelve el mismo tipo de objeto en el que fue llamado.

De forma predeterminada se ignoran las columnas NO numericas
'''

print(data.describe())

# se puede aplicar para Series dentro de un dataFrame basta con agregar que columna tiene:

print(data['Year'].describe()) # imprime solo la columna "Year" con la analitica descriptiva antes mencionada

## tambien se puede usar para una SERIES que no sea numerico, en este caso se usara la columna 'city' que contiene nombres de las ciudades

print(data['city'].describe())
'''
obtenemos la siguiente información útil:

--- > 'count': el número de valores no nulos;
--- > 'unique': el número de valores únicos;
--- > 'top': el valor que aparece con más frecuencia;
--- > 'freq': el número de veces que ocurre el valor más frecuente.

UNIQUE, TOP Y FREQ solo se devuelven o se imprimen en Series/columnas NO numericas
'''

########## parametro INCLUDE= ########

'''
Podemos utilizar el parámetro include= para indicar a describe() qué columnas queremos incluir en nuestro resultado.
Sin embargo, no vamos a pasar una lista de nombres de columnas como argumento. En lugar de eso, pasamos EL TIPO DE DATOS de las columnas
que queremos como una cadena (o una lista de cadenas si queremos más de un tipo de datos).


En python Object suele referirse a cadenas (o columnas con tipos de datos mixtos)
'''

print(data.describe(include=object))

### si queremos incluir todos los tipos de datos basta con usar la palabra 'all'
print(data.describe(include='all'))



