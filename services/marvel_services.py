from infra.login_api import ts, api_key, hash_key
from dao.characters_search import searchCharacters, randomCharacters
import requests

def search(char , page = 0, ts = ts, api_key = api_key, hash_key = hash_key):
    url = "http://gateway.marvel.com/v1/public/characters?ts={}&apikey={}&hash={}&name={}".format(ts, api_key, hash_key, char)
    response = requests.get(url).json()
    return_list = []
    if int(response['data']['count']) > 0:
        name = response['data']['results'][0]['name']
        id_character = response['data']['results'][0]['id']
        pages = (int(response['data']['results'][0]['comics']['available']) // 20)
        thumbnail = thumb(char)
        page = page * 20
        comics_dict = comics(id_character, offset = page)
        return_list.append(name)
        return_list.append(thumbnail)
        return_list.append(comics_dict)
        return_list.append(pages)

        return return_list

    else:
        return None

def search_DB(chars_form):
    chars = searchCharacters(chars_form)
    if len(chars) == 1:
        return chars
    else:
        for char in chars:
            if char[0] == chars_form:
                chars = [char]
                return chars
        return chars

def create_hyperlinks(chars):

    hyperlinks = []
    for char in chars:
        hyperlinks.append(char[0])
    
    return hyperlinks

def randomize(char_id):

    chars = randomCharacters(char_id)

    return [chars]

    

def thumb(char, ts = ts, api_key = api_key, hash_key = hash_key):
    url = "http://gateway.marvel.com/v1/public/characters?ts={}&apikey={}&hash={}&nameStartsWith={}".format(ts, api_key, hash_key, char)
    response = requests.get(url).json()
    image = response['data']['results'][0]['thumbnail']['path'] + "/detail.jpg"
    return image


def comics(id_character ,ts = ts, api_key = api_key, hash_key = hash_key, offset = 0):
    url = "http://gateway.marvel.com/v1/public/characters/{}/comics?ts={}&apikey={}&hash={}&offset={}".format(id_character, ts, api_key, hash_key, offset)
    response = requests.get(url).json()
    comics_ed = response['data']['results']
    comics_dict = {}

    for comic in comics_ed:
        comics_dict[comic["id"]] = {} 
        comics_dict[comic["id"]] = {"id":comic["id"], "title":comic["title"], "thumbnail": comic["thumbnail"]}
        comics_dict[comic["id"]]["thumbnail"]["path"] += "/detail.jpg"
        
    return comics_dict
