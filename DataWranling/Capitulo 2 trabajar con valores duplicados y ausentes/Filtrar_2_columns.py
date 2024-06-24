import pandas as pd 

df_logs = pd.read_csv('/Users/hectorciddelprado/Desktop/datasets/visit_log.csv')

############# filtrar DataFrames con NaNs 

### ejercicio uno Datos sin NaN
'''
Filtra el DataFrame df_logs para que solo contenga filas donde no haya valores ausentes en la columna 'email'.
Asigna el resultado filtrado a una variable llamada df_emails, luego imprime las primeras 10 filas.

Para comprobar si una condición no es verdadera al filtrar un DataFrame, precede la condición 
con el carácter ~ (por ejemplo, df[~df.method()]).

~ se utiliza como operador de negación lógica (NOT). Cuando se aplica a una serie de pandas que contiene valores booleanos (True o False), 
invierte estos valores: convierte True en False y False en True.
'''
df_emails = df_logs[~df_logs['email'].isna()]

print(df_emails.head(10))

######### ejercicio dos valores con NaN
'''
Comprueba si hay filas con valores ausentes en las columnas 'source' y 'email'. 
Si no hay ninguna fila en la que ambas condiciones sean verdaderas, entonces es una buena señal de que los valores ausentes en la columna 'source' 
deberían ser 'email'.

Filtra df_logs en la condición donde las columnas 'email' y 'source' TIENEN valores ausentes. 
Asigna el resultado a una variable llamada df_emails y luego imprímelo.

En este ejercicio es neceario aplicar una condicion para cada columna utilizando el simbolo & para conectarlas
'''

df_emails = df_logs[df_logs['source'].isna() & df_logs['email'].isna()]
print(df_emails)