dados = dict()
dados_lista = list()

nome = str(input('Nome:'))
media = float(input('Média:'))
if nome not in dados_lista:
          dados_lista.append(nome)
if media not in dados_lista:
        dados_lista.append(media)

dados = {'nome':nome,'media':media}

print(' - Nome é igual a {}'.format(dados['nome']))
print(' - Média é igual a {}'.format(dados['media']))
if media <= 5:
        print('Situação é igual a Reprovado.')
else:
        print(' - Situação é igual a Aprovado.')