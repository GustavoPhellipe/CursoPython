def leiafloat(msg):
          válido = False
          while not válido:
                  entradafloat = str(input(msg)).strip()
                  if entradafloat.isalpha() or entradafloat == '':
                    print('\033[0;31m[ERRO] Digite um número REAL conforme pedido!\033[m')
                  else:
                    válido = True
                    return float(entradafloat)