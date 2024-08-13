from datetime import datetime
data_ano = datetime.now().year
Dados = {'nome': str(input('Digite seu nome:' )).strip(), 'idade':int(input('Digite seu ano de nascimento:')), 'carteira':int(input('Carteira de trabalho: [Digite 0 caso não tenha]'))}
valor_idade = data_ano - Dados['idade']
if Dados['carteira'] == 0:
          print('Seu nome é {}.'.format(Dados['nome']))
          print('Sua idade é {} anos.'.format(valor_idade))
          print('-=-' * 9)
          print(f'{"VOLTE SEMPRE!":^27}')
          print('-=-' * 9)
else:
        Dados_carteira = {'contratação':int(input('Digite o ano de sua contratação:')), 'salário':int(input('Digite seu salário: R$'))}
        print('Seu nome é {}.'.format(Dados['nome']))
        print('Sua idade é {} anos.'.format(valor_idade))
        print('Seu número de carteira de trabalho é {}.'.format(Dados['carteira']))
        print('O ano de sua contratação foi em {}.'.format(Dados_carteira['contratação']))
        print('Seu salário é de R${}.'.format(Dados_carteira['salário']))
        Aposentadoria = ((valor_idade + Dados_carteira['contratação']) + 35) - data_ano
        print('A sua aposentadoria será com {} anos.'.format(Aposentadoria))