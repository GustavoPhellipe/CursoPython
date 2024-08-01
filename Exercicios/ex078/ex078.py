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

#Preste muita atenção nos destalhes da variável 'contador' no começo. Observe q ele está no índice zero, e ainda está na primeira repetição do programa (e não no último). O 'Valores[contador]', quer dizer que, o valor da lista está na posição do contador. Já que o contador é zero no começo, eu utilizo o: if contador == 0 --> "Se o contador for igual a zero", Ele receberá alguns códigos abaixo e depois será executado. Mas, o que estou tentando dizer? Bem, resumindo toda a minha explicação, o contador sempre começará em zero em qualquer linha de repetição.