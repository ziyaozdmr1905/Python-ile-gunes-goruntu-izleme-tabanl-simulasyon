
"""
from selenium import webdriver

driver = webdriver.Chrome()


url = "https://www.sadikturan.com/"

driver.get(url)"""


"""
from selenium import webdriver

import time

driver = webdriver.Chrome()

url = "http://github.com"

driver.get(url)

time.sleep(2)

driver.maximize_window()



url ="http://github.com/sadikturan"

driver.get(url)


print(driver.title)

if "sadikturan" in driver.title:
    driver.save_screenshot("github.com-sadikturan.png")

time.sleep(2)
driver.back()


time.sleep(2)
driver.close()
"""




"""
from selenium import webdriver

from selenium.webdriver.common.by import By   #search araması için import tanımlaması yapıyotuz yoksa çalışmaz kodlar

from selenium.webdriver.common.keys import Keys    #enter için import tanımlaması yapıyoruz

import time


driver = webdriver.Chrome()

url = "https://github.com/"

driver.get(url)


searchInput = driver.find_element(By.NAME,"q")

time.sleep(5)


searchInput.send_keys("python")

searchInput.send_keys(Keys.ENTER)

time.sleep(5)

driver.close()
"""


"""
from githubparola import username , password

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys 

import time



class Github:
    def __init__(self, username , password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://github.com/login")    
        time.sleep(2)

        self.browser.find_element(By.XPATH , "//*[@id='login_field']").send_keys(username)
        self.browser.find_element(By.XPATH , "//*[@id='password']").send_keys(password)


        time.sleep(1)

        self.browser.find_element(By.XPATH, "//*[@id='login']/div[4]/form/div/input[13]").click()  #click kullanımı parantezi unutma


github = Github(username , password)
github.signIn()

"""



"""
#from instagram import username, password

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

import time


class Nstgram:
    def __int__(self , username , password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def singIn(self):
        self.browser.get("https://www.secure.instagram.com/accounts/login/")

        time.sleep(3)

        username = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
        password = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")

        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)
        time.sleep(2)


ins = Nstgram(username ="ziya.ozdmir" , password ="ziy@10783346.")
ins.singIn()

"""

"""

import requests

from bs4 import BeautifulSoup


url = "https://sisterslab.co/python-ile-web-scraping-temeller/"

response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi , "html.parser")


print(soup.find_all("td",{"id":"file"}))

"""


"""
from selenium import webdriver

from selenium.webdriver.common.by import By

import instagram

from selenium.webdriver.common.keys import Keys

import time



browser = webdriver.Chrome()

browser.get("https://twitter.com")


time.sleep(3)

browser.maximize_window()

giris_yap = browser.find_element(By.XPATH,"//*[@id='layers']/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a")

giris_yap.click()

time.sleep(3)

username = browser.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")

username.send_keys(instagram.username)

ileri_buton = browser.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")

ileri_buton.click()

time.sleep(2)


guvenlik = browser.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")

guvenlik.send_keys(instagram.guvenlik)

ileri = browser.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div")

ileri.click()

time.sleep(2)

try:
    password = browser.find_element(By.NAME,"password")

    password.send_keys(instagram.password)

    
#    giris = browser.find_element(By.CSS_SELECTOR, ".css-18t94o4 css-1dbjc4n r-1sw30gj r-sdzlij r-1phboty r-rs99b7 r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr")
    giris = browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div/div/span/span")

    giris.click()


except Exception:
    print("Bir hata oluştu..")

time.sleep(5)

browser.close()

"""



#import numpy as np

"""
# 1.soru - (10,15,30,45,60) dizisini oluşturunuz

res = np.array((10,15,30,45,60))

print(res)
"""
"""
# 2.soru - (5 - 15) arasında ki sayılarla bir dizi oluşturunuz

res = np.arange(5 , 15)

print(res)

"""

"""
# 3.soru - (50 - 100) arasında 5 er 5 er artan numpy dizisi oluşturun

res = np.arange(50 , 100, 5)

"""
"""
# 4.soru - 10 elemanlı sıfırdan oluşan bir dizi oluşturunuz
res = np.zeros(10)

"""

"""
# 5.soru - 10 elemenlı 1 den oluşan bir dizi oluşturunuz

res = np.ones(10)
"""
"""
# 6.soru - (0-100) arası eşit arlıklı 5 sayı üretin 
res = np.linspace(0,100,5)
"""

"""
# 7.soru - (10-30) arasında rastgele 5 tane tam sayı üretin
res = np.random.randint(10,30)
"""
"""
# 8.soru - (-1, 1) arasında 10 adet sayı üretin 
res = np.random.uniform(-1,1, 10)
"""

"""
# 9.soru - (3 x 5) boyutlarında (10 - 50) arasında  rastgele bir matris oluşturun
num1 = np.random.randint(10,50,15).reshape(3,5)
"""


"""
# 10.soru - üretinlen matrisin satır ve sütun toplamını hesaplayınız
num1 = np.random.randint(10,50,15).reshape(3,5)
res = num1.sum(axis=1)
res2=num1.sum(axis=0)
"""
"""
# 11.soru - üretilen matrisin en büyük ,en küçük ve ortalaması nedir
num1 = np.random.randint(10,50,15).reshape(3,5)
res = num1.max()
res2 = num1.min()
res3 = num1.mean()
"""
"""
# 12.soru - üretilen matrisin en büyük değerinin index i kaçtır
num1 = np.random.randint(10,50,15).reshape(3,5)
res2 = num1.argmax()
"""


"""
# 13.soru - (10 - 20) arasında sayıları içeren dizinin ilk 3 elemanını seçiniz
num1 = np.arange(10,20)
res2 = num1[:3]

"""


"""
# 14.soru - üretilen dizinin elemenalrını tersten yadırın

num1 = np.arange(10,20)
res2 = num1[::-1]
"""




"""
# 15.soru - üretilen matrisin ilk satırını seçiniz
num1 = np.arange(0,15).reshape(3,5)
res2 = num1[0,:]
"""

"""
# 16.soru - üretilen matrisin 2.satır 3.sütunda ki elemanı hangisdir
num1 = np.arange(0,15).reshape(3,5)
res2 = num1[1,2]
"""
"""
# 17.soru - üretrilen matrisin tüm satırlarında ki ilk elemanı seçiniz 
num1 = np.arange(0,15).reshape(3,5)
res2 = num1[:,:1]
"""
"""
# 18.soru - üretilen matrisin her bir elemanının karesini alınız
num1 = np.arange(0,15).reshape(3,5)

for i in num1:
    print(i**2)
"""


"""
# 19.soru - üretilen matris elemanlarının hangisi pozitif çift sayıdır
#           aralığı (-50, +50) arasında yapınız
num1 = np.random.randint(-50, 50,15)
num2 = num1.reshape(3,5)

#print(num1)
print(num2)

for i in num1:
    
    if i % 2 == 0:
        print(i)
    else:
        print("False")    


"""


#print(res)
#print(num1)
#print(res)
#print(res2)
# print(res3)


