


num_pessoas = int(input("Nº Pessoas: "))
num_peixes = int(input("Nº Peixes: "))


custo_por_pessoa = 20.00
custo_peixe_extra = 12.00


valor_entrada = num_pessoas * custo_por_pessoa
peixes_extras = max(0, num_peixes - num_pessoas)
valor_peixes_extras = peixes_extras * custo_peixe_extra
valor_total = valor_entrada + valor_peixes_extras


print(f"Pagar R$: {valor_total:.2f}")

