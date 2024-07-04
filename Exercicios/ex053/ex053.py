frase = str(input('Digite uma frase:')).strip()
frase_invertida = frase[::-1]
print('A frase {}, invertida fica  {}'.format(frase.upper(),frase_invertida.upper()))
if frase == frase_invertida:
    print('A frase é palíndromo!')
else:
    print('A frase não é um palíndromo!')
