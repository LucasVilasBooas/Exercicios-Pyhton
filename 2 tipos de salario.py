salario = float(input('Digite o valor do salario '))
if salario > 1250:
    salario = salario * 1.10
    print(f"O novo salario é R${salario:.2f}")
else:
    salario = salario * 1.15
    print(f"O novo salario é R${salario:.2f}")