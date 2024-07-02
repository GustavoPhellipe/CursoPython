n1 = input('Digite um número:')
print('É um número inteiro?', n1.isalnum())
print('É uma letra?', n1.isalpha())
print('É um número?', n1.isnumeric())
print('É um número decimal?', n1.isdecimal())
print('Tem espaços?', n1.isspace())
print('Qual é o primitivo?', type(n1))

