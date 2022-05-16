import modulos as mod

def init():
    # usuario = input("ingrese su usuario: ")
    usuario = 'dav?+g@rri'
    users_cdia = ['K?AIKG@A+R', 'FIR=TO@RLS', 'P&RT+L@SUR']
    
    
    if(not mod.verificar_usuario(usuario)):
        print('CDIA invalido')
        init()
    elif  usuario.upper() in users_cdia:
        print('El CDIA ya esta en uso')
        init()
    else:
        print('perfecto!!! ',usuario,' Completa los siguientes datos: ')
        dia_nacimiento = int(input('Dia de nacimiento (01-31): '))
        mes_nacimiento = int(input('Mes de nacimiento (01-12): '))
        anio_nacimiento = int(input('Año de nacimiento (4 digitos): '))

        if mod.validate_date(dia_nacimiento, mes_nacimiento, anio_nacimiento):
            alias = input('Ingresa tu alias: ')
            if mod.validate_alias(alias):
                print('todo va perfecto')
            else:
                print('Alias invalido, Vuelve a Intentarlo.')
                init()
        else:
            print('No tienes la edad suficiente para acceder.')

init()
