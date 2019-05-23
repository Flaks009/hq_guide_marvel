import requests
from infra.login_api import *
from dao.characters_search import totalCharacters, insertCharacters, truncateCharacters, searchCharacters

def characters_list(ts, api_key, hash_key, offset = 0, chars = 1):

    # chars_list = open("Characters", "w+")

    url = "http://gateway.marvel.com/v1/public/characters?ts={}&apikey={}&hash={}&limit=20&offset={}".format(ts, api_key, hash_key, offset)
    request = requests.get(url).json()

    qtyCharacters = totalCharacters()

    if qtyCharacters < int(request['data']['total']):

        truncateCharacters()

        while chars < int(request['data']['total']):
        
            characters_page = request['data']['results']
            
            for character in characters_page:
                
                insertCharacters(str(character['name']))
                # chars_list.write((character['name'] + '\n'))
                chars += 1
                print(chars)
                print(character['name'])
            
            offset += 20
            url = "http://gateway.marvel.com/v1/public/characters?ts={}&apikey={}&hash={}&limit=20&offset={}".format(ts, api_key, hash_key, offset)
            request = requests.get(url).json()
    
    else:
        print("DB Updated")

        # chars_list.close()
