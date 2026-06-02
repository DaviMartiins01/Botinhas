import requests
import ReadingJson
import time

base_url = "https://api.jikan.moe/v4"

#Função que encontra o anime q saiu na TV pelo nome
def search_TVAnime(anime_name):
    start = time.time()

    url = f"{base_url}/anime?q={anime_name}"

    #Pega todos os títulos achados com o nome que o usuário colocou
    anime_data = requests.get(url).json()
    print(f"Tempo da Jikan API no request (por nome): {time.time() - start:.2f} segundos")
    #Seleciona apenas animes que saíram na tv e que o score existe.
    for anime_info in anime_data["data"]:
        if anime_info["type"] == "TV":
            if str(anime_info["score"]) != "None":
                return anime_info


#Função que retorna todos os animes da temporada atual
def searchSeasonAnime():
     start = time.time()
     url = f"{base_url}/seasons/now"
     season_data = requests.get(url).json()
     print(f"Tempo da Jikan API pra pegar dados da season: {time.time() - start:.2f} segundos")
     return season_data["data"]

#Função que utiliza os dados da temporada atual e separa por dia da semana escolhido.
def weeklyAnime(season_data, thisDay):
    thisDayAnimes = []

    #loop que encontra o dia da semana desejado e pega informações de todos os animes desse dia
    for days in season_data:
        if days["broadcast"]["day"] == thisDay:
            #pega as informações dos animes do dia correspondente a váriavel thisDay
            anime_info = {
                "image" : days["images"]["jpg"]["image_url"],
                "title" : days["title"],
            }

            thisDayAnimes.append(anime_info)

    #Retorna um dicionários com todos o anime do dia e a suas informações
    return thisDayAnimes

#Retorna as 10 primeiras recomendações do mal do anime que o usuário escolheu
def get_top_recommendations(anime_id, limit=10):
    start = time.time()
    url = f"{base_url}/anime/{anime_id}/recommendations"
    total_recs = requests.get(url).json()
    print(f"Tempo da Jikan API no request (ID): {time.time() - start:.2f} segundos")
    #pega só as 10 primeiras recomendações
    return total_recs["data"][:limit]



def get_reaction_id(user_reaction):
    #Linka um dos emojis possíveis que o usuário pode reagir a um id.
    anime_reaction_emoji_id = ReadingJson.Emoji_Reaction("dictionary")

    for anime_emoji in anime_reaction_emoji_id.items():
        #faz a comparação dos emojis
        if user_reaction == anime_emoji[0]:
            #retorna o id
            return anime_emoji[1]

    return -1
