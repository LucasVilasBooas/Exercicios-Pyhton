x = int(input("Digite um numero: "))
tot = 0
for c in range (1, x+1):
    if x % c == 0:
        print(f"\33[34m{c}", end=" ")
        tot += 1
    else:
        print(f"\33[m{c}", end=" ")
print(f"\n\33[mO numero {x} foi divisivel {tot} vezes")
if tot ==2:
    print("e por isso ele é primo")
else:
    print("E por isso ele nao é primo")
