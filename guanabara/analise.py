frase = ('Curso em video Python')


print(frase.count("o")) # Conta quantas vezes a letra "o" aparece na frase
print(frase.count("o", 0, 13)) # Conta quantas vezes a letra "o" aparece na frase do 0 ao 13
print(frase.find("deo")) # Procura a palavra "deo" e retorna a posição da primeira letra
print(frase.find("Android")) # Se a palavra não existir, retorna -1
print('Curso' in frase) # Retorna True se a palavra existir na frase


print(frase.replace("Python", "Android")) # Substitui a palavra Python por Android
print(frase.upper()) # Transforma todas as letras em maiúsculas
print(frase.lower()) # Transforma todas as letras em minúsculas
print(frase.capitalize()) # Transforma a primeira letra em maiúscula
print(frase.title()) # Transforma a primeira letra de cada palavra em maiúscula
print(frase.strip()) # Remove espaços inúteis no início e no fim da frase
print(frase.rstrip()) # Remove espaços inúteis no final da frase
print(frase.lstrip()) # Remove espaços inúteis no início da frase