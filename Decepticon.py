import telebot
from extensions import Converter, ApiException
from config import *


@bot.message_handler(commands=['start', 'help'])
def start_help_info(message: telebot.types.Message):
    text = 'Чтобы получить интересующую Вас информацию по актуальному курсу валют' \
           'введите данные в следующем формате: \n <имя валюты> ' \
           '<в какую валюту перевести> ' \
           '<количество валюты>\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    try:
        base, sym, amount = message.text.split()
    except ValueError as e:
        bot.reply_to('Неверное количество параметров!')
    try:
        price = Converter.get_price(base, sym, amount)
        bot.reply_to(message, f"Цена {amount} {base} в {sym} : {price}")
    except ApiException as e:
        bot.reply_to(f"Ошибка в команде:\n{e}")


bot.polling()
