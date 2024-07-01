Compra = int(input('Preço das compras:'))
print('FORMAS DE PAGAMENTOS')
print('[ 1 ] Dinheiro à vista')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
Opçao = int(input('Escolha uma opção seguinte:'))
if Opçao == 1:
          dinheiro_vista = Compra - ((Compra * 10) / 100)
          print('O preço da sua compra é de R${}, mas junto com desconto, custará apenas R${:.0f}'.format(Compra, dinheiro_vista))
elif Opçao == 2:
        Cartao = Compra - ((5 * Compra) / 100)
        print('Na vista no cartão, você receberá 5% de desconto que custará R${:.0f} em sua compra'.format(Cartao))

elif Opçao == 3:
        parcela_2x = Compra / 2
        print('A sua compra parcelada em 2x custará R${:.0f}'.format(parcela_2x))
        print('Você não terá descontos e juros')

elif Opçao == 4:
        parcela = int(input('Escolha a sua parcela (1 à 12x):'))
        cartao = Compra + ((Compra * 20) / 100)
        preço_total = cartao / parcela
        print('O preço total com juros custará apenas R${:.0f}'.format(cartao))
        print('Sua compra parcelada em {}x será de R${:.0f}'.format(parcela, preço_total))

else:
        print('[ERRO] Coloque a opção correta!')