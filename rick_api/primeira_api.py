import requests


def fetch_data(endpoit, filters={}):
   url = f"https://rickandmortyapi.com/api/{endpoit}"
   response = requests.get(url, params=filters)

   return response.json() if response.status_code == 200 else None


   


characters = fetch_data("character", {"name": "Rick"})

if characters:
 print(characters)
else: 
  print("Failed to fetch data")



if characters:
    for character in characters['results']:  # 'results' contém a lista de personagens encontrados
        print(f"Nome: {character['name']}")
        print(f"Status: {character['status']}")
        print(f"Espécie: {character['species']}")
        print(f"Gênero: {character['gender']}")
        print(f"Imagem: {character['image']}")
        print("-----")
else:
    print("Falha ao buscar os dados")


