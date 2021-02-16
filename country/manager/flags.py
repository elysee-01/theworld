url = 'https://www.countryflags.com/fr/galerie-des-fichiers-vectoriels/'
import requests
from bs4 import BeautifulSoup


headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
response = requests.get(url, headers=headers)
html_soup = BeautifulSoup(response.text, 'html.parser')

if response.status_code == 200:
    table = html_soup.find('div', attrs={'class': 'tiles'})
    items = table.findAll('div', attrs = {'class': 'thumb'})

    for item in items:
        img = item.find('img')
        file_url = img.get('src')

        name = file_url.split('/')[-2]

        req = requests.get(file_url, stream=True)

        with open(f"{name}.png", "wb") as fp:
            for partie in req.iter_content():
                fp.write(partie)
