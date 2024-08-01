print('-=-' * 12)
print(f'{"LOJÃO SUPER COMPRAS":^35}')
print('-=-' * 12)
cont_preço = cont_preço_mil = 0
menor = None
barato = ' '
while True:
    nome_produto = str(input('Nome do produto:')).strip()
    preço = int(input('Preço:'))
    cont_preço = cont_preço + preço
    continuação = ' '
    if preço >= 1000:
        cont_preço_mil = cont_preço_mil + 1
    if menor is None or preço < menor:
        menor = preço
        barato = nome_produto
    while continuação not in 'SsNn':
        continuação = str(input('Você quer continuar? [S/N]')).strip().upper()
    if continuação == 'N':
        break
print('A compra no total deu R${}'.format(cont_preço))
print('Apenas {} produto(s) acima de R$1000'.format(cont_preço_mil))
print('O produto {} tem o menor preço, custando R${}'.format(barato,menor))