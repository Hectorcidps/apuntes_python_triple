'''
Como leer archivos de excel 

import pandas as pd 
data = pd.read_excel('nombre_del_archivo_excel.xls') 
Los archivos xls suelen ser mas complejos que los csv por lo cual hay que hacer algo extra con los parametros
En primer lugar los archivos excel tienen o pueden contener varias hojas por lo cual es necesario utilizar el parametro 
sheet_name='nombre_de_la_hoja' solo se puede cargar UNA HOJA A LA VEZ POR LO CUAL SINO SE ESTABLECE SE PRESENTA LA PRIMERA HOJA POR DEFAULT

#### SINTAXIS 
data = pd.read_excel('nombre_del_archivo_excel.xls', sheet_name='nombre_de_la_hoja') 

'''
import pandas as pd 
data = pd.read_excel('/Users/hectorciddelprado/Desktop/datasets/Housing Index Data editable.xlsx')

print(data.head(10))
#print(data.columns)

