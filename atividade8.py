produtos = [
{"nome": "Camisa", "preco": 45},
{"nome": "Calça", "preco": 80},
{"nome": "Boné", "preco": 30}
]

if produto["preco"] > 50:
    for produto in produtos:
        print(produto["nome"])
