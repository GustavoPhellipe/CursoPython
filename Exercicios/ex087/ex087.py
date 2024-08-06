matriz = [[0,0,0],[0,0,0], [0,0,0]]
soma = somap = maior = 0
for linha in range(0,3):
          for coluna in range(0,3):
                  matriz[linha][coluna] = int(input('Digite um número para [{}][{}]'.format(linha,coluna)))
for linha in range(0,3):
        for coluna in range(0,3):
                print(f'[{matriz[linha][coluna]:^5}]',end='')
                if matriz[linha][coluna] % 2 == 0:
                 somap = somap + matriz[linha][coluna]
print('\nOs valores Pares calculados é: {}'.format(somap))
for p in range(0,3):
                soma = soma + matriz[coluna][2]
print('A terceira linha total é: {}'.format(soma))

for c in range(0,3):
 if c == 0:
        maior = matriz[1][c]
 else:
        if matriz[1][c] > maior:
                maior = matriz[1][c]
print('O maior valor na segunda linha é: {}'.format(maior))