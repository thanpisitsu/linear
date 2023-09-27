import requests
from bs4 import BeautifulSoup
import pandas as pd

def digitleft(str) :
    while not str[-1].isdigit() :
        if len(str) == 1 :
            return 0
        str = str[:-1]
    return str

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
list=[]
for i in range(10) :
    url = "https://boardgamegeek.com/boardgame/"+str(i+1)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    keyweight = '"avgweight":"'
    keyminplayer = '"minplayers":"'
    keymaxplayer = '"maxplayers":"'
    keyvote = '"numweights":"'
    keyplaytime = '"maxplaytime":"'
    datastat = str(soup)
    range = datastat.find('"rank":"')
    datastat = datastat[range:range+2000]

    error = soup.find('div',class_='messagebox error')
    if not error :
        keyvote_index = datastat.find(keyvote)
        game_keyvote = digitleft(datastat[keyvote_index + len(keyvote):keyvote_index + len(keyvote) + 10])

        if int(game_keyvote) >= 50 :
            game_title = soup.find("meta", property="og:title")["content"]
            keyweight_index = datastat.find(keyweight)
            keyminplayer_index = datastat.find(keyminplayer)
            keymaxplayer_index = datastat.find(keymaxplayer)
            keyplaytime_index = datastat.find(keyplaytime)
            game_weight = digitleft(datastat[keyweight_index + len(keyweight):keyweight_index + len(keyweight) + 10])
            game_minplayer = digitleft(datastat[keyminplayer_index + len(keyminplayer):keyminplayer_index + len(keyminplayer) + 10])
            game_maxplayer = digitleft(datastat[keymaxplayer_index + len(keymaxplayer):keymaxplayer_index + len(keymaxplayer) + 10])
            game_playtime = digitleft(datastat[keyplaytime_index + len(keyplaytime):keyplaytime_index + len(keyplaytime) + 10])

            data = {
                "Title": game_title,
                "Weight": float(game_weight)*100,
                "Min player": game_minplayer,
                "Max player": game_maxplayer,
                "Play time":game_playtime
            }
            list.append(data)

df = pd.DataFrame(list)

print(df)
