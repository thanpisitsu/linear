import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
url = "https://boardgamegeek.com/collection/user/adi_venturer?rated=1&subtype=boardgame&ff=1"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

list = []
gamename = soup.find_all('a',class_='primary')
gamerate = soup.find_all('div',class_ = 'ratingtext')
for i in range(len(gamename)) :
    list.append({'name':gamename[i].text,'rate':gamerate[i].text})

df = pd.DataFrame(list)
