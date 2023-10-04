print("GERADOR DE PA")
print("*-"*15)

primeiro = int(input("Digite um numero "))
razao = int(input("Digite a razao "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, end=" ->")
        termo += razao
        cont += 1
    print()
    print('->PAUSA<-')
    mais = int(input("quantos termos quer mostrar a mais? "))
print(f"Progressao finaliada com {total} termos mostrados")
