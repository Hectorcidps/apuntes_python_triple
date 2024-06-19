#### METODO SORT 
years = [1994, 1972, 2008, 1993, 2003, 1994, 1966, 1999, 1997]
years.sort() # modifica la lista original en lugar de crear una nueva, ordena de menor a mayor 

 #Si se necesita ordenar de mayor a menor se utiliza lo siguiente:
#years.sort(reverse=True)

print(years)

### CUANDO SE ORDENAN STRINGS se sigue un orden lexicografico, es decir, se respera las reglas de 
# ordenacion para caracteres NO alfabeticos, diferenciando entre mayusculas y minusculas
# ORDENACION LEXICOGRAFICA 
# Signos de puntuacion
# Numeros
# A - Z 
# a - z              EJEMPLO

movies = ['La Sirenita', 'Que Paso ayer', 'dogman', 'Shrek\'s tercero'] 

# Explicacion, Ordena las letras empezando con las que 
# llevan mayusculas, considerando la primera letra de cada string y siguiendo el orden alfabetico, 
# dejando al ultimo las que empiezan con minusculas 
#movies.sort()
movies.sort(reverse=True) # imprime al reves todo el contenido de la lista 
print(movies)



### Funcion SORTED, reordena los elementos de una lista, es una FUNCION  

years_cancion = [1994, 1972, 2008, 1993, 2003, 1994, 1966, 1999, 1997]
years_sorted = sorted(years_cancion) # para agregar la funcion es necesario crear otra variable llamada en este caso "years_sorted"

#years_sorted = sorted(years_cancion, reverse=True) ## TAMBIEN SE PUEDE AGREGAR REVERSE PARA LA FUNCION SORTED

print(years_sorted)


##### DIFERENCIAS ENTRE SORT Y SORTED: 
# SORT SOLO SE APLICA EN OBJETOS DE LISTA, SORTED ES UNA FUNCION SE INVOCA EN CUALQUIER TIPO DE DATO
# METODO SORT MODIFICA LA LISTA, MIENTRAS QUE SORTED CREA UNA LISTA NUEVA ORDENADA.

