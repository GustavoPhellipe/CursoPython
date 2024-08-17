números = []
númerosPares = []
somapares = 0
from time import sleep
import random
def sorteia(números):
        print('Sorteando 5 valores da lista:',end=' ',flush=True)
        print(números)
def somaPar(números):
        global somapares
        for número in números:
         if número % 2 == 0:
                númerosPares.append(número)
                somapares += número
                sleep(0.5)
        print('Os valores pares são: {}'.format(númerosPares))
        sleep(1)
        print('A soma total dos valores pares é: {}'.format(somapares))
for valor in range(0,5):
          sortear = random.randint(1,10)
          números.append(sortear)
sorteia(números)
somaPar(números)