import telebot
import os

TOKEN = os.environ.get("TOKEN")
print(TOKEN)
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(msg: telebot.types.Message):
    bot.reply_to(msg, f"Hi {msg.chat.first_name}, How are you doing today :)")

bot.polling()
