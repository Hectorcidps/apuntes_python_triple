'''
Garantizar la calidad de los datos: 

Si los datos usados para el análisis tienen problemas, las conclusiones arrojadas no serán confiables. 
A esto se le suele conocer como "entra basura, sale basura" (GIGO, por sus siglas en inglés "garbage in, garbage out").

identificar valores ausentes, datos duplicados y errores de presentación en tus datos evitarara que cometas GIGO.
'''

'''
1. Los valores AUSENTES son valores en filas que no estan disponibles, ya sea poque el usuario no respondio a alguna pregunta o simplemente lo dejo en blanco

generalmente se representan con NaN ---> y significa 'not a number' (no es un numero), es una forma comun de marcar valores ausentes
'''

### 2. Los valores DUPLICADOS indican que una o mas FILAS son exactamente iguales en una tabla

'''
3. Errores de estructura o presentacion 

KeyError = el nombre de la columna no existe, esto se debe a que pueden existir espacios en los nombres, pero es dificil identificarlo

BUENAS PRACTICAS ---> utilizar snake_case(palabras inician con minuscula) o camel_case(palabras inician con mayuscula),
para evitar usar espacios en el nombre de las columnas
'''
