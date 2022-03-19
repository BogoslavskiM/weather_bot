import json
import requests
import telebot
import time

# API openweathermap.org
version = '2.5'
URL = 'http://api.openweathermap.org/data/' + version + '/forecast'
key = 'ccb5b713996eaf0fb6e9ce06d0244fcd'
lang = 'ru'
units = 'metric'

# API telegram
TOKEN = 'telegram_bot_token'
bot = telebot.TeleBot(TOKEN)

# Menu status
is_menu = False


