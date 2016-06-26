import requests
import json

def get_your_coordinates():
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    lat = j['latitude']
    lon = j['longitude']
    coordinates = '{latitude},{longitude}'.format(latitude=lat,longitude=lon)
    return coordinates
