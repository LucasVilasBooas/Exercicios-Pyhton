from random import randint

vitoria = 0
soma = 0
escolha = "P" or "I"
while True:
    print("="*30)
    print("vamos Jogar Par ou Impar ")
    player = int(input("Digite um valor "))
    escolha = str(input("Escolha Par ou Impar ")).upper().strip()[0]
    pc = randint(0,10)
    jogo = player+pc
    resultado = jogo % 2
    if escolha == "P":
        if resultado == 0:
            vitoria += 1
            print(f" voce escolheu {player} e o computador escolheu {pc} a soma deles é {jogo} que é par")
            print("Voce venceu!")
            print("=" * 30)
        else:
            print(f" voce escolheu {player} e o computador escolheu {pc} a soma deles é {jogo} que é impar")
            print("=" * 30)
            break
            #print("voce perdeu!")
    if escolha == "I":
        if resultado != 0:
            vitoria += 1
            print(f" voce escolheu {player} e o computador escolheu {pc} a soma deles é {jogo} que é impar")
            print("Voce venceu!")
            print("=" * 30)
        else:
            print(f" voce escolheu {player} e o computador escolheu {pc} a soma deles é {jogo} que é par")
            print("=" * 30)
            break
            #print("voce perdeu!")
print(f"Voce perdeu! voce venceu {vitoria} consecutivas.")