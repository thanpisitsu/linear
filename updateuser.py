import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
import json

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
boardgamename = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=f'user!B1:SG1').execute()['values']
userdata = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=f'cov!A1:SG500').execute()['values']
with open('datacov.json', 'w') as file:
    json.dump(boardgamename+userdata, file, indent=4)



