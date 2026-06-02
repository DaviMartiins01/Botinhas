import json

def MyToken():
    with open("token.json", "r") as arquivo:
        dado_token = json.load(arquivo)

    token = dado_token["TOKEN"]

    return token

def Emoji_Reaction(Choose_emoji_List_or_dictionary):
    with open("emoji_reaction.json", "r", encoding="utf-8") as arquivo:
        dados_emoji = json.load(arquivo)

    if(Choose_emoji_List_or_dictionary == "dictionary"):
        return dados_emoji
    else:
        return list(dados_emoji.keys())