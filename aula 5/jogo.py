import random
import time 
import os # pacote com funçoes do sistema operacional

nome = input("Informe seu nome: ").upper() # transforma o nome em maiúsculo
print(f"Olá {nome}, seja bem-vindo ao jogo da memória!")
time.sleep(3) # espera 3 segundos

temp = "🐸🐸🐻🐻🐯🐯🐵🐵🐮🐮🐼🐼🐷🐷🐔🐔"
figuras = list(temp) # transforma a string em uma lista de caracteres

jogo = [] # lista que vai armazenar os pares de figuras
apostas = [] # lista que vai armazenar os pares de 

def preenche_matriz():
    for i in range(4): #4 linhas
        jogo.append([])
        apostas.append([])
        for _ in range(4):
            num = random.randint(0, len(figuras)-1) # sorteia um número entre 0 e o tamanho da lista figuras
            jogo[i].append(figuras[num])
            apostas[i].append("🟥")
            figuras.pop(num) # remove o número sorteado da lista figuras para não repetir   

def mostra_tabuleiro():
    os.system("cls") # limpa a tela
    print("    1   2   3   4")
    for i in range(4):
        print(f"{i+1} ", end="")
        for j in range(4):
            print(f" {jogo[i][j]} ", end="")
        print("\n") # tem que colar na mesma linha do for

    print("Memorize o tabuleiro!")
    time.sleep(2) # espera 5 segundos

    print("Contagem regressiva para começar o jogo! " , end="")
    for i in range(10, 0, -1): # contagem regressiva de 10 a 1
        print(i, end=" ", flush=True) # flush=True para não pular linha
        time.sleep(1) # espera 1 segundo
    os.system("cls") # limpa a tela novamente 
    
def mostra_cartas_e_acertos():
    os.system("cls") # limpa a tela
    print("    1   2   3   4")
    for i in range(4):
        print(f"{i+1} ", end="")
        for j in range(4):
            print(f" {apostas[i][j]} ", end="")
        print("\n") # tem que colar na mesma linha do for      

preenche_matriz()
mostra_tabuleiro()
mostra_cartas_e_acertos()

def aposta_coordenada(num):
    while True:
        mostra_cartas_e_acertos()
        posicao1 = input(f"{num}ª Coordenada (2 numeros: linha e coluna): ")
        if len(posicao1) != 2:
            print("Informe uma dexena, por exemplo, 12, 13, 24,...")
            time.sleep(2)
            continue # volta para o começo do while
        x = int(posicao1[0]) - 1 # linha ex:34
        y = int(posicao1[1]) - 1 # coluna ex:34
        try:
            if apostas[x][y] == "🟥":
                apostas[x][y] = jogo[x][y] # coloca o valor da carta na aposta
                break # sai do while
            else:
                print("Essa coordenada já foi escolhida!")
                time.sleep(2)

        except IndexError:
            print("Erro... Coordenada Invalida!")
            time.sleep(2)
    return x, y # retorna a coordenada escolhida

def verifica_vencedor():
    contador = 0 # contador de acertos
    for i in range(4):
        for j in range(4):
            if apostas[i][j] == "🟥":
                contador += 1
    return contador             

# ------------------------codigo do prorama principal      

while True:
    x1, y1 = aposta_coordenada(1) 
    x2, y2 = aposta_coordenada(2) 
    mostra_cartas_e_acertos()

    if apostas[x1][y1] == apostas[x2][y2]: # verifica se as cartas são iguais 
        print("Você acertou!")
        cartas_viradas = verifica_vencedor() # verifica se o jogador ganhou
        if cartas_viradas == 0:
            print(f"Parabéns {nome} ! Você ganhou! 🏆")
            break #  sai do jogo
        else:
            print(f"Falta(m) {cartas_viradas//2} cartas para virar!")
            time.sleep(2) 
    else:
        print("Você errou!")
        time.sleep(2)
        apostas[x1][y1] = "🟥" # volta a ser o quadrado
        apostas[x2][y2] = "🟥" 

        continuar = input("Deseja continuar o jogo? (S/N): ").upper()
        if continuar != "S": # se o jogador não quiser continuar, sai do loop
            break
          

aposta_coordenada()
mostra_cartas_e_acertos()

#--------------------------------
# Exercicios:
# 1- Solicitar o nome do usuario no inicio
# 2- Definir uma pontuação para acertos +10 e -5 para erros
# 3- No final mostrar a pontuação obtida pelo jogador
# 4- Obter data e hora do sistema no inicio do jogo e no final, mostrar durante o jogo
# 5- Salvar nome, pontuação e duração em arquivo texto
# 6- Classificar e mostrar o ranking

