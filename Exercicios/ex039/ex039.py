# Alistamento
from datetime import date
ano_atual = date.today().year
nascimento = int(input('Ano de nascimento:'))
idade = ano_atual - nascimento
print('Quem nasceu em {} tem {} anos em {} '.format(nascimento, idade, ano_atual))
if idade == 18:
          print('Você pode se alistar no exército!')

elif nascimento >=  ano_atual:
        print('Ano de Nascimento inválido!')

elif idade < 18:
        anos_listamento = 18 - idade
        listamento = anos_listamento + ano_atual
        print('Falta(m) apenas {} ano(s) para o alistamento no exército'.format(anos_listamento))
        print('O alistamento será no ano {}'.format(listamento))

elif idade > 18:
        print('Você já deveria ter se alistado á muito tempo!')
