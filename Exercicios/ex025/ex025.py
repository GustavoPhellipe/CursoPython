nome = str(input('Qual é seu nome completo?')).strip()
#Silva = 'Silva' in nome or 'silva' in nome
separa = nome.upper().split()
print('Seu nome tem Silva? {}'.format('SILVA' in separa))
