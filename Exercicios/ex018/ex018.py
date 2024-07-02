import math
ângulo = float(input('Digite o ângulo que você deseja:'))
seno = math.sin(math.radians(ângulo))
print('O ângulo {} tem Seno de: {:.2f}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O ângulo {} tem Cosseno de: {:.2f}'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('O ângulo {} tem Tangente de: {:.2f}'.format(ângulo, tangente))