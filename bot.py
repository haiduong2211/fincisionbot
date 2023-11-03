import os
import telebot
BOT_TOKEN = '6433341451:AAE_-5w2L7mFl-oUitK1NyDG1O3AzO-xVfA'
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Xin chào người anh em Fincision")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text + "Fincision")



bot.infinity_polling()

# Here is the token for bot Testbot @Finnyappbot:

# 6433341451:AAE_-5w2L7mFl-oUitK1NyDG1O3AzO-xVfA