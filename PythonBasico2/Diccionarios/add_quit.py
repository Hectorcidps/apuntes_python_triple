##### Agregar y eliminar objetos ##
## de manera sencilla podemos agregar un elemento al diccionario con la siguiente sintaxis:

# variable_del_diccionario ['clave a agregar al dicionario'] = valor de la clave
## despues de la variable NO SE AGREGA EL = la clave va entre corchetes y lleva comillas simples

financial_info = {
    'American Express': 93.23,
    'Boeing': 178.44,
    'Coca-Cola': 45.15,
    'Nike': 97.99,
    'JPMorgan':96.27,
    'Walmart': 130.68 
}
## agregar un elemento al final del diccionario 
#financial_info ['Walt Disney'] = 119.34
#print(financial_info)

## verificar si una clave ya existe, podemos actualizar su valor 
if financial_info.get('Walt Disney') == None: ## el metodo get va con parentesis y no con corchetes 
    financial_info['Walt Disney'] = 119.34 ## si la clave NO esta se agrega
else:
    financial_info['Walt Disney'] += 3.2 # si la clave esta se aumenta 3.2 al valor

print(financial_info)

###### Borrar un elemento con el metodo DEL

del financial_info['Nike'] # Basta con agregar la funcion del antes de la variable del diccionario, y entre corchetes la clave a eliminar
print(financial_info)

elemento_wester = financial_info.pop('Walmart') ## se agrega la clave a eliminar, si se escoje la penultima borrara esa y la ultima
# Si se escoge la 2 de 5 claves solo mostrara la primera clave, ya que todas las demas seran eliminadas.
print(elemento_wester) ## imprime el valor de la clave walmart en este caso 130.68
print(financial_info) # al imprimir ya no estara la clave ni el valor de Walmart


#### convertir esta lista en un diccionario con un ciclo for, usando los siguientes elementos como claves 
# "id"
# "client_name"
# "age"
# "yearly_income"
# "work_field"

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

for client in clients:
    clientes_info = { 'id': client[0],
                     'client_name': client[1],
                     'age':client[2],
                     'yearly_income':client[3],
                     'work_field':client[4]
    }
    print(clientes_info)


#### Ejercicio plataforma, agregar dos valores al work field de la siguiente lista 

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

incomes_per_field = {
    } # aquí colocarás los ingresos para cada campo ES UN DICCIONARIO VACIO

for client in clients:
    nombre = client[4] # primero, extrae el nombre del puesto
    ingresos = client[3] # segundo, extrae los ingresos de cada uno de los puestos
	
## lo confuso aqui es que ya no se usa INDEXACION se usa la clave del diccionario
    if incomes_per_field.get(nombre) == None: # comprueba si el campo extraído NO está en el diccionario incomes_per_field, llamar al diccionario vacio
        incomes_per_field[nombre] = [ingresos] 	# añade un nuevo campo como clave en este caso nombre y establece una lista como valor los ingresos de cada puesto
    else: 
        incomes_per_field[nombre].append(ingresos) # si el campo extraído está en el diccionario incomes_per_field, 
        #añade el segundo ingreso a la lista de ingresos para un campo en particular, esto hara que se tengan 2 valores en lugar de 1


print(incomes_per_field) # imprime el diccionario vacio, con los dos valores agregados a cada puesto