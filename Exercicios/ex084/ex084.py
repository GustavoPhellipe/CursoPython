#COM LISTA
Lista = list()
Cadastro = list()
cont_cadastro = cont_peso_maior50 = cont_peso_menor50 = 0
while True:
          Cadastro.append(str(input('Digite seu nome:')).strip())
          cont_cadastro += 1
          peso = (float(input('Digite seu peso:')))
          Continuar = str(input('Quer continuar? [S/N]')).strip()
          if peso not in Lista:
                  Lista.append(peso)
          if peso >= 50:
                  cont_peso_maior50 += 1
          elif peso < 50:
                  cont_peso_menor50 += 1
          if Continuar not in 'SsNn':
                  print('[ERRO] Coloque a opção correta!')
                  break
          elif Continuar in 'Nn':
                  print('Ao todo, apenas {} pessoa(s) você cadastrou'.format(cont_cadastro))
                  print(f'{cont_peso_maior50} pessoa(s) acima do peso. O maior peso é {max(Lista)}Kg')
                  print(f'{cont_peso_menor50} pessoa(s) abaixo do peso. O menor peso é {min(Lista)}Kg')
                  break

#SEM LISTA
'''cont_cadastro = cont_peso_maior50 = cont_peso_menor50 = 0
while True:
          nome = (str(input('Digite seu nome:')).strip())
          cont_cadastro += 1
          peso = (float(input('Digite seu peso:')))
          Continuar = str(input('Quer continuar? [S/N]')).strip()
          if peso > 50:
                  cont_peso_maior50 += 1
          elif peso < 50:
                  cont_peso_menor50 += 1
          if Continuar not in 'SsNn':
                  print('[ERRO] Coloque a opção correta!')
                  break
          elif Continuar in 'Nn':
                  print('Apenas {} pessoa(s) se cadastrou(traram)'.format(cont_cadastro))
                  print('{} pessoa(s) acima do peso'.format(cont_peso_maior50))
                  print('{} pessoa(s) abaixo do peso'.format(cont_peso_menor50))
                  break'''