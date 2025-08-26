
"""
import requests
import soupsieve

from bs4 import BeautifulSoup


url = "https://www.imdb.com/chart/top/"

response = requests.get(url)

html_icerigi = response.content

soap = BeautifulSoup(html_icerigi , "html.parser")    #şurada ki noktayı unuttuğum için "html (.) parser kod çalışmadı

a = float(input("Rating i giriniz: "))


basliklar = soap.find_all("td" , {"class":"titleColumn"})

ratingler = soap.find_all("td" , {"class":"ratingColumn imdbRating"})


for baslik,rating in zip(basliklar , ratingler):

    baslik = baslik.text
    rating = rating.text

    baslik = baslik.strip()
    baslik = baslik.replace("\n" , "")

    rating = rating.strip()
    rating = rating.replace("\n" , "")

    if (float(rating) > a):
        print(f"Film ismi: {baslik}  Filmin ratingi: {rating}")

    #print(i.text)   film isimlerinin almak için i.text dememiz gerekir

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


    def register(self , user = User):
        self.users.append(user)
        # self.savetoFile()
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

            user = User(username = username , password = password , email = email )

            repository.register(user)

            print(repository.users)

        elif secim == '2':
            pass #login

        elif secim == '3':
            pass #logput

        elif secim == '4':
            pass #display username
        else:
            print("Yanlış seçim")








