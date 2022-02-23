import telebot
import os
from telebot import types
from dotenv import load_dotenv
load_dotenv()


bot = telebot.TeleBot(os.getenv("API_KEY"), parse_mode='None')


@bot.message_handler(commands=["start"])
def send_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    opti = types.KeyboardButton("/Get started")
    optii = types.KeyboardButton("/Why is this important?")
    markup.add(opti, optii)
    bot.send_message(chat_id=message.chat.id, text="Welcome to Atona, I will be your guardian councillor for starting a career with Edukarma", reply_markup=markup)


@bot.message_handler(commands=["Get"])
def send_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    optA = types.KeyboardButton("/Web Development")
    optB = types.KeyboardButton("/Design")
    optC = types.KeyboardButton("/Product Management")
    markup.add(optA, optB, optC)
    bot.send_message(chat_id=message.chat.id, text="What career path do you intend taking?", reply_markup=markup)


@bot.message_handler(commands=["Why"])
def send_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    bot.send_message(chat_id=message.chat.id, text="Why is this important?", reply_markup=markup)
    bot.send_message(chat_id=message.chat.id, text="https://www.facebook.com", reply_markup=markup)


@bot.message_handler(commands=["Web"])
def send_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    opt1 = types.KeyboardButton("/Just for fun")
    opt2 = types.KeyboardButton("/I am simply interested")
    opt3 = types.KeyboardButton("/To improve myself")
    opt4 = types.KeyboardButton("/For money")
    opt5 = types.KeyboardButton("/For my kids")
    opt6 = types.KeyboardButton("/Don't know, just pick for me")
    markup.add(opt1, opt2, opt3, opt4, opt5, opt6)
    bot.send_message(chat_id=message.chat.id, text="Why do you want to learn Web development?", reply_markup=markup)


bot.polling()
