# una tienda online necesita escribir un programa que automatice los descuentos. Si un usuario compra un producto con valor de mas de 100 dls
# recibira un descuento del 5% en ese producto

############ INSTRUCCIONES SIN AGREGAR UNA FUNCION ##########

## Calcular el total de cada uno de los items
## comparar el total con 100
## si es superior a 100, restar el 5%

first_item_price = 10.0
first_item_quantity = 3
# se empieza la suma total multiplicando la cantidad por el precio
first_item_total = first_item_quantity * first_item_price 
if first_item_total > 100: # se compara con if si el total es mayor a 100
    first_item_total -= first_item_total *0.05 # si se cumple la anterior condicion se resta el 5% del total
print(first_item_total) # se imprime el resultado total

# item 2
second_item_price = 51.0
second_item_quantity = 2
# se empieza la suma total multiplicando la cantidad por el precio
second_item_total = second_item_quantity * second_item_price
if second_item_total > 100: # se compara con if si el total es mayor a 100
    second_item_total -= second_item_total * 0.05 # si se cumple la anterior condicion se resta el 5% del total
print(second_item_total) # se imprime el resultado total

# item 3
third_item_price = 4.0
third_item_quantity = 10
# se empieza la suma total multiplicando la cantidad por el precio
third_item_total = third_item_quantity * third_item_price
if third_item_total > 100: # se compara con if si el total es mayor a 100
    third_item_total -= third_item_total * 0.05 # si se cumple la anterior condicion se resta el 5% del total
print(third_item_total) # se imprime el resultado total



#################### RESOLVER CON UNA FUNCION #####################
# --- Las variables se vuelven PARAMETROS
# --- Las instrucciones de calculo se convertiran en el cuerpo

### instrucciones de la funcion
# establecer 2 parametros: precio y cantidad
# calcular el precio total del articulo en el carrito 
# comprar el total con 100 en unsa sentencia condicional
# restar el 5% si el total es superior a 100

def compra(price, quantity):
    aplicar_descuento =  price * quantity
    if aplicar_descuento > 100:
        aplicar_descuento -= aplicar_descuento * 0.05
    return aplicar_descuento

## por ultimo se imprime la funcion y se agregan los parametros 
print(compra(10.0, 100)) ## aqui puedes cambiar los parametros y se seguira ejecutando el codigo de la funcion
print(compra(51.0, 2))
compra(4.0, 10) ## LAS FUNCIONES SE PUEDEN MANDAN A LLAMAR CON SOLO EL NOMBRE DE LA FUNCION, SE PUEDE USAR PRINT PERO NO ES BUENA PRACTICA
