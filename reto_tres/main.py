import modulos as mod

def init(user,d,m,a,ali,is_u):
    if user:
        usuario = user
    else:
        usuario = input("ingrese su usuario: ")
        # usuario = 'dav?+g@rri'

    users_cdia = ['K?AIKG@A+R', 'FIR=TO@RLS', 'P&RT+L@SUR']
    nivel_final = 0
    mundo = 0


    if(not mod.verificar_usuario(usuario)):
        print('CDIA invalido')
        init('','','','','','')
    elif  usuario.upper() in users_cdia:
        print('El CDIA ya esta en uso')
        init('','','','','','')
    else:
        if not user and not d and not m and not a and not ali:
            print('perfecto!!! ',usuario,' Completa los siguientes datos: ')
        if d and m and a:
            dia_nacimiento = d
            mes_nacimiento = m
            anio_nacimiento = a
        else:
            dia_nacimiento = int(input('Dia de nacimiento (01-31): '))
            mes_nacimiento = int(input('Mes de nacimiento (01-12): '))
            anio_nacimiento = int(input('Año de nacimiento (4 digitos): '))

        edad_user = mod.validate_date(dia_nacimiento, mes_nacimiento, anio_nacimiento)

        if  edad_user >= 12:
            if ali:
                alias = ali
            else:
                alias = input('Ingresa tu alias: ')
            if mod.validate_alias(alias):              
                if is_u:
                    is_player = is_u
                else:
                    is_player = input('Has jugado antes? (s)(n): ')              
                if is_player.lower() == 's' or is_player.lower() == 'n':
                    if is_player.lower() == 's' and edad_user < 16:
                        nivel_final = int(input('Hasta que nivel avanzaste? (1-100): '))
                        if nivel_final > 0 and nivel_final <= 100:
                            if nivel_final < 50:
                                mundo = 2
                            if nivel_final >= 50:
                                mundo = 3
                        else:
                            init(usuario,dia_nacimiento,mes_nacimiento,anio_nacimiento,alias,is_player)
                    elif is_player.lower() == 'n' and edad_user < 16:
                        nivel_final = 2
                        mundo = 1
                    elif is_player.lower() == 's' and edad_user >= 16:                  
                        nivel_final = int(input('Hasta que nivel avanzaste? (1-100): ')) + 2                
                        if nivel_final-2 > 0 and nivel_final-2 <= 100:
                            if (nivel_final - 2) < 50 and edad_user <= 20:
                                mundo = 2
                            if (nivel_final - 2) >= 50 and edad_user <= 20:
                                mundo = 3
                            if (nivel_final - 2) < 50 and edad_user > 20:
                                mundo = 5
                            if (nivel_final - 2) >= 50 and edad_user > 20:
                                mundo = 6                      
                        else:
                            init(usuario,dia_nacimiento,mes_nacimiento,anio_nacimiento,alias,is_player)
                    elif is_player.lower() == 'n' and edad_user >= 16:
                        nivel_final = 1
                        if edad_user <= 20:
                            mundo = 1
                        if edad_user > 20:
                            mundo = 4
                    print('Accediste al nivel: ',nivel_final,', e ingresaste al mundo: ',mundo)
                else:
                    init(usuario,dia_nacimiento,mes_nacimiento,anio_nacimiento,alias,'')
            else:
                print('Alias invalido, Vuelve a Intentarlo.')
                init(usuario, dia_nacimiento, mes_nacimiento, anio_nacimiento,'','')
        else:
            print('No tienes la edad suficiente para acceder.')

init('','','','','','')
