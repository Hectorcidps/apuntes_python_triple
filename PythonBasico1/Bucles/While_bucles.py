### Cuando no sabemos cuantas veces tenemos que realizar determinada accion los bucles while son la mejor opcion.

# Utiles cuando debes comprobar el estado de una variable 
# la condicion se verifica antes de cada iteracion 
# Si es True,se ejecuta el codigo
# Si es False, el bucle se detiene

#from random import randint # importamos la funcion randint de la libreria random

# declaramos las variables 
#capacity = 400 # capacidad del asensor en KG 
#total_weight = 0 # variable que almacena el peso total

#while total_weight < capacity: # Mientras que el peso total es menor que la capacidad maxima
   # person_weight = randint(30, 120) # generamos un numero aleatorio de 30 a 120
  #  total_weight += person_weight # el peso generado se agrega al peso total
 #   print(f'Entra una persona. Carga actual del asensor: {total_weight}')
#print("Lo sentimos! El asensor esta lleno, espera al otro por favor")

# Uso de contadores 

num_people = 0 # comienza en 0 y no hay nadie dentro
capacity = 10 # varible que almacena el limite de personas

while num_people < capacity: #mientras el numero de personas es menor a la capacidad
    num_people += 1 # puede ingresar otra persona 
    print(f'Entra una persona. Carga actual del ascensor: {num_people}')

print('Lo sentimos! el ascensor esta lleno. Tendras que esperar al siguiente.')

## Ejemplo de la plataforma 

# La gerencia está interesada en saber cuándo un cliente o una clienta alcanza un millón en ingresos totales 
# y te pidieron que escribieras un código que calcule la cantidad de años que necesita un cliente o una clienta
# para alcanzar este número. Para empezar, te pidieron que probaras tu código para 'Jack Wilson', 
# que gana 150000 al año. Escribe un bucle while que sume los ingresos anuales totales de Jack hasta que llegue a
# un millón. Una vez que lo alcance, muestra el número de años que tardó en alcanzar este ingreso total.

annual_income = 150000 # ingreso anual de Jack
target_income = 1000000 # ingreso objetivo

total_income_sum = 0 # ingresos totales que se actualizarán para cada año
years_to_million = 0 # cantidad de años que también se actualizará

while total_income_sum < target_income:
    total_income_sum += 150000 # aqui se ingresa el valor que se va a iterar
    years_to_million += 1 # se pone 1 para saber cuantos años va a tardar 

print(years_to_million)