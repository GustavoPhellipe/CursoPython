nota = float(input('Primeira nota:'))
segnota = float(input('Segunda nota:'))
nota_total = (nota + segnota) / 2
print('Tirando {} e {}, sua nota em média é {}'.format(nota, segnota, nota_total))
if nota_total >= 5:
          print('APROVADO!')
else:
        print('REPROVADO!')