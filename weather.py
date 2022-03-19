from settings import *

def get_weather(city, country):
    response = requests.get(URL,
    params= {'q': city + ',,' + country, 'units': units, 'lang': lang, 'APPID': key})
    return response.json()

def get_weather_str(city, country='Russia'):
    print('get_weather_str')
    result = 'Такого города не существует. Попробуйте еще раз:'
    try:
        data = get_weather(city, country)
        i = data['list'][0]
        result = city + ': ' + '{0:+3.0f}'.format(i['main']['temp']) + ' ' \
           + i['weather'][0]['description']
    except:
        print('city not found')
    return result