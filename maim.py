import telebot
import os
from dotenv import load_dotenv

load_dotenv() 

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	text = "Assalomu alaykum, meni portfolio botimga xush kelibsiz!"
# 	keyboard = types.ReplyKeyboardMarkup("")
# 	btn1 = types.KeyboardButton("Abbout me")
# 	btn2 = types.KeyboardButton("Contact ")
# 	keyboard.add(btn1, btn2)
# bot.send_message(message.chat.id, text, reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
 if message.text == "Abbout me":
        bot.send_message(message.chat.id, "Menim G'ulomjon Komilovman. \n Men frontent dasturchiman." )
 elif message.text == "Contact ":
        bot.send_message(message.chat.id, "Biz bilan aloqada bo'lish uchun: \n Telegram: @komilov_g \n Email: komilovgulomjon428@gmail.com")
@bot.messsage_handler(func=lambda message: message.text == "Abbout me")
def about_me(message):
    bot.send_message(message.chat.id, "Menim G'ulomjon Komilovman. \n Men frontent dasturchiman.")

@bot.message_handler(func=lambda message: message.text == "Contact ")
def contact(message):
    bot.send_message(message.chat.id, "Biz bilan aloqada bo'lish uchun: \n Telegram: @komilov_g \n Email:komilovgulomjon428@gmail.com ") 


bot.infinity_polling()