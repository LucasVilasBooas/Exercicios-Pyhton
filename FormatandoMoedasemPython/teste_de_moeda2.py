from FormatandoMoedasemPython import moeda2

p = float(input("digite o preço →"))
print(f'A metade de {moeda2.moeda(p)} é {moeda2.moeda(moeda2.metade(p))}')
print(f'O dobro de {moeda2.moeda(p)} é {moeda2.moeda(moeda2.dobro(p))}')
print(f'Aumentando o preço em 10% → {moeda2.moeda(moeda2.aumentar(p, 10))}')
print(f'Baixando o preço em 20% → {moeda2.moeda(moeda2.diminuir(p, 20))}')
