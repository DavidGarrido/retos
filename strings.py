usuario = 'David alexander@ Garrido Hernandez'
encontrado = False
for i in range(len(usuario)):
    if usuario[i] == '@':
        encontrado = True
    if encontrado:
        print(i)
        break
