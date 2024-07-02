peso = float(input('Qual é seu peso? (Kg)'))
altura = float(input('Qual é sua altura? (m)'))
peso_corporal = peso / altura
print('O IMC dessa pessoa é {:.1f}'.format(peso_corporal)) 
if peso_corporal <= 18.5:
          print('Baixo Peso')
elif peso_corporal > 18.5 and peso_corporal <= 24.9:
          print('Peso Normal')
elif peso_corporal > 25 and peso_corporal <= 29.9:
 print('Excesso de peso')
elif peso_corporal == 30:
        print('OBESIDADE')
elif peso_corporal > 30 and peso_corporal <= 34.9:
        print('OBESIDADE GRAU 1')
elif peso_corporal > 35 and peso_corporal <= 39.9:
        print('OBESIDADE GRAU 2')
elif peso_corporal >= 40:
        print('OBESIDADE GRAU 3')