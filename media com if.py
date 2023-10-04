n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1+n2) / 2
if media >= 7 :
    print(f"Parabens voce foi aprovado com media {media}")
elif media >=5 and media < 7:
    print(f"voce ficou de recuperação com media {media}")
else:
    print(f"Voce foi reprovado com media {media}")
