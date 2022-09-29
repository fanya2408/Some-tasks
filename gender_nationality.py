import requests


def gender(some_name):

    url = 'https://api.genderize.io/?name='
    response = requests.get(f'{url}{some_name}')
    response_json = response.json()

    return response_json


def nationality(some_name):

    url = 'https://api.nationalize.io/?name='
    response = requests.get(f'{url}{some_name}')
    response_json = response.json()

    return response_json


# name = input('Enter your name: ')
#
# your_gender = gender(name)
# your_nationality = nationality(name)
#
# print(f'Your gender: {your_gender["gender"]}')
# print(f'Probability: {your_gender["probability"] * 100} %')
#
# for place in your_nationality['country']:
#     print(f'Your nationality: {place["country_id"]} with a probability of {place["probability"] * 100 :.1f} %')
