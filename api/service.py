import json
import requests 
import unicodedata

class Musicas:
    
    def filtro(nome):
        nome = nome.replace(" ", "-")
        
        URL = 'http://api.genius.com/search/'
        TOKEN = 'gcBfPOSLKKx4BXKq5w6R1zzBkj154sO3V-wuYkcOHM97Z_wFeKM4sjkPkYudDj0t'
        acess = 'Bearer {}'.format(TOKEN)
        headers = {'Authorization': acess}    

        parametros ={'q': nome}
        resposta = requests.get(URL,params=parametros,headers=headers)


        lista_de_musicas = resposta.text
        

    
       
        json_retorno = json.dumps(lista_de_musicas)

        return json_retorno

       