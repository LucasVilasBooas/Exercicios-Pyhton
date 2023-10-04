continuar = "S"
cont = media = maior = menor = n = 0
while continuar == "S":
    n = int(input("Digite um numero \n"))
    cont += 1
    media += n
    continuar = (input("Quer continuar ? \n")).upper().strip()[0]
    if cont == 1:
        maior = menor = n
    if maior < n:
        maior = n
    if menor > n:
        menor = n
media = media / cont
print(f"Foram digitados {cont} numeros  e a media foi {media:.2f}")
print(f"O maior valor foi {maior} e o menor foi {menor}")
print(">>>>FIM DO PROGRAMA<<<<")