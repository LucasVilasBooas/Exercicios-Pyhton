frase = str(input('Digite uma frase\n')).upper().strip()
print(f"A letra a aparece {frase.count('A')} na frase")
print(f"A primeira letra A apareceu na posição {frase.find('A')+1}")
print(f"A ultima letra A aparece na posição {frase.rfind('A')+1}")
