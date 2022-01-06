import telebot
import wikipedia
import random

wikipedia.set_lang('ru')
random = random.randint(1, 10)

bot = telebot.TeleBot("5070041001:AAGy0ZQ8uDoIMkdpmgOGDS4QCEnmgL3SaCY", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, message.chat.first_name + ', введите Ваш запрос!')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    print(wikipedia.search(message.text))
    try:
        bot.send_message(message.from_user.id, wikipedia.summary(message.text))
        bot.send_message(message.from_user.id, wikipedia.summary(wikipedia.search(message.text, results=3)))
        bot.send_message(message.chat.id, message.chat.first_name + ', есть еще запросы? Пишите! 🔎')
    except:
        bot.send_message(message.chat.id, 'Ваш запрос слишком короткий или имеет множество значений (или не имеет вовсе). \n\nПожалуйста, замените его на синоним или используйте другой запрос.')


print('Запущен')
bot.polling()
