salario = float(input("Digite o valor do salario "))
nsalario = salario + (salario * 15 / 100)
print(f"O novo salario é de R${nsalario:.2f}")


print("*-"*30)
print("-*"*30)


salario = float(input("Digite o valor do salario "))
if salario > 1250:
    nsalario = salario + (salario * 10 / 100)
    print(f"O novo salario é de R${nsalario:.2f}")
else:
    print(f"O novo salario é de R${salario*1.15:.2f}")