from time import sleep
Primeiro_numero = int(input('Digite um número:'))
Segundo_numero = int(input('Digite um segundo número:'))
Opção = 0
while Opção != 5:
    print('-' * 20)
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos números')
    print('[ 5 ] Sair do programa')
    print('-' * 20)
    Opção = int(input('Escolha algumas das opções:'))
    if Opção > 5:
       print('[ERRO] Coloque a opção correta!')
       sleep(3)
    if Opção == 1:
     Soma = Primeiro_numero + Segundo_numero
     print('A soma entre {} + {} ficou com: {}'.format(Primeiro_numero, Segundo_numero, Soma))
    elif Opção == 2:
       Multiplicação = Primeiro_numero * Segundo_numero
       print('A multiplicação {} x {} é: {}'.format(Primeiro_numero, Segundo_numero, Multiplicação))
    elif Opção == 3:
       if Primeiro_numero > Segundo_numero :
          print('Entre o valor {} e {} o maior valor é: {}'.format(Primeiro_numero, Segundo_numero, Primeiro_numero))
       elif Primeiro_numero == Segundo_numero:
          print('O número {} e {} são iguais!'.format(Primeiro_numero, Segundo_numero))
       else:
          print('Entre o valor {} e {} o maior valor é: {}'.format(Primeiro_numero, Segundo_numero, Segundo_numero))
    elif Opção == 4:
       Primeiro_numero = int(input('Digite um número:'))
       Segundo_numero = int(input('Digite um segundo número:'))
    elif Opção == 5:
       print('Finalizando...')
       sleep(2.5)
print('Fim do programa!')