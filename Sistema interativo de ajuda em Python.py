c = ('\33[m',           # 0 → sem cor
     '\33[0;30;41m',    # 1 → vermelho
     '\33[0;30;42m',    # 2 → verde
     '\33[0;30;43m',    # 3 → amarelo
     '\33[0;30;44m',    # 4 → azul
     '\33[0;30;45m',    # 5 → roxo
     '\33[0;30m',       # 6 → branco
     '')

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 3)
    print(c[2], end='')
    help(com)
    print(c[0], end='')

def titulo(msg, cor=0):
    tam = len(msg) + 4
    tamm = tam//2
    print(c[cor], end='') # o "c" dai esta atrelado ao c da lista das  cores acima
    print('-='*tamm)
    print(f'  {msg}')
    print('-='*tamm)
    print(c[0], end='')

#PROGRAMA PRINCIPAL
comando =''
while True:
    titulo("SISTEMA DE AJUDA PARA INICIANTES", 1)
    comando = str(input("Função ou Biblioteca →"))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
titulo('ATE LOGO', 5)