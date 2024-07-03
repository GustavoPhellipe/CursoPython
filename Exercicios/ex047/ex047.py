num = int(input('Digite o primeiro número:'))
numf = int(input('Digite o número final:'))
nump = int(input('Digite um número que ficará pulando em um valor que você escolheu:'))
for c in range(num, numf+1, nump):
    print(c, end=' ')
print('FIM!')