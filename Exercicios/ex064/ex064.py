n = 0
soma = 0
digi = 0
# Outra forma
# n = soma = digi = 0

while n != 999:
    num = int(input('Digite um número:'))
    if num != 999:
       digi = digi + 1
       soma = soma + num
    else:
       n = 999
print('Você digitou {} vez(es) e o número somado ao todo é: {}'.format(digi, soma))