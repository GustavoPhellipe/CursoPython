import moeda

preço = float(input('Digite um valor:'))
print(f'A metade do preço é: {moeda.metade(preço, True)}')
print(f'O dobro do preço é de: {moeda.dobro(preço, True)}')
print(f'Aumentando 10%, o preço fica: {moeda.aumento(preço, True)}')