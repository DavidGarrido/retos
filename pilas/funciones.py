from clase_pila import libros

l = libros() #instanciamos la clase libros

#ingresar datos a la pila
def ingresar_datos_pila():
    dato = input('escribe el nombre de un libro: ')
    l.push(dato) #insertamos un dato
    l.mostrar() #mostramos los elementos de la pila

    y = input('quieres ingresar otro libro. "s" para si y "n" para no: ')

    if y == 's':
        ingresar_datos_pila()
    else:
        print('no hay mas libros')  


#remover el ultimo elemento de la pila
def eliminar():
    l.pop()
    l.mostrar()


#mostrar top
def mostrar_ultimo():
    print(l.top())

def contar():
    l.mostrar()
