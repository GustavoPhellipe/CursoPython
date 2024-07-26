while True:
          print('-' * 19)
          print('Cadastre uma Pessoa')
          print('-' * 19)
          nome = str(input('Digite o nome:')).strip()
          idade = int(input('Digite sua idade:'))
          sexo = str(input('Digite seu sexo [M/F]:')).strip().upper()
          conth = contf = 0
          if sexo != 'M' and sexo != 'F':
                    print('[ERRO] Coloque o sexo correto!')
                    break
          else:
           continuação = str(input('Quer continuar? [S/N]')).strip().upper()

          if sexo == 'F':
                  contf += 1
          elif sexo == 'M':
                  conth += 1

          if continuação not in 'SsNn':
                    print('[ERRO] Coloque a opção correta!')
                    break
          elif continuação == 'N':
                  break
          if idade 
