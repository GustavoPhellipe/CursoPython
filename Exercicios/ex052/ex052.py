num = int(input('Digite um número:'))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[30m', end='')
        tot = tot + 1
    else:
        print('\033[32m',end='')
    print(c, end=' ')
print('\n\033[97mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
 print('\033[97mEle é um número PRIMO!')
else:
   print('\033[97mEle não é um número PRIMO!')