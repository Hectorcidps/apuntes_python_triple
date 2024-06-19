'''
El ordenamiento de datos es una tecnica fundamental en la manipulacion de datos que aporta estructura a nuestos dataset, 
lo que facilita la identificacion de patrones y de informacion
'''

######## Metodo SORT_VALUES() ############

# sintaxis 
## nombre_data_set.SORT_VALUES(by='nombre_columna_por_ordenar', criterio_de_ordenamiento = True or False)

'''
exoplanetas.sort_values(by='\tradius', ascending=False) ## si se quiere de manera descendente se coloca False
'''

import pandas as pd 

exoplanetas = pd.read_csv('/Users/hectorciddelprado/Desktop/datasets/exoplanet.csv')

print(exoplanetas.sort_values(by='\tradius').head(10))

### obtener planetas menos a < 3 y provenientes del año 2011

# primer paso aplicar 2 filtros 
exo_small_11 = exoplanetas[exoplanetas['\tradius'] < 1] # el primero extra de explanetas todos aquellos cuyo radio sea menor a 2
exo_small_11 = exo_small_11[exo_small_11['\tdiscovered'] == 11 ] # despues se aplica otro filtro llamando al anterior filtro exo_small_11 
# y usando operacion logica == para extraer unicamente los de año 2011

## segundo paso imprimir usando sort_values de manera descendente 

print(exo_small_11.sort_values(by='\tradius', ascending=False))