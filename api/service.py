import json
import requests 
import unicodedata

class Musicas:
    def __init__(self):
        pass
    
    id_artista = input('Insira o id do artista:')
    
    URL = 'http://api.genius.com/artists/' + str(id_artista) + '/songs?sort=popularity'
    TOKEN = 'LgZ_f6BpJjcChErOFai9GG50IL7IDaWZlHLpdvtIfPTJYhl5GbB-XO4SvgS_-YvD'
    acess = 'Bearer {}'.format(TOKEN)
    headers = {'Authorization': acess}
    print('HEADER MONTADO')
    resposta = requests.request('GET',URL,headers=headers)
    lista_de_musicas = resposta.json()['response']['songs']
    print('LSITA DE MUSICAS MONTADA')
    
    top_10 = []
    x=1
    if len(lista_de_musicas) >= 10:
        for musica in lista_de_musicas[:10]:
            print( 'Musica top', x)
            print(musica['full_title'])
            print('========================================================')
            x = x+1
            top_10.append(unicodedata.normalize("NFKD",musica['full_title']))
 
    else:
        for musica in lista_de_musicas:
            top_10.append(unicodedata.normalize("NFKD",musica['full_title']))

    print('Printando Top 10')
    print(top_10)
