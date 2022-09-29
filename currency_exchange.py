import requests


def exchange_rates(your_currency, second_currency, cash):
    url = 'https://open.er-api.com/v6/latest/'
    response = requests.get(f'{url}{your_currency.upper()}')
    response_json = response.json()

    return response_json['rates'][second_currency.upper()] * float(cash)


# currency = input('Введите начальную валюту: ')
# sec_currency = input('Введите желаемую валюту: ')
# your_cash = input('Введите сумму: ')
# print(exchange_rates(currency, sec_currency, your_cash))
