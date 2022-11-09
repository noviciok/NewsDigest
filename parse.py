import requests 
from bs4 import BeautifulSoup

def parse_stiri():
    print("executing parse")
    URL = "https://stiri.md/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content,"html.parser")
    mainlist = soup.find(id="mainlist")
    stiri = mainlist.find_all("article")
    list = []
    for article in stiri:
      titlu = article.find("h3")
      brief = article.find("p")
      if not titlu is None and not brief is None: list.append({'titlu':titlu.text, 'brief':brief.text})
        
    return list
    
#print(parse_stiri())