"""import datetime


an = datetime.datetime.now()

 print(datetime.datetime.strftime(an, '%d %B'))"""

"""
y = (input('tarih ver (2018/2/5): ').split('/'))
x = datetime.datetime(int(y[0]) , int(y[1]) , int(y[2]))
a = (x.strftime(('%d %B')))"""

"""for i in range(15 , 30):
    if i == int(y[2]):
        print("oldu")

"""
"""for i, r in (range(20,0,-1)), range(0, 15):
    print(i , r)    
"""




""" Oğlak =  22 Aralık - 19 Ocak """





"""
gun = int(input("Doğum Gününüz: "))
ay = int(input("Doğduğunuz Ay: "))


burclar ={
    "Kova":     (20, 1, 18, 2),
    "Balık":    (19, 2, 20, 3),
    "Koç":      (21, 3, 19, 4),
    "Boğa":     (20, 4, 20, 5),
    "İkizler":  (21, 5, 20, 6),
    "Yengeç":   (21, 6, 22, 7),
    "Aslan":    (23, 7, 22, 8),
    "Başak":    (23, 8, 22, 9),
    "Terazi":   (23, 9, 22, 10),
    "Akrep":    (23, 10, 21, 11),
    "Yay":      (22, 11, 21, 12),
    "Oğlak":    (22, 12, 19, 1)


}

for burc, (baslangıc_gun , baslangıc_ay , bitis_gun, bitis_ay) in burclar.items():
    if (gun >= baslangıc_gun and ay == baslangıc_ay) or (gun <= bitis_gun and ay == bitis_ay):
        print("Burcunuz: ", burc)
        break
"""


""" genel tekrar"""

"""
with open("li.txt","r",encoding= "utf-8") as file:
    sel = file.read()   
    res = sel.split()
    kes = list()
for i in res:
    i = i.strip("\n")
    i = i.strip(" ")    
    i = i.strip(",")
    i = i.strip(".")
    kes.append(i)
#print(kes)

kelime_sozcuk = dict()

for kelime in kes:

    if (kelime in kelime_sozcuk):
    
        kelime_sozcuk[kelime] += 1
        
    else:
        kelime_sozcuk[kelime] = 1  
    #print(kelime_sozcuk[kelime][0])          
for kelim, sayi in kelime_sozcuk.items():
   
    print("{} kelimesi {} defa geçiyor..".format(kelim, sayi))

    print("----------------------------")            
"""
#sdf

"""
ogrenciler  = []

while True:

    num = int(input("Okul no: "))
    isim = input("isim: ")
    soyisim = input("Soyisim: ")
    tel = int(input("Telefon no: "))
    ogrenciler.append([soyisim ,isim, num , tel])
    ogrenciler.sort()
#    print(ogrenciler)
    for i,j,e,t in ogrenciler:

        print(f"{e} numaralı öğrencinin adı: {j} {i} ve telefon numarası: {t}")
"""

# iç içe fonksiyonlar
"""
def ekstra(fonk):

    def wrapper(sayılar):
        ciftler_toplamı = 0
        cift_sayilar = 0
        tekler_toplamı = 0
        tek_sayilar = 0
        
        for sayı in sayılar:
            if (sayı % 2 == 0):
                ciftler_toplamı += sayı
                cift_sayilar += 1

            else:
                tekler_toplamı += sayı
                tek_sayilar += 1
        print("Teklerin ortalaması:",tekler_toplamı / tek_sayilar)        
        print("Çiftlerin ortalaması:",ciftler_toplamı / cift_sayilar)

        fonk(sayılar)
    return wrapper

@ekstra    
def ortalamabul(sayılar):

    toplam = 0

    for sayı in sayılar:
        toplam += sayı
    print("Genel toplama:",toplam/len(sayılar))

ortalamabul([1,2,3,4,34,60,63,32,100,105])        
"""


