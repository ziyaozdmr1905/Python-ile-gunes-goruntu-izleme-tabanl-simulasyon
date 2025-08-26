# TEKRAR 5

"""
liste = [3,1,24,5,16,8,21,13,7,15]
ort = 0
toplam = 0

for l in liste:
    toplam += l
    ort = (toplam / (10)) 
    l += 1
print(ort)    
"""

"""
musteriler = []

isim1 = input("Müşteri adı giriniz: ")
isim2 = input("Müşteri adı giriniz: ")
isim3 = input("Müşteri adı giriniz: ")

musteriler.append(isim1)
musteriler.append(isim2)
musteriler.append(isim3)

print(musteriler)

for x in musteriler:
    print(x)
"""


"""
musteriSayısı = int(input("Kaç tane müşteri var: "))

musteriler = []
i = 0

while i < musteriSayısı:
    musteri = input("Müşteri ismi: ")
    
    musteriler.append(musteri)
    i += 1

print(musteriler)
    
for x in musteriler:
    print(x)    
"""
# int(input("Öğrencinin okul numarasını giriniz: "))

# ÖĞRENCİ LİSTESİ OLUŞTUR

"""
ogrSayısı = int(input("Öğrenci sayısı: "))

i = 0

ogrenciler = []
ogrNo = 0

while i < ogrSayısı:
    adi = input("Öğrencinin adını giriniz: ")
    if adi not in ["ç","Ç"]:
        soyadi = input("Öğrencinin soyadını giriniz: ")
        #h = soyadi.split()
        #h.sort()
        telNo = int(input("Öğrencinin telefon numarasını giriniz: "))
        ogrNo += 1
        
        ogrenci = [soyadi, adi, ogrNo, telNo ]
        ogrenciler.append(ogrenci)
        
        i += 1
        continue   
    else:
        print("program sonladı")
        break    
print(ogrenciler) 
#print(sorted(i.split(',')[0].strip() for i in ogrenci))
# import locale
# locale.setlocale(locale.LC_ALL, ("tr", 'UTF-8'))
# sorted(soyadi , key=locale.strxfrm)

for x in ogrenciler:
    #for sirala in h:
        print(f" {x[2]} {x[1]} {x[0]} {x[3]} ")
"""      


# YAPILMADI
"""
ogrenciler = []
ogrNo = 0

while 1:
    adi = input("Öğrencinin adını giriniz: ")
    if adi not in ["ç","Ç"]:
        soyadi = input("Öğrencinin soyadını giriniz: ")
        #h = soyadi.split()
        #h.sort()
        telNo = int(input("Öğrencinin telefon numarasını giriniz: "))
        ogrNo += 1
        
        ogrenci = [soyadi, adi, ogrNo, telNo ]
        
        ogrenciler.append(ogrenci)
        

        continue   
    else:
        break    
print(ogrenciler) 
#print(sorted(i.split(',')[0].strip() for i in ogrenci))
# import locale
# locale.setlocale(locale.LC_ALL, ("tr", 'UTF-8'))
# sorted(soyadi , key=locale.strxfrm)
#ogrenciler.sort([soyadi])
for x in ogrenciler:
    #for sirala in h:
    print("Girilen öğrenciler")
    print(" {} {} {} {} ".format(ogrNo , adi , soyadi , telNo))
    #print(f"{x[2]} {x[1]} {x[0]} {x[3]}")
#    x = x.sorted(ogrenci)
    #x.sort[soyadi]
"""    


