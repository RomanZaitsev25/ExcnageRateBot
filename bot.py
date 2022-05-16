'''
Telebot работает с IP телеграмма.
'''

import telebot

from config import config
# Создаём объект класса.
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello!")


@bot.message_handler(commands=['Gt'])
def send_welcome(message):
    bot.send_message(message.chat.id, "ТУц!")

# Слушает какие командыы приходят.
bot.polling()





