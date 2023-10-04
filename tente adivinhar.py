from random import randint
computador = randint(0,5)
from time import sleep
print("*-" * 20)
print("vou pensar em um numero de 0 ate 5, tente adivinhar")
print("*-" * 20)
jogador = int(input('Em que numero eu pensei? '))
print("processando...")
sleep(1)
if jogador == computador:
    print("parabens voce venceu!")
else:
    print(f"Errou, eu pensei no numero {computador} e nao no nuero {jogador} tente novamente!")