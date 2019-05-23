from infra.login_api import *
from dao.characters_search import searchCharacters
import requests

hash1 = key(ts, api_key, pk)

def search(char , page = 0, ts = ts, api_key = api_key, hash1 = hash1):
    url = "http://gateway.marvel.com/v1/public/characters?ts={}&apikey={}&hash={}&name={}".format(ts, api_key, hash1, char)
    response = requests.get(url).json()
    return_list = []
    if int(response['data']['count']) > 0:
        name = response['data']['results'][0]['name']
        id_character = response['data']['results'][0]['id']
        pages = (int(response['data']['results'][0]['comics']['available']) // 20)
        thumbnail = thumb(ts, api_key, hash1, char)
        page = page * 20
        comics_dict = comics(id_character, ts, api_key, hash1, offset = page)
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


    

def thumb(ts, api_key, hash1, char):
    url = "http://gateway.marvel.com/v1/public/characters?ts={}&apikey={}&hash={}&nameStartsWith={}".format(ts, api_key, hash1, char)
    response = requests.get(url).json()
    image = response['data']['results'][0]['thumbnail']['path'] + "/detail.jpg"
    #response_img = requests.get(image)
    #char_tumb = open("img.jpg", "wb")
    #char_tumb.write(response_img.content)
    #char_tumb.close()
    return image


def cover(id_hq ,ts, api_key, hash1):
    url = "http://gateway.marvel.com/v1/public/comics/{}?ts={}&apikey={}&hash={}".format(id_hq, ts, api_key, hash1)
    response = requests.get(url).json()
    cover_info = []
    image = response['data']['results'][0]['thumbnail']['path'] + "/detail.jpg"
    cover_title = response['data']['results'][0]['title']
    #response_img = requests.get(image)
    #image_id = "{}".format(id_hq)
    #cover_img = open(image_id + ".jpg", "wb")
    #cover_img.write(response_img.content)
    #cover_img.close()
    cover_info.append(image)
    cover_info.append(cover_title)
    return cover_info

def comics(id_character ,ts, api_key, hash1, offset = 0):
    url = "http://gateway.marvel.com/v1/public/characters/{}/comics?ts={}&apikey={}&hash={}&offset={}".format(id_character, ts, api_key, hash1, offset)
    response = requests.get(url).json()
    comics_ed = response['data']['results']
    comics_dict = {}

    for comic in comics_ed:
        comics_dict[comic["id"]] = {} 
        comics_dict[comic["id"]] = {"id":comic["id"], "title":comic["title"], "thumbnail": comic["thumbnail"]}
        comics_dict[comic["id"]]["thumbnail"]["path"] += "/detail.jpg"
        
    return comics_dict


#Personagem --> Edicoes e saga em que aparece --> Imagem das capas