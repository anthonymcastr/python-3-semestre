palavra = input("Digite uma palavra: ")


inverso = palavra[::-1]

if palavra == inverso:
    print("É palíndromo")
else:   
    print("Não é palíndromo")