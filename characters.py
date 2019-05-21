import requests
from login_api import *

hash1 = key(ts, api_key, pk)

arquivo = open("Characters", "w+")

offset = 0
chars = 0

url = "http://gateway.marvel.com/v1/public/characters?ts={}&apikey={}&hash={}&limit=20&offset={}".format(ts, api_key, hash1, offset)
retorno = requests.get(url).json()

while chars < 1492:
  
    nomes = retorno['data']['results']
    
    for personagem in nomes:
        arquivo.write((personagem['name'] + '\n'))
        chars += 1
        print(chars)
    
    offset += 20
    url = "http://gateway.marvel.com/v1/public/characters?ts={}&apikey={}&hash={}&limit=20&offset={}".format(ts, api_key, hash1, offset)
    retorno = requests.get(url).json()

arquivo.close()