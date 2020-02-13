# Tente executar o codigo da variavel x.
try:

    x = '''

# somadora4.py - somadora infinita - versao 4 
print 'Digite os valores a somar seguidos de [ENTER].'
print 'Para encerrar apenas [ENTER].'
total = 0
while 1:
    try:
        linha = input(':')
        n = float(linha)
        total = total + n
    except:
        if len(linha) == 0:
            break
        elif ',' in linha:
            print 'Use o . (ponto) como separador decimal.'
        else:
             print 'Isso nao parece um numero valido.'
print 'TOTAL: %s' % total

'''
    # Executa o texto.
    exec(x)

except SyntaxError as erro:
    # Retorna a mensagem de erro em str.
    mensage = erro.msg
    # retorna o print()...S2
    pri = erro.msg[53:64]
    # Me retorna o codigo errado em str
    texto = erro.text
    # Retorna a linha do erro em int
    linha = erro.lineno
    # Retorna quantas letras tem o codigo errado em int
    letras = erro.offset
    # retorna o que tipo é, tem que estudar + n entedi direito
    sla = erro.filename

    # Me retorna o print corrrigido, dentro da variavel test em forma de str.
    aaa = len(mensage)
    test = mensage[53:aaa-1] # Fatia a area do print('') junto com o texto entre ''

    # O erro tem 63 letras contando de 0.
    print(f"Parênteses ausentes na chamada para 'print'. Tratando para você.\n ... Tratando erros")
    print('-----------Apartir daqui o codigo corrigido------------------------')
    # Cria uma lista
    y = x.split('\n')
    print()

#    print(texto)

#    x = x.replace(texto, test)
    # Bora achar os prints
    ad = 0
    for g in y:
        ad += 1
        # A variavel acha vai me retorna a posição inicial do print.
        acha = g.find('print')
        if acha >= 1:
            ad += 1

            print(f'Erro tratado >>> {y[ad-2][acha:]} na linha {ad-2}.')
            # Coloca na lista com o print formatado e corrigido.
            y[ad - 2] = f'{y[ad - 2][0:acha]}print({y[ad-2][5+acha+1:]})'
            ad -= 1

            #
        #print(f'{g[0:5]}')

        # Acessa o que esta dentro do print.
        # g vai me retornar o erro.

        if g[0:5] == 'print':
            ad += 1

            # Tem que ser menos 1, porque a lista começa de 0
            print(f'Erro tratado {g} >>> print({y[ad-2][6:]}) na linha {ad-2}.')

            # Coloca o print corrigido na tabela.
            y[ad-2] = f'print({y[ad-2][6:]})'
            #
            # print(f'{len(y[ad-1])}', end='\n')
            ad -= 1


    #######1234


#    print(f'\n\n {corrigido}')



# Deixa para executar o codigo depois
    # Junta a lista em uma string.
    rrr = 't'
    if rrr == 't':
        corrigido = '\n'.join(map(str, y))
        print('----------------------------\nCodigo corrigido')
        print(f'\n\n {corrigido}')

        print('------Executando codigo corrigido-----------')
        exec(corrigido)
    else:
        print(y)
