'''def escreva(txt):
        print('-' * len(txt))
        print(txt)
        print('-' * len(txt))
        

escreva('Gustavo')
escreva('Roberto')
escreva('José')
escreva('Maria')'''


def escreva(msg):
        comprimento_msg = len(msg) + 4
        print('-' * comprimento_msg)
        print(f'  {msg}')
        print('-' * comprimento_msg)
        

escreva('Gustavo')
escreva('Roberto')
escreva('José')
escreva('Maria')