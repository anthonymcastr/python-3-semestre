cidade = input("Qual sua cidade? ")

cidade = cidade.split()
cidade = cidade[0]

if cidade.lower() == "santo":
    print("Sua cidade começa com Santo")

else:
    print("Sua cidade não começa com Santo")