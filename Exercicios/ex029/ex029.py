vel = float(input('Qual seria a velocidade de seu carro?'))
print('Aguarde...')
if vel > 80:
          soma = ((vel - 80) * 7)
          print('Você vai pagar uma multa de R$7.00 por ter percorrido a velocidade acima de 80km!')
          print('Sua multa será de: R${:.2f}'.format(soma))
else:
        print('Tudo ok... Pode continuar com a sua viagem!')