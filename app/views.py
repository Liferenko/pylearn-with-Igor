from app import app
from flask import render_template, request
import requests

@app.route('/')
@app.route('/index')
def index():
    user_code = request.args.get('code')
    my_app_id = '551066188429081'
    params = {'fb_api_version': 'v2.8',
              'client_id': my_app_id,
              'redirect_uri': 'http://localhost:5000/'
              }
    if user_code:
        result = requests.get('https://graph.facebook.com/v2.8/oauth/access_token',
                     params={'client_id': params['client_id'],
                             'redirect_uri': params['redirect_uri'],
                             'client_secret': '756ff1cf3e2bf9a7e6c017fc8202ed5c',
                             'code': user_code})
        print(result.content.decode())

    return render_template('index.html',
                           title='FacebookAds',
                           index_content='Facebook567',
                           params=params)
