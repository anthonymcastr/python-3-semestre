import random 
import time 
import os 

temp = "😁😁🤣🤣😎😎😍😍🥰🥰🤩🤩🤔🤔😥😥"
figuras = list(temp)

jogo = []
apostas = []
pontuacao_total = 0

def preenche_matriz():
    for i in range(4):
        jogo.append([])
        apostas.append([])
        for _ in range(4):
            num = random.randint(0, len(figuras)-1)
            jogo[i].append(figuras[num])
            apostas[i].append("🔶")
            figuras.pop(num)




def mostra_tabuleiro():
    os.system("cls")
    print("    1   2   3   4")
    for i in range(4):
        print(f"{i+1} ", end="")
        for j in range(4):
            print(f" {jogo[i][j]} ", end="")
        
        print("\n")

    print("Memorize a posição dos bichos...")
    time.sleep(2)

    print("Contagem regressiva...")
    for i in range(10, 0, -1):
        print(i, end=" ", flush=True)
        time.sleep(1)

    os.system("cls")




def mostra_cartas_e_acertos():
    os.system("cls")
    print("    1   2   3   4\n")
    for i in range(4):
        print(f"{i+1} ", end="")
        for j in range(4):
            print(f" {apostas[i][j]} ", end="")
        
        print("\n")    

preenche_matriz()
mostra_tabuleiro()
mostra_cartas_e_acertos()




def aposta_coordenada(num):
    while True:
        mostra_cartas_e_acertos()
        posicao = input(f"{num}ª Coordenada (2 números: linha e coluna): ")
        if len(posicao) != 2:
            print("Informe uma dezena, por exemplo , 12, 21, 32, 24...")
            time.sleep(2)
            continue
        x = int(posicao[0]) - 1
        y = int(posicao[1]) - 1


        try:
             if apostas[x][y] == "🔶":
                apostas[x][y] = jogo[x][y]
                break
             else:
                print("Essa coordenada já foi escolhida, tente novamente")
                time.sleep(2)
                continue
             

        except IndexError:
            print("Erro... coordenada inválida, tente novamente")
            time.sleep(2)
            continue


    return x, y


# ------------------------------------- Código do Programa Principal -------------------------------------
while True:
    pontuacao = 0
    x1, y1 = aposta_coordenada(1)
    x2, y2 = aposta_coordenada(2)
    mostra_cartas_e_acertos()

    if apostas [x1][y1] == apostas[x2][y2]:
        pontuacao += 1
        pontuacao_total += pontuacao
        print("Parabéns, você acertou!")
        print(f"Você fez {pontuacao} ponto(s) nesta rodada")
        print(f"Você tem {pontuacao_total} ponto(s) no total")
        time.sleep(2)

        
    else:
        pontuacao -= 1
        pontuacao_total += pontuacao
        print("Errou... Tente novamente.")    
        print(f"Você tem {pontuacao_total} ponto(s) no total")
        apostas[x1][y1] = "🔶"
        apostas[x2][y2] = "🔶"
        



        continuar = input("Deseja continuar (S/N)? ").upper()
        if continuar != "S":
            break