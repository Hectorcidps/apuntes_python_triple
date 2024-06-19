'''
###### DIFEENCIAS ENTRE TIPOS DE VARIABLES ######

Dentro de la misma funcion es posible usar variables locales y globales con el MISMO nombre, 
La variable LOCAL tiene prioridad sobre la GLOBAL cuando tienen el mismo nombre, cuando se imprime primero arroja la local y luego la global  

Variables Locales
Al usarlas podemos mantener nuestro codigo organizado y evitar conflictos de nombres repetidos las variables locales 
se definen dentro de una funcion y solo sirven dentro de la misma, se termina al arrojar el resultado
no se puede acceder a la variable FUERA DE ELLA 
'''
## En este ejemplo la variable result es local por lo cual NO PUEDE SER UTILIZADA FUERA DE LA FUNCION 
def omelet(cheese, eggs_number):
    result = ' El omelet esta listo!! Huevos utilizados: ' + str(eggs_number)
    if cheese == True:
        result = result + ', y ademas lleva queso'
    else: 
        result = result + ', sorry for you, no trae queso'
    return result
omelet(False, 3) ## LAS FUNCIONES SE PUEDEN MANDAN A LLAMAR CON SOLO EL NOMBRE DE LA FUNCION, SE PUEDE USAR PRINT PERO NO ES BUENA PRACTICA
# print(result)  arroja un error porque es una variable LOCAL, error: name not defined

## Variables Globales
# Resultan utilies cuando las usamos en distintas partes del codigo, incluso desde el interior de las funciones, se puede acceder y modificar desde
# cualquier parte del codigo, sin embargo se debe tener cuidado con ellos  

milk = 50 # variable FUERA DE LA FUNCION

def omelette(cheeses, eggs_numbers): 
    resultados = ' El omelet esta listo!! Huevos utilizados: ' + str(eggs_numbers)
    if cheeses == True:
        resultados = resultados + ', ademas lleva queso'
    else: 
        resultados = resultados + ', sorry for you, no trae queso'
    resultados = resultados + ' y tambien trae la leche  ' + str(milk) + ' ml' # la variable como esta fuera del bloque de la funcion se considera 
    # GLOBAL y puede ser utilizada, por lo cual al llamar a la funcion omelette imprimira el valor de la variable, en este caso 50
    print(resultados)
omelette(True, 5)

