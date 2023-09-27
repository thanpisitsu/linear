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
creds_file = 'stoked-woods-400307-ca98d32d3085.json'  # Replace with your credentials JSON file
if os.path.exists(creds_file):
    creds = service_account.Credentials.from_service_account_file(creds_file, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
spreadsheet_id = '1ixexWYv2zIZn0Fc0RfIXhY7rGn5UsolaFWCKRA8isJc'

for i in range(1) :
    data = []
    url = f"https://boardgamegeek.com/browse/boardgame/page/{i+1}?sort=rank&sortdir=asc"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    id = soup.find_all('a',class_='primary')
    for anchor in id:
        href = anchor.get("href")
        href = href.split('/')
        data.append(href[2:])
    print(data)
    range_name = f'boardgamerank!A{i*100+1}:B{(i+1)*100}'
    request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_name, valueInputOption="RAW", body={"values": data}).execute()




