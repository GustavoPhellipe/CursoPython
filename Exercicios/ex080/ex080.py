
'''valores = list()
for c in range(0,5):
        num = int(input('Digite um número:'))
        if num not in valores:
             valores.append(num)
             valores.sort()
        else:
             print('Número repetido! Adicione outro número!')
          
print(valores)'''

#SEM SORT()
valores = list()
for c in range(0,5):
        num = int(input(f'Digite um número:'))
        if c == 0 or num > valores[-1]:
              valores.append(num)
        else:
              pos = 0
              while pos < len(valores):
                    if num <= valores[pos]:
                          valores.insert(pos,num)
                          break
                    pos += 1
                    
print('Valores em ordem crescente: {}'.format(valores))


