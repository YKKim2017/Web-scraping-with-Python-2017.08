from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://pythonscraping.com/pages/warandpeace.html")
bs0bj = BeautifulSoup(html, "html.parser")
nameList = bs0bj.findAll("span", {"class":"green"}) #bs0bj.findAll(class_="green") #bs0bj.findAll("", class_="green")
for name in nameList:
    print(name.get_text())

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs0bj = BeautifulSoup(html, "html.parser")

for sibling in bs0bj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)
    
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs0bj = BeautifulSoup(html, "html.parser")
images = bs0bj.findAll("img", {"src":re.complie("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
    print(image["src"])
