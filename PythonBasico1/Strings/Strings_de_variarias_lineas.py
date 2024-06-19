# Escribe un codigo que permita crear el siguiente string en varias lineas 

# Texto : mi lista de compras, 2 cartones de leche, cereales de desayuno, huevos, pan 

# Podemos utilizar dobles comillas triples para establecerlo como una forma de lista 

shopping_list = """ Mi lista de compras: 
2 cartones de leche,
cereales de desayuno, 
huevos,
pan"""

print(shopping_list)

# longitud de string con funcion Len nos ayuda a contabilizar las palabras 

sonnet = "lorem ipsum dolor"
print(sonnet)
print(len(sonnet))


string_1 = "HolaAdios"
string_2 = "Hola Adios"
string_3 = "Hola\nAdios"
print(len(string_1))
print(len(string_2))
print(len(string_3))

# string vacio, es un marcador de posicion para los valores ausentes en tablas y archivos de datos 

print(len(''))
print(len(""))


##### INDICES 

# indexacion negativa, no contamos los numeros desde el principio o como la normal, sino que desde el final

word = 'supercalifragilisticexpialidocious'
letter = word[5] # se extrae el sexto caracter del string 
print(letter)

letter_1 = word[-8]
letter_2 = word[-13]

print(letter_1,letter_2)

# ERROR de INDICE 

#word = "word"
#print= (word[8]) este codigo arroja un error debido a que el objeto de la variable no cuenta con la cantidad de caracteres


## SLICES segmentacion

city = 'Rio de Janeiro, Brasil'
substring = city[7:14]
print(substring)

# El slice no aparece el caracter final, es decir el ultimo caracter del resultado no forma parte del resultado, el ressultado sera el caracter final - el caracter de inicio

print(city[4:1000]) # en los rangos finales no importa que no exista el numero de caracteres 
print(city[-15:500])

# SI el primer numero del rango resulta ser mayor arrojara un string vacio
print(city[4:0])

# si se quiere imprimir de un numero hasta el final de la linea basta con poner el siguiente codigo:
print(city [4:]) # omitiendo el rango final

### F - strings o Strings Formateados ###


# Ejemplo de un string normal SIN FORMATEAR 

message = "Victoria tiene 23 años y mide 157 cm"
print(message)

name = 'Victoria'
age = 23
height = 157 

message_1 = name + " tiene " + str(age) + " años y mide " + str(height) + " cm" # Se escribe en otra variable para hacerlo corto y poder concatenar
# Siempre se agrega str si se pretende concatenar un numero con strings 
print(message_1)

# STRINGS CON F-STRINGS CON VARIABLES EMBEBIDAS (inscrustado, integrado)
mensaje = f"{name} tiene {age} años y mide {height} cm"
print(mensaje)

mensaje_1 = f"{name} tendra el proximo año {age + 1 } años" # DENTRO DE LAS LLAVES PUEDEN REALIZARSE OPERACIONES 
print(mensaje_1)


# El metodo format()

# Se colocan llaves vacias entre comillas dobles y al final se agrega .format() 
# y dentro de los parentesis se agregan las variables previamente declaradas, 
# las variables ocuparan de forma ordenada las llaves.

mensaje_2 = "{} tiene {} años y mide {} cm".format(name, age, height)
print(mensaje_2)









