'''def ficha(jo,gol=0):
          if jogador in ' ':
                  print(f'O jogador <desconhecido> marcou {gol} gol(s) no campeonato.')
          else:
           print(f'O jogador {jogador} marcou {gols} gol(s) no campeonato.')

jogador = str(input('Nome do jogador:'))
gols = int(input('Números de gols:'))
ficha(jogador,gols)
'''
def ficha(jo='<<desconhecido>>',gol=0):
          print(f'O jogador {jo} marcou {gol} gol(s) no campeonato.')

jogador = str(input('Nome do jogador:'))
gols = str(input('Números de gols:'))
if gols.isnumeric():
        gols = int(gols)
else:
        gols = 0
if jogador == '':
        ficha(gol=gols)
else:
        ficha(jogador,gols)