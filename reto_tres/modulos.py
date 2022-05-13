import re

def validate_user(name_user):
    long = len(name_user)
    type_name = isinstance(name_user, str)
    is_number = False
    arroba = name_user[5] == '@'
    first_last = name_user[0] == name_user[-1]
    len_k = 0
    simbol = False

    #recorrer todos los caracteres del nombre y comprobar si es numerico
    for i in range(long):

        #comprobar si es numerico
        caracter = name_user[i]
        result = re.search('[0-9]', caracter)
        if isinstance(result, re.Match):
            is_number = True
            break
        if caracter == 'k':
            len_k += 1
        if caracter == '?' or caracter == '=' or caracter == '&':
            simbol = True

    #si no se cumplen las condiciones retornar falso de lo contrario retornar verdadero
    if is_number or long != 10 or type_name == False or arroba == False or first_last or len_k > 3 or simbol == False:
        return False
    else:
        return True
