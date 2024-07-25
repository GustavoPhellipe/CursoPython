dig = soma = 0
while True:
          num = int(input('Digite um número:'))
          if num == 999:
                  break
          soma = soma + num
          dig = dig + 1
print('Você digitou {} números e o valor total foi {}'.format(dig, soma))