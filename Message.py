import discord
import Answers
import FormatInput

def title_TVAnimesearch_message(anime_title):
    try:
        #Vai na função search_TVAnime pegar informações sobre o anime que o usuário pediu
        search_results = Answers.search_TVAnime(anime_title)

        #Cria um embed utilizando as informações dentro da variável search_results
        embed_TVAnime = discord.Embed(
            title= search_results["title"],
            color=discord.Color.dark_blue()
        )

        #Adiciona o field de episódeos
        embed_TVAnime.add_field(
            name="Episodes:",
            value=search_results["episodes"]
        )

        #Adiciona o field de Score
        embed_TVAnime.add_field(
            name = "Score:",
            value= search_results["score"]
        )

        #Coloca a foto no embed usando a variável search_results
        embed_TVAnime.set_image(url=search_results["images"]["jpg"]["image_url"])

        #retorna o embed
        return embed_TVAnime

    except:
        #Se não achar o anime retorna um embed de erro
        embed_Error = discord.Embed(
            title= "Não foi possível achar o seu anime",
            color=discord.Color.dark_red()
        )
        return embed_Error