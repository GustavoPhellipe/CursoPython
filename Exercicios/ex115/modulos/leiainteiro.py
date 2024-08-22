def leiaint(msg):
          while True:
                  try:
                   leiaint = int(input(msg))
                  except (ValueError, TypeError):
                        print('\033[0;31mPor favor, digite a opção válida!\033[m')
                  except KeyboardInterrupt:
                        print('\033[0;31mO usuário não digitou nenhum número.\033[m')
                  else:
                        return leiaint
