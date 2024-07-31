'''for contador in range(0,5):
 valores.append(int(input('Digite um número:')))
valores.sort()
print(valores)
print('O maior número é {} na {} posição '.format(valores[4],valores.index(9)))
print('O menor número é: {}'.format(valores[0]))'''

valores = []
maior = menor = maiorp = menorp = 0
for contador in range(0,5):
 valores.append(int(input('Digite um número:')))
 if contador == 0:
   maior = valores[contador]
   menor = valores[contador]
 else:
  if valores[contador] > maior:
   maior = valores[contador]
  if valores[contador] < menor:
   menor = valores[contador]
print('O maior número é: {} na posição: '.format(maior),end='')
for pos, valor in enumerate(valores):
     if valor == maior:
       print('{}... '.format(pos),end='')
print()
print('O menor número é: {} na posição: '.format(menor),end='')
for pos, valor in enumerate(valores):
     if valor == menor:
       print('{}... '.format(pos),end='')
       print()