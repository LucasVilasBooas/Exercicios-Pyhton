vel = int(input("Digite sua velocidade "))
if vel > 80:
    print("Voce foi MULTADO")
    print(f"Voce tem que pagar R${(vel-80)*7}")
else:
    print("Tenha uma boa viajem")