""" Modulo para la codificación y decodificación de
    mensajes 
    Oscar Franco-Bedoya
    Abril-2022 """

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------

cadena_original = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cadena_interpretada = "DEFGHIJKLMNOPQRSTUVWXYZABC"

def codificar_mensaje(mensaje_original):
    mensaje_final = ''
    for i in range(len(mensaje_original)):
        caracter = mensaje_original[i].upper()
        if caracter != ' ':
            posicion = cadena_original.index(caracter)
            resultado = cadena_interpretada[posicion]
            mensaje_final += resultado
        else:
            mensaje_final += ' '
    return mensaje_final

def decodificar_mensaje(mensaje_codificado):
    mensaje_original = ''
    for i in range(len(mensaje_codificado)):
        caracter = mensaje_codificado[i].upper()
        if caracter != ' ':
            posicion = cadena_interpretada.index(caracter)
            resultado = cadena_original[posicion]
            mensaje_original += resultado
        else:
            mensaje_original += ' '
    return mensaje_original
