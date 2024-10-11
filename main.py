import telebot 
from config import token
from random import randint

from logic import Pokemon, Wizard, Fighter
bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.first_name not in Pokemon.pokemons.keys():
        chance = randint(1,25)
        if chance <= 1:
            pokemon = Pokemon(message.from_user.first_name)
            bot.reply_to(message,'Класс твоего покемона: Обычный(просто обычный покемон), твоя сила и атака средние')
        elif chance <= 10:
            pokemon = Wizard(message.from_user.first_name)
            bot.reply_to(message, 'Класс твоего покемона: Волшебник(в некоторых случиях ты можешь заблокировать урон), твое здоровье больше чем у других, но атака меньше')
        elif chance <= 19:
            pokemon = Fighter(message.from_user.first_name)
            bot.reply_to(message, 'Класс твоего покемона: Воин(Всегда может нанести супер удар),твое здоровье меньше чем у других, но у тебя сильная атака')
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['attack'])
def attack_pok(message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.first_name in Pokemon.pokemons.keys() and message.from_user.first_name in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.first_name]
            pok = Pokemon.pokemons[message.from_user.first_name]
            res = pok.attack(enemy)
            bot.send_message(message.chat.id, res)
        else:
            bot.send_message(message.chat.id, "Сражаться можно только с покемонами")
    else:
            bot.send_message(message.chat.id, "Чтобы атаковать, нужно ответить на сообщения того, кого хочешь атаковать")

@bot.message_handler(commands=['feed'])
def feed(message):
    if message.from_user.first_name in Pokemon.pokemons.keys():
        pokemon = Pokemon.pokemons[message.from_user.first_name]
        bot.send_message(message.chat.id,pokemon.give_food())


@bot.message_handler(commands=['level'])
def level(message):
    if message.from_user.first_name in Pokemon.pokemons.keys():
        pokemon = Pokemon.pokemons[message.from_user.first_name]
        bot.send_message(message.chat.id,pokemon.about_level())

@bot.message_handler(commands=['info'])
def information(message):
    if message.from_user.first_name in Pokemon.pokemons.keys():
        pokemon = Pokemon.pokemons[message.from_user.first_name]
        bot.send_message(message.chat.id,pokemon.info())

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, """\
У меня есть такие команды: /go; /feed; /level; /info\
""")

                  
bot.infinity_polling(none_stop=True)



