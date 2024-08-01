'''
lista = list()
cp = ci = 0
while True:
          num = int(input('Digite um número:'))
          if num not in lista:
                  lista.append(num)
          else:
                  print('[ERRO] Você já repetiu o número! Digite outro.')
          continuação = str(input('Você deseja continuar? [S/N]')).strip()
          if num % 2 == 0:
                  cp += 1
          elif num % 2 != 0:
                  ci += 1
          if continuação not in 'SsNn':
                  print('[ERRO] Coloque a opção correta!')
                  break
          elif continuação in 'Nn':
                  print('Os valores são: {}'.format(lista))
                  print('Existe(m) {} valor(es) Par(es)!'.format(cp))
                  print('Existe(m) {} valor(es) Ímpar(s)!'.format(ci))
                  break
'''

lista = list()
pares = list()
ímpares = list()
while True:
          num = int(input('Digite um número:'))
          if num not in lista:
                  lista.append(num)
          else:
                  print('Número duplicado! Não irei adicioná-lo!')
          res = str(input('Você deseja continuar: [S/N]'))
          if num % 2 == 0:
                  pares.append(num)
          elif num % 2 == 1:
                  ímpares.append(num)
          if res not in 'SsNn':
                  print('[ERRO] Digite a opção correta!')
                  break
          elif res in 'Nn':
                  print('Os valores são: {}'.format(lista))
                  print('Os valores pares são: {}'.format(pares))
                  print('Os valores ímpares são: {}'.format(ímpares))
                  break
