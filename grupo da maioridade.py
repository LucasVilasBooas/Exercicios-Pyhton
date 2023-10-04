from datetime import date
atual = date.today().year
menor = 0
maior = 0
for c in range (0,7):
    ano = int(input("Digite o ano de nascimento: "))
    if atual-ano >= 18:
        maior += 1
    else:
        menor = menor + 1
print(f"Nos temos {maior} pessoas que ja atingiram a maioridade e {menor} pessoa que nao atingiram a maioridade")