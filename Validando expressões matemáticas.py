expr = str(input("Digite uma expressao →"))
n1 = n2 = 0
for c in expr:
    if c == '(':
        n1 += 1
    elif c ==')':
        n2 += 1
if n1 - n2 == 0:
    print("Expressao correta")
else:
    print("Expressao incorreta")



#→→→→→GUANABARA←←←←←←
expr = str(input("Digite uma expressao →"))
pilha = []
for sim in expr:
    if sim == '(':
        pilha.append('(')
    elif sim == ')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print("Expressao correta")
else:
    print("Expressao incorreta")