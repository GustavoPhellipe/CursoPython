'''
num = [1,5,8,3,2]
num[1] = 4
num.append(7)
num.insert(0,2)
num.sort()
num.pop()
print(num)
'''

'''valores = list()
for contador in range(0,5):
    valores.append(int(input('Digite um número:')))
for índice, valor in enumerate(valores):
    print('Na posição {} encontrei o valor {}'.format(índice,valor))
'''

a = [2,6,8,3]
cópia = a[:]
cópia[2] = 1
print('LISTA A: {}'.format(a))
print('LISTA DE CÓPIA: {}'.format(cópia))