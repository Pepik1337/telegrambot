import telebot
from bs4 import BeautifulSoup
import requests
url = "https://yandex.com.am/pogoda/ru?lat=55.030199&lon=82.92043"
response = requests.get(url)
bs = BeautifulSoup(response.text,"lxml")
bot = telebot.TeleBot('7885970209:AAG-65WgoQqahWbKdPXWEG82VYH1wiVuStE');
temp = bs.find('p', class_ = "AppFactTemperature_content__Lx4p9")
weather = bs.find('p', class_ = "AppFact_warning__8kUUn")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "привет":
        bot.send_message(message.from_user.id, "привет далбаеб")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, f"Напиши привет {message.chat.username}")
    elif "видео" in message.text.lower():
        bot.send_message(message.from_user.id, f"Где видео {message.chat.first_name}, https://www.youtube.com/@bananus7452")
    elif "погода" in message.text.lower():
        bot.send_message(message.from_user.id, f"Температура в Новосибирске составляет - {temp.text}\n{weather.text}")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True)