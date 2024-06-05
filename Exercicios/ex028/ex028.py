import random
num = int(input('Digite um número de 0 a 5:'))
print('Aguardando...')
aleatório = random.randint(0, 5)
if aleatório == num:
          print('O computador escolheu o número: {}'.format(aleatório))
          print('O computador foi o vencedor! Tente na próxima!')
else:
        print('Você escolheu o número {} e o computador número {}'.format(num, aleatório))
        print('PARABÉNS! Você venceu!')