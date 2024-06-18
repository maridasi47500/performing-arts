import requests
import urllib.request
from song import Song
from bs4 import BeautifulSoup
from chercherimage import Chercherimage

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
             xx=(str(x).split(">")[1].split("<")[0])
             if len(xx) > 0 and xx != ")":
               print(xx)
    def searchmusic(self):
       html = requests.get("https://archive.org/details/100ClassicalMusicMasterpieces", params=self.someparams)
       soup = BeautifulSoup(html.text, 'html.parser')
       malist=soup.select("#quickdown5 .download-pill")
       for x in malist:
           print(x)
           if x != "None" and x is not None:
               somesoup = str(x).split(">")[1].split("<")[0]
               xx=("https://ia802905.us.archive.org/17/items"+x["href"].replace("/download",""))
               print(xx)
               opener=urllib.request.build_opener()
               opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582')]
               urllib.request.install_opener(opener)
               filename=x["href"].replace("/download/100ClassicalMusicMasterpieces","")
               urllib.request.urlretrieve(xx, f'./uploads/'+filename)
               pic=Chercherimage(somesoup).dlpic()
               print({"artist":"artist","title":somesoup, "filename":filename,"image":pic["nom"]})
               Song().create({"artist":"artist","title":somesoup, "filename":filename,"image":pic["nom"]})
           else:
               print("uknhk")

Cherchermusic().searchmusic()


