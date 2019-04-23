import telebot
import pyowm
import tokenAPI

own = pyowm.OWM(tokenAPI.api_token_weather, language="ru")

bot = telebot.TeleBot(tokenAPI.api_token_bot)

"""@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Напиши город!")
"""
"""while True:
    try:
        place = input("Введите город/страну?:")
        break
    except:
        print("Введите правильно город/страну!")
        continue
"""






@bot.message_handler(content_types=["text"])
def handle_text(message):
    observation = own.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature("celsius")["temp"]


    answer = "В городе " + message.text + " сейчас " + w.get_detalied_status()
    answer += "Температура сейчас в районе " + str(temp) + "\n\n"

    if temp < 10:
        answer += "Будет очень холодно(ниже 10 градусов), так что оденься!"
    elif temp < 20:
        answer += "Будет средняя температура(от 10 до 20 градусов)!"
    else:
        answer += "Будет жарко(больше 20 градусов)"

    bot.send_message(message.chat.id, answer)






"""@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi, motherfucker")
"""

#@bot.message_handler(content_types=["text", "sticker", "pinned_message", "photo", "audio", "document"])
#def reply_mess(message):
#  bot.send_message(message.chat.id, message.text) - Сенд смс
#  bot.reply_to(message, message.chat) - Форвард смс


bot.polling()
