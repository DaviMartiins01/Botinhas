import Answers
import discord
import Token
import FormatInput

class Client(discord.Client):
    async def on_ready(self):
        #Mostra que tá rodando
        print(f'{self.user} entrou na festa')

    async def on_message(self, message):

        #impede que o bot responda a se mesmo
        if message.author == self.user:
            return

        #Pega uma mensagem de usuário que começa com certos caracteres e responde com outra
        #Pesquisa pelo título do anime
        if message.content.startswith("$t"):
            try:
                #tira os caracteres que ativam o bot pra poder fazer a pesquisa só do título
                #CUIDADO COM O ÍNDICE!! Se mudar os caracteres tem q mudar o índice.
                anime_title = message.content[2:]
                search_results = Answers.search_TVAnime(anime_title)

                await message.channel.send(f'{search_results["images"]["jpg"]["image_url"]}')
                await message.channel.send(f'\nTitle: {search_results["title"]}\nScore: {search_results["score"]}\nSynopsis: {search_results["synopsis"]}')

            except:
                await message.channel.send("Não foi possível encontrar o anime, talvez seja um ova.")

        #Pesquisa lançamentos do dia
        if message.content.startswith("$d"):
            #CUIDADO COM O ÍNDICE!! Se mudar os caracteres tem q mudar o índice.
            user_day_of_week = message.content[2:]
            #Formata a mensagem pro padrão da API
            day_of_week = FormatInput.get_days_of_week(user_day_of_week)

            if day_of_week != "Invalid Day":
                #Pega os dados da temporada
                this_seasonAnime = Answers.searchSeasonAnime()
                #pega os dados dos animes do dia (escolhido pelo usuário) em forma de dicionário (utilizando-se dos dados da temporada)
                this_dayAnimes = Answers.weeklyAnime(this_seasonAnime, day_of_week)

                # For que abre o dicionário criado pela função weeklyAnime e pega os animes do dia.
                for anime in this_dayAnimes:
                    await message.channel.send(anime["image"])
                    await message.channel.send(
                        f'Title: {anime["title"]}\nScore: {anime["score"]}\nSynopsis: {anime["synopsis"]}')
            else:
                await message.channel.send(day_of_week)



        #Pesquisa recomendações de animes
        if message.content.startswith("$r"):
            #CUIDADO COM O ÍNDICE!! Se mudar os caracteres tem q mudar o índice.
            recs = message.content[2:]
            #Pega o anime escolhido pelo usuário
            anime_id = Answers.search_TVAnime(recs)
            #Pega as recomendações do anime usando o id dele
            get_recommendations = Answers.searchRecommendations(anime_id["mal_id"])
            #Separa as 10 primeiras recomendações
            top_recs = Answers.topRecommendations(get_recommendations)
            #Manda as recomendações pro chat
            try:
                for recommendation in top_recs:
                    await message.channel.send(f'\nTitle: {recommendation["title"]}')
                    await message.channel.send(f'{recommendation["image"]}')

            except:
                await message.channel.send("Não foi possível achar esse anime")




#doideira da documentação
intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(Token.MyToken())