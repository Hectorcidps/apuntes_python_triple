''' 
Los archivos CSV vienen separados por comas(generalmente) cuando se transforma a un DF de pandas cada elemento separado por una coma 
se separaran en filas y columnas acorde a la informacion

Esta es la forma en que se accede a un archivo CSV usando la funcion read_csv()
import pandas as pd
df = pd.read_csv('/datasets/music_log_chpt_11.csv') <---Aqui se agrega la ruta del archivo

La ruta del archivo depende del sistema operativo, se utiliza:
--- Windows:C\catalog\file.csv
--- MAC y linux: /catalog/file.csv
'''

'''
Archivos EXCEL mediante la funcion read_excel() 

import pandas as pd
df = pd.read_excel('/datasets/music_log_chpt_11.xlsx') <---Aqui se agrega la ruta del archivo

'''

# Para crear un DataFrame se puede hacer apartir de una lista, de un archivo CSV y Excel. 


'''
Metodos HEAD Y TAIL en pandas

Head --- muestra los primeros 5 valores del DF 
Tail --- muestra los ultimos 5 valores del DF
'''

import pandas as pd 

df = pd.read_csv('/Users/hectorciddelprado/Desktop/Python/Ejercicios python/TripleTen/Pandas/music_project_en.csv')
print(df.head(3)) # se puede acceder mediante la indexacion para mostrar en este caso los primeros 3 valores del DF
print(df.tail(7)) # se puede acceder mediante la indexacion para mostrar en este caso los ultimos 7 valores del DF

print(df.info()) # metodo info para traer la informacion del dataset