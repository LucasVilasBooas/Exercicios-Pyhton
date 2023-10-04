import moeda

p = float(input("digite o preço →"))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando o preço em 10% → {moeda.aumentar(p, 10)}')
print(f'Aumentando o preço em 20% → {moeda.diminuir(p, 20)}')
