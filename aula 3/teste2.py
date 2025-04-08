cidade = input("Cidade: ")


partes = cidade.split(" ")


print(f"O nome da cidade é {partes[0]}")


for parte in partes:
    print(parte)