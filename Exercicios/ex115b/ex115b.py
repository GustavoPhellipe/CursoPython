from time import sleep
Nome = list()
Idade = list()
while True:     
 print('-' * 30)
 print('MENU PRINCIPAL'.center(30))
 print('-' * 30)
 print('1 - \033[0;34mCadastrar nova pessoa\033[m')
 print('2 - \033[0;34mVer pessoas cadastradas\033[m')
 print('3 - \033[0;34mSair do programa\033[m')
 def pessoas_cadastradas(msg):
          while True:
                  try:
                          operação = int(input(msg))
                  except (ValueError, TypeError):
                          print('\033[0;31mPor favor, digite a opção válida!\033[m')
                  except KeyboardInterrupt:
                          print('\033[0;31mO usuário não digitou nenhum número.\033[m')
                          return 0
                  else:
                          return operação
          
 opção = pessoas_cadastradas('\033[0;32mEscolha uma opção:\033[m')
 sleep(1)
 if opção == 1:
        print('-=-' * 10)
        print('CADASTRAR PESSOAS'.center(30))
        print('-=-'  * 10)
        nome = str(input('Nome:')).strip()
        if nome == '':
              nome = '<<desconhecido>>'
        while True:
          try:
           idade = int(input('Idade:'))
          except(ValueError, TypeError):
           print('\033[0;31mPor favor, insira um número válido!\033[m')
          except(KeyboardInterrupt):
               print('A pessoa não quis inserir um valor.')
          else:
               print('Cadastro realizado!')
               Nome.append(nome)
               Idade.append(idade)
               break
        
 elif opção == 2:
        print('-=-' * 10)
        print('VER CADASTRO'.center(30))
        print('-=-'  * 10)
        print(f'Pessoa(s) cadastrada(s): {Nome}')
        print(f'Idade(s): {Idade}')
        
 elif opção == 3:
        print('-=-' * 11)
        print('Saindo do sistema... Volte sempre!'.center(30))
        print('-=-'  * 11)
        break
 else:
        print('[ERRO] Digite uma opção válida!')
sleep(1.4)