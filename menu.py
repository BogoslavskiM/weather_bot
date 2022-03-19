from weather import *
import settings as SE

def typing(message, delay):
    if message and delay:
        bot.send_chat_action(
            message.chat.id,
            'typing'
        )
        time.sleep(delay)

def menu(message = None, delay=None):
    typing(message, delay)
    print(menu)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Москва',
            callback_data='moscow'
        ),
        telebot.types.InlineKeyboardButton(
            'Питер',
            callback_data='piter'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Новосибирск',
            callback_data='novosib'
        ),
        telebot.types.InlineKeyboardButton(
            'Калининград',
            callback_data='kaliningrad'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Владивосток',
            callback_data='vladik'
        ),
        telebot.types.InlineKeyboardButton(
            'Казань',
            callback_data='kazan'
        )
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            'Указать свой',
            callback_data='my_city'
        )
    )
    if SE.is_menu:
        bot.send_message(
            message.chat.id,
            'Выбери город, чтобы узнать погоду: ',
            reply_markup=keyboard
        )
    SE.is_menu = False

@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    typing(query.message, 0)
    message = ''
    SE.is_menu = True
    if query.data == 'moscow':
        message = get_weather_str('Москва', 'RU')
    if query.data == 'piter':
        message = get_weather_str('Санкт-Петербург', 'RU')
    if query.data == 'novosib':
        message = get_weather_str('Новосибирск', 'RU')
    if query.data == 'kaliningrad':
        message = get_weather_str('Калининград', 'RU')
    if query.data == 'vladik':
        message = get_weather_str('Владивосток', 'RU')
    if query.data == 'kazan':
        message = get_weather_str('Казань', 'RU')
    if query.data == 'my_city':
        message = 'Введите название города: '
    bot.send_message(
        query.message.chat.id,
        message
    )
    menu(query.message, 3)