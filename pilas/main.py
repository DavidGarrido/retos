import funciones as f
import os
os.system('cls')

# creamos el menu
def menu():
    dato = input('para insertar datos = "a", para eliminar = "e", para mostrar ultimo elemento = "u", para contar = "c", para mostrar pila = "m": ')

    if dato == 'a':
        f.ingresar_datos_pila()
        menu()
    elif dato == 'e':
        f.eliminar()  
        menu()  

    elif dato == 'u':
        f.mostrar_ultimo()
        menu()    
    elif dato == 'c':
        f.contar()
        menu()
menu()     
