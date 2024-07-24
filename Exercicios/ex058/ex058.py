import random
from time import sleep
Computador = random.randint(1,11)
cont = 0
print('Computador: Olá, tudo bem? Vamos jogar um novo jogo de Adivinhação?')
sleep(4.5)
print('Computador: Começarei a "pensar" em um número de 1 à 10, e preciso q vc tente adivinhar o número q eu escolhi')
sleep(4.5)
print('Computador: Vamos lá!')
sleep(2)
num = int(input('Escolha um número:'))
while num != Computador:
    num = int(input('Computador: Número Errado! Tente adivinhar o número que eu pensei:'))
    cont += 1
print('PARABÉNS! Você conseguiu adivinhar o número {}!'.format(Computador))
print('Você fez {} tentativa(s)'.format(cont))