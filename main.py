try:

    x = '''
print (z)

print '0'

'''
    # Executa o texto.
    exec(x)

except SyntaxError as erro:
    # Retorna a mensagem de erro em str.
    mensage = erro.msg
    # retorna o print()...S2
    pri = erro.msg[53:63]
    # Me retorna o codigo errado em str
    texto = erro.text
    # Retorna a linha do erro em int
    linha = erro.lineno
    # Retorna quantas letras tem o codigo errado em int
    letras = erro.offset
    # retorna o que tipo é + estudo n entedi direito
    sla = erro.filename

    test = pri

    print(f'{test} é do tipo >> {type(test)}')
    print(f'{mensage} Erro na linha {linha}...')
    x = pri
    print(x)
    exec(x)
