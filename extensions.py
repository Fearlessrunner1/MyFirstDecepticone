import json
import requests
from config import keys

class ApiException(Exception):
  pass


class Converter():
  @staticmethod
  def get_price(base, sym, amount):
    try:
        base_key = keys[base.lower()]
    except KeyError:
        raise ApiException(f"Валюта {base} не найдена!")

    try:
        sym_key = keys[sym.lower()]
    except KeyError:
        raise ApiException(f"Валюта {sym} не найдена!")

    if base_key == sym_key:
        raise ApiException(f'Невозможно перевести одинаковые валюты {base}!')

    try:
        amount = float(amount)
    except ValueError:
        raise ApiException(f'Не удалось обработать количество {amount}!')
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={sym_key}&from={base_key}&amount={amount}"
    payload = {}
    headers = {
        "apikey": "ihtvdYmiRZiGBg5235HiVErXAXeuQpnc"
    }
    r = requests.request("GET", url, headers=headers, data=payload)
    result = json.loads(r.content)
    price = round(result['result'], 2)
    return price

