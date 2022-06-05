
def simulador_movimiento(a,t):
  
    # Hallar la velocidad
    v = a * t 
    # Hallar distancia segundo a segundo
    for i in range(t+1):
        x = v * i
        print("Se ha recorrido",x,"metros en ",i," segundos")
    
    return "No implementada aún"




def calculador_series(n):

    sumatoria = 0
    dividiendo = 1

    for i in range(n):
        sumatoria = sumatoria + (1 / dividiendo)
        dividiendo = dividiendo * 2
        print("Sumatoria parcial:",sumatoria)



def constructor_triangulos(pisos):
    if pisos > 0:
        num = 1 #variable contador
        for i in range(0, pisos):#ciclo para recorrer los pisos
            for j in range(0, i+1):#si esta en el rango de piso
                if num < 10:#condicional para anteponer el cero en numeros menores de 10
                    print('0'+str(num), end=" ")
                else:
                    print(num, end=" ")#imprime el numero y finaliza con un espacio para que no termine en salto de linea
                num = num + 1#despues de imprimir se aumenta 
            print("\r")
    else:
        print("El numero debe ser mayor a 0")
    
