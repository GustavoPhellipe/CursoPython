Armazenamento = list()
Armazenamento.append('Gustavo')
Armazenamento.append(16)
Lista = list()
Lista.append(Armazenamento[:])
Lista[0][0] = 'Felipe'
Lista[0][1] = 19
Lista.append(Armazenamento[:])
print(Lista)