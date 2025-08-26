
"""
def not_hesapla(satır):
    
    liste = satır.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    son_not =  not1*(3/10) + not2*(3/10) + not3*(4/10)
    
    
    if (son_not >= 90):
        harf = "AA"
    elif (son_not >= 80):
        harf = "BA"    
    elif (son_not >= 70):
        harf = "BB"    
    elif (son_not >= 60):
        harf = "CB"    
    elif (son_not >= 50):
        harf = "CC"    
    elif (son_not >= 40):
        harf = "DC"    
    else:
        harf = "FF"    

    return isim + "---------------------->" + harf + "\n"


with open("dosya.txt","r",encoding="utf-8") as file:

    eklenecekler = []
    for i in file:

        eklenecekler.append(not_hesapla(i))

    with open("notlar.txt" , "w", encoding= "utf-8") as file2:
        for i in eklenecekler:
            file2.write(i)
"""





"""
with open("hayvan.txt" , "a", encoding= "utf-8") as file:
    file.write("Karınca\n")
"""




"""with open("hayvan.txt" , "r", encoding= "utf-8") as file:
    print(file.read())
"""

"""
def dortbacak():
    with open("hayvan.txt" , "r", encoding= "utf-8") as file:
        liste = []
        for i in file:
            liste.append(file.read(i))

        print(liste)

dortbacak()

"""


"""with open("kalanlar.txt" , "r" , encoding= "utf-8") as f:
    list = f.readlines()
    print(list.split())
"""    # for i in liste:
    #     print(i.split("---------------------->")[1],end="")
    #     # if i.split("---------------------->") == "BB":
        #     print("Kaldı")
    # with open("geçenler.txt","w" , encoding= "utf-8") as file:
    #     file.write()


"""
def ort():

    with open("sınav_notları.txt","r",encoding="utf-8") as f:
        liste = []

        for satir in f:
            liste.append(hesapla(satir))
        

def hesapla(satir):
    #satir = satir[:]
    liste = satir.split(":")

    ogrenci_adi = liste[0]
    notlari = liste[1].split(",")

    not1 = int(notlari[0])
    not2 = int(notlari[1])
    not3 = int(notlari[2])
    
    ortalama = (not1+not2+not3)/3
    #print(ortalama)
    
    son_not = ortalama

    if ortalama >= 40:    
        if (son_not >= 90):
            harf = "AA"
        elif (son_not >= 80):
            harf = "BA"    
        elif (son_not >= 70):
            harf = "BB"    
        elif (son_not >= 60):
            harf = "CB"    
        elif (son_not >= 50):
            harf = "CC"    
        elif (son_not >= 40):
            harf = "DC"    
        else:
             harf = "FF"    
        
        liste = []
        liste.append(f"{ogrenci_adi}----------------------> {harf}\n")
        print(liste)
        with open("Gecenler.txt" , "a" , encoding="utf-8") as file2:
            file2.writelines(liste)
            # for i in liste:
            #     file2.write(i)  
               
    else:
        if (son_not >= 90):
            harf = "AA"
        elif (son_not >= 80):
            harf = "BA"   
        else:
             harf = "FF"     
        
        with open("Gecemeyenler.txt" , "a" , encoding="utf-8") as file2:
            liste = []
            liste.append(ogrenci_adi + "---------------------->" + harf + "\n")
            # for i in liste:
            #     file2.write(i)
            file2.writelines(liste)
    

ort()
"""


"""
with open("futbolcular.txt","r",encoding="utf-8") as file:
    gs = list()
    fb = list()
    bjk = list()

    for satır in file:
        satır = satır[:-1]
        satır_elemanları = satır.split(",")

        if (satır_elemanları[1] == "Fenerbahçe"):
            fb.append(satır + "\n")
        elif (satır_elemanları[1] == "Galatasaray"):
            gs.append(satır + "\n")
            
        else:
            bjk.append(satır + "\n") 
    with open("gs.txt" , "w" , encoding="utf-8") as file1:
        for i in gs:
            file1.write(i)
            
    with open("fb.txt", "w" , encoding="utf-8") as file2:
        for i in fb:
            file2.write(i)
    with open("bjk.txt","w", encoding="utf-8") as file3:
        for i in bjk:
            file3.write(i)                               

"""


