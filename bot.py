import datetime
import ephem
from glob import glob
import logging
from random import randint, choice
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import mysettings

logging.basicConfig(filename='bot.log', level=logging.INFO, format="%(levelname)s:%(asctime)s - %(message)s")

def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text("Привет, пользователь! Как джина из лампы, ты вызвал команду /start")

def planet_constel(update, context):
    text_list = update.message.text.split()
    planet = text_list[1].lower()
    today = str(datetime.date.today()).replace("-", "/")
    
    if planet == 'mercury' or planet == 'меркурий':
        planet_for_const = ephem.Mercury(today)
    elif planet == 'venus' or planet == 'венера':
        planet_for_const = ephem.Venus(today)
    elif planet == 'mars' or planet == 'марс':
        planet_for_const = ephem.Mars(today)
    elif planet == 'jupiter' or planet == 'юпитер':
        planet_for_const = ephem.Jupiter(today)
    elif planet == 'saturn' or planet == 'сатурн':
        planet_for_const = ephem.Saturn(today)
    elif planet == 'uranus' or planet == 'уран':
        planet_for_const = ephem.Uranus(today)
    elif planet == 'neptune' or planet == 'нептун':
        planet_for_const = ephem.Neptune(today)
    elif planet == 'pluto' or planet == 'плутон':
        planet_for_const = ephem.Pluto(today)
    
    const = ephem.constellation(planet_for_const)
    print(const)
    update.message.reply_text(f'Эта планета сегодня находится в созвездиии {const}')

def count_words(update, context):
    len_message = len(context.args)
    if len_message == 1:
        answer = f"{len_message} слово."
    elif len_message > 1:
        answer = f"{len_message} слов."
    else:
        answer = "Вы ничего не ввели."
    update.message.reply_text(answer)

def next_full_moon(update, context):
    today = str(datetime.date.today()).replace("-", "/")
    date_moon = ephem.next_full_moon(today).datetime()
    update.message.reply_text(f"Ближайшее полнолуние будет {date_moon.strftime('%d.%m.%Y %H:%M:%S')}")

def play_random_numbers(user_number):
    bot_number = randint(user_number-10, user_number+10)
    if bot_number > user_number:
        message = f"Вы загадали: {user_number}, Я загадал: {bot_number}. Я победил."
    elif bot_number == user_number:
        message = f"Вы загадали: {user_number}, Я загадал: {bot_number}. Ничья."
    elif bot_number < user_number:
        message = f"Вы загадали: {user_number}, Я загадал: {bot_number}. Вы победили."
    return message

def guess_number(update, context):
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_numbers(user_number)
        except (TypeError, ValueError):
            message = "Введите целое число"
    else:
        message = "Введите число"
    update.message.reply_text(message)

def send_cat_picture(update, context):
    cat_photo_list = glob("images/cat*.jp*g")
    cat_photo_filename = choice(cat_photo_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_photo_filename, 'rb'))

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    mybot = Updater(mysettings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_constel))
    dp.add_handler(CommandHandler("wordcount", count_words))
    dp.add_handler(CommandHandler("next_full_moon", next_full_moon))
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(CommandHandler("cat", send_cat_picture))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()
if __name__ == "__main__":
    main()