# BAŞKA BİR ÖRNEK
"""
abonelistesi = [
    [342, 'Melike Başer' , 51],
    [624, 'Ahmet Arıyan' , 67],
    [173, 'Selim Yıldırım' , 31],
    [234, 'Mustafa Akgün' , 89],
    [512, 'Aybüke Çoban' , 12]
]



guncelListe = []



while 1:
    aboneNo = input("Abone numarasını giriniz: ")
    if aboneNo not in ["ç","Ç"]:
        for a in abonelistesi:
            if (int(aboneNo) == a[0]):
                sonEndeksi = int(input("Son endeksini giriniz: "))
                tük = sonEndeksi - a[2]
                odeme = float(tük) * (1.2)
                a.insert(3 , sonEndeksi)
                a.insert(4 , tük)
                a.insert(5 , odeme)
                #print(abonelistesi)
                guncelListe.append(a)
                # guncelListe.append(sonEndeksi)
                # guncelListe.append(tük)
                # guncelListe.append(odeme)    
                #adiSoyadi = input("Abone isim soyisim giriniz: ")
                #print(guncelListe)
                break
        else:  
            adiSoyadi = input("Bir isim soyisim giriniz: ")
            ilkEndeks = int(input("İlk endes numarasını giriniz: "))
            sonEndeks = int(input("Son endeks numarasını giriniz: "))
            tük = sonEndeks - ilkEndeks
            odeme = float(tük) * (1.2)
            yeni = []
            yeni.append(aboneNo)        
            yeni.append(adiSoyadi)
            yeni.append(ilkEndeks)
            yeni.append(sonEndeks)
            yeni.append(tük)
            yeni.append(odeme)
            guncelListe.append(yeni)
            continue
    else:
        print(guncelListe)
        break            

for x in guncelListe:
    print(f" {x[0]} {x[1]} {x[2]} {x[3]} {x[4]} {x[5]} " )                    
                    
"""                    





# STRİNGLER
"""
def harfBul(cumle , harf):
    i = 0
    while i < len(cumle):
        if cumle[i] == harf:
            return i
        i += 1
    return -1
print(harfBul('Melike', 'e'))            
"""

"""
ayse = "Dilek Antalyadan \"Sesim Geliyor mu?\" diye sordu."
print(ayse)
"""


# bir kaçış karakteri (\) koyarak cümleye alt satırdan devam edebiliriz
"""
a = "bir keresinde ankaraya gittim\
    ve bana uzun uzun baktılar"
print(a)
"""

"""
def kelimeBul(cumle , kelime):
    for i in range(len(cumle)):
        if (cumle[i:i+len(kelime)] == kelime):
            return i
    return -1        

print(kelimeBul("Fatih Başer" , "Başer"))
"""


#print('tatlı' in 'Bneim kızım çok tatlı')
#print("Fatih Başer".find("Başer"))

# içinde bolu geçen yerleşim yerleri

"""
yerlesimYerleri = ["Bolu" , "Yozgat" ,"Manavgat" , "Çanakkale" , "Çan" , "Kırıkkale" , "İnebolu"]

for u in yerlesimYerleri:
    if u.find('bolu') > -1:
        print(u)
"""

"""
yerlesimYerleri = ["Bolu" , "Yozgat" ,"Manavgat" , "Çanakkale" , "Çan" , "Kırıkkale" , "İnebolu"]

aranacak = 'Bolu'

for u in yerlesimYerleri:
    kucuk = u.lower()
    if kucuk.find(aranacak.lower()) > -1:
        print(u)

"""



# döngü metotoları
"""
for item in range(1,50,3):
    print(item)
"""
#enumerate metodu
"""
gre = "Hello"

for index,letter in enumerate(gre):
    print(index , letter)
"""

"""
gree = 'Hello'
for i in enumerate(gree):
    print(i)
"""


#zip metodu
"""
liste1 = [1,2,3,4,5]

liste2 = ["a","b","c","d","e"]

#print(zip(liste1 ,liste2))  bu şekilde yaparsak zip metdou çalşmaz çünkü liste tipinde çalması lazım şöyle yani

print(list(zip(liste1 ,liste2)))

"""

"""
numbers = [x for x in range(10)]
print(numbers)
"""

"""
sayi = int(input("Bir sayi: "))
asalmi = True

if sayi == 1:
    asalmi = False
for x in range(2 ,sayi):
    if (sayi % 2 == 0):
        asalmi = False
        break
if asalmi:
    print("Sayı asaldır")
else:
    print("Sayı asal değildir")     
"""

# fonksiyonlar sayma işlemini ne kadar çağırırsak o kadar yazdırır. sürekli print demeye gerek yoktur
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
"""
"""
def say(name):
    print('Hello ' + name)

