days_of_week = ["Mondays", "Tuesdays", "Wednesdays" ,"Thursdays", "Fridays", "Saturdays", "Sundays"]

def get_days_of_week(day):
    user_Day = int(day)
    user_Day -= 1
    if user_Day >= 0 and user_Day <= 6:
        chosen_day = days_of_week[user_Day]
        return chosen_day
    else:
        return "Invalid Day"

def format_anime_synopsis(anime_synopsis, caracter_limit=460):
    #Corta a string em um limite de caracter
    anime_synopsis = anime_synopsis[:caracter_limit]

    #Divide a string em uma lista pra cada quebra de linha
    anime_synopsis = anime_synopsis.splitlines()

    #Ve se realmente dividiu em mais de uma lista, se dividiu é só mandar o texto do primeiro item da lista.
    if(len(anime_synopsis) > 1):
        return anime_synopsis[0]

    #Se não dividiu significa que não teve quebra de linha
    else:
        #Encontra a localização do último espaço do texto
        new_caracter_limit = anime_synopsis[0].rfind(" ")

        #Corta a string pra parar no último espaço do texto (assim não para no meio de nenhuma palavra)
        anime_synopsis[0] = anime_synopsis[0][:new_caracter_limit]

        #adiciona ... no final porque o texto vai ser quebrado antes de finalizar e retorna a sinopse
        anime_synopsis[0] += "..."
        return anime_synopsis[0]