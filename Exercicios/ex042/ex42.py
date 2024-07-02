segmento = str(input('Primeiro segmento:')).strip()
segmento2 = str(input('Segundo segmento:')).strip()
segmento3 = str(input('Terceiro segmento:')).strip()

print('Os segmentos acima podem formar um triângulo', end=' ')

if segmento != segmento2 != segmento3 != segmento:
          print('ESCALENO')

elif segmento == segmento2 == segmento3:
          print('EQUILÁTERO')

elif segmento == segmento3 or segmento == segmento2 or segmento2 == segmento3:
        print('ISÒSCELES')
else:
        print('Os segmentos acima n podem formar um triângulo!')