"""
def ozellik(fonk):

    def reppar(sayılar):
        kupler_toplamı = 0
        kareler_carpimi = 1
        
        for  sayı in sayılar:
            kupler_toplamı += (sayı*sayı*sayı)
            kareler_carpimi *= (sayı* sayı)
        print("Küplerin toplamı:",kupler_toplamı)
        print("Kareler çarpımı:",kareler_carpimi)
       
        fonk(sayılar)
    return reppar


@ozellik
def listeler(sayılar):
    genel = 0
    
    for i in sayılar:
        genel += i
    print("Sayıların genel toplamı:",genel)    

listeler([2,3])
"""


"""
def ekstra(fonk):

    def ekstra_ozellik():
        print("Mükemmel sayılar...")
        for sayı in range(1,1001):
            toplam = 0
            i = 1
            while (i < sayı):
                if (sayı % i == 0):
                    toplam += i
                i += 1
            if (toplam == sayı):
                print(sayı)
        fonk()                
    return ekstra_ozellik

@ekstra
def asal_sayılar():
    print("Asal sayılar...")
    for sayı in range(2,1001):
        i = 2
        say = 0
        while (i < sayı):
            if (sayı % i == 0):
                say += 1
            i += 1
        if (say == 0):
            print(sayı)
asal_sayılar()                    

"""


"""class Mynumbers():
    def __init__(self, start , stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration

list = Mynumbers(10 , 20)
myiter = iter(list)


print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

"""

"""
class Kuvvet():
    def __init__(self, max = 0):
        self.max = max
        self.kuvvet = 0

    def __iter__(self):
        return self
    def __next__(self):
        if (self.kuvvet <= self.max):
            sonuc = 3 ** self.kuvvet
            self.kuvvet += 1
            return sonuc
        else:
            raise StopIteration

kuvvet = Kuvvet(6)

for i in kuvvet:
    print(i)
"""

"""
def fibonacci():
    a = 1 
    b = 1
    yield a
    yield b

    while 1:
        a,b = b, a+b
        yield b

for i in fibonacci():
    if ( i > 100000):
        break
    print(i)
"""
"""
class Vektor:
    def __init__(self , x , y):
        self.x = x
        self.y = y
        print("Bir vektör nesnesi oluşturuldu..")
        print(x , y)


a = Vektor(6,8)

print(a.y)
"""

"""
class Vektor:
    def __init__(self, x , y):
        self.x = x
        self.y = y
    def boyu(self):
        boy = (self.x**2 + self.y**2)**0.5
        return boy
    def __repr__(self):
        return f"{self.x}i + {self.y}j"
    def __add__(self, oteki):
        return Vektor(self.x  + oteki.x , self.y + oteki.y)


a = Vektor(6,8)
b = Vektor(3,4)
c = a + b
print(a)
print(b)
print(c)
"""

"""

class Kareler:
    def __init__(self,max = 0):
        self.max = max
        self.kuvvet = 0
    def __iter__(self):
        return  self
    def __next__(self):
        if (self.kuvvet <= self.max):
            
            sonuc = self.kuvvet ** 2
            
            self.kuvvet += 1
            return sonuc
                
        else:
            raise StopIteration

kareler = Kareler(6)

iteration = iter(kareler)

print(next(iteration))

print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))
"""


"""
class Vektor:
    '''Bu bir vektör nesnesidir...'''

    def __init__(self,x,y):
        self.x = x
        self.y = y
    def boyu(self):
        boy = (self.x**2 + self.y**2)**0.5 
        return boy
    def __repr__(self):
        return f"{self.x}i + {self.y}j"
    def __add__(self,oteki):
        return (self.x + oteki.x , self.y + oteki.y)
    def __gt__(self,oteki):
        if self.boyu() > oteki.boyu(): return True               


A = Vektor(6,8)
B = Vektor(3,4)
C = A + B
print(A)
print(B)
print(A>B)
"""


