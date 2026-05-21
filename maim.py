import telebot
import os

from dotenv import load_dotenv
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# ENV LOAD
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

# BOT
bot = telebot.TeleBot(TOKEN)

# MENU
markup = ReplyKeyboardMarkup(resize_keyboard=True)

btn1 = KeyboardButton("👨‍💻 About Me")
btn2 = KeyboardButton("🛠 Tech Stack")
btn3 = KeyboardButton("💼 Projects")
btn4 = KeyboardButton("📞 Contact")

markup.row(btn1, btn2)
markup.row(btn3, btn4)

# START
@bot.message_handler(commands=['start'])
def start(message):

    text = """
👋 Salom! Men Komilov G'ulomjonman

⚡ Python Developer | Telegram Bot Developer

Quyidagi bo'limlardan birini tanlang 👇
"""

    bot.send_message(
        message.chat.id,
        text,
        reply_markup=markup
    )

# ABOUT
@bot.message_handler(func=lambda message: message.text == "👨‍💻 About Me")
def about(message):

    text = """
👨‍💻 About Me
━━━━━━━━━━━━━━━━

💼 Telegram botlar va Python loyihalar yarataman

⚡ Python, Telegram Bot API va automation bo‘yicha tajribam bor

🌱 Hozirda AI va backend yo‘nalishlarini o‘rganmoqdaman

🧠 Chiroyli va foydali botlar yaratishga qiziqaman

💬 Python, Bot va AI haqida suhbatlashishga tayyorman
"""

    bot.send_message(message.chat.id, text)

# TECH STACK
@bot.message_handler(func=lambda message: message.text == "🛠 Tech Stack")
def tech(message):

    text = """
🛠 Tech Stack
━━━━━━━━━━━━━━━━

🐍 Backend:
• Python
• Aiogram
• PyTelegramBotAPI

🗄 Database:
• SQLite
• PostgreSQL

🎨 Frontend:
• HTML
• CSS

🧰 Tools:
• Git
• GitHub
• VS Code
• Postman

🤖 Extra:
• Telegram Bot API
• REST API
"""

    bot.send_message(message.chat.id, text)

# PROJECTS
@bot.message_handler(func=lambda message: message.text == "💼 Projects")
def projects(message):

    text = """
💼 Projects
━━━━━━━━━━━━━━━━

🤖 Video Downloader Bot
🎵 Music Downloader Bot
🧠 AI Chat Bot
🌐 Portfolio Bot

🚀 Yangi loyihalar tez orada qo‘shiladi
"""

    bot.send_message(message.chat.id, text)

# CONTACT
@bot.message_handler(func=lambda message: message.text == "📞 Contact")
def contact(message):

    text = """
📞 Contact
━━━━━━━━━━━━━━━━

📱 Telegram:
@komilovv_g

📧 Gmail:
komilovgulomjon428@gmail.com

📞 Telefon:
+998 99 329 68 26

📩 Istalgan vaqt bog‘lanishingiz mumkin!
"""

    bot.send_message(message.chat.id, text)

# RUN
print("Bot ishladi ✅")

bot.infinity_polling()