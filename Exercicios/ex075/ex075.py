c = 0
num = (int(input('Digite um número:')),
int(input('Digite outro número:')),
int(input('Digite mais um número:')),
int(input('Digite último número:')))
if num != 9:
    c = c + 1
print('Você digitou os valores: {}'.format(num))
print('Existe(m) {} nove(s)'.format(num.count(9)))
if 3 not in num:
    print('[ERRO] O valor 3 n foi inserido!')
else:
    print('O valor 3 está na posição {}'.format(num.index(3)+1))