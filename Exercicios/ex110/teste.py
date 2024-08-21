'''import ex110_moeda

preço = float(input('Digite um valor:'))
print(f'A metade do preço é: {ex110_moeda.metade(preço, True)}')
print(f'O dobro do preço é de: {ex110_moeda.dobro(preço, True)}')
print(f'Aumentando 10%, o preço fica: {ex110_moeda.aumento(preço, True)}')'''

import ex110_moeda

preço = float(input('Digite um valor:'))
ex110_moeda.moeda_resumo(preço)