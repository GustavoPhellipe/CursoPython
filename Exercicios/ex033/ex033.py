num = int(input('Digite um número:'))
num2 = int(input('Digite o segundo número:'))
num3 = int(input('Digite o terceiro número:'))
#Crescente
if num > num2 and num > num3:
          numtotal = num
          print('O maior número é {}'.format(numtotal))
if num2 > num and num2 > num3:
        num2total = num2
        print('O maior número é: {}'.format(num2total))
if num3 > num and num3 > num:
        num3total = num3
        print('O maior número é {}'.format(num3total))
#Decrescente
if num < num2 and num < num3:
          numtotal = num
          print('O menor número é {}'.format(numtotal))
if num2 < num and num2 < num3:
        num2total = num2
        print('O menor número é: {}'.format(num2total))
if num3 < num and num3 < num:
        num3total = num3
        print('O menor número é {}'.format(num3total))
