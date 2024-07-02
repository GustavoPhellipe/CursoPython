km = float(input('Quantos KM vc percorreu?'))
totkm = km * 0.15
dias = int(input('Quantos dias você ficou com o carro alugado?'))
totdia = dias * 60
total = totkm + totdia
print('O total a pagar é R${:.2f}'.format(total))