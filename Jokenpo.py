from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
print("JO KEN PO ! ")
print(""" Escolha sua opção! 
0 - PEDRA 
1 - PAPEL
2 - TESOURA""")
pc = randint (0, 2)
jogador = int(input("Faça sua escolha: "))
sleep(1)
print("JO")
sleep(1)
print("ken")
sleep(1)
print("PO")
sleep(1)
print(f"O pc escolheu {itens[pc]}")
print(f"O jogador escolheu {itens[jogador]}")
if pc == 0:
    if pc == 0 and jogador == 0:
         print("o jogo deu empate!")
    elif pc == 0 and jogador == 1:
         print("Jogador ganhou!")
    elif pc == 0 and jogador == 2:
         print("PC ganhou!")
    else:
         print("Jogada invalida")
elif pc == 1:
    if pc == 1 and jogador == 0:
         print("PC  ganhou!")
    elif pc == 1 and jogador == 1:
         print("Jogo EMPATOU!")
    elif pc == 1 and jogador == 2:
         print("Jogador ganhou")
    else:
         print("jogada invalida")
elif pc == 2:
    if pc == 1 and jogador == 0:
         print("PC  ganhou!")
    elif pc == 1 and jogador == 1:
         print("Jogo EMPATOU!")
    elif pc == 1 and jogador == 2:
         print("Jogador ganhou")
    else:
         print("jogada invalida")
