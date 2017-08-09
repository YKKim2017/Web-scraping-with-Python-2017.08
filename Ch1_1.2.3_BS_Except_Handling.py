from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
    return None
try:
    badContent = bs0bj
else:
    bs0bj = BeautifulSoup(html.read(), "html.parser")
    print(bs0bj.h1)
