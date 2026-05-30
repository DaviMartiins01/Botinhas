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
            description=f"⭐ {search_results["score"]} ({search_results["members"]} Members)",
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
        title= "☰ Top Recommendations",
        description=f"Mal users recommendations of animes like {anime_id["title"]}",
        color=discord.Color.dark_blue()
    )

    anime_rec_Emoji = ["1️⃣ ","2️⃣ ","3️⃣ ","4️⃣ ","5️⃣ ","6️⃣ ","7️⃣ ","8️⃣ ","9️⃣ ","🔟"]
    anime_rec_emoji_id = 0

    for recommendation in top_recs:
        embed_recommendation.add_field(
            name=f"{anime_rec_Emoji[anime_rec_emoji_id]} {recommendation} ",
            value="",
            inline=False
        )
        anime_rec_emoji_id += 1


    return embed_recommendation

def message_for_top_recommendation_reaction(message_info, user_reaction):
    # Dentro da mensage_info pega o primeiro embed. (Só tem 1 embed, mas tem que colocar pra pegar o primeiro mesmo assim)
    embed_info = message_info.embeds[0]

    #Pega informações de todos os fields no embed
    fields_info = embed_info.fields

    # pega o id correspondente ao field da reação do usuário
    field_id = int(Answers.get_reaction_id(user_reaction))

    #Verifica se o id é válido, se não for significa que reagiram com um emoji nada a ver
    if(field_id != -1):
        #Pega o título do anime que também é o nome do field
        anime_title = fields_info[field_id].name

        #faz a busca das informações do do anime pelo título e retorna um embed
        embed_reaction_message = title_TVAnimesearch_message(anime_title)

        return embed_reaction_message

    else:
        return None