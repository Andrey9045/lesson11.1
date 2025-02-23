import os

import requests
from urllib.parse import urlparse
from dotenv import load_dotenv


def shorten_link(token, url):
    response = requests.post(url, params=token)
    response.raise_for_status()
    adress = response.json()
    try:
        short_link = adress['response']['short_url']
    except requests.exceptions.HTTPError:
        short_link = 'Ошибка'
    return short_link


def count_clicks(token_click, url_click):
    response = requests.post(url_click, params=token_click)
    response.raise_for_status()
    adress = response.json()
    try:
        stats = adress['response']['stats']
        line = stats[0]
        views = line['views']
    except requests.exceptions.HTTPError:
        views = 'Ошибка'
    return views


def is_shorten_link(link):
    parse = urlparse(link)
    if parse.netloc == 'vk.cc':
        print('Количество переходов', count_clicks(token_click, url_click))
    else:
        print('Сокращенная ссылка', shorten_link(token, url))


if __name__ == '__main__':
    link = input('Введите ссылку:')
    load_dotenv()
    token = {
        'access_token': os.getenv("TOKEN"),
        'url': link,
        'v': '5.199',
    }
    url = 'https://api.vk.ru/method/utils.getShortLink'
    url_click = 'https://api.vk.ru/method/utils.getLinkStats'
    link_parse = urlparse(link)
    short_path = link_parse.path.strip('/').split('/')

    token_click = {
        'access_token': os.getenv("TOKEN"),
        'key': short_path,
        'interval': 'forever',
        'intervals_count': '1',
        'v': '5.199',
    }
    is_shorten_link(link)
