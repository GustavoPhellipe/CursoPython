def arquivoExiste(nome):
          try:
           arqui = open(nome, 'rt')
           arqui.close()
          except FileNotFoundError:
                return False
          else:
                return True
          
def criararquivo(nome):
      try:
            a = open(nome, 'wt+')
            a.close()
      except:
            print('Erro na criação do arquivo!')
      else:
            print(f'Arquivo {nome} criado com sucesso!')


def lerarquivo(nome):
      try:
            a = open(nome, 'rt')
      except:
            print('[ERROR] Não consigo ler o arquivo!')
      else:
            print('-' * 25)
            print('PESSOAS CADASTRADAS'.center(25))
            print('-' * 25)
            for linha in a:
                  dado = linha.split(';')
                  dado[1] = dado[1].replace('\n','')
                  print(f'{dado[0]:<30}{dado[1]:>3} anos')
      finally:
            a.close()


def cadastrar(arq,nome='desconhecido',idade=0):
      try:
            a = open(arq, 'at')
      except:
            print('Houve um erro na abertura!')
      else:
            try:
                  a.write(f'{nome};{idade}\n')
            except:
                  print('Houve um error na hora.')
            else:
                  print(f'Novo registro de {nome} realizado!')
                  a.close()