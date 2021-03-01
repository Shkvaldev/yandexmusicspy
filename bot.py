# -*- coding: utf-8 -*-
import telebot
from sqler import Sqler
import qiwier
import config
from telebot import types
import checker
import re
import time

QIWI_TOKENs = config.QIWI_TOKEN
TOKEN = config.TOKEN

bot = telebot.TeleBot(TOKEN)

kassa = qiwier.QiwiKassa()

user_db = Sqler("database.db")

@bot.message_handler(commands=['start'])
def greeting(message):
	text = '''Приветствую, меня зовут Yandex Music Checker bot!
	 Если ты хочешь посмотреть любимый плейлист интересующего тебя человека, то введи комманду /favorite логин (например, /favorite User123).
	 Если ты хочешь посмотреть какие плейлисты слушает интересующий тебя человек, то введи команду /playlists логин (например, /playlists User123).
	 *электронная почта тоже может являться логином, поэтому, если не получится, попробуй ввести электронную почту в качестве логина'''
	bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['favorite'])
def check_favorite(message):
	try:
		target = message.text[10:]
		result = str(checker.favorite(target))
		bot.send_message(message.chat.id, result)
	except Exception as e:
		bot.send_message(message.chat.id, "Ошибка ввода!")
		print(e)


bot.polling()