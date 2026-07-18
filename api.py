import requests
cep = input("Digite seu cep sem pontos e virgulas:")
url = f"https://viacep.com.br/ws/{cep}/json/"

dados = requests.get(url)

endereco = dados.json()

print(endereco)

print(f"Voce mora no bairro {endereco["bairro"]}, voce mora na rua {endereco["logradouro"]}, o seu cep é {endereco["cep"]}, O seu ddd é {endereco["ddd"]},o seu estado é {endereco["estado"]},sua localidade é {endereco["localidade"]}")
# print(f"Voce mora na rua {endereco["logradouro"]}")
# print(f"O seu cep é {endereco["cep"]}")
# print(f"Voce mora no estado de {endereco["estado"]}")

