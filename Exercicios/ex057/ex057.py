#Sexo = str(input('Digite o seu sexo: [M/F]')).strip().upper()[0]
#while Sexo not in 'MmFf':
#  Sexo = str(input('[ERRO]. Digite o sexo correto:'))
#print('Sexo {} registrado com sucesso!'.format(Sexo.upper()))

Sexo = str(input('Digite o seu sexo: [M/F]')).strip().upper()[0]
while Sexo not in ['M', 'F']:
    Sexo = str(input('[ERRO]. Digite o sexo correto: [M/F]')).strip().upper()[0]
print(Sexo)