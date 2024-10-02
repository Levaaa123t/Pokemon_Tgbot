import telebot 
from config import token

from logic import Pokemon
bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.first_name)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['feed'])
def feed(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.first_name)
        bot.send_message(message.chat.id, pokemon.give_food())

@bot.message_handler(commands=['level'])
def level(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.first_name)
        bot.send_message(message.chat.id, pokemon.about_level())

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, """\
У меня есть такие команды: /go; /feed; /level\
""")

                  
bot.infinity_polling(none_stop=True)

