from emoji import emojize
from random import randint, choice
from telegram import ReplyKeyboardMarkup, KeyboardButton

import mysettings

def get_smile(user_data):
    if "emoji" not in user_data:
        smile = choice(mysettings.USER_EMOJI)
        return emojize(smile, language="alias")
    return user_data["emoji"]

def play_random_numbers(user_number):
    bot_number = randint(user_number-10, user_number+10)
    if bot_number > user_number:
        message = f"Вы загадали: {user_number}, Я загадал: {bot_number}. Я победил."
    elif bot_number == user_number:
        message = f"Вы загадали: {user_number}, Я загадал: {bot_number}. Ничья."
    elif bot_number < user_number:
        message = f"Вы загадали: {user_number}, Я загадал: {bot_number}. Вы победили."
    return message

def main_keyboard():
    return ReplyKeyboardMarkup([["Прислать котика", KeyboardButton("Мои координаты", request_location=True)]])