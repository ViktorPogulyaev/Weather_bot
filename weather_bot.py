import telebot
import random


bot = telebot.TeleBot("1384431975:AAEnhITa7WzaWp_WPikAsraDBOM2Nj7DyCo")

hello_variety = ['привет', 'здарова', 'куку', 'ку', 'hello', 'hi', 'приветики']
hello_answer = ["Я тебя не понял(", 'Повтори, я не расслышал', 'Говори по русски эээ', 'Всё х**ня, давай по новой']

#создание меню
keyboard1= telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row("Покажи мне погоду")

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
    else:
        bot.send_message(message.chat.id, random.choice(hello_answer))


#определение id стикера))
@bot.message_handler(content_types=['sticker'])
def sticker_id_show(message):
    print(message)


bot.polling()