menos = 0
tot = 0
Maior = 0
Nome1 = 0
for pessoas in range(1,5):
    print('--- {}ª Pessoa ---'.format(pessoas))
    Nome = str(input('Digite o nome da {}ª pessoa:'.format(pessoas))).strip()
    Idade = int(input('Digite a idade da {}ª pessoa:'.format(pessoas)))
    Sexo = str(input('Sexo (M ou F):')).strip()
    tot = tot + Idade
    Média = tot / 4
    if pessoas == 1:
        Maior = Idade
    else:
        if Idade > Maior and Sexo in 'Mm':
            Maior = Idade
            Nome1 = Nome
    if Idade < 20:
        menos = menos + 1
print('A média das pessoas no total é: {}'.format(Média))
print('A maior idade é: {} anos de {}'.format(Maior, Nome1))
print('Apenas {} pessoa(s) possui(em) uma idade abaixa de 20 anos'.format(menos))