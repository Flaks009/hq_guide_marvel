from infra.login_api import *
import requests

hash1 = key(ts, api_key, pk)

def search(char ,ts = ts, api_key = api_key, hash1 = hash1):
    url = "http://gateway.marvel.com/v1/public/characters?ts={}&apikey={}&hash={}&nameStartsWith={}".format(ts, api_key, hash1, char)
    response = requests.get(url).json()
    list_cover = []
    return_list = []

    if int(response['data']['count']) > 0:
        thumbnail = thumb(ts, api_key, hash1, char)
        hq = response['data']['results'][0]['comics']['items']
        return_list.append(thumbnail)
        for item in hq:
            id_hq = item['resourceURI'][43:48]
            list_cover.append(cover(id_hq, ts, api_key, hash1))
    else:
        return None

    return_list.append(list_cover)    

    return return_list

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
    image = response['data']['results'][0]['thumbnail']['path'] + "/detail.jpg"
    #response_img = requests.get(image)
    #image_id = "{}".format(id_hq)
    #cover_img = open(image_id + ".jpg", "wb")
    #cover_img.write(response_img.content)
    #cover_img.close()
    return image    

#Personagem --> Edicoes e saga em que aparece --> Imagem das capas