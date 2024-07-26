print('-=-' * 5)
print('Banco Nacional')
print('-=-' * 5)
valor = int(input('Você quer sacar quanto?'))
cont = 0
cédula = 50
while True:
    if valor >= cédula:
        valor -= cédula
        cont += 1
    else:
        if cont > 0:
            print('{} cédula(s) de R${}'.format(cont,cédula))
        if cédula == 50:
            cédula = 20
            
        elif cédula == 20:
            cédula = 10
            
        elif cédula == 10:
            cédula = 1
        cont = 0
        if valor == 0:
            break