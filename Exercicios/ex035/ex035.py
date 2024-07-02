print('-=-' * 20)
print('ANALISADOR DE SEGMENTOS')
print('-=-' * 20)
segmento = float(input('Digite o segmento:'))
segmento2 = float(input('Digite o segundo segmento:'))
segmento3 = float(input('Digite o terceiro segmento:'))
if segmento + segmento2 > segmento3:
           print('OS SEGMENTOS ACIMA FORMAM UM TRIÂNGULO!')
else:
           print('OS SEGMENTOS ACIMA NÃO PODEM FORMAR UM TRIÂNGULO!')