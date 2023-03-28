from telebot import TeleBot
import os
from dotenv import load_dotenv
from api import get_reply

load_dotenv()

bot = TeleBot(os.getenv("BOT_TOKEN"))


@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    text = "Welcome to the Ralph's bot , Please dont spam the bot"
    bot.send_message(chat_id, text)
    return


@bot.message_handler()
def on_message(message):
    chat_id = message.chat.id
    prompt = message.text[:250]
    bot.send_chat_action(chat_id, "typing")
    text = get_reply(prompt)
    bot.send_message(chat_id, text)
    return


bot.infinity_polling()
