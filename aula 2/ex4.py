
numero_chinchilas = int(input("Número de chinchilas: "))
anos_criacao = int(input("Anos de criação: "))


if numero_chinchilas < 2:
    print("Número de chinchilas inválido, é necessário um casal de chinchilas para procriar!")
    exit()





chinchilas = numero_chinchilas

for ano in range(1, anos_criacao + 1):
        print(f"{ano}º Ano: {chinchilas} chinchilas")
        chinchilas *= 3 




