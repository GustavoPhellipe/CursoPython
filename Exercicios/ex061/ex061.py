print('---' * 9)
print('Progressão Aritmética 2.0')
print('---' * 9)
Termo = int(input('Digite um número para o termo:'))
Razão = int(input('Digite um número para razão:'))
C = Termo
print('{}'.format(Termo), end=' --> ')
dezena = Termo + (10 - 1) * Razão

while C+1 < dezena:
 C += Razão
 print(C,end=' --> ')
print(' FIM')