# El bloque try-except es una estructura de control en Python
# que se utiliza para manejar excepciones, es decir, situaciones en las que ocurre un error durante 
# la ejecución de un bloque de código. 
# Este mecanismo permite que el programa continúe su ejecución, incluso si se encuentra un error, 
# en lugar de terminar abruptamente.

# try: Este bloque contiene el código que se quiere ejecutar y que puede potencialmente generar una excepción. 
# Si no ocurre ninguna excepción, el bloque except se omite y la ejecución del programa continúa normalmente 
# después del bloque try.

# except: Este bloque contiene el código que se ejecuta si ocurre una excepción en el bloque try. 
# Puedes especificar el tipo de excepción que quieres manejar (por ejemplo, ValueError, TypeError, etc.). 
# Si no especificas un tipo de excepción, el bloque except capturará todas las excepciones.

## ejemplos 

user_age = 'treinta y dos'  # Aquí está la variable que almacena la edad como un string.

try:
    user_age_int = int(user_age)  # Intentamos convertir user_age a un entero
except ValueError:
    print('Please provide your age as a numerical value')  # Si falla, imprime el mensaje de error


user_age = '32'

try:
    user_age_int = int(user_age)
    print(f'Your age is: {user_age_int}') ## se puede usar un sting formateado para agregar texto y variables
except ValueError:
    print('Please provide your age as a numerical value')
