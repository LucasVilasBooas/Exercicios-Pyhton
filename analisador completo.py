idademaior = 0
homemvelho = str("Sem Cadastro")
media = 0
cont = 0
for c in range (1,5):
    print("="*30)
    print(f"Dados da {c} pessoa")
    nome = str(input(f"Digite o nome da pessoa: "))
    idade = int(input(f"Digite a idade : "))
    sexo = str(input(f"Digite o sexo: ")).upper()
    media += idade
    if sexo == "M":
        if idade > idademaior:
            idademaior = idade
            homemvelho = nome
    if sexo == "F":
        if idade < 20:
            cont += 1
print(f"A media de idade do grupo é de {media/4}")
print(f"O homem mais velho é {homemvelho} com {idademaior} anos de idade")
print(f"Existem {cont} mulher(es) com menos de 20 anos")