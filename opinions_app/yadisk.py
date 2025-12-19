import os
import urllib
from pprint import pprint

import requests
from dotenv import load_dotenv

API_HOST = 'https://cloud-api.yandex.net/'
API_VERSION = 'v1'
DISK_INFO_URL = f'{API_HOST}{API_VERSION}/disk/'
REQUEST_UPLOAD_URL = f'{API_HOST}{API_VERSION}/disk/resources/upload'

# Загрузить из .env значение токена.
load_dotenv()
DISK_TOKEN = os.environ.get('DISK_TOKEN')

# Словарь с заголовком авторизации.
AUTH_HEADERS = {
    'Authorization': f'OAuth {DISK_TOKEN}'
}

# Запрос.
response = requests.get(url=DISK_INFO_URL, headers=AUTH_HEADERS)

pprint(response.json())

payload = {
    # Загрузить файл с названием filename.txt в папку приложения.
    'path': 'app:/filename.txt',
    'overwrite': 'True'  # Если файл существует, перезаписать его.
}
response = requests.get(
    headers=AUTH_HEADERS,  # Заголовок для авторизации.
    params=payload,  # Указать параметры.
    url=REQUEST_UPLOAD_URL
)

print(response.json()['href'])

upload_url = response.json()['href']

with open('filename.txt', 'rb') as file:
    response = requests.put(
        data=file,
        url=upload_url,
    )

# Расположение файла находится в заголовке Location.
location = response.headers['Location']
# Декодировать строку при помощи модуля urllib.
location = urllib.parse.unquote(location)
# Убрать первую часть расположения файла /disk,
# она не понадобится.
location = location.replace('/disk', '')
print(location)
