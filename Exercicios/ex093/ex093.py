'''Futebol = dict()
Gols = list()
cont = 0
Futebol['jogador'] = str(input('Digite o nome de um jogador:')).strip()
for n in range(1,5):
          Gol = int(input('Quantos gols o jogador {} marcou na partida {}?'.format(Futebol['jogador'], n)))
          Gols.append(Gol)
          cont = cont + Gol
print('-=-' * 14)
for k, v in enumerate(Gols):
 print(f'{k+1}º Partida: {Gols[k]}')
print('O jogador {} marcou no total {} gols.'.format(Futebol['jogador'],cont))
print('-=-' * 14)'''

Futebol = dict()
Gols = list()
cont = 0
Futebol['jogador'] = str(input('Digite o nome de um jogador:')).strip()
Partidas = int(input('Quantas partidas o jogador {} jogou?'.format(Futebol['jogador'])))
for n in range(0+1,Partidas + 1):
          Gol = int(input('Quantos gols o jogador {} marcou na partida {}?'.format(Futebol['jogador'], n)))
          Gols.append(Gol)
          cont = cont + Gol
print('-=-' * 15)
for k, v in enumerate(Gols):
 print(f'{k+1}º Partida: {Gols[k]}')
print('O(A) jogador(a) {} marcou no total {} gols.'.format(Futebol['jogador'],cont))
print('-=-' * 15)