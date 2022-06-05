""" Programa Codificando el Mensaje
    Realiza codificación y decodificación 
    de mensajes
    incorpora al modulo csi.py
    Oscar Franco-Bedoya
       Abril-2022 """

#---------------- Zona librerias------------
import csi as sh

mensaje = input('Ingresa el mensaje a codificar: ')

codificado = sh.codificar_mensaje(mensaje)
print('El mensaje códificado es: ',codificado)

decodificado = sh.decodificar_mensaje(codificado)
print('El mensaje décodificado es: ',decodificado)


#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
