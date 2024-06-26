import requests
from bs4 import BeautifulSoup as b


URL = 'https://minecraft.fandom.com/wiki/'
r = requests.get('https://www.minecraftcrafting.info')
soup = b(r.content, 'html.parser')
images = soup.find_all('img', src=True)


def item_info_text(item):
    url = URL + item.replace(' ', '_')
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    content = soup.find('div', class_='mw-parser-output')
    try:
        paragraphs = content.find_all('p')
    except AttributeError:
        return False
    text = [c.text for c in paragraphs]
    return text[1:4]


def item_info_image(item):
    for img in images:
        p = img['src']
        if p.find(item) != -1:
            return img['src']