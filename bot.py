import telebot
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('TGTOKEN')

bot = telebot.TeleBot(BOT_TOKEN, colorful_logs=True)

@bot.message_handler(commands=['start'])
def send_test(msg):
    info = (
        f"ID : {msg.chat.id}\n"
        f"Full Name : {msg.from_user.full_name}\n"
        f"Username : @{msg.from_user.username}\n"
        f"Is Premium : {'Yes' if msg.from_user.is_premium else 'No'}\n"
        f"Language : {msg.from_user.language_code}\n"
    )

    with open("patrick.png", "rb") as photo:
        bot.send_photo(msg.chat.id, photo, caption=info)

bot.infinity_polling()
