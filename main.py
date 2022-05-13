import calculadora as cal
#                 CALCULADORA SALUDABLE 
#al desarrollar este programa debes tratar de hacerlo sin condicionales ya que no los hemos visto, trata de crearlo solicitando valores tanto para hombres como para mujeres y en los datos de salida de igual forma que sean tanto de hombres como de mujeres.
#NOTA: aquellos que ya utilicen los condicionales pueden usarlos

# en este espacio declara las variables a utilizar y solicita los valores de entrada. te dejo 2 ejemplos:

# dejo ayudas de las funciones que se usaran, la primera funcion la resolveré pero las otras las completaran ustedes

#podemos usar esta función para incluir todas las demás funciones y que esta nos sirva para mostrarlas

print('//////    //\\\\    //     //////\n//       //  \\\\   //     //\n//      ////\\\\\\\\  //     //\n////// //      \\\\ ////// //////')
print('Esta calculadora esta diseñada para mostrarte tu indice de masa corporal dependiento tu estatura y peso.')
def init():
    res = input('Eres Hombre(h)(por defecto) o mujer(m)?:').lower()
    if res == 'h' or res == 'm' or res == '' :
        if res == '':
            res = 'h'
        return res
    else:
        init()


gener = init()
print('///////////////////////////////')
if gener == 'h':
    print('Calculando los valores para hombre.')

if gener == 'm':
    print('Calculando los valores para mujer.')
print('///////////////////////////////')

peso = int(input('Ingresa tu peso(Kl): '))
edad = int(input('Ingresa tu edad: '))
altura = int(input('Ingresa tu altura(cm): '))
tiempo = int(input('Duracion de la actividad(min): '))
print('Actividades disponibles: \n 1. Caminata \n 2. Tenis \n 3. Ciclismo \n 4. Carrera \n 5. Natacion ')
met = int(input('Ingresa el numero de la actividad: '))

if gener == 'h':
    cal.peso_ideal_h(altura)
    cal.quemando_calorias(tiempo,met,peso)
    cal.porc_gra_corp_h(edad,peso,altura)
    cal.ind_met_bas_h(peso,altura,edad)

if gener == 'm':
    cal.peso_ideal_m(altura)
    cal.quemando_calorias(tiempo,met,peso)
    cal.porc_gra_corp_m(edad,peso,altura)
    cal.ind_met_bas_m(peso,altura,edad)
