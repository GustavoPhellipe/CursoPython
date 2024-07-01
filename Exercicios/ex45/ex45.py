from random import randint
from time import sleep
print( 20 * '-=-')
print('Escolha uma opção:')
print('[ 1 ] PEDRA')
print('[ 2 ] TESOURA')
print('[ 3 ] PAPEL')
jogada = int(input('Escolha um número para sua jogada:'))
print( 20 * '-=-')
computador = randint(1,3)
# Time duration
print('JON...')
sleep(2)
print('KEN...')
sleep(2)
print('PÔ!')
print( 20 * '-=-')
# Disputa
print('Você escolheu o número {} e o computador {}'.format(jogada, computador))
if jogada > 3 or jogada <= 0:
        print('[ERRO] Coloque o número da jogada correta!')
if jogada == computador:
          print('Que coincidência! Você e o computador tiraram a mesma jogada!')
elif jogada == 2 and computador == 1 or jogada == 3 and computador == 2 or jogada == 1 and computador == 3:
        print('O computador foi vencedor!')
elif jogada == 3 and computador == 1 or jogada == 2 and computador == 3 or jogada == 3 and computador == 1:
        print('PARABÉNS! Você foi o vencedor!')

