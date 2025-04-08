print("Vamos calcular o preço a ser pago pelo aluguel de um veiculo")

carro = input("Digite a marca do carro: ").upper()
dias = int(input("Digite a quantidade de dias que o carro foi alugado: "))
km = float(input("Digite a quantidade de km rodados: "))


if carro == "CHEVROLET":
    preco = (dias * 60) + (km * 0.15)
    print(f"O preço a ser pago pelo aluguel do carro é R$: {preco:.2f}")

elif carro == "FIAT":
    preco = (dias * 50) + (km * 0.10)
    print(f"O preço a ser pago pelo aluguel do carro é R$: {preco:.2f}")

elif carro == "FORD":
    preco = (dias * 40) + (km * 0.05)
    print(f"O preço a ser pago pelo aluguel do carro é R$: {preco:.2f}")

