#help()

'''def somar(a=0,b=0,c=0):
          s = a + b + c
          print(s)

somar(4,2,9)
somar(5,7,2) # Não digite mais do que 3
somar(1)'''

def somar(a=0,b=0,c=0):
          s = a + b + c
          return s
r1 = somar(3,2,5)
r2 = somar(9,3)
r3 = somar(7,5,1)

print(f'Os resultados foram {r1}, {r2}, {r3}')