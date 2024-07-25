vitória = 0
while True:
          print('-=-' * 9)
          print('Jogo do Ímpar ou Par')
          print('-=-' * 9)
          import random
          escolha = str(input('Ímpar ou Par? [I/P]')).strip().upper()
          num = int(input('Digite um número [1 à 10]:'))
          if escolha != 'I' and escolha != 'P':
                   print('[ERRO] Coloque a escolha correta!')
          else:
              if num > 10 or num < 1:
               print('[ERRO] Coloque o número conforme pedido!')
              else:
               computador = random.randint(1,10)
               soma = num + computador
          print('Você escolheu o número {} e o computador {}. Total de {} é'.format(num,computador,soma),end=' ')
          if soma % 2 == 0:
                    print('Par')
          else:
           print('Ímpar')

          if escolha == 'P' and soma % 2 == 0 or escolha == 'I' and soma % 2 != 0:
                    print('-' * 50)
                    print('PARABÉNS! Você foi o vencedor!')
                    print('Vamos jogar novamente..')
                    vitória = vitória + 1
          else:
                print('-' * 50)
                print('O computador venceu! Tente novamente.')
                print('Você teve {} vitória(s)!'.format(vitória))
                break


