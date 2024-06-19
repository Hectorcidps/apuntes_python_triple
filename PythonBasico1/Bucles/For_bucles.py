## CICLO FOR, recorre los elementos en una secuencia y realiza operaciones similares en cada uno de ellos, puede ser cualquier objeto 
# ordenado, ya sean listas o strings.

# Partes del bucle: for element in your_list:
    #print(element)

# for -- es el inicio del bucle
# element -- el nombre que le das a la variable dentro del bucle
# in -- palabra clave para definir de donde se extraeran los datos
# your_list -- la lista que contiene los elementos 
# : -- los dos puntos nunca deben faltar.
     # -- identacion (4 espacios, identacion "sencilla")
# print(element) -- Codigo que se ejecuta para cada elemento de la lista. Imprime, llamando a la variable que le asignaste dentro del bucle, NO a la lista tal cual. 

## Ejemplo 

film_genres = ['scifi', 'drama', 'thriller', 'comedy', 'action']
for value in film_genres:
    print(value)


## LOS BUCLES FUNCIONAN CON CUALQUIER LISTA QUE CONTENGA CUALQUIER TIPO DE DATO

film = ['Shrek', 'USA', 2000, 'animada', 120, 9.823]
for peliFav in film:
    print(peliFav)


## BUCLES CON STRIGS -- imprimen letra por letra lo que aparece en el string, debe ser en type de LISTA, es decir entre []

review = ['La sirenita me dejo un muy amargo sabor de boca 0 estrellas JAMAS LA VEAS']
for malPeli in review:
    print(malPeli)



######## BUCLES SOBRE LISTAS ANIDADAS #########

# los bucles funcionan igual para las listas anidadas.
# cada lista se considera 1 elemento, por o que imprime 1 por 1 hasta mostrar todo

movies_info = [
    ['The Shawshank Redemption', 'USA', 1994, 'drama', 142, 9.111],
    ['The Godfather', 'USA', 1972, 'drama, crime', 175, 8.730],
    ['The Dark Knight', 'USA', 2008, 'fantasy, action, thriller', 152, 8.499],
    ["Schindler's List", 'USA', 1993, 'drama', 195, 8.818],
    ['The Lord of the Rings: The Return of the King', 'New Zealand', 2003, 'fantasy, adventure, drama', 201, 8.625],
    ['Pulp Fiction', 'USA', 1994, 'thriller, comedy, crime', 154, 8.619],
    ['The Good, the Bad and the Ugly', 'Italy', 1966, 'western', 178, 8.521],
    ['Fight Club', 'USA', 1999, 'thriller, drama, crime', 139, 8.644],
    ['Harakiri', 'Japan', 1962, 'drama, action, history', 133, 8.106],
    ['Good Will Hunting', 'USA', 1997, 'drama, romance', 126, 8.077]
]
for lista in movies_info:
    print(lista[0])


#### Tambien podemos usar la indexacion para acceder a un solo elemento dentro de la lista 
#for lista in movies_info:
#    print(lista[0]) el cero es la ubicacion del elemento en las listas, es deci el titulo de la pelicula



## EJEMPLO DE LA PLATAFORMA PARA HACER LO SIGUIENTE: 

# El departamento de marketing del Banco ABC está interesado en conocer la edad promedio de su clientela. 
# La edad promedio es simplemente la suma de las edades de todos los clientes dividida entre la cantidad de clientes. 
# Utiliza el bucle for para iterar sobre la lista clients y actualiza las variables total_age y num_clients 
# en cada iteración del bucle.

# La variable total_age debe almacenar la suma de edades, mientras que la variable num_clients se usa para almacenar 
# el número total de clientes.

# Las variables total_age y num_clients ya están declaradas para que hagas tus cálculos con ellas. 
# Tras recorrer la lista y actualizar estas dos variables, calcula la edad promedio de todos los clientes, 
# almacénala en la variable average_age y muéstrala

clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"]
]

total_age = 0
num_clients = 0

for age in clients:
    total_age += age[2]
    num_clients +=1

average_age = total_age / num_clients

print("El numero de clientes es: ", average_age)