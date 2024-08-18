'''def leiaint(num):
        print('\033[0;32m Você digitou o valor {} \033[m'.format(num))
while True:
 núm = str(input('Digite um número:'))
 if núm.isnumeric():
          núm = int(núm)
          leiaint(núm)
          break
 else:
          print('\033[0;031m [ERRO] Digite um valor válido!\033[m')'''

def leiaint(num):
  ok = False
  valor = 0
  while True:
    n = str(input(num))
    if n.isnumeric():
      valor = int(n)
      ok = True
    else:
      print('\033[0;031m [ERRO] Digite um valor válido!\033[m')
    if ok:
     break
  return valor


n = leiaint('Digite um número:')
print(f'Você acabou de digitar o valor {n}')