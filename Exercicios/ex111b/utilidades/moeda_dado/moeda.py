
def metade(preço=0, formato=False):
         metade = preço / 2
         return metade if formato == False else moeda(metade)
          

def dobro(preço, formato=False):
        dobro = preço * 2
        return dobro if formato == False else moeda(dobro)
          

def aumento(preço=0, formato=False):
        res =  ((preço / 100) * 10) + preço
        return res if formato == False else moeda(res)

def moeda(preço=0, moeda='R$'):
        return f'{moeda}{preço}'.replace('.', ',')

def moeda_resumo(preço):
        print('-' * 30)
        print('RESUMO DO VALOR'.center(30))
        print('-' * 30)
        print(f'Preço analisado: \t{moeda(preço)}')
        print(f'O dobro do preço: \t{moeda(dobro(preço))}')
        print(f'Aumento do preço de 10%: {moeda(aumento(preço))}')
        print('-' * 30)
        return moeda