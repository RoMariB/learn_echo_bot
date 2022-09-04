import logging
from wsgiref.handlers import format_date_time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import mysettings

logging.basicConfig(filename='bot.log', level=logging.INFO, format="%(levelname)s:%(asctime)s - %(message)s")

def greet_user(update, context):
    print("Вызван /start")
    #print(update)
    update.message.reply_text("Привет, пользователь! Как джина из лампы, ты вызвал команду /start")

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    mybot = Updater(mysettings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()
if __name__ == "__main__":
    main()