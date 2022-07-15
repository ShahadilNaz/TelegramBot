import telebot
import time
import os

TOKEN = os.environ.get("TOKEN")
print(TOKEN)
bot = telebot.TeleBot(TOKEN)

count = 0
@bot.message_handler(commands=["start"])
def start(msg: telebot.types.Message):
    while True:
        bot.reply_to(msg, f"Hi {msg.chat.first_name}, How are you doing today :)\nCount: {count}")
        count += 1
        time.sleep(300)
bot.polling()
