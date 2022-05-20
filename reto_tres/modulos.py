import re
from datetime import datetime
import datetime as dtm


def verificar_usuario(nombre):
    leng = len(nombre) #numero_de_caracteres
    tipo_dato = isinstance(nombre,str)
    is_number = re.search("[0-9]",nombre)
    arroba = False
    if leng > 6:
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


def validate_date(d,m,a):
    today = datetime.today()
    nacimiento = dtm.datetime(a, m, d).strftime('%s')
    unix_act = dtm.datetime(today.year, today.month, today.day).strftime('%s')
    edad = int((int(unix_act) - int(nacimiento))/31556926)
    return edad

def validate_alias(al):
    long = len(al)
    space = re.search(' ', al)
    if not space and long >= 5:
        return True
    else:
        return False


