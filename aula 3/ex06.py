import random
import time

print("Bem vindo ao CRAPS! A seguir, aperte a tecla ENTER para jogar os dados")
input()

dado1 = int(random.randint(1, 6))
dado2 = int(random.randint(1, 6))

soma = dado1 + dado2
primeiro_resultado = soma

print(f"Você tirou {soma}", flush=True)
time.sleep(1)

if soma == 7 or soma == 11:
    print(f"Você tirou {soma}, ou seja, um natural.. parabéns você ganhou")
else:
    while True:
        print("Pressione ENTER para jogar os dados novamente")
        input()
        dado1 = int(random.randint(1, 6))
        dado2 = int(random.randint(1, 6))

        soma = dado1 + dado2
        print(f"Você tirou {soma}", flush=True)
        time.sleep(1)

        if soma == 7:
            print("Você perdeu")
            break
        elif soma == primeiro_resultado:
            print("Você ganhou")
            break