"""
liste = [(3,4),(10,3),(5,6),(1,9)]

def alan_hesapla(demet):
    return demet[0] * demet[1]

print(list(map(alan_hesapla, liste)))

"""


"""
liste = [(3,4,5),(6,8,10),(3,10,7)]

def ucgen(kenar):
    if (abs(kenar[0] + kenar[1]) > kenar[2] and (kenar[0] + kenar[2]) > kenar[1] and (kenar[1] + kenar[2]) > kenar[0]):
        return True
    else:
        return False

print(list(filter(ucgen,liste)))

"""

"""
from functools import reduce

liste = [1,2,3,4,5,6,7,8,9,10]

filtre = list(filter(lambda x : x % 2 == 0, liste))

print(reduce(lambda x,y : x + y , filtre))
"""


"""
isimler = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

soyisimler = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

for i,j in zip(isimler , soyisimler):
    print(i,j)
"""



# dosya işlemleri


"""
def sel():
    with open("hayvanlar.txt","r" , encoding= "utf-8") as file:
        ikibacak = list()
        dörtbacak = list()
        altıbacak = list()
        
        for satır in file:

            satır = satır[:-1]
            res = satır.split(":")

            ikibck = int(res[1])

            dörtbck = int(res[1])

            altıbck = int(res[1])
        
            if ikibck == 2:
                ikibacak.append(satır + "\n")
        #print(ikibacak)    
            elif (dörtbck == 4):
                dörtbacak.append(satır + "\n")
            elif (altıbck == 6):
                altıbacak.append(satır + "\n")        
        
        
        
        with open("ikibacak.txt" , "w" , encoding="utf-8") as file1:
            for i in ikibacak:
                file1.write(i)
        with open("dörtbacak.txt", "w" , encoding="utf-8") as file2:
             for i in dörtbacak:
                file2.write(i)
        with open("altıbacak.txt","w", encoding="utf-8") as file3:
             for i in altıbacak:
                file3.write(i)                         
    

sel() 

"""
#gömülü fonksiyonlar

# def squ(num): return num ** 2

# res = squ(2)
# print(res)

"""
liste = ((1,2),(4,5),(7,9),(6,3))

def islem(deme):
    return deme[0] * deme[1]


print(list(map(islem, liste)))

"""

"""
liste = ((2,5,9), (4,7,2) , (2,3,7))

def islem(deme):
    return deme[0] + deme[1] + deme[2]

print(list(map(islem , liste)))
"""


# map fonksiyonu ne işe yarar => dizi içinde ki her bir elemana ulaşmamızı sağlar
"""
liste = [1,5,7]
def sel(num): return num**2

#print(list(map(sel,(4,8))))
for i in list(map(sel,liste)):
    print(i)
"""
# lambda
"""
num = [1,3,5,9]
res = list(map(lambda x : x ** 2 , num))
print(res)
"""


"""
with open("hayvanlar.txt" , "w", encoding= "utf-8") as file:
    er = file.write("Tavşan,4\n")
print(er)

"""
#map foksiyonu
"""
l = [1, 2, 3, 4, 5]
l_karaasi = []
for i in l:
    l_karaasi.append(i**2)

print(l)
print(l_karaasi)
"""
#aynı işlemi daha kısa yoldan yaptık
"""
l = [1, 2, 3, 4, 5]
l_karaasi = list(map(lambda x: x**2, l))

print(l)
print(l_karaasi)
"""

"""
def capma(x):
    return (x*x)

def toplam(x):
    return (x+x)

fonk = [capma , toplam]

for i in range(5):
    print(list(map(lambda x : x(i), fonk)))
"""

#filter fonksiyonu
"""
l = list(range(-5 , 5))

print(l)

sıfıdanbuyuk = list(filter(lambda x: x > 0 , l))

print(sıfıdanbuyuk)
"""
#reduce fonksiyonu


