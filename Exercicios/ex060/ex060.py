from time import sleep
print('Calculadora Fatorial')
cont = 0
fatorial = 1
Maiorf = 0
numf = int(input('Digite um número:'))
print('Calculando...')
sleep(2.5)

while cont < numf:
    cont = cont + 1
    fatorial = fatorial * cont
    if cont > numf:
        Maiorf = fatorial
    else:
        if fatorial > Maiorf:
            Maiorf = fatorial

print('O fatorial de {} é {}'.format(numf,Maiorf))

