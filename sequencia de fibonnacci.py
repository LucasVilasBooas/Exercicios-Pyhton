print("="*10)
print("Sequencia de Fibo")
print("="*10)
n = int(input("Digite quantos termos vc quer mostrar: "))
t1 = 0
t2 = 1
c = 3
print(f"{t1}->{t2}->", end="")
while c <= n:
    t3 = t1 + t2
    print(f"{t3}->", end="")
    t2 = t3
    t1 = t2
    c += 1
print("FIM")
print("~~~~~FIM DO PROGRAMA~~~~")