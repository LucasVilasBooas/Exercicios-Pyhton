def dobra (lst):
    pos=0
    while pos < len(lst):
        lst[pos]*=2
        pos += 1
def mostralinha():      '''para criar funções/rotinas basta criar uma def sempre colocando () no final'''
    print('------------------')

def soma(* valores:         '''criado uma rotina para fazer a soma de 2 numeros'''
        s = 0
        for num in valores:
            s += num
        print(f'somando os valores {valores} temos {s}')

def contador(*num):     '''desempacotar ... o * faz com que a quantidade seja dinamica'''
def mensagem(msg):      '''podem ser criadas de formas mais elabroradas, onde ve MSG sera trocado pelo que for escrito'''
    print('-'*30)       '''dentro de mensagem(teste)'''
    print(msg)
    print('-'*30)


mostralinha()
print('teste')
mostralinha()
mostralinha()
print('teste 2')
mostralinha()
mostralinha()
print('teste 3')
mostralinha()
print()
print()
mensagem('Lucas')
mensagem('Reis')
mensagem('Vilas Boas')
print()
print()
valores = [2,6,4,5,8]
dobra(valores)
print(valores)