"""
sonuc = 1
liste = [1,2,3,4,5]
for i in liste:
    sonuc *= i
print(sonuc)    
"""

"""
from functools import reduce
liste = [1,2,3,4,5]

sonuc = reduce((lambda x ,y: x*y), liste)
print(sonuc)
"""




# python iç içe fonksiyonlar
"""
def outer(num1):
    print("outer")

    def inner_increment(num1):
        print("inner")
        return num1 + 1
    #inner_increment(num1)    
    num2 = inner_increment(num1)
    print(num1 , num2)


(outer(10))
"""

"""
def factorial(number):
    if not isinstance(number , int):
        raise TypeError("Number must be an integer")
    if not number >= 0:
        raise ValueError("Number must be zero or positive")

    def inner(number):
        if number <=1:
            return 1

        return number * inner(number - 1)

    return inner(number)

try: 
    print(factorial("4"))                
except Exception as ex:
    print(ex)
"""

"""
def yetki_sorgula(page):
    def inner(role):
        if role == "admin":
            return "{0} rolü {1} sayfasına ulaşabilir.".format(role , page)

        else:
            return "{0} rolü {1} sayfasına ulaşamaz.".format(role , page)
    return inner



user1 = yetki_sorgula("product edit")
print(user1("admin"))
print(user1("user"))
"""


"""
def islem(islem_adi):
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam

    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim

    if islem_adi == "toplama":
        return toplama
    else:
        return carpma    



toplam = islem("toplama")
print(toplam(1,2,5,7))
carpma = islem("carpma")
print(carpma(2,6,8,9))
"""


"""
def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b        

def islem_sec(f1,f2,f3,f4,islem):
    if islem == "toplama":
        print(f1(2,3))
    elif islem == "cikarma":
        print(f2(8,7))
    elif islem == "carpma":
        print(f3(4,6))
    elif islem == "bolme":
        print(f4(9,3))
    else:
        print("Geçersiz işlem...")            



islem_sec(toplama,cikarma,carpma,bolme, "toplama")
islem_sec(toplama,cikarma,carpma,bolme, "cikarma")
islem_sec(toplama,cikarma,carpma,bolme, "carpma")
islem_sec(toplama,cikarma,carpma,bolme, "bolme")

"""

# python da decorator fonksiyonlar
"""
def my_decorator(func):
    def wrapper():
        print("fonksiyondan önceki işlemler")
        func()
        print("fonksiyondan sonraki işlemler")
    return wrapper

def sayHello():
    print("hello")

sayHello = my_decorator(sayHello)
sayHello()
"""

#yada şöyle yapabiliriz

"""
def my_decorator(func):
    def wrapper():
        print("fonksiyondan önceki işlemler")
        func()
        print("fonksiyondan sonraki işlemler")
    return wrapper

@my_decorator   # dersek yukarki ile aynı sonuca ulaşırız kısa yol budur
def sayHello():
    print("hello")

sayHello()
"""

"""
import time
import math

def calculete_time(func):
    def inner(*args , **kwargs):
        start = time.time()
        time.sleep(1)
        func(*args , **kwargs)
        finish = time.time()

        print("fonksiyon" + func.__name__ + str(finish - start) + "saniye sonrası")
    return inner

@calculete_time
def usalma(a,b):
    print(math.pow(a,b))

@calculete_time
def faktorial(num):
    print(math.factorial(num))

usalma(3,4)
faktorial(5)

"""

# PYTHON ITERATORS

"""
liste = [1,2,3,4,5]

itarator = iter(liste)

print(next(itarator))

"""

"""
liste = [1,2,3,4,5]

itarator = iter(liste)

while True:
    try:
        element = next(itarator)
        print(element)
    except StopIteration:
        break    
"""
"""
class MyNambers:
    def __init__(self, start, stop):
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

list = MyNambers(10,20)
myiter = iter(list)

print(next(myiter))
"""


