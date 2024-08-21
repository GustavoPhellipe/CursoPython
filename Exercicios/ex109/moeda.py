def metade(preço=0, formato=False):
         metade = preço / 2
         return metade if formato == False else moeda(metade)
          

def dobro(preço, formato=False):
        dobro = preço * 2
        return dobro if formato == False else moeda(dobro)
          

def aumento(preço, formato=False):
        res =  ((preço / 100) * 10) + preço
        return res if formato == False else moeda(res)

def moeda(preço=0, moeda='R$'):
        return f'{moeda}{preço}'.replace('.', ',')