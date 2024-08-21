'''try:
          p = int(input('Valor:'))
          p2 = int(input('Valor2:'))
          s = p/p2
          print(s)
except:
        print('Ops.. deu algum problema.')
else:
        print('Tudo certo!')'''


'''try:
          p = int(input('Valor:'))
          p2 = int(input('Valor2:'))
          s = p/p2
          print(s)
except Exception as erro:
        print(f'Ops.. deu algum problema. O erro encontrado foi {erro.__class__}')
else:
        print('Tudo certo!')

'''

try:
          p = int(input('Valor:'))
          p2 = int(input('Valor2:'))
          s = p/p2
          print(s)
except (ValueError, TypeError):
        print('Ops.. tivemos algum problema.')
except ZeroDivisionError:
        print('Não é possível dividir um número por zero. Tente novamente!')
except KeyboardInterrupt:
        print('O usuário não preferiu informar os dados.')
else:
        print('Tudo certo!')
finally:
        print('Volte sempre!')
