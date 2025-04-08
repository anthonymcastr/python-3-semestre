# Elaborar um programa que leia e informe se a senha é valida ou não, p validar ela tem q ter letra maiuscula, minuscula, numero e de 8 a 12 caracteres


input = input("Digite a senha: ")

if len(input) < 8 or len(input) > 12 or not any(char.isupper() for char in input) or not any(char.islower() for char in input) or not any(char.isdigit() for char in input):
    print("Senha invalida")
else:
    print("Senha valida")