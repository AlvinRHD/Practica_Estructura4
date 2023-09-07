# declaracion de diccionarios
from array import array


miDiccionario = dict()

otraoDiccionario = {}

otraFormaDeclaracion = {
    'clave1' : 10, 
    1: True,
    'otraclave': [1,2,3],
    'cadena' : 'Este es un mensaje',
    'diccionario' : miDiccionario
}

print(otraFormaDeclaracion)
# print(otraFormaDeclaracion['clave1'])
# print(otraFormaDeclaracion[1])
# print(otraFormaDeclaracion['otraclave'])
# print(otraFormaDeclaracion['cadena'])
# print(otraFormaDeclaracion['diccionario'])

#limpiar
#otraFormaDeclaracion.clear()

copia = otraFormaDeclaracion.copy()
print(otraFormaDeclaracion)
print(copia)