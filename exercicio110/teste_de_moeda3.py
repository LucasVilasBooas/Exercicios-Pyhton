import moeda3

p = float(input("digite o preço →R$"))
print(f'A metade de {moeda3.moeda(p)} é {moeda3.metade(p, True)}')
print(f'O dobro de {moeda3.moeda(p)} é {moeda3.dobro(p, True)}')
print(f'Aumentando o preço em 10% → {moeda3.aumentar(p, 10, True)}')
print(f'Baixando o preço em 20% → {moeda3.diminuir(p, 20, True)}')
