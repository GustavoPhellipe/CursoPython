Casa = float(input('Digite o valor da casa:'))
Salario = float(input('Digite o seu salário:'))
Anos = int(input('Até quantos anos você vai pagar a casa?'))
Prestação = Casa / (Anos * 12)
Mínimo = Salario * 30 / 100
print('Para pagar uma casa de R${} em {:.2f} anos, a prestação será de {:.2f}'.format(Casa, Anos, Prestação))
if(Prestação <= Mínimo):
          print('CONCEDIDA')

else:
        print('NÂO CONCEDIDA')
