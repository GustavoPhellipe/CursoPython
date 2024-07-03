cont = 0
soma = 0
for contador in range(1, 500, 2):
    if contador % 3 == 0:
         cont = cont + 1
         soma = soma + contador
print('A soma de todos os {} valores solicitados é: {}'.format(cont, soma)) 