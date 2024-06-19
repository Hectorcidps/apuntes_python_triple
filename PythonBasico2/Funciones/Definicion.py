## Son pequeños programas que sirven para automatizar operaciones rutinarias.
# es una forma estandarizada de compartir codigo con alguien mas 

#### sintaxis ####

#encabezado de la funcion
## def(es la palabra clave de funcion) + nombreDeLaFuncion +(nombre de los parametros de la funcion) + :
# cuerpo de la funcion
    # (agregar una identacion) + variable_temporal (donde se realizan todos los pasos en la funcion)
    #return (plabra clave que indica el valor que devolvera la funcion) + variable_temporal
    
    # EL USO DE RETURN ES PARA TRAER INMEDIATAMENTE EL RESULTADO EJECUTADO EN EL CUERPO, SI SE AGREGA UNA INSTRUCCION MAS DESPUES DE 
    # RETURN NO SE EJECUTARA!!

## ejemplo 
def omelet(eggs_number):
    result = 'El omelet esta listo! Huevos utilizados: ' + str(eggs_number)
    return result

## LAS FUNCIONES SE PUEDEN MANDAN A LLAMAR CON SOLO EL NOMBRE DE LA FUNCION, SE PUEDE USAR PRINT PERO NO ES BUENA PRACTICA

omelet_type = omelet(2) ## agregas un parametro a la funcion omelet 
print(omelet_type) # imprimira que se han usado 2 huevos por lo anteriormente establecido
print(omelet(3)) # imprimira 3 huevos, porque no lo suplanta solo se cambia el parametro