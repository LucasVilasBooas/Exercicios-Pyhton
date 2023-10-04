maior18 = homem = mulhermenos20 = 0
continuar = "S"
while True:
    idade = int(input("Digite a idade: "))
    sexo = " "
    while sexo not in "MF": #melhora do programa pelo guanabara
        sexo = str(input("Digite o sexo [M] masculino ou [F] Feminino: ")).upper().strip()[0]
    if idade > 18:
        maior18 += 1
    if "M" in sexo:
        homem += 1
    if "F" in sexo and idade < 20:
        mulhermenos20 += 1
    continuar = str(input("Deseja coninuar? [S] Sim ou [N] Não: ")).upper().strip()[0]
    if continuar != "S":
        break
print()
print(f"Foram cadastradas {maior18} pessoas maior de 18 anos.")
print(f"Temos {homem} homen(s) cadastrados na lista.")
print(f"E {mulhermenos20} mulheres com menos de 20 anos.")