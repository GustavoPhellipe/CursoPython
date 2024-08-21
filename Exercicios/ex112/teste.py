from moeda import moeda
from dado import dados
'''while True:
 preço = str(input('Digite um valor:'))
 if preço.isnumeric():
  preço = float(preço)
  moeda.moeda_resumo(preço)
  break
 else:
  print('\033[0;31m[ERRO] Coloque o número corretamente! \033[m')'''

preço = dados.leiadinheiro('Digite um número:')
moeda.moeda_resumo(preço)