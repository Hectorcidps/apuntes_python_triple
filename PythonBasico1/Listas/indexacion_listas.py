# Crear una lista, Las listas siempre van entre corchetes  

favorite_films = ["Diablo viste a la moda", "rapidos y furiosos 1", "yo antes de ti"]

print(favorite_films)
print(type(favorite_films))
print(len(favorite_films))

# las listas permiten almacenar distintos tipos de datos, pero no es frecuente verlo 
# ademas permite tambien almacenar otras listas 

my_list = ['<3', 77, 3.89, True, False, ["sub", "list", 0.2]] 

# las listas que estan 
# dentro de una lista se consideran una sub lista la cual se considerara un 
# solo elemento sin importar la longitud que esta tenga.
print(my_list)
print(len(my_list))


# indexacion o segmentacion de listas de listas

movie_info = ['el club de la pelea', 1999, ['thiller', 'drama', 'crime'], 139, 8.644]
print(movie_info[0]) # se selecciona que valor de la lista queremos consultar 
print(type(movie_info[0])) # nos muesta el tipo de dato segun el rango que seleccionamos 

#slicing 
print(type(movie_info[1:4])) # se selecciona que valor de la lista queremos consultar 
print(len(movie_info[1:4])) # se selecciona que valor de la lista queremos consultar 



