'''import random
num = (random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))
for c in (num):
    print('{}'.format(c),end= ' ')
print('\nO maior número: {}'.format(max(num)))
print('O menor número é: {}'.format(min(num)))
'''

import random
num = (random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))
ordem = sorted(num)
print(ordem)
print('O maior número é: {}'.format(ordem[4]))
print('O menor número é: {}'.format(ordem[0]))