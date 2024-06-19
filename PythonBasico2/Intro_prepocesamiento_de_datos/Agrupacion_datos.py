'''
La agrupacion nos permite dividir los datos en grupos segun ciertos criterios
Se puede agrupar por fecha para conocer el trafico de compras mas relevante
Se puede agrupar por ID_cliente para conocer sobre la lealtad de un cliente hacia la marca 
'''

#### Etapas de la agrupacion (Standard)

## dividir -- > en grupos o segementos similares
## aplicar -- > aplicar calculos matematicos con el metodo count o sum 
## combinar -- > combinar los resultados obtenidos 

import pandas as pd
exoplanet = pd.read_csv('/Users/hectorciddelprado/Desktop/datasets/exoplanet.csv')

## print(exoplanet.columns)

#print(exoplanet.head(30))

#print(exoplanet.groupby(by='\tdiscovered')) # Aqui imprime los años de descubrimiento 
print() # linea vacia
#print(exoplanet.groupby(by='\tdiscovered').count()) # aqui aparece el conteo por año y muestra todas las columnas

## Para hacer comparaciones entre parametros hacer lo siguiente, donde se agrega el objeto de la columna que quieres comparar 

##### dividir ####
exo_number = exoplanet.groupby('\tdiscovered') ["\tradius"].count()
print(exoplanet) ## obtuvimos la columna discovered y el conteo de planetas encontrados por radio

### aplicar #####
### obtener la suma de los radios 
exo_number_sum = exoplanet.groupby('\tdiscovered') ["\tradius"].sum()
print(exo_number_sum) 

### combinar ####
### obtener el promedio de los radios encontrados diviendo el numero de radios encontrados por año ENTRE la suma de los radios 
exo_number_average = exo_number_sum / exo_number
print(exo_number_average)




