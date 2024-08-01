valores = list()
c = 0
while True:
          num = int(input(('Digite um número:')))
          if num not in valores:
                  valores.append(num)
                  valores.sort(reverse=True)
                  c += 1
          else:
                  print('Número repetido! Não irei adicioná-lo!')
          continuação = str(input('Você quer continuar? [S/N]'))

          if continuação not in 'SsNn':
                  print('[ERRO] Coloque a opção correta!')
                  break
          elif continuação in 'Nn':
                  print('Você digitou {} elementos'.format(c))
                  print('Os valores são: {}'.format(valores))
                  if 5 in valores:
                   print('O valor 5 foi encontrado! Ele está na posição: {}'.format(valores.index(5)))
                  else:
                   print('O valor 5 n foi encontrado na lista!')
                  break