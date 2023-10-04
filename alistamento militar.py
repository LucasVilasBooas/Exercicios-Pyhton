from datetime import date
ano = int(input("Qual o ano de nascimento? "))
atual = date.today().year
idade = atual-ano
print(f"quem nasceu em {ano} hoje tem {idade} anos de idade")
if idade < 18 :
    print(F"Ainda faltam {idade-18} para se alistar!")
elif idade > 18:
    print(f"voce tem que se alistar urgente. Se passaram {18-idade} anos do alistamento")
else:
    print("Esta na hora de se alistar!!!")