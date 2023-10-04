n = str(input("digite seu nome completo: \n")).strip()
nome = n.split()
print(f"Bem vindo {nome[0]}")
print(f"Seu primeiro nome é {nome[0]}")
print(f"Seu ultimo nome é {nome[len(nome)-1]}") # len faz a contagem e o -1 ajusta a posição que sempre começa com o 0
