import re

user = 'DavidG@=rado'

if(re.search('[0-9]', user)):
    print('hay numero')
else:
    print('No hay numero')

def  numero_codigo(codigo):
  num_codigo=(any(chr.isdigit() for chr in codigo))
  if num_codigo==False:
      print("Código valido, no tiene numero")
  else:
    print("Código Invalido. El código no puede tener número ")


numero_codigo(user)

