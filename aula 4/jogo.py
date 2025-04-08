import random
import time
import sys


naipes = "♦️♥️♠️♣️"
extras = "JQKA"

baralho = []

#cria uma função pythin

def monta_baralho():
    for i in range(2,11):
        for naipe in naipes:
            baralho.append(str(i)+naipe)
    
    for extra in extras:
        for naipe in naipes:
            baralho.append(extra+naipe)
            
#chama a função
monta_baralho()
# print(baralho)

# função que recebe o parametro /argumento carta
def pontos_carta(carta):
    # se tam da carta é 3: so pode ser 10
    if len(carta) == 3:
        valor = 10
    #Se 1 caracter da cara for um num o valor e o num    
    elif carta [0].isdigit():
        valor = int(carta[0])
        # se for AS, vale 11
    elif carta [0] == "A":
        valor = 11
    # senão, so pode ser as letras JQK Valem 10
    else:
        valor = 10
    return valor

pontos_jogador = 0
contador = 0
while True:
    #gera um numero aleatório entre 0 e o tam do bnaralho
    num = random.randint(0, len(baralho)-1)
    #Obtém e retira a cara do baralho
    carta = baralho.pop(num) 
    contador += 1
    print(f"Sua {contador}ª Carta é: {carta}")
    time.sleep(2)

    pontos_jogador += pontos_carta (carta)
    
    if pontos_jogador > 21:
        break
    
    if contador >= 2:
        outra = input('Deseja outra carta (S/N)?')
        if outra.upper() == 'N':
            break
        
print()
print("="*40)
print(f'Total de pontos do Jogador: {pontos_jogador}')
print("="*40)

if pontos_jogador > 21:
    print("Você perdeu!")
    sys.exit()



pontos_pc = 0
contador = 0
while True:
    #gera um numero aleatório entre 0 e o tam do bnaralho
    num = random.randint(0, len(baralho)-1)
    #Obtém e retira a cara do baralho
    carta = baralho.pop(num) 
    contador += 1
    print(f"{contador}ª Carta do Computador é: {carta}")
    time.sleep(2)

    pontos_pc += pontos_carta (carta)
    
    if pontos_pc > 21 or pontos_pc >= pontos_jogador:
        break
    
    if contador >= 2:
        outra = input('Deseja outra carta (S/N)?')
        if outra.upper() == 'N':
            break
        
print()
print("="*40)
print(f'Total de pontos do PC: {pontos_pc}')
print("="*40)

if pontos_pc > 21:
    print("Você ganhou!")
elif pontos_pc == pontos_jogador:
    print("Empate!")
else:
    print("Você perdeu!")