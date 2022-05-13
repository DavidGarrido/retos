#funcion 1 peso ideal de un hombre
def peso_ideal_h(altura):
    IBM = 56.2 + 1.41*(altura / 2.54 -60)

    print('Tu peso ideal es: ', round(IBM,2), 'kl')

#peso ideal de una mujer
def peso_ideal_m(altura):
    IBM =  53.1 +1.36 *(altura /2.54 -60)

    print('Tu peso ideal es: ', round(IBM,2), 'Kl')

#quemando calorías en hombre
def quemando_calorias(tiempo,met,peso):
    valor_met = 0
    if met == 1:
        valor_met = 2
    if met == 2:
        valor_met = 5
    if met == 3:
        valor_met = 14
    if met == 4:
        valor_met = 6
    if met == 5:
        valor_met = 9.8
    calorias_quemadas =  (tiempo * valor_met * peso ) /200

    print('Has quemado ', round(calorias_quemadas, 2), ' calorias.')


#porcentaje de grasa corporal hombre adulto
def porc_gra_corp_h(edad,peso,altura):
    #TODO: aquí hay que usar las variables que   solicitamos, peso y altura para calcular el IMC-- convertir de cm a metros la altura divide los centímetros entre 100
    metros = altura/100
    IMC = peso/metros
    hombre_adulto=  1.20 * IMC + 0.23 * edad - 16.2
    print('Tu porcentaje de grasa corporal es: ', round(hombre_adulto,2))

#porcentaje de grasa corporal mujer adulta  
def porc_gra_corp_m(edad,peso,altura):
    #TODO: aquí hay que usar las variables que   solicitamos, peso y altura para calcular el IMC -- convertir de cm a metros la altura divide los centímetros entre 100
    metros = altura/100
    IMC = peso/metros
    mujer_adulta=  1.20 * IMC + 0.23 * edad - 5.4
    print('Tu porcentaje de grasa corporal es: ', round(mujer_adulta,2))


#índice Metabólico Basal Hombres
def ind_met_bas_h(peso,altura,edad):
    p= peso
    a= altura
    e= edad

    hombre= p + a + e + 88.362
    print('Tu índice metabólico basal es: ', round(hombre,2))

#índice Metabólico Basal Mujeres
def ind_met_bas_m(peso,altura,edad):
    p= peso
    a= altura
    e= edad

    mujer= p + a + e +447.593
    print('Tu índice metabólico basal es: ', round(mujer,2))



