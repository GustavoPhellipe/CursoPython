import random
alu = str((input('Primeiro aluno:')))
alu2 = str((input('Segundo aluno:')))
alu3 = str((input('Terceiro aluno:')))
alu4 = str((input('Quarto aluno:')))
lista = [alu, alu2, alu3, alu4]
aleatório = random.choice(lista)
print('O aluno escolhido foi: {}'.format(aleatório))