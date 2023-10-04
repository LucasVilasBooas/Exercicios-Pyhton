from math import hypot
co = float(input("Digite o valor do Cateto Oposto: "))
ca = float(input("Digite o valor do Cateto Adjacente: "))
hi = hypot(co, ca)
print(f"O valor da hipotenusa é de {hi:.2f}")