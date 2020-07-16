import telebot
import random
import requests


bot = telebot.TeleBot("1384431975:AAEnhITa7WzaWp_WPikAsraDBOM2Nj7DyCo")

hello_variety = ['привет', 'здарова', 'куку', 'ку', 'hello', 'hi', 'приветики']
hello_answer = ["Я тебя не понял(", 'Повтори, я не расслышал', 'Говори по русски эээ', 'Всё х**ня, давай по новой']

#создание меню
keyboard1= telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row("Покажи мне погоду в Москве")

@bot.message_handler(commands=['start'])
def introduction(message):
    bot.send_message(message.chat.id, "Привет я телеграм бот Виктора! И я пока нихера не умею((((")
    bot.send_message(message.chat.id, "Но подождии....")
    bot.send_message(message.chat.id, "Возможно скоро я научусь показывать погоду. Чтобы проверить эту функцию нажми на кнопочку ниже", reply_markup=keyboard1)
    #bot.send_message(message.chat.id, "тут будет смайлик")
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAANbXwxIrDB-SFAu1wiluxb8YbjgT-8AAsoBAAJQqW0IOf8zhGhpxP8aBA')



@bot.message_handler(content_types=["text"])
def send_message(message):
    if message.text.lower() in hello_variety:
        bot.send_message(message.chat.id, "И тебе привет))")
    elif message.text.lower() == "покажи мне погоду в москве":
        weather_check()
    else:
        bot.send_message(message.chat.id, random.choice(hello_answer))


#определение id стикера))
@bot.message_handler(content_types=['sticker'])
def sticker_id_show(message):
    print(message)


#определение погоды в Москве
def weather_check():
    city = "Moscow"
    city_id = 0
    app_id = "e5e82507b3ea72413ed58f0accde697d"
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'q': city, 'type': 'like', 'units': 'metric', 'lang': 'ru', 'APPID': app_id})
        data = res.json()
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
              for d in data['list']]
        print("city:", cities)
        city_id = data['list'][0]['id']
        print('city_id=', city_id)
    except Exception as e:
        print("Exception (find):", e)
        pass

    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': app_id})
        data = res.json()
        print("conditions:", data['weather'][0]['description'])
        print("temp:", data['main']['temp'])
        print("temp_min:", data['main']['temp_min'])
        print("temp_max:", data['main']['temp_max'])
    except Exception as e:
        print("Exception (weather):", e)
        pass

bot.polling()