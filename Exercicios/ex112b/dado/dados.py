def leianumero(msg):
          válido = False
          while not válido:
            entrada = str(input(msg)).replace(',','.').strip()
            if entrada.isalpha() or entrada == '':
                  print('\033[0;31m[ERRO] Coloque o número corretamente! \033[m')
            else:
                  válido = True
                  return float(entrada)