import requests
from bs4 import BeautifulSoup
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

creds = None
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds_file = 'stoked-woods-400307-ca98d32d3085.json'
if os.path.exists(creds_file):
    creds = service_account.Credentials.from_service_account_file(creds_file, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
spreadsheet_id = '1ixexWYv2zIZn0Fc0RfIXhY7rGn5UsolaFWCKRA8isJc'
datasheet = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=f'user!A2:A401').execute()['values']
allgame = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=f'boardgame!A2:A501').execute()['values']

for i in range(len(datasheet)) :
    print(i)
    url = f"https://boardgamegeek.com/collection/user/{''.join(datasheet[i])}?rated=1&subtype=boardgame&ff=1"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    list = [[None]*500]
    gamename = [i.text for i in soup.find_all('a',class_='primary')]
    gamerate = [i.text for i in soup.find_all('div',class_ = 'ratingtext')]
    for j in range(len(gamename)) :
        try :
            a = allgame.index([gamename[j]])
            list[0][a] = int(gamerate[j])
        except ValueError :
            pass
    request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=f'user!B{i+2}:SH{i+2}', valueInputOption="RAW", body={"values": list}).execute()