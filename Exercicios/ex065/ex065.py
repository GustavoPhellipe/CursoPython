cont = media = tot = 0
maior = menor = None
n = 1
while n != 0:
    num = int(input('Digite um número:'))
    conti = str(input('Quer continuar?? [S/N]')).strip().upper()
    cont = cont + 1
    tot = tot + num
    media = tot / cont

    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num

        ''' if cont == 0:
            maior = num
            menor = num
    else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num'''


    if conti != 'S' and conti != 'N':
        print('[ERRO] Coloque a alternativa correta!')

    elif conti == 'N':
        n = 0
        print('Você digitou {} vez(es)'.format(cont))
        print('A média dos números é {}'.format(media))
        print('O maior número é {}'.format(maior))
        print('O menor número é {}'.format(menor))
        