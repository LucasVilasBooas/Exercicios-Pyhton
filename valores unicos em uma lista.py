lista = []
while True:
    n = int(input('Digite um valor '))
    if n in lista:
        print("Voce ja digitou esse numero. Nao sera adicionado!")
    else:
        lista.append(n)
    continuar = str(input("Deseja cadastrar outro numero ? [S] para continuar →")).strip()[0] .upper()
    if continuar != "S":
        break
print(f"VOCE DIGITOU OS VALORES >>> {sorted(lista)}")