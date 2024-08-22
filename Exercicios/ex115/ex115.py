from modulos import textos
from modulos import leiainteiro
from modulos.arquivo import arquivos
from time import sleep
arq = 'arquivo_novo.txt'
arquivos.criararquivo(arq)
      
while True:
 textos.cabeçalho()
 textos.texto_opções()
 operação = leiainteiro.leiaint('\033[0;32mEscolha uma opção:\033[m')
 if operação == 1:
       arquivos.lerarquivo(arq)
 elif operação == 2:
        print('-=-' * 10)
        print('NOVO CADASTRO'.center(30))
        print('-=-'  * 10)
        nome = str(input('Nome:'))
        idade = leiainteiro.leiaint('Idade:')
        arquivos.cadastrar(arq,nome,idade)
 elif operação == 3:
        print('-=-' * 12)
        print('Encerrando o sistema... Volte sempre!'.center(30))
        print('-=-'  * 12)
        break
 else:
        print('\033[0;31mDigite uma opção válida!\033[m')
 sleep(1.4)