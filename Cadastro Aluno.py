
entrada = 0
print("Digite 1 para CADASTRO.")
print("Digite 2 para LISTA DE ALUNOS.")
print("Digite 3 para EXCLUIR ALUNO.")
entrada = int(input())
ContadorAluno = 0
if entrada == 1:
    aluno[ContadorAluno] = input("Digite o Nome do Aluno: ")
    nota[ContadorAluno] = input("Digite a Nota do Aluno: ")
    print("Deseja Cadastrar outro aluno ?")
    input()