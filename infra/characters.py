import requests
from infra.login_api import ts, api_key, pk, key
from dao.characters_search import totalCharacters, insertCharacters, truncateCharacters, searchCharacters

hash1 = key(ts, api_key, pk)

def characters_list(ts = ts, api_key = api_key, hash_key = hash1, offset = 0, chars = 1):

    url = "http://gateway.marvel.com/v1/public/characters?ts={}&apikey={}&hash={}&limit=20&offset={}".format(ts, api_key, hash_key, offset)
    request = requests.get(url).json()

    qtyCharacters = totalCharacters()

    if qtyCharacters < int(request['data']['total']):

        truncateCharacters()

        while chars < int(request['data']['total']):
        
            characters_page = request['data']['results']
            
            for character in characters_page:
                
                insertCharacters(str(character['name']))
                chars += 1
            
            offset += 20
            url = "http://gateway.marvel.com/v1/public/characters?ts={}&apikey={}&hash={}&limit=20&offset={}".format(ts, api_key, hash_key, offset)
            request = requests.get(url).json()
            print(offset)
    
    else:
        print("DB Updated")