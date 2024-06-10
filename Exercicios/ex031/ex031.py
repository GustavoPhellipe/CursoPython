distancia = float(input('Digite a distância de sua viagem:'))
print('A sua viagem vai ser de {}km'.format(distancia))
if distancia <= 200:
          passagem = distancia * 0.50
          print('Sua passagem será de {:.2f}'.format(passagem))
else: 
        passagemlonga = distancia * 0.45
        print('Sua passagem custará apenas R${:.2f}'.format(passagemlonga))