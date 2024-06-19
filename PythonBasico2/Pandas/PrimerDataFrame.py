## importar libreria pandas y nombrarla pd, es la mas comun
import pandas as pd

## importar los datos a un dataframe
# Usar clases para importarlo DataFrame es la mas usada,
# DataFrame (data(espera una lista que contenga los datos),columns(espera una lista que contenga nombres de columnas que correspondan a lista de datos))

atlas = [
    ['France', 'Paris'],  
    ['Russia', 'Moscow'],  
    ['China', 'Beijing'],  
    ['Mexico', 'Mexico City'],  
    ['Egypt', 'Cairo']
]

geography = ['country', 'capital']

world_map = pd.DataFrame(data=atlas, columns=geography)

print(world_map)

### ejemplo plataforma 

music = [
    ['Bob Dylan', 'Like A Rolling Stone'],
    ['John Lennon', 'Imagine'],
    ['The Beatles', 'Hey Jude'],
    ['Nirvana', 'Smells Like Teen Spirit'],
]

entries = ['artist','track']

playlist = pd.DataFrame(data=music, columns=entries)
print(playlist)