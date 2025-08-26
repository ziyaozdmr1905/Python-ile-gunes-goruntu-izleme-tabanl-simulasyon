

"""

import requests

from bs4 import BeautifulSoup


url = "https://en.yellowpages.com.tr/search?q=Ankara"

response = requests.get(url)


html_icerigi = response.content

soup = BeautifulSoup(html_icerigi , "html.parser")



for i in soup.find_all("a"):
    print(i)
    print("*******************")
"""



"""

class User:
    def __int__(self, username , password , email):
        self.username = username
        self.password = password
        self.email = email



class UserRepository:


    def __int__(self):
        self.users = []  #boş bir liste oluşturduk
        self.isloggedin = False
        self.currentUser = {}

        self.loadUser()


    def loadUser(self):
        pass


    def register(self , user : User):
        self.users.append(user)
        #self.savetoFile()
        print("Kullanıcı oluşturuldu.")



    def Login(self):
        pass
    def savetoFile(self):
        pass



repository = UserRepository()

while True:
    print("Menü".center(50,'*'))
    secim = input('1 - Register\n2 - Login\n3 - Logout\n4 - identity\n5 - Exit\nSeçiminiz: ')
    if secim == '5':
        break
    else:
        if secim == '1':
            username = input("username: ")
            password = input("password: ")
            email = input("email: ")

            user = User(username = username , password = password , email = email)

            repository.register(user)

#            print(repository.users)

        elif secim == '2':
            pass #login

        elif secim == '3':
            pass #logput

        elif secim == '4':
            pass #display username
        else:
            print("Yanlış seçim")

"""






html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
</html>
"""



"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc , "html.parser")


res = soup.prettify()  # düzenleme işlemi yapar.
res = soup.title
res = soup.title.name    # title ismini yazdırır

res = soup.title.string    # title etiketi içinde ki string ifadeyi yazdırır

res = soup.find_all("a")

print(res)

"""

"""

import requests

from bs4 import BeautifulSoup




url = "https://www.imdb.com/chart/top/"


html = requests.get(url).content

soup = BeautifulSoup(html, 'html.parser')

list = soup.find("tbody" , {"class" : "lister-list"}).find_all("tr", limit=10)


for tr in list:
    title = tr.find("td", {"class" : "titleColumn"}).find("a").text
    year = tr.find("td", {"class" : "titleColumn"}).find("span").text.strip("()")
    rating = tr.find("td", {"class" : "ratingColumn"}).find("strong").text


    print(title , year , rating)

#print(list)

"""








