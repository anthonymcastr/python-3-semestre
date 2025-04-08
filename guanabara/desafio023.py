numero = int(input("Digite um número: "))

numero = str(numero)

if len(numero) > 4 or len(numero) < 0:
    print("Número inválido, digite um número de 0 até 9999")
elif len(numero) == 1:
   print(f"1º: {numero[0]}") 
elif len(numero) == 2:
    print(f"1º: {numero[0]}\n2º: {numero[1]}")
elif len(numero) == 3:
    print(f"1º: {numero[0]}\n2º: {numero[1]}\n3º: {numero[2]}")
elif len(numero) == 4:
    print(f"1º: {numero[0]}\n2º: {numero[1]}\n3º: {numero[2]}\n4º: {numero[3]}")
else:
    print("Número inválido, digite um número de 0 até 9999")