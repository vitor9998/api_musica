import json
import requests 
import unicodedata

class Musicas:
    
    def filtro(nome):
        nome = nome.replace(" ", "-")
        
        URL = 'http://api.genius.com/search/'
        TOKEN = 'HDtgGosj0bcrers8lnX_W0cmO6el8DRIlnLrOX4fh6BYN9u6xttBu-xSiegzi8f_'
        acess = 'Bearer {}'.format(TOKEN)
        headers = {'Authorization': acess}    

        parametros ={'q': nome}
        resposta = requests.get(URL,params=parametros,headers=headers)


        lista_de_musicas = resposta.text    
        

    
       
        json_retorno = json.loads(lista_de_musicas)

       
        A = []
        a=0
        for OBJETO in json_retorno['response']['hits']:
            B = {}
            a += 1
            B[f'top:{a}'] = OBJETO['result']['title']

            A.append(B)

        return A

            


        


    











        
       
       