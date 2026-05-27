days_of_week = ["Mondays", "Tuesdays", "Wednesdays" ,"Thursdays", "Fridays", "Saturdays", "Sundays"]

def get_days_of_week(day):
    user_Day = int(day)
    user_Day -= 1
    if user_Day >= 0 and user_Day <= 6:
        chosen_day = days_of_week[user_Day]
        return chosen_day
    else:
        return "Invalid Day"

