from urllib.request import urlopen
from bs4 import BeautifulSoup

titleLinks = []
titleSpan = []
page=1
max_page=3

# html = urlopen('https://habr.com/ru/all/page'+ str(page)+'/')

for i in range(page, max_page):
    html = urlopen('https://habr.com/ru/all/page'+str(page)+'/')
    bs = BeautifulSoup(html, "html.parser")
    for link in bs.findAll('a', {'class': 'tm-article-snippet__title-link'}, href=True):
        titleLinks.append('https://habr.com' + link['href'])
        titleSpan.append(link.get_text())
        print(link.get_text() + ' link = ' + 'https://habr.com' + link['href']);



# for item in Mass:
    # if item.a['href'] == True:
    #     titleLinks.append(item.a['href'])
    # else:
    #     titleLinks.append("no")
    # titleLinks.append('https://habr.com' + item.a['href'])
    # titleH2.append(item.get_text())
    # print(item.get_text())
# print(titleLinks)
# print(titleH2)

    # try:
    #     if "Windows" in new_str or "OS" in new_str or "MacOS"in new_str or "Linux" in new_str or "ОС" in new_str :    
    #         print(new_str)
    # except:
    #     pass