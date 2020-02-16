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
