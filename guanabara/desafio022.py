nome = input("Qual seu nome? ")

primeiro_nome = nome.split()[0]
sobre_nome = nome.split()[-1]
letras_primeiro_nome = len(primeiro_nome)

nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()




print(f"Olá, {nome}")

print(f"Seu primeiro nome é {primeiro_nome} e ele tem {letras_primeiro_nome} letras.")
print(f"Seu sobrenome é {sobre_nome} e ele tem {len(sobre_nome)} letras.")
