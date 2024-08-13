from time import sleep
print('-=-' * 13)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-=-' * 13)
sorteio = int(input('Quantos jogos você quer que eu sorteie?'))
print('-' * 10, 'SORTEANDO {} JOGOS'.format(sorteio),end='')
print('-' * 10)
import random
jogos = list()
lista = list()
tot = 1 
while tot <= sorteio:
      cont = 0
      while True:
          num = random.randint(1,60)
          if num not in lista:
           lista.append(num)
           cont += 1
          if cont >= 6:
            break
      lista.sort()
      jogos.append(lista[:])
      lista.clear()
      tot += 1
for i, l in enumerate(jogos):
          print('JOGO {}: {}'.format(i+1,l))
          sleep(1.5)
