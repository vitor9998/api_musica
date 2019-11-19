import json
import requests 
import unicodedata
 
URL = 'http://api.genius.com/artists/16775/songs?sort=popularity'
TOKEN = 'AKqLwbINrDB5ArARDt-d7mHESoQEzkZSOoSWXUcAdI5ZvsjneeKJdFsQZCsrqWvg'
acess = 'Bearer {}'.format(TOKEN)
headers = {'Authorization': acess}

resposta = requests.request('GET',URL,headers=headers)
lista_de_musicas = resposta.json()['response']['songs']
 
top_10 = []
if len(lista_de_musicas) >= 10:
    for musica in lista_de_musicas[:10]:
        top_10.append(unicodedata.normalize("NFKD",musica['full_title']))
 
else:
    for musica in lista_de_musicas:
        top_10.append(unicodedata.normalize("NFKD",musica['full_title']))


