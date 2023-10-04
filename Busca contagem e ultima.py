frase = str(input("Digite uma frase:\n")).strip()
print(f"A letra A aparece {frase.lower().count('a')} vezes")
print('*-' * 20)
print(f'A primeira A apareceu na posição {frase.lower().find("a")+1}') # o +1 foi coloado para devido contar a primeira posição no numero 0
print(f'A ultima letra A apareceu na posição {frase.lower().rfind("a")+1} ') # o +1 segue a mesma idea
