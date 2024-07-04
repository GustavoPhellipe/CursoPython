maior = 0
menor = 0
for p in range(1,7):
    peso = float(input('Digite o peso da {}ª pessoa (entre 10kg á 150kg):'.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior número é: {}Kg'.format(maior))
print('O menor número é: {}Kg'.format(menor))