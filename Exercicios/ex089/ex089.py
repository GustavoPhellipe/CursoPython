cont = 0
Lista_alunos = list()
notas = list()
notas2 = list()
media = list()
while True:
          nome = str(input('Digite seu nome:')).strip()
          cont += 1
          if nome not in Lista_alunos:
           Lista_alunos.append(nome)
          nota_prova = float(input('Digite sua nota da primeira prova:'))
          nota_prova2 = float(input('Digite sua nota da segunda prova:'))
          media.append((nota_prova + nota_prova2) / 2)
          if nota_prova not in notas:
                  notas.append(nota_prova)
          if nota_prova2 not in notas2:
                  notas2.append(nota_prova2)

          if nota_prova > 10 or nota_prova2 > 10:
                  print('[ERRO] Você digitou uma nota acima do limite! Tente novamente.')
                  break
          else:
                  continuar = str(input('Você deseja continuar? [S/N]')).strip()
                  if continuar not in 'SsNn':
                          print('[ERRO] Digite a opção correta conforme acima.')
                          break
                  elif continuar in 'Nn':
                          print('-' * 33)
                          print('Nomes:',end='')
                          print(Lista_alunos)
                          print('Notas da primeira prova: {}'.format(notas))
                          print('Notas da segunda prova: {}'.format(notas2))
                          print('Médias: {}'.format(media))
                          print('-' * 33)
                          mostrar_notas = int(input('Você deseja ver a nota de qual aluno?'))
                          for i, no in enumerate(Lista_alunos):
                              if mostrar_notas == i:
                                      print(f'Nome: {Lista_alunos[mostrar_notas]}')
                                      print(f'Nota 1: {notas[mostrar_notas]}')
                                      print(f'Nota 2: {notas2[mostrar_notas]}')
                                      print(f'Media: {media[mostrar_notas]}')
                                      print('-' * 12)
                                      print('VOLTE SEMPRE!')
                                      print('-' * 12)
                              
                          break