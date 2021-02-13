# 1673769130:AAHlaJugS59B8HGnU1CTBmTLKbqCXvVzWAM
import telebot

bot = telebot.TeleBot("1673769130:AAHlaJugS59B8HGnU1CTBmTLKbqCXvVzWAM", parse_mode=None)
# You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(content_types=['text'])
def start(message):
    login = 'Tom'
    bot.send_message(message.from_user.id, "enter login");
    if message.text == login:
        bot.register_next_step_handler(message,get_proccessing)
    else:
        bot.send_message(message.from_user.id, "try enter login");


def get_proccessing(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?");
        bot.register_next_step_handler(message, get_name);  # следующий шаг – функция get_name
    elif message.text == '/calc':
        val = message.text
        bot.send_message(message.from_user.id, "enter value");
        bot.register_next_step_handler(message, get_calc);  # следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg or /calc');


def get_calc(message):
    values = message.text.split(" ");
    x = int(values[0])
    op = values[1]
    y = int(values[2])
    if op =='+':
        value = x+y;
    if op =='-':
        value = x-y;
    bot.send_message(message.from_user.id,"result = "+str(value));

def get_name(message): #получаем фамилию
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?');
    bot.register_next_step_handler(message, get_surname);

def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message(message.from_user.id,'Сколько тебе лет?');
    bot.register_next_step_handler(message, get_age);

def get_age(message):
    global age;
    while True: #проверяем что возраст изменился
        try:
            age = int(message.text) #проверяем, что возраст введен корректно
            break
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    bot.send_message(message.from_user.id, 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?')

bot.polling()