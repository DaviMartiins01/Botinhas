import discord
import Answers
import FormatInput

def title_TVAnimesearch_message(anime_title):
    try:
        #Vai na função search_TVAnime pegar informações sobre o anime que o usuário pediu
        search_results = Answers.search_TVAnime(anime_title)

        #Cria um embed utilizando as informações dentro da variável search_results
        embed_TVAnime = discord.Embed(
            title= f"**{search_results["title"]}**",
            description=f"⭐ Score: {search_results["score"]} ({search_results["members"]} Members)",
            color=discord.Color.dark_blue()
        )

        #Adicionando diferentes fields
        embed_TVAnime.add_field(
            name="Synopsis",
            #value=search_results["synopsis"],
            value= "Finge que tem uma sinopse muito maneira aqui, daquelas que te fazem querer largar tudo só pra descobrir o que acontece no próximo capítulo. Uma história cheia de mistério, personagens memoráveis, reviravoltas inesperadas e momentos que vão te fazer rir, sofrer e ficar olhando pro teto depois. Tem ação, emoção, talvez um trauma psicológico leve, e aquela sensação de ‘só mais um capítulo’ às três da manhã. Enfim… imagina a melhor sinopse possível. É essa.",
            inline=False
        )


        embed_TVAnime.add_field(
            name = "📺 Type",
            value= search_results["type"]
        )

        embed_TVAnime.add_field(
            name="📆 Year",
            value=search_results["year"]
        )

        embed_TVAnime.add_field(
            name="🎬 Episodes",
            value=search_results["episodes"]
        )

        embed_TVAnime.add_field(
            name="📊 Status",
            value=search_results["status"]
        )

        embed_TVAnime.add_field(
             name="🎭 Genres",
             value=search_results["genres"][0]["name"]
         )

        embed_TVAnime.add_field(
            name="⏳ Duration",
            value=search_results["duration"]
        )

        embed_TVAnime.set_footer(
            text="Source: MyAnimeList"
        )

        #Coloca a foto no embed usando a variável search_results
        embed_TVAnime.set_thumbnail(url=search_results["images"]["jpg"]["image_url"])

        #retorna o embed
        return embed_TVAnime

    except Exception as error:
        #Se não achar o anime retorna um embed de erro
        print(error)
        embed_Error = discord.Embed(
            title= "Não foi possível achar o seu anime",
            color=discord.Color.dark_red()
        )
        return embed_Error

def embed_top_recommendation(user_anime):

    #Pega o anime escolhido pelo usuário
    anime_id = Answers.search_TVAnime(user_anime)

    # Pega as recomendações do anime usando o id dele
    get_recommendations = Answers.searchRecommendations(anime_id["mal_id"])

    # Separa as 10 primeiras recomendações
    top_recs = Answers.topRecommendations(get_recommendations)

    embed_recommendation = discord.Embed(
        title= "🔥 **Top Recommendations**",
        description=f"Mal users recommendations of animes like '{user_anime}'",
        color=discord.Color.dark_red()
    )

    anime_rec_id = 1
    for recommendation in top_recs:
        embed_recommendation.add_field(
            name=f"{anime_rec_id} - {recommendation["title"]} ⭐ ⭐ ⭐ ⭐ 8.2",
            value=f"Ação, Aventura ",
            inline=False
        )
        anime_rec_id += 1


    return embed_recommendation