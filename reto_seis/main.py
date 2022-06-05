import os
os.system('clear')

import funciones as func


def menu():
    print()
    number_students = func.length_students()
    print('1. Ingresar un estudiante.')

    if number_students > 0:
        print('2. Modificar estudiante.')
        print('3. Eliminar estudiante.')

    if number_students > 1:
        print('4. Ordenar lista.')
        print('5. Buscar estudiante.')

    print('6. Salir')

    accion = int(input('Selecciona la acción que vas a realizar: '))

    if accion == 1:
        func.create_student()
        menu()

    if number_students > 0:
        if accion == 2:
            ident = int(input('Id del estudiante: '))
            func.modify_student(ident)
            menu()

        if accion == 3:
            ident = int(input('Id del estudiante: '))
            func.delete_student(ident)
            menu()

    if number_students > 1:
        if accion == 4:
            print('1. Nombre')
            print('2. Apellidos')
            print('3. Email')
            print('4. Documento')
            print('5. Genero')
            print('6. Nacimiento')
            print('7. Ciclo')
            valor = int(input('Ingrese el numero por el cual quiere ordenar la lista: '))
            if valor > 0 and valor < 8:
                func.order_students(valor)
            else:
                print('Valor incorrecto')
            menu()

        if accion == 5:
            print('Buscar por')
            print('1. Nombre')
            print('2. Apellidos')
            print('3. Email')
            print('4. Documento')
            print('5. Genero')
            print('6. Nacimiento')
            print('7. Ciclo')
            clave = int(input('Ingrese el numero del dato por el cual desea hacer la busqueda: '))
            if clave > 0 and clave < 8:
                valor = ''
                if clave == 1 or clave == 2 or clave == 3 or clave == 5 or clave == 6:
                    valor = input('Ingresa el valor a buscar: ')
                else:
                    valor = int(input('Ingresa el valor a buscar: '))
                func.search_student(clave,valor)
            else:
                print('Valor incorrecto')
            menu()

    if accion == 6:
        print('Gracias')
    
    print()


menu()
