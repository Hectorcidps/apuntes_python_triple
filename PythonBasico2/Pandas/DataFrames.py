''' PANDAS es una Libreria (una libreria es una coleccion de codigo que puede reusarse) nos proporciona
una forma sencilla de manipular y analizar datos. 

Para grandes volumenes de datos es mejor usan pandas 

objeto basico -> DATAFRAME es basicamente una tabla con datos en pandas, combina las ideas tanto de diccionarios como de listas anidadas. son estructuras de datos
rapidas, flexibles y expresivas.

Cada dato tiene 2 cordenadas, una fila y una columna

FILA se accede mediante indices (indexacion) comienzan desde 0, las filas suelen representar 1 entidad
COLUMNA se accede por medio de sus nombres, las columnas son los atributos de las entidades(filas)
'''

''' ATRIBUTOS EN PANDAS, es similiar a llamar a un metodo, excepto que NO van seguidos de ()

shape ---> tamaño de un DF(data frame) ejemplo df(nombre de variable).shape
[0] es el indice para filas EJEMPLO --- rows = df.shape[0] arroja el numero de FILAS dentro del DF
[1] es el idice para columnas EJEMPLO --- columns = df.shape[1] arroja el numero de COLUMNAS dentro del DF

dtypes ---> una columna dentro de un DF puede tener varios atributos, al llamar a este atributo nos arroja una lista 
con los tipos de datos que hay en las columnas. Los datos que muestra son distintos a los vistos en PY:

############# Tipos de datos en PANDAS #######
object => string
int64 => interger
### float64 => float 
boal => boal
Columns ---> Almacena una lista que contiene los nombres de las columnas, en formato string:
Ejemplo ---> index['user_id', 'total play', 'Artist', 'genre', 'track'], [dtype='object']
''' 


'''
##### metodo INFO() #####
sintaxis ---  print(df.info())

arroja toda la informacion del data frame:

###### EJEMPLOS DE SALIDAS ######

--- informacion de la estructura de datos --- <class 'pandas.core.frame.DataFrame'>
--- informacion de los indices --- RangeIndex: 67934 entries, 0 to 67933
--- nombre de columnas --- 'user_id', 'total play', 'Artist', 'genre', 'track'
--- cantidad de valores no nulos --- 67934 non-null, 67923 non-null
--- tipos de datos --- object, int64, float64
--- que tipos de datos entran en el dataset --- dtypes: float64(1), object(4)
--- uso de la memoria --- memory usage: 2.6+ MB 
'''
