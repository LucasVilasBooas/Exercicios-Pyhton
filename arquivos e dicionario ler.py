f = open (r'C:\Users\Lucas\PycharmProjects\pythonProject\aula de arquivos/x.txt')
for linha in f.readlines():
    print(linha.strip())
f.close()
