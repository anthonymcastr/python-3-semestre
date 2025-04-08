import random

print("Vamos realizar um sorteio para ordenar a lista de alunos.")
print("Digite o nome de cada aluno e pressione Enter. Escreva SAIR para finalizar a lista.")
print("")

alunos = []

while len(alunos) < 4:  
    nomes = input("Aluno: ").upper()
    
    if nomes == "SAIR":  
        break
    
    alunos.append(nomes)

if len(alunos) > 0: 
    print("A ordem de apresentação será:")
    print(random.sample(alunos, len(alunos)))
else:
    print("Nenhum aluno foi adicionado.")
