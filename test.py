from funcao import Corrigir

if __name__ == '__main__':
    # Código que você que que seja corrigido.
    codigo = open('codigo.py').read()
    # converter = True, executa o código e não exibi as linhas em forma de lista.
    Corrigir(codigo, converter=False)

