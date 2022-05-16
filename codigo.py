import re

# usuario = input("ingrese su usuario: ")
usuario = 'P&rt+l@sur'
users_cdia = ['K?AIKG@A+R', 'FIR=TO@RLS', 'P&RT+L@SUR']

def verificar_usuario(nombre):
    leng = len(nombre) #numero_de_caracteres
    tipo_dato = isinstance(nombre,str)
    is_number = re.search("[0-9]",nombre)
    arroba = nombre[6] == "@"
    first_last = nombre[0] != nombre[-1]
    k = 0
    exist_plus = False
    signo = 0

    for i in range(leng):
        caracter = nombre[i]
        if caracter == "k":
            k += 1
        if caracter == '+':
            exist_plus = True
        if caracter == '?' or caracter == '=' or caracter == '&':
            signo += 1

    if leng == 10 and tipo_dato and arroba and first_last and k <= 3 and exist_plus and signo > 0 and not is_number :
        return True
    else:
        return False

if(not verificar_usuario(usuario)):
    print('CDIA invalido')
elif  usuario.upper() in users_cdia:
    print('El CDIA ya esta en uso')
else:
    dia_nacimiento = int(input('Ingresa tu dia de nacimiento (01-31): '))
    mes_nacimiento = int(input('Ingresa tu mes de nacimiento (01-12): '))
    anio_nacimiento = int(input('Ingresa tu año de nacimiento (4 digitos): '))

