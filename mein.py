import os

import requests
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv


def shorten_link(url, token):
    parameters = {
        'access_token': token, 
        'url': url,
        'v': '5.199',
    }
    shorten_link_url = 'https://api.vk.ru/method/utils.getShortLink'
    response = requests.post(shorten_link_url, params=parameters)
    response.raise_for_status()
    answer = response.json()
    short_link = answer['response']['short_url']
    return short_link


def count_clicks(url, token):
    link_parse = urlparse(url)
    short_path = link_parse.path.strip('/').split('/')
    click_parameters = {
        'access_token': token,
        'key': short_path,
        'interval': 'forever',
        'intervals_count': '1',
        'v': '5.199',
    }
    count_clicks_url = 'https://api.vk.ru/method/utils.getLinkStats'
    response = requests.post(count_clicks_url, params=click_parameters)
    response.raise_for_status()
    answer = response.json()
    stats = answer['response']['stats']
    line = stats[0]
    views = line['views']
    return views


def is_shorten_link(url, token):
    link_parse = urlparse(url)
    short_path = link_parse.path.strip('/').split('/')
    click_parameters = {
        'access_token': token,
        'key': short_path,
        'interval': 'forever',
        'intervals_count': '1',
        'v': '5.199',
    }
    count_clicks_url = 'https://api.vk.ru/method/utils.getLinkStats'
    response = requests.post(count_clicks_url, params=click_parameters)
    response.raise_for_status()
    answer = response.json()
    return 'error' in answer
   

if __name__ == '__main__':
    #url = input('Введите ссылку:')
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    args = parser.parse_args()
    url = args.name
    load_dotenv()
    token=os.environ['TOKEN_VK']
    try:
        if is_shorten_link(url, token):
            print('Короткая ссылка:', shorten_link(url, token))
        else:
            print('Количество переходов:', count_clicks(url, token)) 
   
    except requests.exceptions.HTTPError:
        print('Ошибка')
