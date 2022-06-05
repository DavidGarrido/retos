import funciones as func

aceleracion = int(input('Ingresa la aceleracion: '))
tiempo = int(input('Ingresa el tiempo: '))
func.simulador_movimiento(aceleracion, tiempo)
print()
series = int(input('Ingresa el numero de series: '))
func.calculador_series(series)
print()
pisos = int(input('Ingresa el numero de pisos: '))
func.constructor_triangulos(pisos)


