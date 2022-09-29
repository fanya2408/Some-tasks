import requests


def find_ip():

    url = 'https://api.ipify.org?format=json'
    response = requests.get(url)
    response_json = response.json()

    return response_json['ip']


def find_location_by_ip(ip_):

    url = 'https://sys.airtel.lv/ip2country/'
    response = requests.get(f'{url}{ip_}/?full=true')
    response_json = response.json()

    return response_json


ip = find_ip()
location_data = find_location_by_ip(ip)

print(f'Country: {location_data["country"]}')
print(f'City: {location_data["city"]}')
print(f'Lat: {location_data["lat"]}')
print(f'Lon: {location_data["lon"]}')