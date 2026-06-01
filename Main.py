import discord
import Token
import FormatInput
import Message
import time

class Client(discord.Client):
    async def on_ready(self):
        #Mostra que tá rodando
        print(f'{self.user} entrou na festa')

    async def on_message(self, message):

        #Impede que o bot responda a se mesmo
        if message.author == self.user:
            return

        #Pesquisa pelo título do anime que o usurário colocou
        if message.content.startswith("$t"):
            #pega só otítulo do anime tirando o $t
            #CUIDADO COM O ÍNDICE!! Se mudar os caracteres tem q mudar o índice.
            anime_title = message.content[2:]

            #Vai para a função title_TVAnimesearch_message com o parâmetro sendo o título do anime
            embed_TVAnimeMessage = Message.embed_TVAnimesearch_message(anime_title)

            #Envia a mensagem retornada pela função title_TVAnimesearch_message
            await message.channel.send(embed=embed_TVAnimeMessage)

        #Pesquisa lançamentos do dia
        if message.content.startswith("$d"):
            #CUIDADO COM O ÍNDICE!! Se mudar os caracteres tem q mudar o índice.
            user_day_of_week = message.content[2:]
            #Formata a mensagem pro padrão da API
            day_of_week = FormatInput.get_days_of_week(user_day_of_week)

            if day_of_week != "Invalid Day":
                embed, list_of_animes = Message.embed_weekly_anime(day_of_week)
                embed_day_of_week = Message.make_reaction_embed(embed, list_of_animes)
                await message.channel.send(embed=embed_day_of_week)

            else:
                await message.channel.send(day_of_week)



        #Pesquisa recomendações de animes
        if message.content.startswith("$r"):
            #CUIDADO COM O ÍNDICE!! Se mudar os caracteres tem q mudar o índice.
            user_anime = message.content[2:]

            #Pega o embed (simples) e a lista de animes recomendados
            embed, list_of_animes = Message.embed_top_recommendation(user_anime)

            #Transforma o embed simples no embed final com os emojis para reagir
            embed_top_recs = Message.make_reaction_embed(embed, list_of_animes)

            #manda o embed
            await message.channel.send(embed=embed_top_recs)


    #Pega as reações (Emojis) dos usuários
    async def on_raw_reaction_add(self, payload):
        start = time.time()
        # pega a reação do usuário
        user_reaction = payload.emoji.name

        #pega o canal onde a reação foi feita. Ex: Geral, Músicas etc.
        get_channel = self.get_channel(payload.channel_id)

        #pega a menssagem(embed) que o usuário reagiu dentro do canal
        message_info = await get_channel.fetch_message(payload.message_id)

        print(f"Tempo da Discord API: {time.time() - start:.2f} segundos")

        #recebe o embed pra mandar a mensagem no discord
        embed_reaction_message = Message.message_for_reaction(message_info, user_reaction)

        #Verifica se realmente é um embed antes de mandar
        if(embed_reaction_message != None):
            await message_info.channel.send(embed=embed_reaction_message)

#doideira da documentação
intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(Token.MyToken())