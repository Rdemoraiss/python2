boletim = {}

while True:
    resposta = input("Deseja adicionar um aluno? (sim/não): ")

    if resposta.lower() == "não":
        break

    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    
    boletim[nome] = nota

    if nota >= 6.0:
        print(f"O aluno {nome} está Aprovado!")
    else:
        print(f"O aluno {nome} está Reprovado!")
        
    print() 
