from login_api import *
import requests

hash1 = key(ts, api_key, pk)

def search(ts, api_key, hash1, char):
    url = "http://gateway.marvel.com/v1/public/characters?ts={}&apikey={}&hash={}&nameStartsWith={}".format(ts, api_key, hash1, char)
    print(url)
    response = requests.get(url).json()

    if int(response['data']['count']) > 0:
        thumb(ts, api_key, hash1, char)
        hq = response['data']['results'][0]['comics']['items'] 
        for item in hq:
            id_hq = item['resourceURI'][43:48]
            print(item['name'])
            cover(id_hq, ts, api_key, hash1)
    else:
        print('Nao encontrado')

def thumb(ts, api_key, hash1, char):
    url = "http://gateway.marvel.com/v1/public/characters?ts={}&apikey={}&hash={}&nameStartsWith={}".format(ts, api_key, hash1, char)
    response = requests.get(url).json()
    image = response['data']['results'][0]['thumbnail']['path'] + "/detail.jpg"
    response_img = requests.get(image)
    char_tumb = open("img.jpg", "wb")
    char_tumb.write(response_img.content)
    char_tumb.close()



def cover(id_hq ,ts, api_key, hash1):
    url = "http://gateway.marvel.com/v1/public/comics/{}?ts={}&apikey={}&hash={}".format(id_hq, ts, api_key, hash1)
    response = requests.get(url).json()
    image = response['data']['results'][0]['thumbnail']['path'] + "/detail.jpg"
    response_img = requests.get(image)
    image_id = "{}".format(id_hq)
    cover_img = open(image_id + ".jpg", "wb")
    cover_img.write(response_img.content)
    cover_img.close()


character = input("Nome personagem:")
search(ts, api_key, hash1, character)

#Personagem --> Edicoes e saga em que aparece --> Imagem das capas