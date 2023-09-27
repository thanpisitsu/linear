import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load credentials from JSON file
creds = None
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds_file = 'stoked-woods-400307-ca98d32d3085.json'  # Replace with your credentials JSON file
if os.path.exists(creds_file):
    creds = service_account.Credentials.from_service_account_file(creds_file, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
spreadsheet_id = '1ixexWYv2zIZn0Fc0RfIXhY7rGn5UsolaFWCKRA8isJc'
data = [
    ["Cell A1", "Cell B1", "Cell C1"],
    ["Cell A2", "Cell B2", "Cell C2"]
]
range_name = 'Sheet1!A1:C2'

request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_name, valueInputOption="RAW", body={"values": data})
response = request.execute()

print("Data pushed to Google Sheets.")
