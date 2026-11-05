produtos = [
    {"nome": "Camisa", "preco": 45},
    {"nome": "Calça", "preco": 80},
    {"nome": "Boné", "preco": 30}
]

for produto in produtos:
    if produto["preco"] > 50:
        print(produto["nome"])
