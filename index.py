import telebot
import os
from flask import Flask, request
from telebot import types
from dotenv import load_dotenv

server = Flask(__name__)

load_dotenv()

token = "5206417777:AAGbqmq538gaGPvBCbgM_uY0vxD2PDPlhw0"

bot = telebot.TeleBot(os.getenv("API_KEY"), parse_mode='None')


@bot.message_handler(commands=["start"])
def send_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    opti = types.KeyboardButton("/Let's go")
    optii = types.KeyboardButton("/Why is this important?")
    markup.add(opti, optii)
    bot.send_message(chat_id=message.chat.id, text="Welcome to Atona, I will be your guardian councillor for starting a career with Edukarma", reply_markup=markup)


@bot.message_handler(commands=["Get"])
def send_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    optA = types.KeyboardButton("/Software Development")
    optB = types.KeyboardButton("/Design")
    optC = types.KeyboardButton("/Product Management")
    markup.add(optA, optB, optC)
    bot.send_message(chat_id=message.chat.id, text="What career path do you intend taking?", reply_markup=markup)


@bot.message_handler(commands=["Why"])
def send_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    bot.send_message(chat_id=message.chat.id, text="Why is this important?", reply_markup=markup)
    bot.send_message(chat_id=message.chat.id, text="https://www.facebook.com", reply_markup=markup)


@bot.message_handler(commands=["Software"])
def send_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    opt1 = types.KeyboardButton("/Just for fun")
    opt2 = types.KeyboardButton("/I am simply interested")
    opt3 = types.KeyboardButton("/To improve myself")
    opt4 = types.KeyboardButton("/Monetary cause")
    opt5 = types.KeyboardButton("/For my kids")
    opt6 = types.KeyboardButton("/Don't know, just pick for me")
    markup.add(opt1, opt2, opt3, opt4, opt5, opt6)
    bot.send_message(chat_id=message.chat.id, text="Why do you want to learn Web development?", reply_markup=markup)


@bot.message_handler(commands=["Just", "To", "I"])
def send_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    yes = types.KeyboardButton("/Yes")
    no = types.KeyboardButton("/Nope - Just want to get started")
    markup.add(yes, no)
    bot.send_message(chat_id=message.chat.id, text="Have a brilliant idea/platform in mind?", reply_markup=markup)


@bot.message_handler(commands=["For"])
def send_message(message):
    bot.reply_to(message, "Start with scratch then move on to Python 🐍")


@bot.message_handler(commands=["Monetary"])
def send_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    g = types.KeyboardButton("/Get a job")
    gg = types.KeyboardButton("/Got a start-up idea")
    markup.add(g, gg)
    bot.send_message(chat_id=message.chat.id, text="How do you want to make money?", reply_markup=markup)


@bot.message_handler(commands=["Get"])
def send_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    k = types.KeyboardButton("/Wanna work for big tech companies")
    kk = types.KeyboardButton("/Doesn't matter, i just want money")
    kkk = types.KeyboardButton("/Web-development")
    kkkk = types.KeyboardButton("/Enterprise")
    kkkkk = types.KeyboardButton("/3D Gaming")
    markup.add(k, kk, kkk, kkkk, kkkkk)
    bot.send_message(chat_id=message.chat.id, text="Which platform or field?", reply_markup=markup)


@bot.message_handler(commands=["Wanna"])
def send_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    h = types.KeyboardButton("/Facebook")
    hh = types.KeyboardButton("/Google")
    hhh = types.KeyboardButton("/Microsoft")
    hhhh = types.KeyboardButton("/Apple")
    markup.add(h, hh, hhh, hhhh)
    bot.send_message(chat_id=message.chat.id, text="Which company would you love to work at?", reply_markup=markup)


@bot.message_handler(commands=["Facebook"])
def send_message(message):
    bot.reply_to(message, "I'll recommend Python 🐍")


@bot.message_handler(commands=["Google"])
def send_message(message):
    bot.reply_to(message, "I'll recommend Python 🐍")


@bot.message_handler(commands=["Microsoft"])
def send_message(message):
    bot.reply_to(message, "I'll recommend C#")


@bot.message_handler(commands=["Don't"])
def send_message(message):
    bot.reply_to(message, "I'll recommend Objective-C")


@bot.message_handler(commands=["Doesn't"])
def send_message(message):
    bot.reply_to(message, "I will recommend Java")


@bot.message_handler(commands=["Web-development"])
def send_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    j = types.KeyboardButton("/Front-end (web interface)")
    jj = types.KeyboardButton("/Back-end (brain behind a website)")
    markup.add(j, jj)
    bot.send_message(chat_id=message.chat.id, text="Which company would you love to work at?", reply_markup=markup)


@bot.message_handler(commands=["Front-end"])
def send_message(message):
    bot.reply_to(message, "I'll recommend Javascript")


@bot.message_handler(commands=["Back-end"])
def send_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    x = types.KeyboardButton("/Corporate")
    xx = types.KeyboardButton("/Start-up")
    markup.add(x, xx)
    bot.send_message(chat_id=message.chat.id, text="I want to work for?", reply_markup=markup)


