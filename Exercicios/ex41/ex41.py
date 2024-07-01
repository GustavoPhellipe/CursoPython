from datetime import date
ano_atual = date.today().year
Ano_de_nascimento = int(input('Ano de nascimento:'))
idade = ano_atual - Ano_de_nascimento
print('O atleta tem {} anos'.format(idade))
if idade > 25:
          print('CLASSIFICAÇÂO: MASTER')
elif idade > 19 and idade <= 25:
        print('CLASSIFICAÇÂO: SÊNIOR')
elif idade > 14 and idade <= 19:
        print('CLASSIFICAÇÂO: JUNIOR')
elif idade > 9 and idade <= 14:
        print('CLASSIFICAÇÂO: INFANTIL')
elif idade <= 9:
        print('CLASSIFICAÇÂO: MIRIM')