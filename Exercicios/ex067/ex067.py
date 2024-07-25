'''cont = 0
num = int(input('Você quer ver a tabuada de qual valor?'))
while True:
          cont += 1
          soma = num * cont
          print('{} x {} = {}'.format(num, cont, soma))
          if cont == 10:
                  break
          '''
cont = 0
while True:
          num = int(input('Digite um número para tabuada [0 para encerrar]:'))
          if num == 0:
                  break
          for cont in range(1,11):
                  soma = num * cont
                  print('{} x {} = {}'.format(num,cont,soma))
print('Programa Tabuada Encerrado!')