import datetime
ano_atual = datetime.datetime.today().year
total_pessoas = 0
total2_pessoas = 0
for repetição in range(1,8):
  ano_nascimento = int(input('Em que ano a {}ª pessoa nasceu?'.format(repetição)))
  idade = ano_atual - ano_nascimento
  if idade >= 18:
    total_pessoas = total_pessoas + 1
  else:
    total2_pessoas = total2_pessoas + 1
print('Ao todo temos {} pessoas de maior idade!'.format(total_pessoas))
print('Ao todo tivemos {} pessoas de menor idade!'.format(total2_pessoas))