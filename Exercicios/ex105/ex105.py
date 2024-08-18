'''números = dict()
def notas(nota, nota2,nota3):
          print(f'A quantidade de notas é {nota}, {nota2}, {nota3}')
          if nota > nota2 and nota > nota3:
                  print(f'O maior valor é {nota}')
          elif nota2 > nota and nota2 > nota3:
                  print(f'O maior valor é {nota2}')
          elif nota3 > nota2 and nota3 > nota:
                  print(f'O maior valor é {nota3}')
          if nota < nota2 and nota < nota3:
                  print(f'O menor valor é {nota}')
          elif nota2 < nota and nota2 < nota3:
                  print(f'O menor valor é {nota2}')
          elif nota3 < nota2 and nota3 < nota:
                  print(f'O menor valor é {nota3}')
          s = (nota + nota2 + nota3) / 3
          print(f'A média da turma é de {s}')
          if s  >= 7:
                  print('MUITO BOM!')
          elif s >= 5 and s < 6.9:
                  print('BOM!')
          else:
                  print('RUIM!')
notas(10,10,10)
'''


def notas(*num, sit=False):
          r = dict()
          r['total'] = len(num)
          r['maior'] = max(num)
          r['menor'] = min(num)
          r['média'] = sum(num)/len(num)
          if sit:
                  if r['média'] >= 7:
                          r['situação'] = 'MUITO BOM!'
                  elif r['média'] >= 5 and r['média'] < 6.9:
                          r['situação'] = 'RAZOÁVEL'
                  else:
                          r['situação'] = 'RUIM'
          return r

resp = notas(5.5, 3, 8, 2.3, 9, sit=True)
print(resp)