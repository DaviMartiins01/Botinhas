import discord
import Answers
import FormatInput

def embed_TVAnimesearch_message(anime_title):
    try:
        #Vai na função search_TVAnime pegar informações sobre o anime que o usuário pediu
        search_results = Answers.search_TVAnime(anime_title)

        #Cria um embed utilizando as informações dentro da variável search_results
        embed_TVAnime = discord.Embed(
            title= f"**{search_results["title"]}**",
            description=f"⭐ {search_results["score"]} ({search_results["members"]} Members)",
            url=search_results["url"],
            color=discord.Color.dark_grey()
        )

        #Adicionando diferentes fields
        embed_TVAnime.add_field(
            name="Synopsis",
            value= FormatInput.format_anime_synopsis(search_results["synopsis"]),
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
    list_top_recs = Answers.get_top_recommendations(anime_id["mal_id"])

    embed_recommendation = discord.Embed(
        title= "☰ Top Recommendations",
        description=f"Mal users recommendations of animes like {anime_id["title"]}",
        color=discord.Color.dark_blue()
    )

    return embed_recommendation, list_top_recs

def embed_weekly_anime(day_of_week):
    # Pega os dados da temporada
    this_seasonAnime = Answers.searchSeasonAnime()
    # pega os dados dos animes do dia (escolhido pelo usuário) em forma de dicionário (utilizando-se dos dados da temporada)
    list_this_dayAnimes = Answers.weeklyAnime(this_seasonAnime, day_of_week)

    embed_weekly_anime = discord.Embed(
        #[:-1] só tira o "s" do final da string.
        title= f"☰ {day_of_week[:-1]} Anime Releases",
        color=discord.Color.dark_blue()
    )

    return embed_weekly_anime, list_this_dayAnimes

def make_reaction_embed(embed, list_of_animes):
    anime_rec_Emoji = ["1️⃣ ", "2️⃣ ", "3️⃣ ", "4️⃣ ", "5️⃣ ", "6️⃣ ", "7️⃣ ", "8️⃣ ", "9️⃣ ", "🔟"]
    anime_rec_emoji_id = 0

    # For que abre o dicionário criado pela função weeklyAnime e pega os animes do dia.
    for anime in list_of_animes:
        embed.add_field(
            #mais tarde se o webhook funcionar tenho que colocar a imagem aqui
            #Lembrando que da pra mudar a forma que eu pego pelo ["image"] no weeklyAnime pra ficar igual no recommendations
            #pra fazer isso é só mudar no for do weeklyAnime lá em Answers.py
            name=f"{anime_rec_Emoji[anime_rec_emoji_id]} {anime.get("entry", anime)["title"]}",
            value="",
            inline=False
        )

        anime_rec_emoji_id += 1

    embed.set_footer(text="Note: React with the number of the anime you want to now more.")

    return embed

def message_for_reaction(message_info, user_reaction):
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
        embed_reaction_message = embed_TVAnimesearch_message(anime_title)

        return embed_reaction_message

    else:
        return None