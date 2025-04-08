aluno_nome = input("Digite seu nome completo: ")

composto = aluno_nome.split(" ")

numero = int(len(composto))


if numero > 1 and aluno_nome.find(" "):
    print(f"Seu nome é {aluno_nome}")
else:
    print("Digita teu nome completo infeliz")


