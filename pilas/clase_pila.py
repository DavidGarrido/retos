class libros: #creamos la clase
    #creamos el constructor
    def __init__(self):
        self.caja = []

    #verifico si la pila esta vacia
    def isEmpty(self):
        return True if len(self.caja) == 0 else False
        """ if len(self.caja) == 0:
            return True
        else:
            return False   """ 

    #insertar datos a la pila
    def push(self,x):
        self.caja.append(x)  

    #eliminar ultimo elemento de la pila
    def pop(self):
        if self.isEmpty():
            print('la pila esta vacia')
        else:
            self.caja.pop()    

    #retornar elemento en el tope de la pila
    def top(self):
        if self.isEmpty():
            print('la pila esta vacia')
        else:
            return self.caja[-1]  

    #retornar numero de elementos en la pila
    def length(self):
        return len(self.caja)                  

    #mostrar elementos de la pila
    def mostrar(self):
        print(self.caja)
