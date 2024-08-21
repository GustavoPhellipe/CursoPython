from numeros import numero
#Pasta  --  Arquivo
num = int(input('Digite um número:'))
fat = numero.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numero.dobro(num)}')
print(f'O triplo de {num} é {numero.triplo(num)}')