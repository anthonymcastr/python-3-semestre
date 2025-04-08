import math

def numero_perfeito(n):
    if n <= 1:
        return False  
    
    soma_divisores = 1  
    
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: 
            soma_divisores += i
            if i != n // i:  
                soma_divisores += n // i
    
    return soma_divisores == n  


numero = input("Digite um número inteiro: ")
numero = int(numero)
if numero_perfeito(numero):
    print(f"{numero} é um número perfeito.")
else:
    print(f"{numero} não é um número perfeito.")