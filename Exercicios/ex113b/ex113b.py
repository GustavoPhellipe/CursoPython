def leiaint(msg):
 while True:
  try:
   valorint = int(input(msg))
  except (ValueError, TypeError):
   print('\033[0;31mPor favor, digite um número inteiro válido!\033[m')
   continue
  except KeyboardInterrupt:
   print('\033[0;31mO usuário preferiu não digitar esse número.\033[m')
   return 0
  else:
   return valorint
  

def leiafloat(msg):
 while True:
  try:
   valorfloat = float(input(msg))
  except (ValueError, TypeError):
   print('\033[0;31mPor favor, digite um número real válido!\033[m')
  except KeyboardInterrupt:
   print('\033[0;31mO usuário não preferiu digitar esse valor. \033[m')
   return 0
  else:
   return valorfloat
  
  
res = leiaint('Digite um número INTEIRO:')
res2 = leiafloat('Digite um número REAL:')
print(f'Você digitou um número inteiro {res} e o real {res2}')
