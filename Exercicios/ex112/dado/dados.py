def leiadinheiro(msg):
          válido = False
          while not válido:
                  entrada = str(input(msg)).replace(',','.')
                  if entrada.isalpha() or entrada.strip() == '':
                        print('[ERRO] Coloque o número corretamente!')
                  else:
                        válido = True
                        return float(entrada)
                  