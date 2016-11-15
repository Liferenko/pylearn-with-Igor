from facebookads.api import FacebookAdsApi
from facebookads import objects

me = objects.AdUser(fbid='me')
my_account = list(me.get_ad_accounts())
print(my_account)

def facebook_init(access_token):
    my_app_id = '551066188429081'
    my_app_secret = '756ff1cf3e2bf9a7e6c017fc8202ed5c'
    FacebookAdsApi.init(my_app_id, my_app_secret, access_token)