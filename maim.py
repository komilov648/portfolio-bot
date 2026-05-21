import telebot
import os

from dotenv import load_dotenv
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

# MENU
markup = ReplyKeyboardMarkup(resize_keyboard=True)

markup.add(
    KeyboardButton("👨‍💻 About Me"),
    KeyboardButton("🛠 Tech Stack")
)

markup.add(
    KeyboardButton("💼 Projects"),
    KeyboardButton("📞 Contact")
)

# START
@bot.message_handler(commands=['start'])
def start(message):

    text = f"""
👋 Salom! Men Komilov G'ulomjonman

⚡ Python Developer | Telegram Bot Developer

Quyidagi bo'limlardan birini tanlang:
"""

    bot.send_message(
        message.chat.id,
        text,
        reply_markup=markup
    )

# BUTTONS
@bot.message_handler(func=lambda message: True)
def portfolio(message):

    # ABOUT
    if message.text == "👨‍💻 About Me":

        text = """
👨‍💻 About Me
━━━━━━━━━━━━━━━━

💼 Telegram botlar va Python loyihalar yarataman

⚡ Python, Telegram Bot API va automation bo‘yicha tajribam bor

🌱 Hozirda AI, Web App va backend yo‘nalishlarini o‘rganmoqdaman

🧠 Chiroyli dizayn va foydali botlar yaratishga qiziqaman

💬 Python, Telegram Bot va AI haqida suhbatlashishga tayyorman
"""

        bot.send_message(message.chat.id, text)

    # TECH STACK
    elif message.text == "🛠 Tech Stack":

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
    elif message.text == "💼 Projects":

        text = """
💼 Projects
━━━━━━━━━━━━━━━━

🤖 Video Downloader Bot
🎵 Music Downloader Bot
🧠 AI Chat Bot
🌐 Portfolio Bot

Tez orada yangi loyihalar qo‘shiladi 🚀
"""

        bot.send_message(message.chat.id, text)

    # CONTACT
    elif message.text == "📞 Contact":

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

print("Bot ishladi ✅")

bot.infinity_polling()