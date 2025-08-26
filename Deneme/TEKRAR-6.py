"""
def yazdir(kelime , adet):
    return kelime * adet
print(yazdir("elif",2))    
"""

"""
def yazdir(kelime , adet):
    print( kelime * adet)
yazdir('merhaba' , 10)    
"""

"""
def gonderilen(*args):
    liste = []
    for t in args:
        liste.append(t)
    return liste

r = gonderilen(10,20,40,70)         
print(r)
"""
"""
def gonder(*args):
    araba = []
    for t in args:
        araba.append(t)
    return araba

r = gonder("BMW","Opel","Mazda")
print(r)
"""    

"""
birinci = int(input("Bir sayı girin: "))
ikinci = int(input("Bir sayı girin: "))
def asalbul(birinci , ikinci):
    for sayi in range(birinci , ikinci + 1):
        if sayi > 1:
            for i in range(2 , sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)
asalbul(birinci , ikinci)                    
"""

"""
# mükemmel sayı örneği
sayi = int(input("Bir sayı giriniz: "))
i = 1
toplam = 0 
while (i < sayi):
    
    if (sayi % i == 0):
        toplam += i
    i += 1
if (toplam == sayi):
    print(sayi,"Mükemmel bir sayıdır")        
else:
    print(sayi,"Mükemmel bir sayı değildir.")
"""

"""
sayi = (input("Sayı: "))

basamakSayısı = len(sayi)
sayi = int(sayi)
toplam = 0
basamak = 0

geciciSayi = sayi
while geciciSayi > 0:
    basamak = geciciSayi % 10
    toplam += basamak ** basamakSayısı
    geciciSayi //= 10
if (toplam == sayi):
    print(sayi,"Bir armstrong sayısıdır")    
else:
    print(sayi,"Bir armstrong sayısı değildir")
"""


"""
def harfbul(cumle,harf):
    i = 0
    while i < len(cumle):
        if cumle[i] == harf:
            return i     
        i += 1
    return -1
print(harfbul("Fatig Başer","ş"))        
"""


# if else blokları
"""
x = 20
y = 20

if (x > y):
    print("X Y'den büyük ")
elif (x == y):
    print("X Y'ye eşit")    
else:
    print("X Y'den küçük")
"""


# Ehliyet Alma durumu
"""
isim = input("İsim: ")
okul = input("Okul: ")
yas = int(input("Yaşı: "))



if (yas > 18):
    print(f"sayın {isim} yaşı ehliyet almaya uygundur.")
    if (okul == "lise") or (okul == "üniversite"):
        print(f"sayın {isim} eğitim durumu ehliyet almaya uygundur.")
    else:
        print(f"maalesef sayın {isim}, ehliyet alamaz.")
else:
    print(f"maalesef sayın {isim}, ehliyet almaya yaşı uygun değildir.")                
"""

"""
sayi = [1,3,5,7,9,12,19,21]
toplam = 0
for k in sayi:
    if (k % 2 == 1):
        toplam +=k
        print(k)
print("toplam: ", toplam)
"""


"""
x = 1
while x <= 100:
    if x % 2 == 1:
        print(f"sayı tek {x}")
    else:
        print(f"sayı çift {x}")    
    
    x += 1    
print("Bitti..")
"""


"""
sayilar = [1,3,5,7,9,12,19,21]

i = 0
while (i < len(sayilar)):
    print(sayilar[i])
    i += 1
"""

"""
baslangic = int(input("Başlangıç: "))
bitis = int(input("Bitiş.."))

i = baslangic

while i < bitis:
    i += 1
    if (i % 2 == 1):
        print(i)
"""
"""
uruler = []

adet = int(input("Kaç ürünü eklemek istiyorsun: "))
i = 0

while (i < adet):
    name = input("Ürün ismi: ")
    price = input("Ürün fiyatı: ")
    uruler.append({
        'name' : name,
        'fiyat' : price
    })
    i += 1
for urun in uruler:
    print(f"ürün adı: {urun['name']} ürün fiyatı: {urun['fiyat']}")    
"""
"""
name = 'sadık turan'

for k in name:
    if k == "ı":
        continue
    print(k) 
"""

"""
x = 0
while x < 5:
    if x == 2:
        break
    x +=1
    print(x)    
"""
"""
res = 0
x = 0

while x <= 100:
    x += 1
    if x % 2 == 1:
        continue
    res += x
print(res)
"""

