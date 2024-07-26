cont_ma = cont_fe = cont_idade = cont_idade_baixa = 0
while True:
          print('-' * 19)
          print('Cadastre uma Pessoa')
          print('-' * 19)
          idade = int(input('Digite sua idade:'))
          sexo = ' '
          if idade >= 18:
                 cont_idade = cont_idade + 1
          elif idade < 18:
                 cont_idade_baixa += 1
                 
          while sexo not in 'MF':
                  sexo = str(input('Digite seu sexo [M/F]:')).strip().upper()

          if sexo == 'F':
                  cont_fe += 1
          elif sexo == 'M':
                  cont_ma += 1

          continuação = ' '
          while continuação not in 'SsNn':
                  continuação = str(input('Quer continuar? [S/N]')).strip().upper()

          if continuação == 'N':
                  break
print('Ao todo temos {} pessoa(s) de maior de idade e {} pessoa(s) de menor idade'.format(cont_idade, cont_idade_baixa))
print('{} pessoa(s) Masculina(s) fez(fizeram) o cadastro'.format(cont_ma))
print('{} pessoa(s) Feminina(s) fez(fizeram) o cadastro'.format(cont_fe))

'''if sexo != 'M' and sexo != 'F':
                print('[ERRO] Coloque o sexo correto!')
                break'''