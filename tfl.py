import requests
import json

URL = 'https://api.tfl.gov.uk/'

def get_url(url):
    url = url + '?app_id=2a3e2338&app_key=240b28f5941f4c099fc40f5af851d5d6'
    response = requests.get(url)
    content = response.content.decode('utf8')
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def getTubeStatus():
    url = URL + 'Line/Mode/Tube/Status'
    js = get_json_from_url(url)
    tubeStat = []
    N = len(js)
    for i in range(N):
        tubeStat.append({'id':js[i]['id'],'status':js[i]['lineStatuses'][0]['statusSeverityDescription']})
    return tubeStat
