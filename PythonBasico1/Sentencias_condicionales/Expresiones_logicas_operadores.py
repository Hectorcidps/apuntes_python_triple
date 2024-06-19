## sintaxis de cualquier sentencia condicional es 
# IF <statement is True> THEN <do this> traduccion = SI <la sentencia es Verdadera> ENTONCES <haz esto>

## LAS EXPRESIONES LOGICAS SE CONSIDERAN BOOLEANAS, ES DECIR, TRUE OR FALSE

#### Expresiones de comparadores de expresion: 

# == igualdad ejemplo, 5 == 5 True
# !< desigualdad, 5!= 2 True
# > mayor que, 5 > 2 True 
# < menor que, 5 < 2 False 
# >= mayor o igual que, 5 >= 2 True
# <= menor o igual que, 5 <= 2 True

### Con estos operadores los tipos de datos tienen que ser similares por ejemplo float con int, pero NO admite strig con int 


#### Expresiones que contienen operadores logicos (and, or, not)

## And -- Ambas condiciones deben de ser verdaderas, 5 > 2 and 3 < 5 is True. Pero SI alguna condicion no es verdadera todo sera False

## Or -- Al menos una condicion o ambas son verdaderas, al menos 1 debe ser verdadera, 5 > 2  or 3 > 5 is True.
# Solo arrojara False si las DOS condiciones son falsas

## Not -- Revierte el valor verdadero de una condicion, not(5 > 2) False. Si una condicion es verdadera NOT la hara falsa y viceversa.

## Ejemplo, ver si la pelicula de tiburon fue estrenada antes que la de titanic

tiburo_year = 1994
titanic_year =1997

print(tiburo_year > titanic_year)

## Comprobemos si Figth club se estreno entre 1996 y 1998

movie = ['Figth club', 'Usa', 1999, 'thirller, drama, crime', 139, 8.644]
print(movie[2] > 1996 and movie[2] < 1998)

print(movie[2] > 1996 or movie[2] < 1998) ## Aqui arroja True porque 1999 (movie[2] AQUI LO MANDA A LLAMAR) es mayor a 1996.

print(not(movie[2] > 1996 and movie[2] < 1998)) ## Aqui la respuesta es True porque al usar and nos da como resultado False, 
# porque solo se cumple una condicion, y como estamos usando al principio NOT invierte el resultado. 



#### Funciones de predicado son aquellas que devuelven True or False aplicado a STRINGS

# islower() arroja TRUE SI UN STRING TIENE TODAS LAS LETRAS EN MINUSCULAS
# isdigit() arroja TRUE SI UN STRING TIENE SOLO NUMEROS
# isalpha() arroja TRUE SI TODAS SON LETRAS, si un STRING contiene espacios y signos de puntuacion arroja FALSE 

print('hola'.islower())
print('777'.isdigit())
print('la cadena contiene espacios, asi como signos de puntuacion'.isalpha())

