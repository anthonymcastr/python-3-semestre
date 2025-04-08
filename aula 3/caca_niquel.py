import random 
import time


import pygame

pygame.init()
pygame.mixer.music.load('musica123.mp3')
pygame.mixer.music.play()
pygame.event.wait()


print("BEM VINDO AO JOGO DO TIGRINHO, miauuuu")
nome = input("Digite seu nome trouxa: ")
valor = float(input("Digite o valor da aposta: "))

caixa = 1000 + valor



input("Pressione Enter para iniciar o jogo....")
print("Tá pagando muito....")

figuras = "🍒🍋🌭"
jogo = ""

print("Suas apostas: ", end="")

for _ in range(3):
    num = random.randint(0, 2)
    print(figuras[num], end="", flush=True)
    time.sleep(1)
    jogo = jogo + figuras[num]



print()
if jogo [0] == jogo[1] and jogo[1] == jogo[2]:
    print("Parabéns, você ganhou! Deposita mais, tá pagando")
    print(f"Seu prêmio é de R${valor * 5:.2f}")
    caixa =+ valor * 5
elif jogo[0] == jogo[1] or jogo[1] == jogo[2] or jogo[0] == jogo[2]:
    print("Parabéns, você ganhou! Deposita mais, tá pagando")
    print(f"Seu prêmio é de R${valor * 3:.2f}")
    caixa =+ valor * 3
else:
    print("Que pena, você perdeu! Deposita mais, tá pagando")
    print(f"Você perdeu R${valor:.2f}")
    print("Tente novamente!")
    caixa =- valor 



