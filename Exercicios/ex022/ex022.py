nome = str(input('Digite seu nome:')).strip()
nomema = nome.upper()
print('Seu nome em letra MAIÚSCULA é:{}'.format(nomema))
nomemi = nome.lower()
print('Seu nome em letra MINÚSCULA é:{}'.format(nomemi))
caracteres = len(nome) - nome.count(' ')
print('O seu nome ao todo tem:{} caracteres'.format(caracteres))
primenome = nome.split()[0]
primecaracte = len(primenome)
print('Seu primeiro nome é {} e ele tem {} caracteres'.format(primenome, primecaracte))


#nome = str(input('Digite seu nome:')).strip()
#print('Analisando...')
#print('Seu nome em letras MAIÚSCULAS é: {}'.format(nome.upper()))
#print('Seu nome em letras MINÚSCULAS é: {}'.format(nome.lower()))
#print('Seu nome ao todo tem: {} caracteres'.format(len(nome) - nome.count(' ')))
#separa = nome.split()
#print('Seu primeiro nome é {} e ele tem {} caracteres'.format(separa[0], len(separa[0])))
