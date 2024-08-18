from time import sleep
while True:
 print(f"\033[0;0;42m {'~' * 36} \033[m")
 print('\033[0;0;42m Sistema interativo de ajuda em Python\033[m')
 print(f"\033[0;0;42m {'~' * 36} \033[m")
 comando = str(input('Função ou Biblioteca [FIM para parar:]')).strip()
 sleep(2)
 print(f"\033[0;0;45m {'~' * 35} \033[m")
 print(f'\033[0;0;45m Acessando o manual do comando "{comando}" \033[m')
 print(f"\033[0;0;45m {'~' * 35} \033[m")
 help(f'{comando}')
 if comando in 'FIMFimfim'.upper():
  print('PROGRAMA ENCERRADO!')
  print('VOLTE SEMPRE!')
  break
 print('<<ENCERRADO>>')

