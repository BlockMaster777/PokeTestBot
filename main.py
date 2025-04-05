# coding=utf-8
import telebot
from config import TOKEN

from logic import Pokemon

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_front_img())
        bot.send_photo(message.chat.id, pokemon.show_back_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")


bot.infinity_polling(none_stop=True)