@bot.message_handler(commands=["Don't"])
def send_message(message):
    bot.reply_to(message, "I'll recommend Python 🐍")


@bot.message_handler(commands=["Yes", "Got"])
def send_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    p = types.KeyboardButton("/Web")
    q = types.KeyboardButton("/Enterprise")
    r = types.KeyboardButton("/Mobile")
    s = types.KeyboardButton("/3D Gaming")
    markup.add(p, q, r, s)
    bot.send_message(chat_id=message.chat.id, text="Which platform/field?", reply_markup=markup)


@bot.message_handler(commands=["Web"])
def send_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    yess = types.KeyboardButton("/yeah")
    noo = types.KeyboardButton("/No")
    markup.add(yess, noo)
    bot.send_message(chat_id=message.chat.id, text="Does your website provide info in real-time, like Twitter", reply_markup=markup)


@bot.message_handler(commands=["yeah"])
def send_message(message):
    bot.reply_to(message, "I will recommend Javascript")


@bot.message_handler(commands=["No", "Start-up"])
def send_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    nut = types.KeyboardButton("/Not sure")
    nah = types.KeyboardButton("/No!")
    markup.add(nut, nah)
    bot.send_message(chat_id=message.chat.id, text="Do you want to try something new with huge potential but less mature", reply_markup=markup)


@bot.message_handler(commands=["Not", "No!"])
def send_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    lego = types.KeyboardButton("/Lego")
    play = types.KeyboardButton("/Play-doh")
    one = types.KeyboardButton("/one old and ugly toy but i love it so much")
    markup.add(lego, play, one)
    bot.send_message(chat_id=message.chat.id, text="Which one is your favorite toy?", reply_markup=markup)


@bot.message_handler(commands=["Lego"])
def send_message(message):
    bot.reply_to(message, "I will recommend starting with Python programming language")


@bot.message_handler(commands=["Play-doh"])
def send_message(message):
    bot.reply_to(message, "I will recommend starting with Ruby programming language")


@bot.message_handler(commands=["one"])
def send_message(message):
    bot.reply_to(message, "I will recommend starting with PHP 🐘")


@bot.message_handler(commands=["Nope"])
def send_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    l = types.KeyboardButton("/easy way")
    m = types.KeyboardButton("/best way")
    n = types.KeyboardButton("/slightly harder way")
    o = types.KeyboardButton("/really hard way")
    markup.add(l, m, n, o)
    bot.send_message(chat_id=message.chat.id, text="I prefer to lean things the...", reply_markup=markup)


@bot.message_handler(commands=["easy, best"])
def send_message(message):
    bot.reply_to(message, "I will recommend starting with Python Programming language")


@bot.message_handler(commands=["slightly"])
def send_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    auto = types.KeyboardButton("/Automatic")
    manual = types.KeyboardButton("/Manual")
    markup.add(auto, manual)
    bot.send_message(chat_id=message.chat.id, text="Automatic or Manual car", reply_markup=markup)


@bot.message_handler(commands=["Automatic"])
def send_message(message):
    bot.reply_to(message, "I will recommend starting with Java programming language")


@bot.message_handler(commands=["Manual"])
def send_message(message):
    bot.reply_to(message, "I will recommend starting with C programming language")


@bot.message_handler(commands=["really"])
def send_message(message):
    bot.reply_to(message, "I will recommend C++")


@bot.message_handler(commands=["Enterprise", "Corporate"])
def send_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    j = types.KeyboardButton("/I'm")
    jj = types.KeyboardButton("/Not-bad")
    jjj = types.KeyboardButton("/sucks")
    markup.add(j, jj, jjj)
    bot.send_message(chat_id=message.chat.id, text="What do you think about Microsoft?", reply_markup=markup)


@bot.message_handler(commands=["I'm"])
def send_message(message):
    bot.reply_to(message, "I will recommend starting with C#")


@bot.message_handler(commands=["Not-bad"])
def send_message(message):
    bot.reply_to(message, "I will recommend starting with Java")


@bot.message_handler(commands=["sucks"])
def send_message(message):
    bot.reply_to(message, "I will recommend starting with Java")


@bot.message_handler(commands=["Mobile"])
def send_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    i = types.KeyboardButton("/iOS")
    ii = types.KeyboardButton("/Android")
    markup.add(i, ii)
    bot.send_message(chat_id=message.chat.id, text="What operating system?", reply_markup=markup)


@bot.message_handler(commands=["iOS"])
def send_message(message):
    bot.reply_to(message, "I will recommend starting with objective-C")


@bot.message_handler(commands=["Android"])
def send_message(message):
    bot.reply_to(message, "I will recommend starting with Java")


@bot.message_handler(commands=["3D"])
def send_message(message):
    bot.reply_to(message, "I will recommend starting with C++")


@server.route('/' + token, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://atona.herokuapp.com/' + token)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))


