import telebot
import os

TOKEN = os.environ.get('TOKEN', 'Значение не установлено!')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_hello(message):
    chat_id = message.chat.id
    response = "Hello, World!"
    bot.send_message(chat_id, response)

if __name__ == "__main__":
    bot.polling(none_stop=True)