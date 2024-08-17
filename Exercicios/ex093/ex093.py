'''jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador:')).strip()
tot = int(input('Quantas partidas ele jogou?'))
for c in range (0,tot):
          partidas.append( int(input(f'Quantos gols na partida {c}?')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=-' * 30)
print(jogador)
print('-=-' * 30)
for k, v in jogador.items():
        print(f'O campo {k} tem o valor {v}.')
print('-=-' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
        print(f'   => Na partida {i}, fez {v} gols')
print(f'O total de gols foram {jogador["total"]}')'''

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