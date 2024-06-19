#### Hacer bucles para modificar datos en listas 

movies = [
    ["The Shawshank Redemption", 1994, "Frank Darabont"],
    ["The Godfather", 1972, "Francis Ford Coppola"],
    ["The Dark Knight", 2008, "Christopher Nolan"],
    ["12 Angry Men", 1957, "Sidney Lumet"],
    ["Schindler's List", 1994, "Steven Spielberg"],
    ["The Lord of the Rings: The Return of the King", 2003, "Peter Jackson"]
]
## Primero cres dos variables 1: donde agregas el titulo de la pelicula y 2: el año corregido o que va a sustituir
movie_name = "Schindler's List"
correct_year = 1993

## creacion ciclo for 
for año_corregido in movies:
    if año_corregido[0] == movie_name: # se pone [0] porque es el lugar de la indexacion del titulo, y depues se pone el nombre de la pelicula a corregir 
        año_corregido[1] = correct_year # se localiza el indice a corregir en este caso [1] y se redefine la variable

for año_corregido in movies:
    print(año_corregido) ## por ultimo se imprime todo la lista para ver que sea correcto


## otro ejemplo de la plataforma 

movie_1 = [
    ["The Shawshank Redemption", 1994, "Frank Darabont"],
    ["The Godfather", 1972, "Francis Ford Coppola"],
    ["The Dark Knight", 2008, "Christopher Nolan"],
    ["12 Angry Men", 1957, "Sidney Lumet"],
    ["Schindler's List", 1993, "Steven Spielberg"],
    ["The Lord of the Rings: The Return of the King", 2003, "Peter Jackson"]
]

movie_to_change = "The Lord of the Rings: The Return of the King"
new_movie = "The Lord of the Rings: The Fellowship of the Ring"
new_year = 2001

for movie in movie_1:
    if movie[0] == movie_to_change:
        movie [0] = new_movie
## en este caso se hace otro ciclo for para usar la indexacion y localizar el año en la nueva variable new_movie
for movie in movie_1: 
    if movie [0] == new_movie:
        movie [1] = new_year

# no modifiques el código de abajo, ya que imprime el resultado
for movie in movie_1:
    print(movie)
