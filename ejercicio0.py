#almacena el numero de estudintes a ingresar
from statistics import mean


cantidad = int(input("Cuantos estudiantes desea ingresar: "))

#este diccionario almacena los resultados academicos
resultados = {}

for i in range(0, cantidad):
    print("")
    print('Ingresando datos del estudiante: ')
    nombre  = input("Ingresa el nombre del estudiante {0}°".format(i))
    notas = []

    for j in range (0, 3):
        nota = float(input("Ingresa la nota {0}°".format(j)))
        notas.append(nota)

    resultados.setdefault(nombre, notas)

# print(resultados)
for nombre , notas in resultados.items():
    print("-"*60)
    fila = nombre.ljust(10)
    for nota in notas:
        fila += "| "+str(nota).ljust(10)

    # fila += "| "+str(round(mean(notas), 2)).ljust(10)
    fila += "| "+str(round((sum(notas) / len(notas)), 2)).ljust(10)

    print(fila)
