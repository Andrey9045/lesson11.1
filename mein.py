import os

import requests
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
    response_answer = response.json()
    short_link = response_answer['response']['short_url']
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
    response_answer = response.json()
    stats = response_answer['response']['stats']
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
    response_answer = response.json()
    response_list='error' in response_answer#list(response_answer.keys())[0]
 #   result=response_list=='error'
    return response_list#result


if __name__ == '__main__':
    url = input('Введите ссылку:')
    load_dotenv()
    token=os.environ['TOKEN_VK']
    try:
        if is_shorten_link(url, token):
            print('Короткая ссылка:', shorten_link(url, token))
        else:
            print('Количество переходов:', count_clicks(url, token)) 
   
    except requests.exceptions.HTTPError:
        print('Ошибка')
