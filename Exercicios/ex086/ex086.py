'''print('-=-' * 10)
print(f'{"MATRIZ":^30}')
print('-=-' * 10)
Lista = []
for c in range(1,10):
 num = int(input('Digite um valor:'))
 Lista.append(num)
print('[{:^5}] [{:^5}] [{:^5}]'.format(Lista[0],Lista[1],Lista[2]))
print('[{:^5}] [{:^5}] [{:^5}]'.format(Lista[3],Lista[4],Lista[5]))
print('[{:^5}] [{:^5}] [{:^5}] '.format(Lista[6], Lista[7], Lista[8]))
'''

matriz =[[0,0,0], [0,0,0], [0,0,0]]
for l in range(0,3):
          for c in range(0,3):
                  matriz[l][c] = int(input(f'Digite um valor para [{l}],[{c}]'))
print('-=-'*30)
for l in range(0,3):
        for c in range(0,3):
                print(f'[{matriz[l][c]:^5}]',end=' ')
print()
