from datetime import date
ano = int(input('Que ano você quer que eu analise? Caso queira saber o ano atual, digite 0:'))
if ano == 0:
          ano = date.today().year
          print(ano)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print('O ano {} é BISSEXTO!'.format(ano))
else:
        print('O ano {} não é BISSEXTO!'.format(ano))