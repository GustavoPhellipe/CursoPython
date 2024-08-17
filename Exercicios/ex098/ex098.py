print('-' * 18)
print('FUNÇÃO DE CONTADOR')
print('-' * 18)
print('-=-' * 10)
def contador(inicio,fim,passo):
        if fim >= inicio:
                print('Contagem de {} até {} de {} em {}'.format(inicio,fim,passo,passo))
                for contc in range(inicio,fim+1,passo):
                        print(contc,end=' ')
                print('\n<< ENCERRADO >>')
        elif inicio >= fim:
                print('Contagem de {} até {} de {} em {}'.format(inicio,fim,passo,passo))
                for contde in range(inicio,fim-1,passo):
                        print(contde,end=' ')
                print('\n<< ENCERRADO >>')
print('Contagem de 1 até 10 de 1 em 1')
for cont in range(1,11):
          print(cont,end=' ')

print('\nContagem de 10 até 0 em 2 em 2')
for contd in range(10,-2,-2):
        print(contd,end=' ')

print('\nAgora é sua vez de personalizar!')
inicio = int(input('Início: '))
fim = int(input('Fim:'))
passo = int(input('Passo: '))
contador(inicio,fim,passo)