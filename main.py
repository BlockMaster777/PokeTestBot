# coding=utf-8

from random import randint
import telebot
from config import TOKEN

from logic import Fighter, Pokemon, Wizard

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        if randint(1, 2) == 1:
            pokemon = Fighter(message.from_user.username)
        else:
            pokemon = Wizard(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_front_img())
        bot.send_photo(message.chat.id, pokemon.show_back_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")


@bot.message_handler(commands=['promo'])
def promo(message):
    if message.text.split()[1] == "QT4FX5R":
        bot.send_message(message.chat.id, "Как ты смог получить это сообщение?")

bot.infinity_polling(none_stop=True)
