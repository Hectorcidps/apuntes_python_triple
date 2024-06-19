#### LAS LISTAS ANIDADAS SON LISTAS DENTRO DE OTRAS LISTAS, NUNCA OLVIDAR LA COMA DESPUES DE CADA LISTA ANIDADA
 
movies_info = [
    
    ['Tiburon', 'USA', 1994, 'Drama', 142, 9.111],
    ['El padrino', 'USA', 1980, 'Drama', 'crime', 175, 8.730],
    ['El señor de los anillos', 'New Zealand', 2003, 'Fantasy, adventure', 201, 8.625],
    ['Harakiri', 'Japan', 1962, 'Drama, action, history', 133, 8.8106]
]
print(movies_info)

## para acceder a una lista especifica podemos usar la indexacion, estableciendo el indice de la lista a solicitad.
# En este caso el INDICE representa cada una de las listas y NO su contenido 

#print(movies_info[0])
#print(movies_info[-1])

print(movies_info[0][2]) # EXPLICACION DE LA LISTA 0, TRAEME EL INDICE 2 (1994)
print(movies_info[-1][0]) # DE LA LISTA -1 TRAEME EL INDICE 0 (HARAKIRI)

