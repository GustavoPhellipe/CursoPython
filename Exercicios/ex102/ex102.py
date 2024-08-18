def fatorial(n,show=False):
          """
          --> Fatorial
          ;Para n: O número a ser calculado
          ;Para show: (Opcional) mostrar ou não o cálculo
          ;Return: O valor fatorial
          
          """
          soma = 1
          for c in range(n, 0, -1):
               if show:
                  print(c,end=' ')
                  if c > 1:
                          print('x ',end='')
                  else:
                         print('=',end=' ')
               soma *= c
          return soma
print(fatorial(5,show=True)) # False = Não mostra o cálcula; True = O contrário.
help(fatorial)