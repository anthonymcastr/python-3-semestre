


palavra = input("Palavra: ")
letra = input("Letra: ")


if letra in palavra:
    print("A letra está na palavra.")
else:
    print("A letra não está na palavra.")


    posicao = palavra.find(letra)

    if posicao == -1:
        print("A letra não está na palavra.")
        print(f"A letra está na posição {posicao}.")
    else:
        print("A letra não está na palavra")