'''
Tipos de variables 

Las variables CUANTITATIVAS tienen valores numéricos que podemos usar para cálculos aritméticos, 
por ejemplo, la altura, el peso, la edad y los ingresos. En Python, estos valores tienden a almacenarse como números enteros o flotantes.

Las variables CATEGÓRICAS representan un conjunto de valores posibles que puede tener una observación particular, 
por ejemplo, el color, la marca y el modelo de un automóvil. En Python, estos valores tienden a almacenarse como CADENAS,
pero también pueden ser valores booleanos o incluso números enteros.
'''

import pandas as pd 

df_logs = pd.read_csv('/Users/hectorciddelprado/Desktop/datasets/visit_log.csv')

### PASO 4 ---> cambiar los valores NaN por '' asi ya no se leeran los valores ausentes en la DF
df_logs['email'] = df_logs['email'].fillna('')
print(df_logs.head(5))
df_logs.info()

'''
Usar fillna() no es la única forma en que podemos rellenar los valores ausentes con cadenas vacías. 
Por cierto, también podemos hacerlo directamente al leer los datos mediante read_csv().

### Ejemplo 
df_logs = pd.read_csv('/Users/hectorciddelprado/Desktop/datasets/visit_log.csv', keep_default_na= False)
'''
df_logs = pd.read_csv('/Users/hectorciddelprado/Desktop/datasets/visit_log.csv', keep_default_na= False)
print(df_logs.head())
df_logs.info()

'''
En la impresión podemos ver que los valores ausentes son cadenas vacías. Ahora info() ya no detectará ningún valor nulo, 
esto significa que depende de nosotros reconocer que '' representa un valor ausente a medida que avanzamos con nuestro análisis.

Ten en cuenta que establecer keep_default_na=False convierte todos los valores ausentes en cadenas vacías, incluso para columnas numéricas. 
Esto hace que las columnas numéricas se lean como cadenas cuando tienen valores ausentes. Así que asegúrate de usar solo keep_default_na=False 
cuando desees que todos los valores ausentes en cada columna se lean como cadenas vacías.

En el caso de visit_log.csv, nos conviene hacer esto porque todas nuestras columnas son categóricas. 
¡Pudimos leer los datos y reemplazar todos los valores ausentes con tan solo una pequeña línea de código!
'''
### PASO 5 ---> utilizar el metodo replace para reemplazar los valores ausenes en source por la cadena 'email'

df_logs['source'] = df_logs['source'].replace('', 'email')

print(df_logs['source'].unique()) # verificar con el metodo unique, para que imprima los valores unicos 


#### PASO 6 ---> Para calcular la tasa de conversión de cada fuente de tráfico, primero determina cuántas visitas hubo de cada fuente.
# utilizar el metodo groupby para dividir por cada una de las fuentes de trafico 

visitas = df_logs.groupby('source')['user_id'].count()
print(visitas)

### PASO 7 ---> sumar el numero de compras (purchase) para cada una de las fuentes (visita) almacenaros en una variable llamada purchases

purchases = df_logs.groupby('source')['purchase'].sum()
print(purchases)

### PASO 8 ---> Calcular la tasa de conversion para cada una de las fuentes de trfico, almacenar en una variable llamada "conversion"
# esto se obtiene diviendo el numero de compras entre el numero de visitas

conversion = purchases / visitas
print(conversion)

'''
Aunque "otros" tiene más compras en general, parece que el correo electrónico tiene la mejor tasa de conversión.
En unas pocas líneas de código, has conseguido calcular la métrica más importante del marketing.
'''

