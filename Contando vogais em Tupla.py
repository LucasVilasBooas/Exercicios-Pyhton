palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'Na palavra {p.upper()} temos', end=" ")
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=" ")
    print()