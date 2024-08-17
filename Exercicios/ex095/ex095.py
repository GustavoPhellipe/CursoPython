'''# Lista para armazenar os dados dos jogadores
jogadores = []

while True:
    # Criação do dicionário para armazenar os dados do jogador atual
    jogador = {}
    
    jogador['nome'] = input('Digite o nome de algum jogador: ').strip()
    
    partidas = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou? '))
    gols = []
    
    for c in range(1, partidas + 1):
        gols.append(int(input(f'Quantos gols o jogador {jogador["nome"]} marcou na {c}ª partida? ')))
    
    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    
    jogadores.append(jogador)
    
    resp = input('Deseja continuar? [S/N] ').upper().strip()
    if resp == 'N':
        break
    elif resp != 'S':
        print('[ERRO] Digite S ou N.')

print('-=' * 30)
print('Relatório dos Jogadores:')
for jogador in jogadores:
    print(f'Jogador: {jogador["nome"]}')
    for i, gol in enumerate(jogador['gols'], start=1):
        print(f'   Partida {i}: {gol} gols')
    print(f'   Total de gols: {jogador["total"]}')
    print('-=' * 30)

while True:
    nome = input('Digite o nome do jogador que você deseja consultar: ').strip()
    jogador_encontrado = next((j for j in jogadores if j['nome'].lower() == nome.lower()), None)
    
    if jogador_encontrado:
        print(f'Jogador: {jogador_encontrado["nome"]}')
        for i, gol in enumerate(jogador_encontrado['gols'], start=1):
            print(f'   Partida {i}: {gol} gols')
        print(f'   Total de gols: {jogador_encontrado["total"]}')
        break
    else:
        print('Jogador não encontrado. Tente novamente.')'''

jogadores = list()
while True:
          jogador = dict()
          jogador['nomes'] = str(input('Nome do jogador:')).strip()
          partidas = int(input(f'Quantas partidas o jogador {jogador["nomes"]} jogou?'))
          gols = []
          for c in range(1,partidas+1):
                  gols.append(int(input('Quantos gols ele marcou na {}ª partida?'.format(c))))
          jogador['gols'] = gols
          jogador['total'] = sum(gols)

          jogadores.append(jogador)
          resp = str(input('Você deseja continuar? [S/N]')).upper().strip()
          if resp not in 'SN':
                  print('[ERRO] Digite S ou N!')
                  break
          elif resp in 'N':
                  break
print('-=' * 30)
print('Relatórios dos Jogadores')
for jogador in jogadores:
        print('Jogador: {}'.format(jogador["nomes"]))
        for i, gol in enumerate(jogador['gols'], start=1):
                print(f' {i}ª partida: {gol} Gols.')
        print('   Gol total é {}'.format(jogador['total']))
print('-=' * 30)
while True:
        nome = str(input('Digite o nome do jogador que você deseja consultar:')).strip()
        jogador_encontrado = next((j for j in jogadores if j["nomes"].lower() == nome.lower()), None)
        if jogador_encontrado:
                print(f'Jogador {jogador_encontrado["nomes"]}')
                for i, gol in enumerate(jogador_encontrado['gols'], start=1):
                        print(f'  Partida {i}: {gol} gols.')
                print(f'Total de gols: {jogador_encontrado['total']}')
                break
        else:
                print('Jogador não encontrado. Tente novamente.')