'''def soma(a,b):
          print(f'A = {a} B = {b}')
          s = a + b
          print(f'A soma entre A e B é {s}')
          print('-' * 11)

soma(3,5)
soma(9,17)
soma(43,29)'''

def contador(*num):
          tam = len(num)
          print(f'Os valores {num} tem a quantidade de {tam} dígitos')


contador(1,2,5,9)
contador(8,2,7,3)