"""
def asal_mi(sayi):
    i = 2

    while i < sayi:
        if (sayi % i == 0):
            return False
        i += 1
    return True
def asal_generator():
    i = 2
    while True:
        if (asal_mi(i)):
            yield i
        i += 1
for sayı in asal_generator():
    if (sayı > 1000):
        break
    print(sayı)                        

"""


"""
sayı = int(input("Sayi: "))
asal_mi = True
if (sayı == 1):
    asal_mi = False
for i in range(2,sayı):
    if (sayı % i ==0):
        asal_mi = False
        break
if asal_mi:
    print("Sayı asaldır..")
else:
    print("Sayı asal değildir..")        
"""
"""
sayi1 = int(input("Sayi1: "))

sayi2 = int(input("Sayi2: "))

def asalsayılaribul(sayi1, sayi2):
    for i in range(sayi1 , sayi2+1):
        if i > 1:
            for t in range(2, i):
                if (i % t == 0):
                    break
            else:
                print(i)
asalsayılaribul(sayi1 , sayi2)"""

"""
sayi = int(input("Sayı: "))

def asalbul(sayi):
    
    for say in range(1,sayi+1):
        
        if say > 1:
            
            for i in range(2, say):
                
                if (say % i == 0):
                    print(say * "*")
                    break
            else:
                print(say)    

asalbul(sayi)
"""

"""
def asalbul(sayi):
    for say in range(1 , sayi+1):
        if say > 1:
            for i in range(2,say):
                if (say % i == 0):
                    #print(say * "*")
                    break
            else:
                print(say)        

asalbul(1000)
"""


"""
def asalmi(sayi):
    i = 2
    while i < sayi:
        if (sayi % i == 0):
            return False
        i += 1
    return True    

def asal_generator():
    i = 2
    while True:
        if (asalmi(i)):
            yield i
        i += 1
for sayı in asal_generator():
    if (sayı > 1000):
        break
    print(sayı)    

"""


"""
import requests

res = requests.get("http://www.google.com")

print(res)
print(type(res))
"""


""""""





#import sys

#print(dir(sys))

"""
stdin = Bu standart dosya, işlemimizin kullanıcıdan input almamızı sağlar.

stdout = Bu standart dosya işlemimizin çıktı vermesini sağlar

stderr = Bu standart dosya işlemimizin hat mesajlarını çıktı olarak vermek için kullanır.

"""


"""#sys.exit()  bu fonksiyonu bitir demektir"""

"""
sys.stderr.write("Bu bir hata mesajıdır\n")

sys.stderr.flush()

sys.stdout.write("Bu bir normal yazıdır.\n")
"""


"""
import sys


def  kokbulma(a,b,c):
    delta = b**2 - 4 * a * c 

    if (delta < 0):
        print("Reel kök yok")

    else:
        x1 = (- b - delta ** 0.5) / (2*a)

        x2 = (- b + delta ** 0.5) / (2*a)

        return(x1 , x2)

if len(sys.argv) == 4:
    print("Kök bulma " , kokbulma (int(sys.argv[1])),(int(sys.argv[2])),(int(sys.argv[1])))

else:
    sys.stderr.write("Lütfen doğru değerler giriniz")
    sys.stderr.flush()
"""

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
import requests

from bs4 import BeautifulSoup


url = "https://en.yellowpages.com.tr/search?q=Ankara"

response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi , "html.parser")


print(soup)
"""

"""
import sys

def kokbulma(a ,b , c):
    delta = b ** 2 - 4 * a * c

    if (delta < 0):
        print("Reel Kök yok")
    else:
        x1 = (-b  - delta ** 0.5) / (2 * a)
        x2 = (-b + delta ** 0.5) / (2 * a)
        return (x1, x2)


if len(sys.argv) == 4:
    print("kök bulma" , kokbulma(int(sys.argv[1]), int(sys.argv[2]) ,int(sys.argv[3])))
else:
    sys.stderr.write("lütfen doğru değerler giriniz")
    sys.stderr.flush()
"""







































