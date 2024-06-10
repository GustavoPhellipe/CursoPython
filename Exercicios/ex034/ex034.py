salário = float(input('Qual é seu salário?'))
if salário > 1250:
          aumento10 = ((salário / 100) * 10) + salário
          print('O seu salário vai ter um aumento de 10%, que vai passar a equivaler: R${:.2f}'.format(aumento10))

if salário <= 1250:
        aumento15 = ((salário / 100 ) * 15) + salário
        print('O seu salário vai ter um aumento de 15%, que vai passar a equivaler: R${:.2f}'.format(aumento15))