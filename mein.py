import os

import requests
from urllib.parse import urlparse
from dotenv import load_dotenv


def shorten_link(parameters):
    shorten_link_url = 'https://api.vk.ru/method/utils.getShortLink'
    response = requests.post(shorten_link_url, params=parameters)
    response.raise_for_status()
    response_dict = response.json()
    short_link = response_dict['response']['short_url']
    return short_link


def count_clicks(click_parameters):
    count_clicks_url = 'https://api.vk.ru/method/utils.getLinkStats'
    response = requests.post(count_clicks_url, params=click_parameters)
    response.raise_for_status()
    response_json = response.json()
    stats = response_json['response']['stats']
    line = stats[0]
    views = line['views']
    return views


def is_shorten_link(click_parameters):
    count_clicks_url = 'https://api.vk.ru/method/utils.getLinkStats'
    response = requests.post(count_clicks_url, params=click_parameters)
    response.raise_for_status()
    response_json = response.json()
    response_json_list=list(response_json.keys())
    response_json_str=response_json_list[0]
    if response_json_str=='error':
        return False
    else:   
        return True


if __name__ == '__main__':
    url = input('Введите ссылку:')
    load_dotenv()
    parameters = {
        'access_token': os.getenv("TOKEN"), 
        'url': url,
        'v': '5.199',
    }
    link_parse = urlparse(url)
    short_path = link_parse.path.strip('/').split('/')
    click_parameters = {
        'access_token': os.getenv("TOKEN"),
        'key': short_path,
        'interval': 'forever',
        'intervals_count': '1',
        'v': '5.199',
    }
    try:
        if is_shorten_link(click_parameters)==True:
            print('Количество переходов:', count_clicks(click_parameters))
        else:
            print('Короткая ссылка:', shorten_link(parameters)) 
   
    except requests.exceptions.HTTPError:
        print('Ошибка')
