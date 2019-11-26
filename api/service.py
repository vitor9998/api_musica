import json
import requests 
import unicodedata

class Musicas:
    def __init__(nome):
        pass
    def filtro(nome):
        
        nome = nome.replace("","-")
        URL = 'http://api.genius.com/search/' + str(nome)
        TOKEN = 'NnasQ_313kmVSFmWp9fujcP7GgP_QQ1kHK1ho-fiAgW7heMhcmjGXmsSj-bIG0zh'
        acess = 'Bearer {}'.format(TOKEN)
        headers = {'Authorization': acess}    
   
        resposta = requests.request('GET',URL,headers=headers)
        lista_de_musicas = resposta.json()['response']['songs']
   
    
        top_10 = []
        x=1 
        if len(lista_de_musicas) >= 10:
            for musica in lista_de_musicas[:10]:
            
                x = x+1
                top_10.append(unicodedata.normalize("NFKD",musica['full_title']))
 
        else:
            for musica in lista_de_musicas:
                top_10.append(unicodedata.normalize("NFKD",musica['full_title']))

    

        return lista_de_musicas

       