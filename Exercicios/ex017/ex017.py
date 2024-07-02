from math import sqrt
cateo = float(input('Digite o comprimento do cateto oposto: '))
catea = float(input('Digite o comprimento do cateto adjacente: '))
soma = (cateo ** 2) + (catea ** 2)
raiz = sqrt(soma)
print('A hipotenusa vai medir {:.1f}'.format(raiz))