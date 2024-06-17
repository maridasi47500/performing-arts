import requests
from bs4 import BeautifulSoup

class Chercherimage():
    def __init__(self,q):
       self.someparams={"q":q,"tbm":"isch"}
    def search(self):
       html = requests.get("https://www.google.com/search", params=self.someparams)
       soup = BeautifulSoup(html.text, 'html.parser')
       malist=soup.select("img")
       malist.pop(0)
       wow=[]
       ye={}
       for k in malist:
           ye=dict(k)
           ye["q"]=self.someparams["q"]
           wow.append(ye)
       return wow


