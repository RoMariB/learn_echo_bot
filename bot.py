import logging
import ephem

import datetime
from wsgiref.handlers import format_date_time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import mysettings

logging.basicConfig(filename='bot.log', level=logging.INFO, format="%(levelname)s:%(asctime)s - %(message)s")

def greet_user(update, context):
    print("Вызван /start")
    #print(update)
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


def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    mybot = Updater(mysettings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_constel))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()
if __name__ == "__main__":
    main()