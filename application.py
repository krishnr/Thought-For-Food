from flask import Flask
from flask import render_template

import requests
import requests.auth
import json
import re
from personal import private
import video

app = Flask(__name__)

@app.route('/')

def index():
    num_videos = 5

    url = 'https://reddit.com/r/mealtimevideos/top/.json?t=week&limit=%s' % num_videos
    response = requests.get(url, headers = {'User-agent': 'Chrome'})

    links = []
    assert len(response.json()['data']['children']) == num_videos

    for i in range(num_videos):
        url = response.json()['data']['children'][i]['data']['url']
        link = video.get_video_id(url)
        links.append(link)

    src = 'https://youtube.com/embed/' + links[0] + '?playlist=' + ','.join(links[1:])

    return render_template('index.html', src=src)

if __name__ == '__main__':
        app.run(debug=True)