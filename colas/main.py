import funciones as func
import os
os.system('clear')

def menu():
    print('1 - Insertar')
    print('2 - Eliminar el primero')
    print('3 - Ver primero')
    print('4 - Ver ultimo')
    print('5 - Mostrar')
    dato = int(input('Selecciona la accion:'))
    
    if dato == 1:
        func.insertar()
        menu()
    elif dato == 2:
        func.eliminar()
        menu()
    elif dato == 3:
        func.first()
        menu()
    elif dato == 4:
        func.last()
        menu()
    elif dato == 5:
        func.mostrar()
        menu()
    else:
        print('Gracias')
    
menu()
