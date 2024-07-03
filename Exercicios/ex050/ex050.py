soma = 0
cont = 0
for c in range(1, 6+1):
  num = int(input('Digite o {} valor:'.format(c)))
  if num % 2 == 0:
    soma = soma + num
    cont = cont + 1
print('Você informou {} valores pares. Os valores pares somados ficará no total: {}'.format(cont, soma))


    