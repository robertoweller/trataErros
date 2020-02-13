
try:

    x = '''
f = '231'
len(f)

print '12345678'

xxx = 54546

print 'roberto'

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
    print(f'{test} é do tipo >> {type(test)} \n')
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

        #print(f'{g[0:5]}')

        # Acessa o que esta dentro do print.
        # g vai me retornar o erro.
        if g[0:5] == 'print':
            ad += 1
            print(f'{g}')
            # Tem que ser menos 1, porque a lista começa de 0
            print(f'print({y[ad-2][6:]})')
            #
            # print(f'{len(y[ad-1])}', end='\n')
            ad -= 1

    #####

    print(f'\n\n {y}')


# Deixa para executar o codigo depois
#    exec(x)
