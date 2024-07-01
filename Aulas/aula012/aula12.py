nome = str(input('Digite seu nome:')).strip()
if nome == 'Gustavo':
          print('Olá, {}! Seu nome é bem bonito..'.format(nome))

elif nome == 'Pedro' or nome == 'Maria' or nome == 'Eduardo':
        print('Bom dia, {}! Seu nome é bem popular'.format(nome))

elif nome in 'Ana Clara de Souza':
        print('Seu nome (ou sobrenome) é mais usado no Brasil!')
else:
        print('Olá, seja muito bem-vindo(a), {}!'.format(nome))