produto1k = MaisBarato = total = c =0
continuar = nomemenos =""
while True:
    nome = str(input("Digite o nome do produto "))
    valor = float(input("Preço R$ "))
    total = total + valor
    while c == 0:
        MaisBarato = valor
        c += 1
    if valor >= 1000:
        produto1k += 1
    if valor < MaisBarato:
        nomemenos = nome
        MaisBarato = valor
    continuar = str(input("Deseja continuar? [S] para continuar ou aperte qualquer tecla para finalizar ")).upper().strip()[0]
    if continuar != "S":
        break
    print("*-"*30)
print()
print(f"O total da compra é R${total:.2f}")
print(f"Existem {produto1k} produto que custam mais de R$1.000")
print(F"O produto mais barato é {nomemenos} com o preço de R${MaisBarato:.2f}")
print(nomemenos)
print(">>>FIM PROGRAMA<<<")