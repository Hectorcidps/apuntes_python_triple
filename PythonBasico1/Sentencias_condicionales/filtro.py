## un FILTRO es una herramienta para procesar datos, son una serie de condiciones 
# y estas condiciones se usan para construir nuevas tablas

#### PARTES DE UN FILTRO 
## una variable con una lista vacia para agregar filas coincidentes
## un bucle que recorre la tabla original 
## Una sentencia condicional con if 

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

movies_filtered = [] ## Lista vacia para almacenar resultados

## creacion de ciclo for
for tiempo in movies_info:
    if tiempo[4] > 180: ## condicion encontrar todas las peliculas con una duracion mayor a 180 minutos
        movies_filtered.append(tiempo) # agregar las pelis encontradas con una duracion mayor a 180 en la variable
        #con la lista vacia

for tiempo in movies_filtered: # otro ciclo for aplicado a la variable que contiene las peliculas > 180 minutos
    print(tiempo) # imprimir resultados 


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

filtro_pelicula = []

for nacionalidad in movies_info:
    if nacionalidad [1] == "USA":
        filtro_pelicula.append(nacionalidad)
        print(nacionalidad) ## tambien se pude solo imprimir la variable creada para el ciclo for, pero solo muestra los resultados en una fila


## filtros con multiples condiciones 

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

año_pais = []

for pelicula in peli_info:
    if pelicula[2] > 1990 and pelicula[1] == "USA":
        año_pais.append(pelicula) ## en la variable lista vas a agregar(append) todo lo que se extraiga de pelicula

for pelicula in año_pais: ## en este paso despues del in va la variable del filtro 
    print(pelicula)



### Ejemplo platforma El departamento de marketing quiere una lista de todos los clientes y las clientas del banco, 
# dividida en cuatro segmentos de cuenta. Te han pedido que les presentes la lista. 
# Divide a todos los clientes del Banco ABC en cuatro segmentos: 
# la cuenta Standard para los clientes con ingresos inferiores a $100 000 (exclusive), 
# la cuenta Plus para ingresos de $100 000 (inclusive) a $200 000 (exclusive), 
# la cuenta Elite para ingresos de $200 000 (inclusive) a $300 000 (exclusive),
# y la cuenta Executive para ingresos de $300 000 (inclusive) o más.

#En el precódigo a continuación, verás cuatro variables con las listas: standard, p
# lus, elite y executive. Escribe código para iterar sobre los clientes y las clientas, 
# comprueba a qué categoría pertenecen sus ingresos y agrégalos a la lista correspondiente. 
# Muestra la lista de clientes y clientas executive al final.

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

# listas vacías para agregar clientes y clientas
standard = []
plus = []
elite = []
executive = []

## en este caso es mejor usar if , elif porque se debe iterar en cada una de los elementos de la lista 

for cuentas in clients:
    if cuentas [3] < 100000:
        standard.append(cuentas)
    elif cuentas[3] <200000:
        plus.append(cuentas)
    elif cuentas[3] <300000:
        elite.append(cuentas)
    elif cuentas[3] >300000:
        executive.append(cuentas)


print(executive)



## segundo ejemplo Es el Día de la Juventud y el equipo de marketing desea enviar un correo electrónico para atraer 
# a nuestros clientes y clientas jóvenes.
# Para mejorar la solución anterior, debemos actualizar los criterios de edad para identificar a 
# los clientes y las clientas jóvenes. 

# Hemos actualizado el código anterior con las nuevas categorías juveniles, 
# pero necesitas añadir filtros de edad a tus filtros de ingresos previos para que funcionen como se espera.

# Las reglas son las siguientes:

# standard_young: Ingreso anual inferior a $100 000 (exclusive) Y la edad es menor a 40 años (exclusive).

# plus_young: Ingreso anual inferior de $100 000 (inclusive) a $200 000 (exclusive) Y la edad es menor a 35 años (exclusive).

# elite_young: Ingreso anual inferior de $200 000 (inclusive) a $300 000 (exclusive) Y la edad es menor a 35 años (exclusive).

# executive_young: Ingreso anual superior a $300 000 (inclusive) Y la edad es menor a 35 años (exclusive).

#### Por favor, proporciona listas actualizadas con base en estas reglas y luego mostrar de nuevo solo
# la lista incluyendo los clientes "executive young".

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

standard_young = []
plus_young = []
elite_young = []
executive_young = []

for client in clients:
    if client[3] < 100000 and client[2] < 40 : 
        standard_young.append(client)
    elif client[3] < 200000 and client[2] < 35: 
        plus_young.append(client)
    elif client[3] < 300000 and client[2] < 35: 
        elite_young.append(client)
    elif  client[3] > 300000 and client[2] < 35:
         executive_young.append(client)

# no modifiques nada por debajo de esta línea
print(executive_young)
