import datetime
import ephem
from glob import glob
from random import choice

import mysettings
from utils import get_smile, play_random_numbers, main_keyboard

def greet_user(update, context):
    print("Вызван /start")
    context.user_data["emoji"] = get_smile(context.user_data)
    update.message.reply_text(
        f"Привет, пользователь!{context.user_data['emoji']}",
        reply_markup=main_keyboard()
    )
def talk_to_me(update, context):
    context.user_data["emoji"] = get_smile(context.user_data)
    text = update.message.text
    print(text)
    update.message.reply_text(f"{text} {context.user_data['emoji']}", reply_markup=main_keyboard())


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
    update.message.reply_text(f'Эта планета сегодня находится в созвездиии {const}',
                              reply_markup=main_keyboard())

def count_words(update, context):
    len_message = len(context.args)
    if len_message == 1:
        answer = f"{len_message} слово."
    elif len_message > 1:
        answer = f"{len_message} слов."
    else:
        answer = "Вы ничего не ввели."
    update.message.reply_text(answer, reply_markup=main_keyboard())

def next_full_moon(update, context):
    today = str(datetime.date.today()).replace("-", "/")
    date_moon = ephem.next_full_moon(today).datetime()
    update.message.reply_text(f"Ближайшее полнолуние будет {date_moon.strftime('%d.%m.%Y %H:%M:%S')}",
                              reply_markup=main_keyboard())

def guess_number(update, context):
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_numbers(user_number)
        except (TypeError, ValueError):
            message = "Введите целое число"
    else:
        message = "Введите число"
    update.message.reply_text(message, reply_markup=main_keyboard())

def send_cat_picture(update, context):
    cat_photo_list = glob("images/cat*.jp*g")
    cat_photo_filename = choice(cat_photo_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_photo_filename, 'rb'), reply_markup=main_keyboard())

def cities_game(update, context):
    context.user_data["cities"] = mysettings.CITY_LIST
    city_list = context.user_data["cities"]
    if context.args:
        user_city = context.args[0].lower()
        if user_city in city_list:
            city_list.remove(user_city)
            for city in city_list:
                if city[0] == user_city[-1]:
                    bot_city = city
                    city_list.remove(bot_city)
                    message = f"{bot_city.capitalize()}, Ваш ход."
                    break
                else:
                    message = "Я не знаю города на тукаю букву. Вы победили!"
        else:
            message = "Такого города нет в списке. Введите другой."
    else:
        message = "Введите название города"
    update.message.reply_text(message, reply_markup=main_keyboard())

def calculation(update, context):
    exercise = context.args
    if exercise:
        try:
            message = "In progress"#eval("".join(exercise))
        except ZeroDivisionError:
            message = "Не делите на ноль, пожалуйста."
        except ValueError:
            message = "Пожалуйста, введите пример корректно. Например: 2+4, 6/8 и т.д"
    else:
        message = "Введите Ваш пример"
    update.message.reply_text(message, reply_markup=main_keyboard())

def user_coordinates(update, context):
    context.user_data["emoji"] = get_smile(context.user_data)
    coords = update.message.location
    update.message.reply_text(f"Ваши координаты {coords} {context.user_data['emoji']}!",
                              reply_markup=main_keyboard())
