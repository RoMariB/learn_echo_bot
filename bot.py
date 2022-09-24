import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from handlers import (greet_user, planet_constel, count_words,
                      next_full_moon, guess_number, send_cat_picture,
                      cities_game, calculation, user_coordinates, talk_to_me)
import mysettings

logging.basicConfig(filename='bot.log', level=logging.INFO, format="%(levelname)s:%(asctime)s - %(message)s")

def main():
    mybot = Updater(mysettings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_constel))
    dp.add_handler(CommandHandler("wordcount", count_words))
    dp.add_handler(CommandHandler("next_full_moon", next_full_moon))
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(CommandHandler("cat", send_cat_picture))
    dp.add_handler(CommandHandler("cities", cities_game))
    dp.add_handler(CommandHandler("calc", calculation))
    dp.add_handler(MessageHandler(Filters.regex("^(Прислать котика)$"),send_cat_picture))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()