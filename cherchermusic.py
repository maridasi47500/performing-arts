import requests
from bs4 import BeautifulSoup

class Cherchermusic():
    def __init__(self):
       self.someparams={"tbm":"isch"}
    def searchcompos(self):
       html = requests.get("http://www.mp3classicalmusic.net/composerslist.htm", params=self.someparams)
       soup = BeautifulSoup(html.text, 'html.parser')
       malist=soup.select("a[href*=Composers]")
       for x in malist:
           #print(x)
           if x:
             print(str(x).split(">")[1].split("<")[0])

Cherchermusic().searchcompos()


