def ficha():
    '''
    Faz um cadastro simples de um jogador pedindo NOME e quantidade de GOLS
    :return: Retorna com o nome e a quantidade de gols feitos.
    '''
    nome = str(input("Digite o nome do Jogador →"))
    gols = str(input('Digite a quantidade de gols →'))
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    if nome.strip() == "":
        nome = 'Desconhecido'
    return f'O jogador {nome} fez {gols} gols no campeonato'


print(ficha())

# PELO GUANABARA

def ficha( jog='desconhecido', gols = 0):
    print(f"o jogador {jog} fez {gols} gol(s) no campeonato.")

#programa principal
n=str(input("Digite o nome do jgoador "))
g=str(input("Quantidadade de gols "))
if g.isnumeric():
    g =int(g)
else:
    g = 0
if n.strip() == "" :
    ficha(gol=g)  # ele so passa a quantidade de gols porque ele inicia o nome do jogador JOG ele ja vem como desconhecido
else
    ficha(n, g)

