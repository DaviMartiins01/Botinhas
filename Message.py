import discord
import Answers
import FormatInput

def make_embed_message_TV_Movie():
    return

def title_TVAnimesearch_message(anime_title):
    try:
        #Vai na função search_TVAnime pegar informações sobre o anime que o usuário pediu
        search_results = Answers.search_TVAnime(anime_title)

        #Cria um embed utilizando as informações dentro da variável search_results
        embed_TVAnime = discord.Embed(
            title= f"{search_results["title"]}",
            description=f"⭐ Score: {search_results["score"]} ({search_results["members"]} Members)",
            color=discord.Color.dark_blue()
        )

        #Adiciona o field de episódeos
        embed_TVAnime.add_field(
            name="Synopsis",
            #value=search_results["synopsis"],
            value= "Finge que tem uma sinopse muito maneira aqui, daquelas que te fazem querer largar tudo só pra descobrir o que acontece no próximo capítulo. Uma história cheia de mistério, personagens memoráveis, reviravoltas inesperadas e momentos que vão te fazer rir, sofrer e ficar olhando pro teto depois. Tem ação, emoção, talvez um trauma psicológico leve, e aquela sensação de ‘só mais um capítulo’ às três da manhã. Enfim… imagina a melhor sinopse possível. É essa.",
            inline=False
        )

        #Adiciona o field de Score
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