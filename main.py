# Exemplo de código que já funciona
def codigo():
    cod = '''
    
sla = 133

if sla == 13:
    print sla
   
    
    print len(str(sla))
    
    '''
    return cod


class Corrigir:

    def __init__(self, *args, converter=True):
        cod = list(args)

        # print(f'Código(s) corrigido(s) >> {cod}')

        try:
            # Abre o arquivo de texto ou o que for passado como texto.
            x = codigo()

            # Executa o texto.
            exec(x)

        except SyntaxError as erro:
            # Retorna a mensage de erro em str.
            mensage = erro.msg
            # retorna o print()...S2
            pri = erro.msg[53:64]
            # Me retorna o código errado em str
            texto = erro.text
            # Retorna a linha do erro em int
            linha = erro.lineno
            # Retorna quantas letras tem o código errado em int
            letras = erro.offset
            # retorna o que tipo é, tem que estudar + n entedi direito
            sla = erro.filename

            # Me retorna o print corrigido, dentro da variável test em forma de str.
            aaa = len(mensage)
            test = mensage[53:aaa - 1]  # Fatia a area do print('') junto com o texto entre ''

            # O erro tem 63 letras contando de 0.
            print(f"Parênteses ausentes na chamada para 'print'. Tratando para você.\n ... Tratando erros")
            print('-----------Apartir daqui o código corrigido------------------------')
            # Cria uma lista
            y = x.split('\n')
            print()

            #    print(texto)

            #    x = x.replace(texto, test)
            # Bora achar os prints
            ad = 0
            for g in y:
                ad += 1
                # A variável acha vai me retorna a posição inicial do print.
                acha = g.find('print')
                if acha >= 1:
                    ad += 1

                    print(f'Erro tratado >>> {y[ad - 2][acha:]} na linha {ad - 2}.')
                    # Coloca na lista com o print formatado e corrigido.
                    y[ad - 2] = f'{y[ad - 2][0:acha]}print({y[ad - 2][5 + acha + 1:]})'
                    ad -= 1
                    #

                # print(f'{g[0:5]}')

                # Acessa o que esta dentro do print.
                # g vai me retornar o erro.

                if g[0:5] == 'print':
                    ad += 1

                    # Tem que ser menos 1, porque a lista começa de 0
                    print(f'Erro tratado {g} >>> print({y[ad - 2][6:]}) na linha {ad - 2}.')

                    # Coloca o print corrigido na tabela.
                    y[ad - 2] = f'print({y[ad - 2][6:]})'
                    #
                    # print(f'{len(y[ad-1])}', end='\n')
                    ad -= 1
                    # y é a nossa tabela corrigida.

            self.cov(conv=converter, yy=y)

    def cov(self, conv, yy):
        # Se a pessoa não definine ele executa o código por padrão
        # yy é nossa tabela corrigida.
        # Junta a lista em uma string.
        if conv:
            corrigido = '\n'.join(map(str, yy))
            print('----------------------------\nCódigo corrigido')
            print(f'\n\n {corrigido}')

            print('------Executando código corrigido-----------')
            exec(corrigido)
        else:
            corrigido = '\n'.join(map(str, yy))
            print('----------------------------\nCódigo corrigido')
            print(f'\n\n {corrigido}')
            print('----------Tabelamento------?')
            print(yy)


if __name__ == '__main__':

    Corrigir()
