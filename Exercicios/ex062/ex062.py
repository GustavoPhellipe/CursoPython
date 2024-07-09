'''primeiro = int(input('Digite um número para o termo:'))
razao = int(input('Digite um número para a razão:'))
termo = primeiro
contador = 1
mais_termos = 10

while mais_termos != 0:
    total = 0
    while total < mais_termos:
        print(f'{termo}', end=' - ')
        termo += razao
        total += 1
    print('Pausa')
    mais_termos = int(input('Você quer adicionar quantos termos a mais?'))

print('Fim da progressão aritmética')'''


primeiro = int(input('Digite um valor para o termo:'))
razao = int(input('Digite um valor para a razão:'))
termo = primeiro
mais_termo = 10
while mais_termo != 0:
    total = 0
    while total < mais_termo:
        print('{}'.format(termo),end=' --> ')
        termo += razao
        total += 1
    print('Pausa')
    mais_termo = int(input('Você quer adicionar quantos termos a mais??'))
print('Fim do programa')