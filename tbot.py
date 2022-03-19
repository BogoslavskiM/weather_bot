import urllib

from menu import *

def value(value):
    if value:
        return value
    else:
        return ' '

@bot.message_handler(commands=['start'])
def start_message(message):
    user = message.from_user
    print(user)
    typing(message, 0)
    bot.send_message(
        message.chat.id,
        '👍 Привет, '
        + value(user.first_name)
        + ' ' + value(user.last_name)
    )
    typing(message, 0)
    menu(message)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(
        message.chat.id,
        'Внимание! *Ты можешь*: \n' +
        '/start - перезапускает бота \n' +
        '/help - выводит справку'
    )

@bot.message_handler(content_types=['text'])
def message_callback(message):
    print(message)
    typing(message, 0)
    if message.text == 'document':
        file = open('documents/file_9.docx', 'rb')
        bot.send_document(
            message.chat.id,
            file
        )
    else:
        bot.send_message(
            message.chat.id,
            get_weather_str(message.text)
        )
    bot.send_message(
        message.chat.id,
        menu(message)
    )


@bot.message_handler(content_types=['sticker'])
def message_sticker(message):
    mes = ''
    em = message.sticker.emoji
    print(em)
    if em == '🙈': mes = 'Не пугайся!'
    if em == '😂': mes = 'Ура! Мне нравится, когда ты смеешься!'
    if em == '😭': mes = 'ооо... что тебя так сильно расстроило?'
    if em == '👋': mes = 'И тебе привет'
    if em == '👍': mes = 'ХЕЕЕЕ! Мне тоже это нравится :)'
    bot.send_message(
        message.chat.id,
        mes
    )


@bot.message_handler(content_types=['document'])
def message_document(message):
    document_id = message.document.file_id
    file_info = bot.get_file(document_id)
    urllib.request.urlretrieve(f'http://api.telegram.org/file/bot{TOKEN}/{file_info.file_path}', file_info.file_path)


@bot.message_handler(content_types=['voice'])
def message_voice(message):
    print(message)
    print(message.voice)
    print(message.voice.file_id)