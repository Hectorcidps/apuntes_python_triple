# Las listas son mutables, mientras que los strings son inmutables, es decir, 
# los valores de las listas PUEDEN ser modificados o actualizados 

######  METODOS DE MODIFICACION DE LISTAS ####

# append()
# extend() 
# insert() 
# pop()

#### METODO APPEND 
# Agregar un elemento al final de una lista APPEND SOLO AGREGA 1 ELEMENTO AL FINAL DE LA LISTA 
Fyf_movie = ['Fast & furious 1', 'USA', '1998', 'action', 120, 7.4]
Fyf_movie.append ('Toreto') # no se redefine la variable, solo se agrega.append y que se desea agregar
print(Fyf_movie) 

row = [1,2]
row.append([3,4])
print(row)

## Este metodo (APPEND) tiene dos limitantes:
# 1 Añade solamente un elemento 
# 2 Añade el elemento unicamente al final de la lista 



#### METODO EXTEND 
# Agregar varios elementos al final de una lista con el metodo EXTEND se agregan varios elementos al final de la lista 
harry_movies = ['La piedra filosofal', 'UK', 2000]
# Agregar a los protagonistas
harry_movies.extend (['Harry', 'Hermaioni', 'Ron', 9.4]) # se tiene que indicar que es una lista usando los []
print(harry_movies)

## El metodo extend elimina la primera limitacion de APPEND, pero mantiene la segunda limitante que es 
##Añadir los elementos al final de la lista 


#### METODO INSERT
# Agregar un elemento en un indice determinado
# lista.insert(indice, elemento)

dart_knight_movie = ['The dark knight', 'USA', 'Fantasy, action, thriller', 152]
dart_knight_movie.insert(2, 2008) # primero va la posicion donde se va a agregar el elemento y luego el atributo a agregar
dart_knight_movie.insert(0, 'Batman')
print(dart_knight_movie)


#### METODO POP eliminar un elemento dentro de una lista 
# lista.pop(indice)

movies = ['Matrix', 'Matrix 2', 'Matrix 3']
#movies.pop()  si se aplica sin argumentos elimina el ultimo elemento al final de la lista
#Si se quiere eliminar un elemento especifico basta con agregar el indice exacto donde se muestra dicho elemento 
movies.pop(1)
print(movies)
