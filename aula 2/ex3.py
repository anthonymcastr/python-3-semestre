
produto = input("Produto: ")
n_etiquetas = int(input("Nº de Etiquetas: "))


contador = 0


for i in range(n_etiquetas):
    print(produto, end=" ")  
    contador += 1

   
    if contador == 2:
        print()  
        contador = 0  




