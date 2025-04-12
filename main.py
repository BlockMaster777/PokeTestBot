# coding=utf-8

from random import randint
import telebot
from config import TOKEN

from logic import Pokemon

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_front_img())
        bot.send_photo(message.chat.id, pokemon.show_back_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")
    if randint(0, 500) == 0:
        bot.send_message(message.chat.id, "Ты получил супер-покемона! Твой промокод: QT4FX5R. Используй /promo твой_промокод чтобы активировать его")


@bot.message_handler(commands=['promo'])
def go(message):
    if message.text.split()[1] == "QT4FX5R":
        bot.send_message(message.chat.id, "Как ты смог получить это сообщение? Шанс этого 1 к 1000!!!")

bot.infinity_polling(none_stop=True)
