n = int(input("Digite um numero para ver a tabuada: "))
while True:
    for c in range (0,11):
        print(f"{n}x{c}= {n * c}")

    if n < 0:
        break
    n = int(input("Quer ver a tabuada de qual valor?  "))
print(">>>FIM DA TABUADA<<<<")