galera = list()
pessoa = dict()
soma = media = cont = 0
while True:
          pessoa.clear()
          pessoa['nome'] = str(input('Digite seu nome:')).strip()
          cont += 1
          while True:
                  pessoa['sexo'] = str(input('Digite seu sexo:')).upper().strip()
                  if pessoa['sexo'] in 'MF':
                     break
                  print('[ERRO] Digite M ou F!')
          pessoa['idade'] = int(input('Digite sua idade:'))
          soma += pessoa['idade']
          galera.append(pessoa.copy())
          while True:
                  resp = str(input('Você deseja continuar? [S/N]')).upper().strip()
                  if resp in 'SN':
                     break
                  print('[ERRO] Digite S ou N')
          if resp in 'N':
             break
print('A) Ao todo, temos {} pessoa(s) cadastrada(s)'.format(cont))
media = soma / cont
print('B) A média de idade é {} '.format(media))
print('C) As mulheres cadastradas são: ',end='')
for p in galera:
      if p['sexo'] in 'Ff':
            print(f'{p["sexo"]}',end='')
print()
print('D) As pessoas que ficaram na média foram:')
for p in galera:
      if p['idade'] >= media:
            print(' ',end='')
            for k, v in p.items():
                  print(f'{k} = {v};',end='')
                  print()
print('<< ENCERRADO >>')

'''Dicionário = dict()
Lista = list()
pessoas_acima_media = list()
cont_cadastro = media_valor = 0
while True:

        Dicionário['nome'] = str(input('Digite seu nome:')).strip()
        Dicionário['sexo'] = str(input('Coloque o seu Sexo [M/F]:')).strip()
        cont_cadastro += 1
        if Dicionário['sexo'] in 'Ff':
                feminino = Dicionário['nome']
                Lista.append(feminino)
        if Dicionário['sexo'] not in 'MmFf':
                print('[ERRO] Digite o sexo correto!')
                break
        else:
                Dicionário['idade'] = int(input('Digite sua idade:'))
                media_valor += Dicionário['idade']
                media = media_valor / cont_cadastro
                if Dicionário['idade'] >= media:
                        pessoas = Dicionário['nome']
                        pessoas_acima_media.append(pessoas)
                Dicionário['continuação'] = str(input('Você deseja continuar? [S/N]')).strip()
                if Dicionário['continuação'] not in 'SsNn':
                        print('[ERRO] Coloque a opção conforme desejado.')
                        break
                elif Dicionário['continuação'] in 'Nn':
                        print('A) Ao todo, temos {} pessoa(s) cadastrada(s).'.format(cont_cadastro))
                        print('B) A média de idade é {}'.format(media))
                        print('C) As mulheres que se cadastraram foram: {}'.format(Lista))
                        print('D) As pessoas que conseguiram ficar acima da media ({}) foram: {}'.format(media, pessoas_acima_media))
                        break
'''