tabuada = int(input('Digite um número para ver a tabuada:'))
for multiplicaçao in range(0, 11):
    soma = tabuada * multiplicaçao
    print('{} x {} = {}'.format(tabuada, multiplicaçao, soma))