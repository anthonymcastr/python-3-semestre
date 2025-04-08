# Elaborar um programa que leia ‘n’ números, até ser digitado 0. Ao final, exiba quantos números
# foram digitados, a soma dos números e qual o maior número digitado


print("Informe os números ou 0 para sair do loop")

numeros = int(input("Digite um número: "))
quantidade = 0
soma = 0 
maior = 0



while numeros != 0:
    quantidade += 1
    soma += numeros
    numeros = int(input("Digite um número: "))
    if numeros > maior:
        maior = numeros


    if numeros == 0:
        print(f"Quantidade de números digitados: {quantidade}")
        print(f"Soma dos números digitados: {soma}")
        print(f"Maior número digitado: {maior}")
        break
