parede = float(input('Qual seria a altura de sua parede?'))
largura = float(input('Qual é a largura?'))
área = parede * largura
tinta = área / 2
print('A área é {:.2f} e a quantidade necessária de tinta será {:.2f}'.format(área,tinta))