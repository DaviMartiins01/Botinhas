import json

def MyToken():
    with open("token.json", "r") as arquivo:
        dado_token = json.load(arquivo)

    token = dado_token["TOKEN"]

    return token
