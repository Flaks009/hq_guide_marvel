import requests
from infra.login_api import *
from dao.characters_search import totalCharacters
from dao.characters_insert import insertCharacters

def characters_list(ts, api_key, hash_key, offset = 0, chars = 0):

    # chars_list = open("Characters", "w+")

    url = "http://gateway.marvel.com/v1/public/characters?ts={}&apikey={}&hash={}&limit=20&offset={}".format(ts, api_key, hash_key, offset)
    request = requests.get(url).json()

    qtyCharacters = totalCharacters()

    if qtyCharacters < int(request['data']['total']):

        while chars < int(request['data']['total']):
        
            characters_page = request['data']['results']
            
            for character in characters_page:
                
                insertCharacters(character)
                # chars_list.write((character['name'] + '\n'))
                chars += 1
            
            offset += 20
            url = "http://gateway.marvel.com/v1/public/characters?ts={}&apikey={}&hash={}&limit=20&offset={}".format(ts, api_key, hash_key, offset)
            request = requests.get(url).json()

        # chars_list.close()
