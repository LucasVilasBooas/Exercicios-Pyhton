from random import randint
computador = randint(0,10)
cont = 1
print("Ola eu sou o seu computador, vamos jogar ? ")
print("Acabei de pensar em um numero de 0 a 10, tente adivinhar! ")
usuario = int(input("EM que numero eu pensei? "))
while computador != usuario:
    if usuario > computador:
        usuario = int(input("Um pouco menos, tente de novo "))
        cont += 1
    else:
        usuario = int(input("um pouco mais, tente de novo "))
        cont += 1
print(f"Voce acertou e so precisou de {cont} tentativas")