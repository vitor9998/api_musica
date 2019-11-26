import json
import requests 
import unicodedata

class Musicas:
    
    def filtro(nome):
        
        nome = nome.replace(" ","-")
        URL = 'http://api.genius.com/search/' + str(nome)
        TOKEN = 'gcBfPOSLKKx4BXKq5w6R1zzBkj154sO3V-wuYkcOHM97Z_wFeKM4sjkPkYudDj0t'
        acess = 'Bearer {}'.format(TOKEN)
        headers = {'Authorization': acess}    
   
        resposta = requests.get(URL,headers=headers)
        lista_de_musicas = resposta.text
        

    

        return lista_de_musicas

       