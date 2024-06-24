'''
Ejercicio de la plataforma 
Los datos están en un archivo CSV llamado visit_log.csv y cada fila representa una visita al sitio web de una empresa. Hay cuatro columnas:

--- > 'user_id': identificador único para cada persona que visita el sitio web.
---> 'source': fuente de tráfico de la visita al sitio web. Aquí nos interesan tres categorías para la fuente:
        - Visitas desde enlaces de marketing por correo electrónico: 'email'
        - Visitas de anuncios contextuales en línea: 'context'
        - Visitas de cualquier otra fuente: 'other'
---> 'email': dirección de correo electrónico encriptada asociada con la persona que visita el sitio.
---> 'purchase': indica si la persona compró algo en esa visita (1 en caso afirmativo, 0 en caso negativo).
'''
'''
Tu objetivo es determinar la tasa de conversión para cada fuente, que es la proporción de visitas en las que se realizó una compra 
con respecto al número total de visitas en general. Comparar la tasa de conversión para cada fuente te permitirá determinar cuál de ellas 
genera la mayor cantidad de ventas.
'''

## PASO UNO -->  darle un vistazo general con el metodo info para observar si hay datos nulos y en que columnas

import pandas as pd 

df_logs = pd.read_csv('/Users/hectorciddelprado/Desktop/datasets/visit_log.csv')

## llamar al metodo info, se puede usar print o solo llamar a la variable y pasarle el metodo 
#print(df_logs.info())
df_logs.info() 

## PASO DOS -->  contar los valores ausentes en el DF
valores_ausentes = df_logs.isna().sum()
print(valores_ausentes)

'''
#### VALUE_COUNTS()
para sumar los valores obtenidos con isna(), podemos contar los valores ausentes en una Series(1 columna) con el metodo value_counts(),
esto devuelve la cantidad de veces que cada valor unico aparece en esa columna, este metodo contiene el parametro dropna=
-- True - excluira los valores None - NaN, es decir, solo imprime valores unicos
-- False - imprime los valores unicos y los None - NaN
'''
print(df_logs['source'].value_counts(dropna=False))
#### esto imprime los resultados de manera descendente podemos utilizar el metodo sort_index() para ordenarlos alfabeticamente
print(df_logs['source'].value_counts(dropna=False).sort_index())

'''
Podemos ver que la columna 'source' contiene valores para las fuentes de tráfico que nos interesan, 
que son 'context' para anuncios contextuales, 'email' para correos electrónicos de marketing y 'other' para todo lo demás. 
También vemos que tenemos 1674 valores ausentes de la columna 'source', lo cual representa aproximadamente el 1% de los datos. 
También está el valor 'undef', pero todavía no sabemos a qué se refiere.
'''

## PASO 3 --- > indagar sobre la columna email y mostrar valores usando value_count() pero sin incluir valores None - NaN, usar la variable 
# email_value para almacenar el resultado 

email_value = df_logs['email'].value_counts(dropna=True)
print(email_value)


