termo = int(input('Digite o termo:'))
razao = int(input('Digite a razão:'))
décimo = termo + (11 - 1) * razao
for pa in range(termo, décimo, razao):
    print(pa, end=' --> ')
print('FINALIZADO')