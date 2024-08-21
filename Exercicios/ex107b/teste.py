import moeda

preço = float(input('Digite um valor:'))
print(f'O preço do valor é: R${preço}')
print(f'A metade do preço é: R${moeda.metade(preço)}')
print(f'O dobro do preço é de: R${moeda.dobro(preço)}')
print(f'Aumentando 10%, o preço fica: R${moeda.aumento(preço)}')
