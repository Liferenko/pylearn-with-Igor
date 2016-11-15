# coding: utf-8
"""
найти функции и запросы, которые нужны нам для использования от Фейсбука. Какие запросы фб должен получить для выполнения операции.
прочитать что такое requests - http://docs.python-requests.org/en/master/

подготовить авторизацию для приложения

рабочие запросы ищем здесь - https://developers.facebook.com/docs/marketing-api/buying-api

ссылка на Гитхаб фейсбук питон эдс сдк - https://github.com/facebook/facebook-python-ads-sdk


Возможно, это то, что нужно для постановки рекламы на паузу (https://developers.facebook.com/docs/marketing-api/ads-management/your-first-ad#campaign)
from facebookads.adobjects.ad import Ad

ad = Ad(parent_id='act_<AD_ACCOUNT_ID>')
ad[Ad.Field.name] = 'My Ad'
ad[Ad.Field.adset_id] = <AD_SET_ID>
ad[Ad.Field.creative] = {
    'creative_id': <CREATIVE_ID>,
}
ad.remote_create(params={
    'status': Ad.Status.paused,
})
"""

# import requests
from facebookads.api import FacebookAdsApi
from facebookads import objects

def request_by_url(url, method='get'):
    pass

my_app_id = '551066188429081'
my_app_secret = '756ff1cf3e2bf9a7e6c017fc8202ed5c'
my_access_token = '551066188429081|f9vbeY6E6y0KeMwM4FMuvq3WHB0'
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

me = objects.AdUser(fbid='me')
my_account = list(me.get_ad_accounts())
print(my_account)