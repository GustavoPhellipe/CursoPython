from random import randint
from time import sleep
jogo = {'jogador 1': randint(1,6),
         'jogador 2': randint(1,6),
         'jogador 3': randint(1,6),
         'jogador 4': randint(1,6)}
ranking = list()
print('Valores:')
for jogador, valor in jogo.items():
          print('O {} tirou {} no dado'.format(jogador,valor))
          sleep(1.5)
ranking = sorted(jogo.items(), key=lambda x: x[1], reverse=True)
print('\nRANKING DOS JOGADORES:')
for i, (jogador, valor) in enumerate(ranking):
        print(f'{i+1} lugar: {jogador} com {valor}')