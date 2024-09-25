## Crie um programa que receba uma lista com os nomes dos alunos presentes em uma aula e exiba quantos alunos
#  estão presentes e a lista dos nomes.
#  Se o total de alunos presentes for menor que 5, exiba uma mensagem sugerindo uma revisão da lista de chamada.
alunos = []
while True:
    nm_alunos = input("Digite o nome de um aluno (ou '0' para sair): ")
    if nm_alunos == "0":
        break
    alunos.append(nm_alunos)  

total_presentes = len(alunos)
print(f"Alunos presentes: {total_presentes}")
print("Lista de alunos presentes:")

alunos_presentes = alunos
print(alunos_presentes)


if total_presentes < 5:
    print("AVISO: A quantidade de alunos presentes é inferior a 5. Considere revisar a lista de chamadas.")