# PYTHON GENERATORS

"""
def cube():
    result = []

    for i in range(5):
        result.append(i**3)
    return result    

#print(cube())
generator = cube()
iterator = iter(generator)

print(next(iterator))
"""

"""
liste = [i ** 3 for i in range(5)]

for i in liste:
    print(i)
"""




"""
with open("dosya.txt", "r" , encoding= "utf-8") as file:
    file.write("d")
"""





"""
class Dosya():

    def __init__(self):
        with open("dosya.txt" , "r" , encoding= "utf-8") as file:
            dosya_icerigi = file.read()

            kelimeler = dosya_icerigi.split()

            self.sade_kelimeler = list()

            for i in kelimeler:
                i = i.strip("\n")

                i = i.strip(" ")

                i = i.strip(".")

                i = i.strip(",")
                self.sade_kelimeler.append(i)
    
    def tum_kelimeler(self):

        kelimer_kumesi = set()

        for i in self.sade_kelimeler:
            kelimer_kumesi.add(i)

            print("Tüm kelimeler....")

        for i in kelimer_kumesi:
            print(i)

            print("************************")

    def kelime_frekansi(self):
        kelime_sozcuk = dict()

        for i in self.sade_kelimeler:
            if (i in kelime_sozcuk):
                kelime_sozcuk[i] += 1
            else:
                kelime_sozcuk[i] = 1
        for kelime, sayi in kelime_sozcuk.items():

            print("{} kelimesi {} defa geçiyor..".format(kelime, sayi))

            print("----------------------------")            






dosya = Dosya()

dosya.kelime_frekansi()
"""



# örnek



"""cumle = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

kelimeler = cumle.strip("")


kel = list()
for ic in kelimeler:
    kel.append(ic)


kelime_sozcuk = dict()

for i in kel:

    

    if (i in kelime_sozcuk):
        kelime_sozcuk[i] += 1
    else:
        kelime_sozcuk[i] = 1
for kelime, sayi in kelime_sozcuk.items():
    print("{} kelimesi {} defa geçiyor..".format(kelime, sayi))

    print("----------------------------")    

"""



"""
# çok önemli bir örnek zor yaptım for döngülerini iç içe kullanma yanlış çıkıtor
cumle ="akşamevegeldinmibilmiyorumamaistanbulagelkesinliklebekliyorum"

kel = cumle.strip("")

liste = list()

for i in kel:
    liste.append(i)    


sel = dict()

for i in liste:
    
    if (i in sel):
        sel[i] += 1
            
    else:
        sel[i] = 1
              
for kelime,sayi in sel.items():
        
    print("{} kelimesi {} defa geçiyor..".format(kelime, sayi))

    print("----------------------------")    
    
"""
    
"""
bas_harfler = ""
with open("siir.txt","r",encoding="utf-8") as file:
    for satir in file:
        bas_harfler += satir[0]

print(bas_harfler)

"""


"""
with open("mailler.txt" , "r" , encoding="utf-8") as file:
    
    for i in file:
        i = i[:-1]
        if(i.endswith(".com") and i.find("@") != -1):
            print(i) 
"""

"""sel = ["elifgildeyiz işte"]        
    
for i in sel:
    i = i[:-1]
    if i.endswith("işte"):
        print(i)"""



"""
isim = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

soyisim = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

liste = list(zip(isim , soyisim))
liste.sort()

for i,j in liste:
    print(i,j)
"""

"""asassasas"""




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
    print("Kök bulma " , kokbulma (int(sys.argv[0])),(int(sys.argv[1])),(int(sys.argv[2])))

else:
    sys.stderr.write("Lütfen doğru değerler giriniz")
    sys.stderr.flush()




kokbulma(2 , 1 , 2)
"""





import requests

from bs4 import BeautifulSoup


url = "https://en.yellowpages.com.tr/search?q=Ankara"

response = requests.get(url)


html_icerigi = response.content

soup = BeautifulSoup(html_icerigi , "html.parser")



for i in soup.find_all("a"):
    print(i)
    


