from inteiro import leiainteiro
from real import leiareal
while True:
 try:
  valorint = leiainteiro.leiaint('Digite um número inteiro:')
 except Exception as error:
     print(f'\033[0;31m[ERROR] Você informou o dado errado. Tente novamente. Error: {error.__class__}\033[m')
     break
 else: 
     valorfloat = leiareal.leiafloat('Digite um número real:')
     print(f'O valor digitado inteiro foi {valorint} e o real {valorfloat}')
     break