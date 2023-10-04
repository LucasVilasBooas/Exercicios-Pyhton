from datetime import date
ano  = int(input("Digite o ano que queira consultar. Para o ano atual digite 0. "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"o ano de {ano} é bissexto")
else:
    print(f"o ano de {ano} nao é bissexto")