"""
num = []

for k in range(10):
    num.append(k)
print(num)
"""
"""
num = [x for x in range(10)]

print(num)
"""

# Armstrong sorusu
"""
sayi = input("Sayi: ")
basamakSayisi = len(sayi)
sayi = int(sayi)

basamak = 0
toplam = 0

gecicisayi = sayi
while (gecicisayi > 0):
    basamak = basamakSayisi % 10
    toplam += basamak ** basamakSayisi
    gecicisayi //= 10

if (toplam == sayi):
    print(sayi,"Armstrong sayıdır")    
else:
        print(sayi,"Armstrong sayısı değildir")    
"""

#çarpım tablosu
"""
for k in range(1,11):
    print("*******************************")
    for t in range(1,11):
        
        print(f" {k} x {t} = {k*t} ")
"""

"""
toplam = 0
while 1:
    sayi = input("Sayi : ")
    if (sayi == "q"):
        print("Program sonlandı")
        break
    else:
        sayi = int(sayi)
        toplam += sayi
        print("toplamı: ",toplam)
"""

"""
for i in range(1,101):

    if (i % 3 != 0):
        continue
    print(i)
"""        

"""
liste = list(range(0,101))
cift = []

for i in liste:
    if (i % 2 == 0):
        cift.append(i)
print(cift)
"""

"""
def say():
    print("Hello")
say()     
say()     
say()     
say()     
say()     
say()     
say()     
say()     
say()     
"""

"""
def say(x,y,z):
    print("toplamları:", x+y+z)
say(1,5,7)
"""

"""
def say(x,y,z):
    return x+y*z
def sar(say):
    return say/9

print(sar(say(7,8,4)))
"""


"""
def say(name):
    print("Hello" , name)

say("zeynep")
say("ali")
"""


"""
def say(name = 'çınar'):
    return "Hello " + name

smg = say("ada")
print(say())
print(smg)
"""



"""
def yashesapla(dogum_yili):
    return 2023 - dogum_yili

def emekliligekacyil(dogum_yili , isim):
    yas = yashesapla(dogum_yili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f"Sayın {isim} emeliliğinize {emeklilik} yıl kaldı.")
    else:
        print("Sayın {isim} zaten emekli oldunuz.")    


emekliligekacyil(1965,"ada")
"""

"""
def change(n):
    n[0] = "istanbul"
sehirler = ["ankara", "izmir"]

change(sehirler)
print(sehirler)
"""

"""
def cahneg(n):
    n[0] = "istnabul"

sehirler = ["ankara","izmir"]
n = sehirler
n[0] = "istnabul"    
print(sehirler)
"""

"""
def say(n):
    n[0] = "istanbul"
sehirler = ["ankara", "izmir"] 
n = sehirler[:]

n[0] = "istanbul"
print(sehirler)
print(n)

"""

"""
def say(a, b):
    return sum((a,b))
print(say(10,20))    
print(say(10,40))
"""

"""
def say(*par):
    return sum((par))
print(say(10,20))
print(say(107,70,40))
print(say(101,202))
print(say(45,25,75,95))
"""


"""
def say(kelime, adet):
    return (kelime * adet)

print(say("muz" , 4))
"""

"""
def say(*par):
    liste = []
    for k in par:
        liste.append(k)
    return liste

res = say(10 , 20 , 30 , "merhaba")
print(res)    
"""


"""
sayi1 = int(input("Bir sayı giriniz: "))
sayi2 = int(input("İkinci bir sayı daha giriniz: "))

def asalSayiBul(sayi1 , sayi2):
    for sayi in range(sayi1 , sayi2 + 1):
        if sayi > 1:
            for i in range(2 ,sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)

asalSayiBul(sayi1 , sayi2)
"""


"""
def tambolen(sayi):
    tambol = []
    for k in range(2, sayi):
        if (sayi % k == 0):
            tambol.append(k)
    return tambol

print(tambolen(20))
"""
"""
def bolenler(sayi):
    ucbolenler = []
    for i in range(2, sayi):
        if (i % 3 == 0):
            ucbolenler.append(i)
    return ucbolenler
print(bolenler(30))            
"""

"""
sayi1 = int(input("1.Sayı: "))
sayi2 = int(input("2.Sayı: "))

def asalBul(sayi1 , sayi2):
    for sayi in range(sayi1 , sayi2):
        if sayi > 1:
            for i in range(2 , sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)

asalBul(sayi1 , sayi2)
"""