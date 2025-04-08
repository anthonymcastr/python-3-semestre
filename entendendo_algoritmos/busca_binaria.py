lista = [1, 3, 5, 7, 9]
chute = int(input("Digite um número: "))
n_certo = lista[2]  
n_tentativas = 0

while chute != n_certo:
    n_tentativas += 1
    if chute < n_certo:
        print("Seu chute é menor que o número correto")
        
    elif chute > n_certo:
        print("Seu chute é maior que o número correto")
    chute = int(input("Digite um número: "))  

print("Parabéns! Você acertou o número correto")
print("Número de tentativas: ", n_tentativas)



