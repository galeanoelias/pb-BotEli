# Api cat
#https://api.thecatapi.com/v1/images/search


"""
curl --location --request GET 'https://api.thecatapi.com/v1/images/search?format=json' \
--header 'Content-Type: application/json' \
--header 'x-api-key: "524a37ea-4ee5-47c6-a5ef-6be689adb009"'
"""

from config import * # Importamos el token
import telebot # Para manejar la apì de telegram
import requests

# Instaciamos el bot de telegram
bot = telebot.TeleBot(TELEGRAM_TOKEN)

url = 'https://api.thecatapi.com/v1/images/search'
response = requests.get('{}'.format(url))
data = response

# Responder al comando start
@bot.message_handler(commands=["start"])
def bot_start(message):
    # Da la bienvenida
    bot.reply_to(message, "Buenas, mi nombre es BotEli. Gracias por comunicarte")

@bot.message_handler(commands=["Foto"])
def bot_imageStar(message):
    bot.reply_to(message, data)

@bot.message_handler(func=lambda message:True, content_types=['photo', 'video', 'document', 'text', 'sticker'])
def all_message(message):
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "Comando no disponible")
    elif message.text.startswith("Hola"):
        bot.send_message(message.chat.id, 'Hola, ¿como te llamas?. ya te he saludado anteriormente, "soy BotEli" pideme una foto.')
    elif message.text.startswith('Foto'):
        bot.send_message(message.chat.id, data)
    else:
        bot.send_message('Sorry! No encontramos al gatito =( ')

if __name__ == '__main__':
    print('Iniciando el bot')
    bot.infinity_polling()
    print('Fin')