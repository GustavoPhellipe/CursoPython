import moedas

preço = float(input('Digite um valor:'))
print(f'O preço do valor é: R${preço:.2f}'.replace('.',','))
print(f'A metade do preço é: R${moedas.metade(preço):.2f}'.replace('.',','))
print(f'O dobro do preço é de: R${moedas.dobro(preço):.2f}'.replace('.',','))
print(f'Aumentando 10%, o preço fica: R${moedas.aumento(preço):.2f}'.replace('.',','))
