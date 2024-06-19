

#### ASIGNACION AUMENTADA Y FUNCIONES INTEGRADAS
## Objetivo: modificar valores de variables con asignacion aumentada
## Calcular el valor usando min(), max(), y sum()

### Actualizar valores 

f_speaker = 284.9
f_speaker = 284.9 + 2.5 ## aqui se actualiza la variable, sobreescribiendola,  pero no es lo ideal 
print(f_speaker)


## ASIGNACION AUMENTADA 
#Ejemplos

speakers = 359.9 # declaras una variable 

# SUMA
speakers += 6.7
print(speakers) # cada operacion necesita su print

# RESTA 
speakers-= 4.7
print(speakers)

# MULTIPLICACION 
speakers *= 10.4
print(speakers)

# DIVISION
speakers /= 8 
print(speakers)

### FUNCIONES INTEGRADAS 

## Variable muestra una lista con argumentos 
movies_duration = [142, 175, 152, 195, 201, 154, 178, 139, 133, 126] 

# Sum Toma una lista como argumento y devuelve una suma de sus elementos
total_duration = sum(movies_duration) # primero va la funcion y luego se llama a la variable 

# Max -  obtiene el elemento mas grande en la lista 
max_duration = max(movies_duration)

# Min - obtiene el valor mas pequeño dentro de la lista 
min_duration = min(movies_duration)

print(total_duration)
print(max_duration)
print(min_duration)
