#####  operaciones condicionales 

## IF sintaxis if -- declaracion -- :
            #  identacion  print('accion')

weather = 'lluvia'

if weather == 'lluvia':
    print('Lleva un paraguas')

print('Vamos')

## Else se utiliza despues de una sentencia IF para ejecutar un codigo en caso de que la sentencia IF no se haya cumplido

clima = "sol"
if clima == "Lluvia":
    print("Lleva un paraguas")
else: ## PERO SI NO SE CUMPLE IF IMPRIME ESTO 
    print("Mejor lleva un sombrero y lentes")
print("Vamos!!")

###### Comprobacion de Substrings, se utiliza el in despues del if para indicar donde revisar dicha substring 

if "estoy" in "el equipo":
    print('Aqui estoy yo en el equipo')
else:
    print("Es verdad, no hay yo en el equipo")


quote = "El progreso es imposible sin cambio y aquellos que no pueden cambiar de opinion no pueden cambiar nada"

if "ogres" in quote: 
    print("Donde hay progreso, hay queso !") ## imprime esta porque ogres esta en progreso 
else: 
    print('Aqui no bromista!!')



#### Creacion de multiples ramas con else y elif

## elif es una abreviatura de else - if  que permite comprobar sentencias adicionales despues de if y else 

weather_1 = 'lluvia'

if weather_1 == 'lluvia':
    item_to_take = "Paraguas"
if weather_1 == 'sol':
    item_to_take = "Sombrero"
if weather_1 == 'nieve':
    item_to_take = "Gorra y bufanda"
else:
    item_to_take = "nada"

print(weather_1)
print(item_to_take)

# En el ejemplo de arriba imprime lluvia y nada porque el valor de item_to_take se asigno 'nada'

## correccion de codigo con elif, se ejecutara aquella rama que cumpla primero con la condicion, todas las demas ramas seran ignoradas 

clima_1 = 'lluvia'

if clima_1 == 'lluvia':
    item = "Paraguas"
elif clima_1 == 'sol':
    item = "Sombrero"
elif clima_1 == 'nieve':
    item = "Gorra y bufanda"
else:
    item = "nada"

print(clima_1)
print(item)

###### Ejemplo con una lista y usando el ciclo for con sentencias if, elif y else

years = [1994, 1972, 2008, 1993, 2003, 1994, 1966, 1999, 1962, 1997]

for year_movie in years:
    if 1960 <= year_movie <= 1969:
        print('La pelicula se estreno en la decada de los 60\'s')
    elif 1970 <= year_movie <= 1979:
        print('La pelicula se estreno en la decada de los 70\'s')
    elif 1980 <= year_movie <= 1989:
        print('La pelicula se estreno en la decada de los 80\'s')
    elif 1990 <= year_movie <= 1999:
        print('La pelicula se estreno en la decada de los 90\'s')
    elif 2000 <= year_movie <= 2009:
        print('La pelicula se estreno en la decada de los 2000')
    else:
        print('Tiempo no definido')


### ejemplos en la plataforma: 
# Las puntuaciones de las películas se almacenan en la variable ratings (puntuaciones). 
# Te pedimos que conviertas estas calificaciones de un sistema de 100 puntos a un sistema de 5 puntos. 
# Para ello, debes iterar sobre la lista original de ratings y utilizar sentencias condicionales para convertir 
# la escala original al sistema de 5 puntos siguiendo la siguiente lógica:

#imprime 2 si la calificación original se encuentra en un intervalo de 0 a 59 puntos, ambos incluidos;
#imprime 3 si la calificación original se encuentra en un intervalo de 60 a 72 puntos, ambos incluidos;
#imprime 4 si la calificación original se encuentra en un intervalo de 73 a 84 puntos, ambos incluidos;
#imprime 5 si la calificación original se encuentra en un intervalo de 85 a 100 puntos, ambos incluidos.


ratings = [91, 35, 65, 89, 78, 93]

for conversion in ratings:
    if conversion <= 59:
        print('2')
    elif 60 <= conversion <= 72:
        print('3')
    elif 73 <= conversion <= 84:
        print('4')
    elif 85 <= conversion <= 100:
        print('5')

## en este ejemplo al tratarse de rangos debe ser menor o igual que para que cubra en su totalidad el rango
# Esto se debe  a que si se compara (conversion) se elige el numero 65 de la lista de la variable ratings y se compara
# con 60 quedaria asi 60 <= 65 esto es verdadero, pero si dijera 60 >= 65 esto es COMPLETAMENTE FALSO ya que 60 es menor que 65
