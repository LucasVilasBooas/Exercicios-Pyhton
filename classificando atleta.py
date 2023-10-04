from datetime import date
atual = date.today().year
ano = int(input("Digite o ano que o atleta nasceu: "))
idade =  atual - ano
if idade <= 9:
    print("Classificação MIRIM")
elif idade <=14:
    print("Classificação INFANTIL")
elif idade <=19:
    print("Classificação JUNIOR")
elif idade <=25:
    print("Classificação SENIOR")
elif idade >25:
    print("Classificação MASTER")
