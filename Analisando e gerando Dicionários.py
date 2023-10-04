def notas(*n, situação=False):
    '''
    Função para analisar notas e a situação em que o aluno se encontra
    :param n: quantidade de notas
    :param situação: valor opcional para se mostra ou nao a situação
    :return: maior, menor, quantidade de notas e a media do aluno
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if situação:
        if r['media'] >7 :
            r['situação'] = 'Boa'
        elif 5 < r['media'] <=7:
            r['situação'] = 'Regular'
        else:
            r['situação'] = 'Ruim'
    return r

resp = notas(2.4, 5.6, 8.7, situação=True )
print(resp)