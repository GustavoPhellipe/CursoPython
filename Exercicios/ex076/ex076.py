print('-=-' * 10)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-=-' * 10)
materias = ('Mochila', 79.99, 'Estojo', 24.99, 'Caderno', 49.99, 'Lápis', 1.99, 'Caneta', 2.99, 'Borracha', 2.50, 'Apontador', 3.50, 'Agenda', 29.99)
for pos in range(0, len(materias)):
          if pos %  2 == 0:
                  print('{}'.format(materias[pos]),end='.................. ')
          else:
                  print('R${:.2f}'.format(materias[pos]))
'''
print('{}.................. R${}'.format(materias[0],valor_materias[0]))
print('{}.................. R${}'.format(materias[1],valor_materias[1]))
print('{}.................. R${}'.format(materias[2],valor_materias[2]))
print('{}.................. R${}'.format(materias[3],valor_materias[3]))
print('{}.................. R${}'.format(materias[4],valor_materias[4]))
print('{}.................. R${}'.format(materias[5],valor_materias[5]))
print('{}.................. R${}'.format(materias[6],valor_materias[6]))
print('{}.................. R${}'.format(materias[7],valor_materias[7]))
'''
'''
print('{}.................. R$79.99'.format(materias[0]))
print('{}.................. R$24.99'.format(materias[1]))
print('{}.................. R$49.99'.format(materias[2]))
print('{}.................. R$1.99'.format(materias[3]))
print('{}.................. R$2.99'.format(materias[4]))
print('{}.................. R$1.59'.format(materias[5]))
print('{}.................. R$3.49'.format(materias[6]))
print('{}.................. R$29.99'.format(materias[7]))
'''