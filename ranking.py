import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
f=1
for i in range(5) :
    url = f"https://boardgamegeek.com/browse/boardgame/page/{i+1}?sort=rank&sortdir=asc"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    id = soup.find_all('a',class_='primary')
    for anchor in id:
        href = anchor.get("href")
        print(f,href)
        f+=1