say('çınar')
"""

# print dışarda kullandık çünkü içeride return kullandık
"""
def total(name = 'user'):
    return 'hello' + name
msg = total('çınar')    
msg = total()
print(msg)
"""


"""
def total(num1 , num2):
    return num1 + num2
res = total(10 , 20)    

print(res)
"""
"""
def yasHesapla(dogum_yılı):
    return 2019 - dogum_yılı

agecınar = yasHesapla(2000)
ageada= yasHesapla(1998)    

print(ageada , agecınar)
"""


"""
def kisidogum(dogumyili):
    return 2022 - dogumyili 

def kisiİsim(isim):
    return 'Hello' + isim

k3 = kisidogum(2008)
k4 = kisidogum(1999)

k1 = kisiİsim(' çınar')

k2 = kisiİsim(' ada')

print(k1 , k3)
print(k2 , k4)
"""

"""
def yasHesapla(dogumyili):
    return 2022 - dogumyili

def emekliligekacyil(dogumyili , isim):
    yas = yasHesapla(dogumyili)  # buradaa 'yashesapla' fokiyonunu çağırdık
    emeklilik = 65 - yas
    if emeklilik > 0:
        print(f" {isim} bey, emekliliğinize {emeklilik} yıl kalmış")
    else:
        print("Zaten emekli oldunuz")
emekliligekacyil(1983 , 'Ali')
"""


"""
def chan(n):
    n = 'ada'
name = 'çınar'    
chan(name)
print(name)
"""



"""
def chnage(n):
    n[0] = 'İstanbul'       # kısaca şu şekilde oluyor  chnage(sehirler) = chnage(n) oluyor. yani sehirler[0] = "İstanbul" oluyor
sehirler = ["Ankara" , "İzmir"]


chnage(sehirler)
print(sehirler)
"""
# aynı işlemi terardan yapalım ama fonskiyon çağırmadan
""" 
def change(n):
    n[0] = 'İstanbul'
sehirler = ["Ankara", "İzmir"]

n = sehirler
n[0] = 'İstanbul'

print(sehirler)
"""

"""
def change(n):
    n[0] = 'İstanbul'
sehirler = ["Ankara" , "İzmir"]
n = sehirler[:]       # sehirler listesini n ye aktardık demek    

n[0] = 'İstanbul'

print(sehirler)
print(n)
"""
"""
message = ['Hello', 'There.', 'My', 'name', 'is', 'Sadık', 'Turan']
n = message[:2]
# bu örnkte var [:2] en başla ve 2.index e kadar demektir yani o kadar olan yeri n ye atar
print(message)
print(n)

"""
"""
def change(n):
    n[0] = 'İstanbul'
sehirler = ["Ankara" , "İzmir"]
n = sehirler       # sehirler listesini n ye aktardık demek    

n[0] = 'İstanbul'


print(sehirler)
print(n)

"""
"""
def add(a,b):
    return sum((a,b)) #sum fonksiyonu direk toplama yapıyor
print(add(10,20))    
"""

"""
def add(a,b,c=0,d=0):
    return sum((a,c,b,c,d))

print(add(10,20,30,40))
print(add(80,40))
"""

"""
def add(*params):
    print(params)
    return sum ((params))
print(add(10 ,20))
print(add(10,80,40,47,56,32))
"""

# sum fonksiyonu kulanamka istemzsek
"""
def add(*params):
    sum = 0

    for i in params:
        sum = sum + i
    return sum
print(add(10,20,30,80))        
"""
# **params dersek dictionary listesi oluşturmuş oluruz
"""
def dis(**args):
    for key , value in args.items():
        print(f" {key} is {value} ")
dis(name = 'çınar' , age = 2, city = 'istanbul') 
dis(name = 'yiğit' , age = 21, city = 'izmir') 
dis(name = 'ada' , age = 12, city = 'ankara') 
"""

"""
def myfunk(a , b , *args , **params):
    print(a)
    print(b)
    print(args)
    print(params)
myfunk(10,20,30,50,70 , key1='ali' , key2= 'veli')    
"""