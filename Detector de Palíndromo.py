frase = str(input("Digite uma frase ")).strip().upper() # strip tira os espaços  // upper deixa tudo em maiusculo
palavras = frase.split() # separou as palavras em um vetor
junto = "".join(palavras) # juntou as palavras em uma "palavra" so
inverso = ""
for letra in range (len(junto)-1, -1, -1): # pode substituir o for por -> inverso = junto[::-]
    inverso = inverso + junto[letra]
print(f"Voce digitou {inverso}")
print(f"o inverso é {inverso}")
if inverso == junto :
    print("é palindromo")
else:
    print("nao é palindromo")



