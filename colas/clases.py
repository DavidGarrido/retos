class banco:
    def __init__(self)->None:
        self.personas = []

    #vefifico si esta vacia la cola
    def isEmpty(self):
        return True if len(self.personas) == 0 else False

    #insertar ellemento al final de la cola
    def enqueue(self, x):
        self.personas.append(x)

    #remover el elmento al incio de la cola
    def dequeue(self):
        if not self.isEmpty():
            del self.personas[0]
        else:
            print('la cola esta vacia')

    #retornar el elemento al inicio de la cola
    def front(self):
        if not self.isEmpty():
            print(self.personas[0])
        else:
            print('La cola esta vacia')

    #retornar el ultimo de la cola
    def rear(self):
        if not self.isEmpty():
            print(self.personas[-1])
        else:
            print('la cola esta vacia')

    #retornar el numero de elementos de la cola
    def length(self):
        print('El numero de elementos es igual a ',len(self.personas))

    #mostrar
    def mostrar(self):
        print(self.personas)    
