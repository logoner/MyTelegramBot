# -*- coding: utf-8 -*-

# The first inspiration from: https://www.gitbook.com/book/groosha/telegram-bot-lessons/details

import config
import telebot

bot = telebot.TeleBot(config.token)
bot.delete_webhook()

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)