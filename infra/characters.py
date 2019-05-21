import requests
from login_api import *

hash1 = key(ts, api_key, pk)

def characters_list(ts, api_key, hash1, offset = 0, chars = 0):

    chars_list = open("Characters", "w+")

    url = "http://gateway.marvel.com/v1/public/characters?ts={}&apikey={}&hash={}&limit=20&offset={}".format(ts, api_key, hash1, offset)
    request = requests.get(url).json()

    while chars < 1492:
    
        characters_page = request['data']['results']
        
        for character in characters_page:
            chars_list.write((character['name'] + '\n'))
            chars += 1
            print(chars)
        
        offset += 20
        url = "http://gateway.marvel.com/v1/public/characters?ts={}&apikey={}&hash={}&limit=20&offset={}".format(ts, api_key, hash1, offset)
        request = requests.get(url).json()

    chars_list.close()

characters_list(ts, api_key, hash1)