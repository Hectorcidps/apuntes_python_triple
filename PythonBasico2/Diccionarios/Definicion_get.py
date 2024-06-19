##### Coleccion de elementos similar a una lista, sin embargo cada elemento tiene una clave(valor especifico), 
### las claves son similares a los indices. Los diccionarios son utiles para describir las propiedades individuales de los elementos.

## Entregar informacion de identificacion (clave)
## Recibir datos correspondientes (valor)

#### SINTAXIS 

# primer diferencia usar llaves en lugar de corchetes
## nombre_diccionario = {
#    'clave': 'Valor', se usan las comas para separar clave-valor
#    'clave': 'Valor',
#    'clave': 'Valor'
# }

# Ejemplo: 

schedule = {
    'SU2222':'12.06.18 12:30',
    'SU1111':'12.07.19 14:04',
    'SU0777':'12.06.20 19:23'
}
print(schedule) 
# print(len(schedule)) se puede pasar el metodo len para saber la longitud del diccionario
# print(schedule['SU0777']) en lugar de usar el index se usa la clave para extraer un valor especifico

### Recuperar datos es mas facil
### Ocupa MAS espacio
### Almacena cualquier tipo de dato 
### Las claves solo pueden ser tipos de datos inmutables(strings o numeros int o float)

# crea un diccionario Ejemplo
movies = {
    'Her':2013,
    'Big Eyes':2014,
    'Taxi Driver':1976,
    'The King of Comedy': 1982
}
print(movies)

## otro ejemplo plataforma 
financial_info = {
    'American Express': 93.23,
    'Boeing': 178.44,
    'Coca-Cola': 45.15,
    'Walt Disney': 119.34,
    'Nike': 97.99,
    'JPMorgan':96.27,
    'Walmart': 130.68 
}

walmart_price = financial_info['Walmart'] # para extraer el valor es necesario usar la clave, se declara una variable para guardarla
print(walmart_price)

### ejemplo con uso del metodo GET 

##### MUY IMPORTANTE EL METODO GET VA CON PARENTESIS Y NO CON CORCHETES
pepsi_price = financial_info.get("Pepsi") ## Al no contar con la informacion de Pepsi dentro del diccionario no nos arrojara un error

# pepsi_price = financial_info.get("Pepsi", -1) Tambien se puede asignar el valor que queramos asignandolo despues de la clave

nike_price = financial_info.get('Nike')

print(pepsi_price) ## sino que al imprimir nos devolvera 'None'
print(nike_price)