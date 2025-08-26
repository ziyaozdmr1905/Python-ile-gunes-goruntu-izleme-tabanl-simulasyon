# FONKSİYONLAR İYİCE ÖĞREN

"""
import random

sayi = random.randint(1 , 100)
can = int(input("Kaç hak kullanmak istersiniz: "))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("Tahmin: "))
    if sayi == tahmin:
        print(f"Tebrikler {sayac}. defa da bildiniz. Toplam puan: {100 - (100/can)*(sayac -1)} ")
        break
    elif sayi > tahmin:
        print("Yukarı")
    else:
        print("Aşağı")    
    if hak == 0:
        print(f"Hakkınız bitti, tutulan sayı {sayi}")
"""

# İN operatörü
"""
x = ["Elma", "Armut","Nar","Portakal"]

print("Armut" not in x)
print("Armut" in x)
"""

"""
while True:
    print("Atpacık babul ")
    break
"""


"""
meyveler = []

girilen = input("Bir meyve giriniz: ")

if ("a" in girilen):
    meyveler.append(girilen)
    print("Girilne kelimenin içinde a harfi olğu için listeye aldık liste: ", meyveler)
else:
    print("Üzgünüm kelime içinde a harfi yok")    
"""

"""
meyveler = []

girilen = input("Bir meyve giriniz: ")

while ("a" in girilen):
    meyveler.append(girilen)
    print("Girilne kelimenin içinde a harfi olğu için listeye aldık liste: ", meyveler)
    break
"""
    

"""
import datetime

tarih  = input("Aracınız hangi tarihte trafiğe çıktı (2019/8/9): ")
tarih = tarih.split('/') #yani tarih kısmını / buradan ayır
trafigeCikis = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))
simdi = datetime.datetime.now()  # şimdi ki zanı ele al diyor
fark = simdi - trafigeCikis
days = fark.days

if days <= 365:
    print("1.Servis aralığı")
elif (days > 365) and (days <= 365 * 2):
    print("2.Servis aralığı")
elif (days > 365 * 2) and (days <= 365 * 3):
    print("3.Servis aralığı")
else:
    print("Hatalı süre")            
"""

"""
numbers = [1,2,3,4,5]

for x in numbers:
    print(x)
"""
"""
numbers = [1,2,3,4,5]

for num in range(0,50,2):
    print(num)
"""
"""
tuple = [(1,2),(1,3),(3,5),(5,7)]

for a,b in tuple:
    print(a,b, end='*')
    #print(a,end=',')
"""

"""
d = {"k1" : 1, "k2": 2, "k3": 3}

for x in d.items():
    print(x)
"""    
"""
sayılar = [1,3,5,7,9,12,19,21]

for x in sayılar:
    if (x % 3 == 0):
        print("3 ün katları: ",x, end=' , ')
"""        

"""
sayılar = [1,3,5,7,9,12,19,21]
toplam = 0

for x in sayılar:
    toplam += x
    print("Toplam: " , toplam)
"""

"""
sayılar = [1,3,5,7,9,12,19,21]

for x in sayılar:
    if (x % 2 == 1):
        print(x**2)
"""

"""
sehirler  =["kocaeli","istanbul","ankara","izmir","rize"] 

for x in sehirler:
    if (len(x) < 5):
        print(x)
"""




"""
urunler = [
    {'name' : 'samsung s6' , 'price' : '3000'},
    {'name' : 'samsung s7' , 'price' : '4000'},
    {'name' : 'samsung s8' , 'price' : '5000'},
    {'name' : 'samsung s9' , 'price' : '6000'},
    {'name' : 'samsung s10' , 'price' : '7000'}
]
"""

#                  :ÇOK ÖNEMLİ: 
# print kullanımı fon döngüsü içinde olursa eğer
# yani şöyle : 
"""
toplam = 0
for x in urunler:
    #print(int(x['price']), end=' , ')
    toplam += int(x['price'])
    print(toplam)
"""
#  çıkan sonucu döngü halinde toplar yani şöyle = 
# EKRAN ÇIKTISI
# 3000 , 3000
# 4000 , 7000
# 5000 , 12000
# 7000 , 25000
# ŞEKLİNDE ÇIKAR


# AMA ŞÖYLE YAPARSAK, YANİ PRİNT FOR DÖGÜSÜ İZASINDA DIŞARIDA OLURSA, SADE TOPLAMINI ALIR
"""
toplam = 0
for x in urunler:
    print(int(x['price']), end=' , ')
    toplam += int(x['price'])
print(toplam)
"""
"""
toplam = 0
for x in urunler:
    fiyat = int(x['price'])
    toplam += fiyat
print(toplam)     
"""
# EKRAN ÇIKTISI
# 25000 
# OLUR 

# while döngüsü
"""
name = ' '
while not name.split():
    name  = input("İsiminzi giriniz: ")
print(f"Merhaba {name}")
"""



sayılar = [1,3,5,7,9,12,19,21]

#1.soru cevabı
"""
while sayılar:
    print(sayılar)
    break
"""

#2.soru cevabı
"""
baslangic = int(input("Başlangıç için sayı giriniz: "))
bitis = int(input("Bitiş için sayı giriniz: "))

i = baslangic

while i < bitis :
    i += 1
    if i % 2 == 1:
        print(i)
"""

#3.srou cevabı
"""
i = 1
while i < 100:
    i += 1
    print(i)
"""    

#4.soru cevabı
"""
numbers = []

i = 0

while i < 5:
    sayi = int(input("Sayı: "))
    numbers.append(sayi)
    i += 1
numbers.sort()
print(numbers)    
"""    
    

#5.soru cevabı
"""
urunler = []

adet = int(input("kaç adet ürün gireceksiniz: "))
i = 0

while (i < adet):
    name = input("Ürünün ismi: ")
    price = input("Ürün fiyatı: ")
    urunler.append( {
        "name" : name,
        "price" : price
    })
    i += 1

for urun in urunler:
    print(f'ürün adı: {urun["name"]} ürün fiyatı: {urun["price"]}')
"""
"""
name = "Sadık turan"
for letter in name:
    if letter == "d":
        break
    print(letter)
"""
"""
x = 0
while x < 5:
    print(x)
    x += 1
"""

"""
x = 1
toplama  =0

while x <= 100:
    toplama += x
    x += 1
print(f"toplam: {toplama}")    
"""

"""
x = 1
toplam = 0

while x <= 100:
    x += 1
    if x % 2 == 0:
        continue
    toplam += x
print(f"toplam : {toplam}")    
"""








































