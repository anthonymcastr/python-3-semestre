palavra = input("Digite uma palavra: ")

first_letra = palavra[0]



acertos = ['_' if letra != first_letra else first_letra for letra in palavra]



print(" ".join(acertos))
print(f"A letra '{first_letra}' aparece {palavra.count(first_letra)} vezes.")




