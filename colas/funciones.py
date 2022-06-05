from clases import banco

banc = banco()

#agregar un elemento a la cola
def insertar():
    dato = input('Ingresa el nombre del usuario: ')
    banc.enqueue(dato)
    banc.mostrar()

    y = input('Quiere ingresar otro usuario? (s-n): ')

    if y.lower() == 's':
        insertar()

#eliminar el primero de la cola
def eliminar():
    banc.dequeue()
    banc.mostrar()

#mostrar el primero en la cola
def first():
    banc.front()

#mostrar el ultimo elemento de la cola
def last():
    banc.rear()

#listar todos los elementos y la cantidad en la cola
def mostrar():
    banc.length()
    banc.mostrar()
    
