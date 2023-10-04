km = int(input("Digite quantos km é a vjagem: "))
if km <= 200:
    print(f"o valor da passagem é de R${km * 0.45::.2f}")
else:
    print(f"o valor da passagem é de R${km * 0.5:.2f}")