import requests

base_url = "https://api.jikan.moe/v4"

#Função que encontra o anime q saiu na TV pelo nome
def search_TVAnime(anime_name):
    url = f"{base_url}/anime?q={anime_name}"

    #Pega todos os títulos achados com o nome que o usuário colocou
    anime_data = requests.get(url).json()

    #Seleciona apenas animes que saíram na tv e que o score existe.
    for anime_info in anime_data["data"]:
        if anime_info["type"] == "TV":
            if str(anime_info["score"]) != "None":
                return anime_info


#Função que retorna todos os animes da temporada atual
def searchSeasonAnime():
     url = f"{base_url}/seasons/now"
     season_data = requests.get(url).json()

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
                "score" : str(days["score"]),
                "synopsis" : days["synopsis"]
            }

            thisDayAnimes.append(anime_info)

#Retorna um dicionários com todos o anime do dia e a suas informações
    return thisDayAnimes

#Retorna todas as recomendações do mal pro anime específico
def searchRecommendations(id):
    url = f"{base_url}/anime/{id}/recommendations"
    total_recs = requests.get(url).json()
    return total_recs["data"]

#Separa as 10 primeiras recomendações
def topRecommendations(total_recs):
    x = 0
    topRecommendations = []

    for rec in total_recs:
        recommendation = rec["entry"]
        if x < 10:
            recs_info =  {
                "image" : recommendation["images"]["jpg"]["image_url"],
                "title" : recommendation["title"]
            }
            topRecommendations.append(recs_info)
            x += 1

    return topRecommendations
