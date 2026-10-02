boletim = {}

while True:
resposta = input("Deseja adicionar um aluno? (sim/não): ")

if resposta.lower() == "não":
break

nome = input("Digite o nome do aluno: ")
nota = float(input("Digite a nota do aluno: "))
