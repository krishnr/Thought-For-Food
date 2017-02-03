from flask import Flask
from flask import render_template

import requests
import requests.auth
import json
import re

app = Flask(__name__)

@app.route('/')
def index():

    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    access_token = response.json()['access_token']
    token_type = response.json()['token_type']
    auth_string = token_type + ' ' + access_token

    url = 'https://oauth.reddit.com/r/mealtimevideos/top/.json?t=week&limit=5'
    headers['Authorization'] = auth_string
    response = requests.get(url, headers=headers)
    links = []
    for i in range(0,len(response.json()['data']['children'])):
        print response.json()['data']['children'][i]['data']['url']
        links.append(re.search(r"([\w-]+)$",response.json()['data']['children'][i]['data']['url']).group(0))
    print links
    src = 'https://youtube.com/embed/' + links[0] + '?playlist=' + ','.join(links[1:])
    print src
    return render_template('index.html', src=src)

if __name__ == '__main__':
        app.run(debug=True)
