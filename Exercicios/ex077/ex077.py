palavras = ('Programação', 'Doce', 'Algoritmo', 'Praticando',  'Estudar', 'Aprender', 'Ensinar', 'Raciocínio', 'Lógica')
for p in palavras:
    print('\nNa palavra {} temos:'.format(p.upper()),end=' ')
    for letras in p:
        if letras in 'aáâãeéêiíîoóôõuúû':
            print(letras, end=' ')

'''
#SEM ACENTO
for pos in range(0, len(palavras)):
    print('Na palavra {} temos:'.format(palavras[pos],end='..........')
    print('A:{}'.format(palavras[pos].count('A')),end=' ')
    print('E:{}'.format(palavras[pos].count('E')),end=' ')
    print('i:{}'.format(palavras[pos].count('I')),end=' ')
    print('O:{}'.format(palavras[pos].count('O')),end=' ')
    print('U:{}'.format(palavras[pos].count('U')))
'''