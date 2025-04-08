email = input("Digite seu email: ")

arroba = int(email.find("@"))
ponto = int(email.find("."))
espaco = email.count(" ")


if arroba < ponto and espaco == 0:
    print("Email valido")
else:
    print("Email invalido")