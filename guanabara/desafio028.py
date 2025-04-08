import random

numero_aleatorio = random.randint(1, 5)
chute = int(input('Escolha um número de 1 a 5: '))

while numero_aleatorio != chute:
    if chute < numero_aleatorio:
        print('Você escolheu um número menor que o número aleatório!')
    else:
        print('Você escolheu um número maior que o número aleatório!')
    
    chute = int(input('Escolha um número de 1 a 5: '))

print("Parabéns! Você acertou o número aleatório!")

    


