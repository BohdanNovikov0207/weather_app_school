import requests
from .write_json import write
# requests - module for sending requests
# get - gets date about adress
api_key = "f45b384d06f8d6558d2f50d57cd3220f"

# Ilmainfo päring(запрос) API kaudu
def get_info_weather(city_name: str, file_name: str, forecast: bool):
    if forecast:
        url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&lang=en&units=metric'
    else:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&lang=en&units=metric'

    data = requests.get(url)
    if data.status_code == 200:
        write(file_name, data.json())
    else:
        print("Error - ",data.status_code)
        