#### El procesamiento de string sirve para eliminar palabras repetidas o sustituir determinados fragmentos,
# esto mediante la transformacion de strings a listas, se utilizan los sigueintes metodos.

#### METODO SPLIT dividir un string en una lista, al aplicar este metodo cada palabra del string se convertira en un elemento en la lista
# de manera predeterminada separa la palabra o letras como un elemento, por ejemplo

phrase = 'dividir o no dividir'   
word = phrase.split()
print(len(word))
print(type(word))

## resultado ['dividir', 'o', 'no', 'dividir']

frase = 'Esta-noche-no-se-ven-las-estrellas' ### se pueden utilizar cualquier tipo de separadores
palabras = frase.split('-') # Aqui se define que tipo de separador es 
print(palabras)


#### METODO JOIN, es al reves, transformar una lista en un string

words = ['Mi', 'pelicula', 'favorita', 'es', 'Shrek']
frase_1 = ' '.join(words) # Se pone al principio que tipo de comilla usa el string y despues se utiliza el metodo.join seguido de
#la variable que contiene la lista
print(frase_1)
