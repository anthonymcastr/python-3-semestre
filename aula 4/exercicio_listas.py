contas = []
valores = []
escolha = 0
print("Sistema de controle de contas")

print("Escolha uma opção")
print("1 - Incluir conta")
print("2 - Listar contas")
print("3 - Listar contas em ordem")
print("4 - Pesquisar conta")
print("5 - Excluir conta")
print("6 - Finalizar")



while escolha != 6 :
    escolha = int(input("Opção: "))
    if escolha ==  1:
        
        conta = input("Digite o nome da conta: ").upper()
        contas.append(conta)
        valor = float(input("Digite o valor da conta: "))
        valores.append(valor)
        print("Conta adicionada com sucesso")
        
    elif escolha == 2:
        print("Contas cadastradas:")
        for i in range(len(contas)):
            print(f"Conta: {contas[i]}, Valor: {valores[i]}")

    elif escolha == 3:
        listas_ordenadas = sorted(zip(contas, valores))
        listas_ordenadas.sort()
        print("Contas cadastradas, em ordem:")
        for item in listas_ordenadas:
            print(item)
    elif escolha == 4:
        pesquisa = input("Digite o número da conta que deseja pesquisar: ").upper()
        if pesquisa in contas:
            index = contas.index(pesquisa)
            print(f"Conta: {contas[index]}, Valor: {valores[index]}")
        else:
            print("Conta não encontrada")
    elif escolha == 5:
        excluir_item = input("Digite o número da conta que deseja excluir: ")

        if excluir_item in contas:
            contas.remove(excluir_item)
            print("Conta excluída com sucesso")
    elif escolha != 6 and escolha > 6 or escolha < 1:
        print("Opção inválida, digite novamente")
    else:
        print("Sistema finalizado")
        break



