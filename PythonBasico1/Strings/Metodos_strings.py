# Metodo UPPER Convierte todas las minisculas a mayusculas 

message = "hola, me llamo HECTOR cid"
print(message)
message_new = message.upper() # la almacenas en otra variable para convertirla en mayusculas 
print(message_new)


# Metodo LOWER Convierte todas las letras mayusculas a minusculas

message_1 = "HOLA ME LLAMO HECTOR cid"
print(message)
message_new = message_1.lower() # la almacenas en otra variable para convertirla en minusculas
print(message_new)

## un EJEMPLO USANDO UN CICLO FOR  CON LOWER
fav_categories = ['ELECTRONICS', 'SPORT', 'BOOKS']
fav_categories_low = []

for minusculas in fav_categories:
    fav_categories_low.append (minusculas.lower()) ## primero va donde se va almacenar 
#y luego el metodo con la variable asignada a for 

print(fav_categories_low) # por ultimo se imprime la lista donde se almaceno el resultado 


# Metodo REPLACE
shopping_list = ''' aciete de colza
aceite de girazol
aceite de aguacate
aceite de cacahuat3

'''
# reemplaza una palabra por una nueva, y lo va haciendo en cada uno de los print
print(shopping_list.replace('aciete', 'aceite')) 
print(shopping_list.replace('girazol', 'girasol'))
print(shopping_list.replace('cacahuat3', 'cacahuate'))

vale = "Hola que tal"
print(vale.replace('tal','hace'))

## SOLO FUNCIONA CON STRINGS PARA LISTAS SE USA OTRO METODO

# Tambien se pueden eliminar caracteres utilizando el metodo replace
user_ids = "_151234_, _792051_, _995247_"
user_ids = user_ids.replace('_', " ")
print(user_ids)


# Metodo STRIP Elimina todos los espacios en blanco (espacios, tabulaciones y saltos de linea)
# antes y al final del string

column_name = '       fecha de compra  '
print(column_name)
print(len(column_name))
print()
print(column_name.strip())
print(len(column_name.strip()))
