from collections import namedtuple
User = namedtuple('User', ['Nombre', 'Telefono', 'Documento'])
users = []
def insert_user():
    print(' ')
    print('Ingresar usuario ',len(users)+1,':')
    nombre = input('Nombre: ')
    tel = int(input('Numero de telefono: '))
    doc = int(input('Numero de documento: '))

    u = User(nombre, tel, doc)

    users.append(u)
    
    other = input('Deseas agregar otro usuario? (s-n): ')

    if other.lower() == 's':
        insert_user()
    else:
        print('')
        print('Listado de usuarios ingresado: ')
        print('---------------------------------------------------------------------')
        print('{:<20}| {:<20}| {:<20}|'.format('Nombre','Telefono','Documento'))
        print('---------------------------------------------------------------------')
        for u in users:
            nombre, tel, doc = u
            print('{:<20}| {:<20}| {:<20}|'.format(nombre,tel,doc))
        print('---------------------------------------------------------------------')
            
insert_user()

    
