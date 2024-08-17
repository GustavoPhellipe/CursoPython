'''from random import randint
from time import sleep
Valores = list()

print('-=-' * 12)
print('Analisando os valores passados:')
for valores in range(0,4):
          alea = randint(1,10)
          Valores.append(alea)
          print(f'{alea}',end=' ')
print('Temos informado ao todo {}'.format(valores+1))
print('O maior valor entre eles é o valor {}'.format(max(Valores)))
print('-=-' * 12,end='')


print('-=-' * 12)
print('Analisando os valores passados:')
for valores in range(0,6):
          aleat = randint(1,10)
          Valores.append(aleat)
          print(f'{aleat}',end=' ')
print('Temos informado ao todo {}'.format(valores+1))
print('O maior valor entre eles é o valor {}'.format(max(Valores)))
print('-=-' * 12,end='')


print('-=-' * 12)
print('Analisando os valores passados:')
for valores in range(0,3):
          aleat = randint(1,10)
          Valores.append(aleat)
          print(f'{aleat}',end=' ')
print('Temos informado ao todo {}'.format(valores+1))
print('O maior valor entre eles é o valor {}'.format(max(Valores)))
print('-=-' * 12,end='')

'''
'''
from random import randint, sample
from time import sleep
Valores = list()

def maior(valores):
        print('\nO maior valor é {}'.format(max(valores)),end='')
for rep in range(3):
 print('-=-' * 12)
 print('Analisando os valores passados:')
 for_aleatório = randint(1, 8)
 
 for valor in range():
  print('Temos informado {} números dígito(s)'.format(for_aleatório))
 print('-=-' * 12,end='')
 maior(valores_unicos)
 print()
'''
from time import sleep
from random import randint

def maior(valores):
    print('\nO maior valor é {}'.format(max(valores)), end='')

for rep in range(3):
    print('-=-' * 12)
    print('Analisando os valores passados:')
    Valores = []
    
    for_aleatório = randint(1, 8)  # Move a definição de for_aleatório para dentro do loop
    
    for valores in range(for_aleatório):
        alea = randint(1, 10)
        Valores.append(alea)
        print(f'{alea}', end=' ',flush=True) # Utilize o flush para que o sleep possa funcionar
        sleep(0.5)
    
    print('\nForam informados ao todo {} valores'.format(for_aleatório))
    print('-=-' * 12, end='')
    
    maior(Valores)
    print()