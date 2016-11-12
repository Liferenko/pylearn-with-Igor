# coding: utf-8
"""
найти функции и запросы, которые нужны нам для использования от Фейсбука. Какие запросы фб должен получить для выполнения операции.
прочитать что такое requests - http://docs.python-requests.org/en/master/

подготовить авторизацию для приложения

рабочие запросы ищем здесь - https://developers.facebook.com/docs/marketing-api/buying-api

ссылка на Гитхаб фейсбук питон эдс сдк - https://github.com/facebook/facebook-python-ads-sdk
"""

import requests
from facebookads.api import FacebookAdsApi
from facebookads import objects

def request_by_url(url, method='get'):
    pass

my_app_id = '551066188429081'
my_app_secret = '756ff1cf3e2bf9a7e6c017fc8202ed5c'
my_access_token = '551066188429081|f9vbeY6E6y0KeMwM4FMuvq3WHB0'
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

