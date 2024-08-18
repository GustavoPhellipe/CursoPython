'''print('-=-' * 8)
print(F'{"FUNÇÕES PARA VOTAÇÃO":^24}')
print('-=-' * 8)
from datetime import datetime
ano_atual = datetime.now().year
def votação(idade):
          idade = ano_atual - ano_nascimento
          if idade >= 18:
                  print('VOTO OPCIONAL.')
          else:
                  print('VOTO NÂO OBRIGATÓRIO.')
ano_nascimento = int(input('Digite seu ano de nascimento:'))
votação(ano_nascimento)
'''

print('-=-' * 8)
print(F'{"FUNÇÕES PARA VOTAÇÃO":^24}')
print('-=-' * 8)
from datetime import datetime
ano_atual = datetime.now().year
def votação(idade):
          idade = ano_atual - ano_nascimento
          if idade >= 18:
                  print('VOTO OPCIONAL.')
                  return idade
          else:
                  print('VOTO NÂO OBRIGATÓRIO.')
                  return idade
ano_nascimento = int(input('Digite seu ano de nascimento:'))
r1 = votação(ano_nascimento)
print('A sua idade é de {} anos'.format(r1))