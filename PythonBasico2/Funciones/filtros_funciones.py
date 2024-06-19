## Filtrar a partir de una lista utilizando una funcion 

## paso 1 funcion para filtar peliculas de la lista 
def filtro_movie(data, target_duration):
    filtro_resultado = [] # lista donde se almacenara los parametros solicitados
    for celda in data: # se inicia ciclo for, usando el primer parametro data  
        if celda [4] > target_duration: filtro_resultado.append(celda) # se agrega la condicion con indexacion para ubicar el elemento a 
        # extraer en este caso duracion. Se compara con el segundo parametro y por ultimo se agrega a la lista vacia por medio del metodo append
        # la informacion extraida de row
    return filtro_resultado # por ultimo se regresa el resultado de los datos almacenados en filtro_resultado

## paso 2 mostrar(imprimir) los nombres cuando se filtren
# esta funcion no regresa nada solo imprime el resultado
def print_movie_info(data): # se inicia la funcion con el parametro data
    for movie in data: # en el ciclo for se coloca data porque ahi se va a realizar todas las condiciones 
        print(movie) # solo imprime el resultado


peli_info = [
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

filtro_movie = filtro_movie(peli_info, 180) # se llama la primer funcion, entre parentesis, se ponde de donde viene la data, 
# en este caso de la lista 'peli_info' y despues el parametro de duracion con el que sera comparado, en este caso 180
print_movie_info(filtro_movie) # por ultimo se llama la segunda funcion y dentro de los parametros se imprime la primer funcion 


###### EJEMPLO DE LA PLATAFORMA ##### 

## funcion para imprimir resultados
def print_movie_info(data):
    for movie in data:
        print(movie)

## funcion de filtro para encontrar la data 
def filter_by_year(data, year): ## se establece la funcion con dos parametros
    filter_year = [] # lista vacia donde se almacena lo extraido
    for celda1 in data:
        if celda1 [2] > year: filter_year.append(celda1) # ciclo for usando los parametros y almacenandolos en la lista 
    return filter_year # regresa el resultado de lo extraido y agregado en la la lista vacia filter_year

## esto es el parametro data
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

# A continuación tienes dos llamadas a funciones: para filtrar y para imprimir

movies_filtered = filter_by_year(movies_info, 1990) # se crea una variable movies_filtered, donde se llama a la variable filter_by_year, despues se agrean los parametros
print_movie_info(movies_filtered) # por ultimo se llama a la funcion print_movie_info y en parametro se agrega la nueva variable

## LAS FUNCIONES SE PUEDEN MANDAN A LLAMAR CON SOLO EL NOMBRE DE LA FUNCION, SE PUEDE USAR PRINT PERO NO ES BUENA PRACTICA


### Ejemplo 1 plataforma, filtrar con una funcion el campo(field) al que se dedican las personas

def filter_clients(clients_list, field):
    filter_list = []
    for client in clients_list:
        if client [-1] == field:
            filter_list.append(client)
    return filter_list ### EN ESTE CASO SE SACA EL RETURN DEL CICLO PARA QUE RETORNE TODOS LOS VALORES DENTRO DE LA LISTA

clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"],
    [34556, "Lucas Hernandez", 37, 75000, "Education"],
    [64291, "Jessica Li", 25, 125000, "IT"],
    [74512, "Emma Davis", 47, 197000, "Finance"],
    [83191, "Sophia Perez", 34, 225000, "Transportation"],
    [91023, "Liam Kim", 29, 98000, "Retail"],
    [96435, "Ava Chen", 31, 175000, "Marketing"],
    [100571, "Noah Rodriguez", 28, 85000, "Architecture"],
    [101321, "Olivia Wilson", 44, 310000, "Telecom"],
    [104556, "William Brown", 38, 289000, "Finance"],
    [105491, "Emily Smith", 29, 193000, "Healthcare"],
    [107512, "Michael Perez", 53, 415000, "Transportation"]
]

filtered_list  = filter_clients(clients,"Transportation")
print(filtered_list)


######## Segundo ejemplo Plataforma, crea 2 funciones donde extraigas la edad (>40) de los clientes y su ingreso(>250,000)

clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"],
    [34556, "Lucas Hernandez", 37, 75000, "Education"],
    [64291, "Jessica Li", 25, 125000, "IT"],
    [74512, "Emma Davis", 47, 197000, "Finance"],
    [83191, "Sophia Perez", 34, 225000, "Transportation"],
    [91023, "Liam Kim", 29, 98000, "Retail"],
    [96435, "Ava Chen", 31, 175000, "Marketing"],
    [100571, "Noah Rodriguez", 28, 85000, "Architecture"],
    [101321, "Olivia Wilson", 44, 310000, "Telecom"],
    [104556, "William Brown", 38, 289000, "Finance"],
    [105491, "Emily Smith", 29, 193000, "Healthcare"],
    [107512, "Michael Perez", 53, 415000, "Transportation"]
]

### Escribe la funcion para filtrar la edad de los clientes 
def filter_age(clients_list, age):
    edad = []
    for age_client in clients_list:
        if age_client [2] > age:
            edad.append(age_client)
    return edad ### EN ESTE CASO SE SACA EL RETURN DEL CICLO PARA QUE RETORNE TODOS LOS VALORES DENTRO DE LA LISTA

### Escribe la funcion para filtrar el ingreso de los clientes 

def filter_income(clients_list, income):
    ingreso = []
    for income_client in clients_list:
        if income_client [-2] > income:
            ingreso.append(income_client)
    return ingreso ### EN ESTE CASO SE SACA EL RETURN DEL CICLO PARA QUE RETORNE TODOS LOS VALORES DENTRO DE LA LISTA
        
# escribe aquí dos funciones de filtrado: filter_age y filter_income

# llama a la función filter_age aquí
filtered_age = filter_age(clients, 40) 

# llama a la función filter_income aquí
filtered_income = filter_income(clients, 250000)

# muestra el resultado
print(filtered_age)
print(filtered_income)