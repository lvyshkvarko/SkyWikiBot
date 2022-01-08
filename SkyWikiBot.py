import telebot
import wikipedia

wikipedia.set_lang('ru')

bot = telebot.TeleBot('token', parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, message.chat.first_name + ', введите Ваш запрос! \n\nНапример: Игра престолов, Grand Theft Auto, Крысиный король, Зона 51, Семь чудес света, Гипотеза симуляции. \n\nДанный бот ищет статьи на wikipedia.org, выдавая краткое содержание запрошенной статьи.')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    try:
        bot.send_message(message.from_user.id, '🔑 Ключевая версия\n\n' + wikipedia.summary(message.text))
        bot.send_message(message.from_user.id, '🗂️ Версия №1\n\n' + wikipedia.summary(wikipedia.search(message.text, results=2)))
        bot.send_message(message.from_user.id, '🗂️ Версия №2\n\n' + wikipedia.summary(wikipedia.search(message.text, results=3)))
        bot.send_message(message.from_user.id, '🗂️ Версия №3\n\n' + wikipedia.summary(wikipedia.search(message.text, results=4)))
        bot.send_message(message.from_user.id, '🗂️ Версия №4\n\n' + wikipedia.summary(wikipedia.search(message.text, results=5)))
        bot.send_message(message.from_user.id, '🗂️ Версия №5\n\n' + wikipedia.summary(wikipedia.search(message.text, results=6)))
        bot.send_message(message.chat.id, message.chat.first_name + ', есть еще запросы? Пишите! 🔎')
    except:
        bot.send_message(message.chat.id, 'Ваш запрос слишком короткий или имеет множество значений (или не имеет вовсе). \n\nПожалуйста, замените его на синоним или используйте другой запрос. \n\nНапример: Иван (имя), Титаник (фильм)')

print('Запущен')
bot.polling()
