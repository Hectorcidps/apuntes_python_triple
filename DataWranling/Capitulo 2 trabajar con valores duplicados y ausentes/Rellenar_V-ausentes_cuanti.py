##### analizar datos cuantitativos ausentes #### 
# OBJETIVO: comparar el tiempo promedio que pasan en el sitio web los usuarios y las usuarias de dispositivos moviles y de escritorio

import pandas as pd

analytics_data = pd.read_csv('/Users/hectorciddelprado/Desktop/datasets/web_analytics_data.csv')

print(analytics_data.head(10))
analytics_data.info()


'''
## PASO 1 --- > comprobar si hay valores atipicos importantes, es decir, si los valores ausentes son bastantes y afectan a la muestra entonces
es necesario modificarlos. En el caso contrario, es decir, que los valores solo sean una pequeña parte de los datos, sean aleatorios puede ser
una buuena idea dejarlos como NaN, los cuales no se incluiran en ningun calculo numerico.

--- Si no hay valores atípicos significativos, calcula la MEDIA utilizando el método mean().
--- Si tus datos tienen valores atípicos significativos, calcula la MEDIANA utilizando el método median().
## despues de definir se hace lo siguiente:
--- Reemplaza los valores ausentes con la media o la mediana utilizando el método fillna().
'''

## en el caso de este dataSet no hay valores atipicos importantes por lo cual podemos usar mean()

age_avg = analytics_data['age'].mean() # se eligio la media al no tener tantos valores atipicos 
print(f'La media del DF es: {age_avg}')

## despues se Reemplazan los valores ausentes con la media 
analytics_data['age'] = analytics_data['age'].fillna(age_avg)

'''
Recuerda que queremos comparar el tiempo promedio que pasan en el sitio web las personas que utilizan dispositivos móviles y de escritorio,
luego usaremos esos tiempos promedio para rellenar los valores ausentes.

Comienza dividiendo los datos en dos DataFrames(usando filtros logicos): uno para visitas desde dispositivos de escritorio y otro para visitas 
desde dispositivos móviles.
Asigna las visitas de escritorio a una variable llamada desktop_data y las visitas móviles a otra variable llamada mobile_data.
'''
# filtro logico para desktop
desktop_data = analytics_data[analytics_data['device_type'] == 'desktop']
# filtro logico para mobile
mobile_data = analytics_data[analytics_data['device_type'] == 'mobile']

# ahora Asigna la media del tiempo de visita de los usuarios de escritorio a una variable llamada desktop_avg y 
# la media de los usuarios móviles a mobile_avg. 

desktop_avg = desktop_data['time'].mean()
mobile_avg = mobile_data['time'].mean()
print(f"Tiempo de escritorio promedio: {desktop_avg:.2f} segundos")
print(f"Tiempo móvil promedio: {mobile_avg:.2f} segundos")

## Utiliza el tiempo promedio de visita de escritorio para rellenar los valores ausentes en la columna 
# 'time' de desktop_data y el tiempo promedio de visita móvil para rellenarlos en mobile_data.

# rellenar los valores ausentes del Df temporal desktop_data
desktop_data['time'] = desktop_data['time'].fillna(desktop_avg)
# rellenar los valores ausentes del Df temporal mobile_data
mobile_data['time'] = mobile_data['time'].fillna(mobile_avg)

desktop_data.info() # se imprime el Df temporal desktop_data con los valores NaN rellenos con el tiempo promedio
mobile_data.info() # se imprime el Df temporal mobile_data con los valores NaN rellenos con el tiempo promedio