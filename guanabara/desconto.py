print("Digite o valor do produto e vamos lhe dar 5% de desconto")


valor = float(input("Digite o valor do produto: "))
desconto = valor * 0.05
valor_final = valor - desconto

print(f"O valor do produto com desconto é R$: {valor_final:.2f}")