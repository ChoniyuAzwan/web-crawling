# get link

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

req = Request("https://warstek.com/category/sains-alam")
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")

links = []
for result in soup.findAll('a'):
    links.append(result.get('href'))

print(links)



# get web content & write to text file

import requests

f = open('datamentah.txt','w', encoding="utf-8")
for item in links:
    f = open('datamentah.txt','a', encoding="utf-8")
    if 'http' in str(item):
        page = requests.get(item)

        soup = BeautifulSoup(page.content, 'html.parser')
        for contentData in soup.find_all('p'):
            f.write(contentData.get_text())
            f.write('\n')
        f.write("\n\n")
    f.close()
    
    count=0
    file = open("datamentah.txt","r", encoding="utf-8")
    for word in file.read().split():
        count +=1
    file.close();
    
    if count > 100000:
        break
        
print('total word is', count)