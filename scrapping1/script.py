from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

titleLinks = []
titleSpan = []
keys = [ 
    'Windows',
    'OS',
    'MacOS',
    'Linux',
    'ОС',
    'Операционная'
]
Mass = []
for i in range(1,2):
    html = urlopen('https://habr.com/ru/all/page'+str(i)+'/')
    bs = BeautifulSoup(html, "html.parser")
    authors = bs.find_all('a', { 'class' : 'tm-user-info__username'})
    # theme_keys = bs.find_all()
    for link in bs.findAll('a', {'class': 'tm-article-snippet__title-link'}, href=True):
        try:
            if keys[0] in link.get_text() or keys[1] in link.get_text() or keys[2] in link.get_text() or keys[3] in link.get_text() or keys[4] in link.get_text() :
                Mass.append({
                    'author' : authors[i].get_text(),
                    'title': link.get_text(),
                    'link' : 'https://habr.com'+link['href']
                })
        except:
            pass
with open("example.json", "w", encoding='utf-8') as f: #, separators=(',', ': '), 
    json.dump(json.dumps(Mass, indent=2, ensure_ascii=False), f, ensure_ascii=False)
