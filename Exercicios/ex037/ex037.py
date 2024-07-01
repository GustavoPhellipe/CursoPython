num = int(input('Escolha um número inteiro:'))
print('Escolha algumas das bases abaixo')
print('[1] Converter para binário')
print('[2] Converter para octal')
print('[3] Converter para hexagonal')
escolha = int(input('Escolha um número:'))
# BINÁRIO
if escolha == 1:
          print('O número {} convertendo BINÁRIO vai ser igual á {}'.format(num, bin(num)[2:]))
# OCTAL
elif escolha == 2:
        print('O número {} convertendo em BINÁRIO vai ser igual á {}'.format(num, oct(num)[2:]))
# HEXADECIMAL
elif escolha == 3:
        print('O número {} convertendo em BINÁRIO vai ser igual á {}'.format(num, hex(num)[2:]))
