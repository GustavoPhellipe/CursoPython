def leiaint(msg):
          válido = False
          while not válido:
                  entradaint = str(input(msg)).strip()
                  if entradaint.isalpha() or entradaint == '' or entradaint == ValueError:
                    print('\033[0;31m[ERRO] Digite um número INTEIRO conforme pedido!\033[m')
                  else:
                    válido = True
                    return int(entradaint)