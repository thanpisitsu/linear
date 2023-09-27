import requests
from bs4 import BeautifulSoup
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

def digitleft(str) :
    while not str[-1].isdigit() :
        if len(str) == 1 :
            return 0
        str = str[:-1]
    return str

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
creds = None
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds_file = 'stoked-woods-400307-ca98d32d3085.json'  # Replace with your credentials JSON file
if os.path.exists(creds_file):
    creds = service_account.Credentials.from_service_account_file(creds_file, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
spreadsheet_id = '1ixexWYv2zIZn0Fc0RfIXhY7rGn5UsolaFWCKRA8isJc'

f=254
datasheet = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=f'boardgamerank!A{f}:B500').execute()['values']
list=[]


for i in datasheet :
    url = "https://boardgamegeek.com/boardgame/"+ '/'.join(i)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    print(str(soup))
    
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
        game_title = soup.find("meta", property="og:title")["content"]
        keyvote_index = datastat.find(keyvote)
        keyweight_index = datastat.find(keyweight)
        keyminplayer_index = datastat.find(keyminplayer)
        keymaxplayer_index = datastat.find(keymaxplayer)
        keyplaytime_index = datastat.find(keyplaytime)
        game_keyvote = digitleft(datastat[keyvote_index + len(keyvote):keyvote_index + len(keyvote) + 10])
        game_weight = digitleft(datastat[keyweight_index + len(keyweight):keyweight_index + len(keyweight) + 10])
        game_minplayer = digitleft(datastat[keyminplayer_index + len(keyminplayer):keyminplayer_index + len(keyminplayer) + 10])
        game_maxplayer = digitleft(datastat[keymaxplayer_index + len(keymaxplayer):keymaxplayer_index + len(keymaxplayer) + 10])
        game_playtime = digitleft(datastat[keyplaytime_index + len(keyplaytime):keyplaytime_index + len(keyplaytime) + 10])

        data = [[game_title,float(game_weight)*100,int(game_minplayer),int(game_maxplayer),int(game_playtime)]]

        request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=f'boardgame!A{f+1}:E{f+1}', valueInputOption="RAW", body={"values": data})
        response = request.execute()
        f+=1