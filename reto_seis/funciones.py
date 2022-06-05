from collections import namedtuple

Student = namedtuple('Student',['id','document','gener','name', 'last_name', 'email','date','cicle'])

students = []


ident = len(students) + 1
name = 'David'
last_name = 'Garrido'
document = 27349827
date = '10/07/1992'
gener = 'm'
email = 'www.davidalexander@gmail.com'
cicle = 2
s = Student(ident, [document], [gener], [name], [last_name], [email], [date], [cicle] )
students.append(s)

ident = len(students) + 1
name = 'Alex'
last_name = 'Hernandez'
document = 37349827
date = '20/07/1992'
gener = 'm'
email = 'alexander@gmail.com'
cicle = 1
s = Student(ident, [document], [gener], [name], [last_name], [email], [date], [cicle] )
students.append(s)


def create_student():
    print('vas a crear un estudiante:')
    ident = len(students) + 1
    name = input('Nombre(s): ')
    last_name = input('Apellido(s): ')
    document = int(input('Documento: '))
    date = input('Fecha de nacimiento (DD/MM/AAAA): ')
    gener = input('Genero (m-f): ')
    email = input('Email: ')
    cicle = int(input('Ciclo: '))

    s = Student(ident, [document], [gener], [name], [last_name], [email], [date], [cicle] )

    students.append(s)
    list_students(students)

def modify_student(ident):
    print('vas a modificar el estudiante: ',ident)
    for s in students:
        if s.id == ident:
            print('Nombre(s): ',s.name[0])
            print('Apellido(s): ',s.last_name[0])
            print('Documento: ',s.document[0])
            print('Nacimiento: ',s.date[0])
            print('Genero: ',s.gener[0])
            print('Email: ',s.email[0])
            print('Ciclo: ',s.cicle[0])

            dato = int(input('Que dato deseas cambiar: \n(1)Nombre(s) \n(2)Apellido(s) \n(3)Documento \n(4)Nacimiento \n(5)Genero \n(6)Email \n(7)Ciclo : '))

            if dato == 1:
                nombre = input('Ingresa el nuevo nombre: ')
                s.name[0] = nombre
            if dato == 2:
                last_name = input('Ingresa el nuevo apellido: ')
                s.last_name[0] = last_name
            if dato == 3:
                document = int(input('Ingresa el nuevo documento: '))
                s.document[0] = document
            if dato == 4:
                date = input('Ingresa la nueva fecha: ')
                s.date[0] = date
            if dato == 5:
                gener = input('Ingresa el nuevo valor de genero (m-f): ')
                s.gener[0] = gener
            if dato == 6:
                email = input('Ingresa el nuevo email: ')
                s.email[0] = email
            if dato == 7:
                cicle = int(input('Ingresa el nuevo ciclo: '))
                s.cicle[0] = cicle
    list_students(students)


def delete_student(ident):
    print('vas a eliminar un estudiante',ident)
    for i in range(len(students)):
        if students[i].id == ident:
            students.remove(students[i])
            print(students)

def order_students(by):
    order = []
    final = []
    for e in students:
        if by == 1:
            order.append([e.name[0], e.id])
        if by == 2:
            order.append([e.last_name[0], e.id])
        if by == 3:
            order.append([e.email[0], e.id])
        if by == 4:
            order.append([e.document[0], e.id])
        if by == 5:
            order.append([e.gener[0], e.id])
        if by == 6:
            order.append([e.date[0], e.id])
        if by == 7:
            order.append([e.cicle[0], e.id])

    order.sort()

    for i in order:
        for e in students:
            if by == 1:
                if i[1] == e.id and i[0] == e.name[0]:
                    final.append(e)
            if by == 2:
                if i[1] == e.id and i[0] == e.last_name[0]:
                    final.append(e)
            if by == 3:
                if i[1] == e.id and i[0] == e.email[0]:
                    final.append(e)
            if by == 4:
                if i[1] == e.id and i[0] == e.document[0]:
                    final.append(e)
            if by == 5:
                if i[1] == e.id and i[0] == e.gener[0]:
                    final.append(e)
            if by == 6:
                if i[1] == e.id and i[0] == e.date[0]:
                    final.append(e)
            if by == 7:
                if i[1] == e.id and i[0] == e.cicle[0]:
                    final.append(e)
           

    
    # print(final)
    list_students(final)

def search_student(clave, valor):
    final = []
    for e in students:
        if clave == 1 and e.name[0].lower() == valor.lower():
            final.append(e)
        if clave == 2 and e.last_name[0].lower() == valor.lower():
            final.append(e)
        if clave == 3 and e.email[0].lower() == valor.lower():
            final.append(e)
        if clave == 4 and e.document[0].lower() == valor.lower():
            final.append(e)
        if clave == 5 and e.gener[0].lower() == valor.lower():
            final.append(e)
        if clave == 6 and e.date[0].lower() == valor.lower():
            final.append(e)
        if clave == 7 and e.cicle[0].lower() == valor.lower():
            final.append(e)
    list_students(final)



def length_students():
    return len(students)

def list_students(lista):
    if len(lista) > 0:
        for e in lista:
            print('{:<5} | {:<20} | {:<20} | {:<30}| {:<20} | {:<5} | {:<15} | {:<5}'.format(e.id,e.name[0],e.last_name[0],e.email[0],e.document[0],e.gener[0],e.date[0],e.cicle[0]))
    else:
        print('No hay elemento para mostrar')
        # print(e.name)

list_students(students)
# order_students(4)
