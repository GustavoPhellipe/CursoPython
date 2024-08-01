'''
valores = []
while True:
          valor = int(input('Digite um número:'))
          if valor not in valores:
             valores.append(valor)
             print('Número adicionado com sucesso!')
          else:
            print('Número repetido! Não irei adicioná-lo!')

          continuar = str(input('Quer continuar? [S/N]')).strip()
          if continuar not in 'SsNn':
                  print('[ERRO] Coloque a opção correta!')
                  break
          elif continuar in 'Nn':
                  print('Você digitou o(s) valor(es): {}'.format(valores))
                  break
'''
valores = list()
while True:
          num = int(input('Digite um número:'))
          if num not in valores:
                  valores.append(num)
                  print('Valor adicionado com sucesso!')
          else:
                  print('Número duplicado! Não irei adicioná-lo!')
          continuaçao = str(input('Quer continuar? [S/N]'))
          if continuaçao not in 'SsNn':
                  print('[ERRO] Digite a opção correta!')
                  break
          elif continuaçao in 'Nn':
                  valores.sort()
                  print('Os valores adicionados foram: {}'.format(valores))
                  break