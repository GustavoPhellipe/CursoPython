'''Lista = list()
Ímpares = list()
Pares = list()
for co in range(1,8):
          num = int(input('Digite o {}º número:'.format(co)))
          Lista.append(num)
          if num % 2 == 0:
                  Pares.append(num)
                  Pares.sort()
          else:
                  Ímpares.append(num)
                  Ímpares.sort()
          
print('Você digitou os valores: {}'.format(Lista))
print('Os valores Ímpares são: {}'.format(Ímpares))
print('Os valores Pares são: {}'.format(Pares))'''

Num = [[],[]]

for co in range(1,8):
          valor = int(input('Digite o {}º número:'.format(co)))
          if valor % 2 == 0:
                  Num[0].append(valor)
                  Num[0].sort()
          else:
                  Num[1].append(valor)
                  Num[1].sort()
          
print('Você digitou os valores: {}'.format(Num))
print('Os valores Ímpares são: {}'.format(Num[1]))
print('Os valores Pares são: {}'.format(Num[0]))