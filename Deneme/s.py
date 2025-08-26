#          FONKSİYONLAR

#fonksiyon oluşturmak için def kullanıyoruz
"""
def sayHello():
    print("Hello")
"""
# Eğer bu kodu böyle yaparsak ekran çıktısı vermez çünkü sayHello isimli fonkisyonu çağırmamız gerekecek

# kısaca kodumuz şöyle olacak
"""
def sayHello():
    print("Hello")
sayHello()    
"""
# bu fonkisyonu istediğişz kadar çağırırız
"""
def sayHello():
    print("Hello")
sayHello()    
sayHello()
sayHello()
"""

# name adanda bir değişken tamamlayarak böyle bir yol kullanabiliriz
"""
def sayHello(name):
    print("Hello" + name)
sayHello(" çınar")    
sayHello(" Ada")
"""

#eğer name belirtip sayhello isimli fonksiyonun içini belirli bir sisim yazmazsak name değikeninin baz alır
"""
def sayHello(name = " User"):
    print("Hello" + name) 
sayHello(" Çınar")
sayHello(" Ada")
sayHello()
"""

# geri çağırma işlemi de var fonkiyonlarda return il yapılıyor
#Örnek
"""
def sayHello(name = " User"):
    return "Hello" + name
msg = sayHello(" Çınar")
print(msg)
"""

"""
def total(num1 , num2):
    return num1 + num2
result = total(10,20)   #atama işlemi yapıyorum buarada, yukarıda num1 ve num2 belirliyorum. burada değer atıyorum 
print(result)
"""

# burada yasHesapla isimli fonksiyon sayesinde bir çok işi kolaycacık yaptık. yani uzun uzun tek tek çıkarma işlemi yapmadık 
"""
def yasHesapla(dogumyili):
    return 2019 - dogumyili
agecınar = yasHesapla(2017)    
ageada= yasHesapla(2010)
agesena = yasHesapla(1999)

print(ageada , agecınar, agesena)
"""
#Başka bir örnek
"""
def yasHesapla(dogumyili):
    return 2019 - dogumyili

def emekliligekacyilkaldi(dogumyili,isim):
    yas =yasHesapla(dogumyili)
    emelilik = 65- yas

    if emelilik > 0:
        print(f"emekliliğinize {emelilik} yıl kaldı ")
    else:
        print("zaten emekli oldunuz")
emekliligekacyilkaldi(1983 , "ALİ")        

emekliligekacyilkaldi(1960 , "ALİ")        
emekliligekacyilkaldi(1952 , "ALİ")        
"""




# kullanıcıya bilgi verme içiçn üç üst kullandık
"""
def yasHesapla(dogumyili):
    return 2019 - dogumyili

def emekliligekacyilkaldi(dogumyili,isim):
    '''
    DOCSTRİNG : Dogum yiliniza gore emekliliginize kac yil kaldi
    INPUT : Dogum yili
    OUTPUT : Hesaplanan yil bilgisi
    '''
    yas =yasHesapla(dogumyili)
    emelilik = 65- yas

    if emelilik > 0:
        print(f"emekliliğinize {emelilik} yıl kaldı ")
    else:
        print("zaten emekli oldunuz")
emekliligekacyilkaldi(1983 , "ALİ")
# help komutu bilmediğimiz metotları nasıl kullanılacak anlatır        
print(help(emekliligekacyilkaldi))
"""

#              FONKSİYON PARAMETRELERİ
"""
def changename(n):
    n = "Ada"
name = "Yiğit"
changename(name)
print(name)
"""

"""
def change(n):
    n[0] ="İstanbul"
sehirler = ["Ankara" , "İzmir"]
# burada change(n) = change(sehirler) aslında bir birine aktarıldı
change(sehirler)
print(sehirler)
"""
# görüldüğü gibi yukarıda bahsettiğim şeyi aşağıdaki örnekte yaptık
"""
def change(n):
    n[0] ="İstanbul"
sehirler = ["Ankara" , "İzmir"]
n = sehirler
n[0] = " İstanbul"
print(sehirler)
"""

#atama işlemi yapmak yerine bir kopyalama işlemi yapmak istersek

"""
def change(n):
    n[0] ="İstanbul"
sehirler = ["Ankara" , "İzmir"]
n = sehirler[:]

n[0] = " İstanbul"
print(sehirler)
print(n)

"""
# bu fonksiyon en fazla 5 parametreli olur daha fazla parametre eklemek istersek 
"""
def add(a,b, c = 0):
    return sum((a,b,c))
print(add(10,20))
print(add(10,20,30))
"""
#bir yıldız ekleyerek istediğimiz kadar parametre ekleriz artık
"""
def add(*params):
    return sum((params))
print(add(10,20))
print(add(10,20,30,40,50))
print(add(10,20,60,80,70,90,100))
"""

#  sum fomkiyonunu kullanmak istemezsek
"""
def add(*params):
    sum = 0

    for n in params:
        sum = sum + n
    return sum
print(add(10,20))
print(add(10,20,30))
print(add(10,20,60,80,70,90,100))
"""


# eğer dictionary listesi yapmak istersek iki( yıldız) ** ekleriz, önceki örnekte tek yıldız vardı tuple listesi oluyordu
"""
def display(**args):
    for key,value in args.items():
        print(" {} is {} ".format(key,value))

display(name = "Çınar" , age = 2 , city = "İstanbul")
display(name = "Ada" , age = 12 , city = "Kocaeli" , phone = "123647")
display(name = "Sena" , age = 14 , city = "Ankara" , phone = "456789")
"""

"""
def myfunc(a,b, *args ,**params):
    print(a)
    print(b)
    print(args)
    print(params)

myfunc(10,20,30,40,50, key1 ="value", key2 = "value2")
"""


"""
def f(x):
    print("x parametresinin aldığı değer: ",x)
    y = x +5
    print("Hesaplama sonucu: ",y)
    return y
s = f(3)    
"""

"""
def f(x):

    s = f(2*3)
    print(s)
f(3)
"""
"""
def deneme(k):
    l = 3
    print(l)
    print(k*l)
deneme(7)    
deneme(21)
deneme(9)
"""

"""
def f(x):
    return x+5
s = f(3)    
print(s)
"""

#gönderilen x,y sayılarının çarpımını alır
"""
def carp(x,y):
    print(x*y)

carp(10,5)   #gönderilen sayılar bunlar
"""
"""
def bolum(bolunen , bolen):
    print(bolunen/bolen)

bolum(16,2)
bolum(12,4)
bolum(96,4)
"""

#parametre ifadelerini belirtirsek en sonda belitmeye gerek yok
"""
def bolum(bolunen= 10,bolen=5):
    print(bolunen/bolen)

bolum()
"""

# sep parametresi boşluklar arasına istediğimizi koyarız
#print("python","öğrenmek","çok","kolaydır",sep="*")


#kök alma işlemi nasıl yapılır

"""
def kokAl(sayi):
    kok = sayi**(1/2)
    print(kok)

kokAl(81)
kokAl(56)
kokAl(30)
kokAl(24)
kokAl(8)
"""

# 3.dereceden de kök alabiliriz şimdi bir örbek yapalım
"""
def kokAl(sayi,derece):
    kok =sayi**(1/derece)
    print(kok)

kokAl(81,3)
kokAl(36,3)
kokAl(120,3)
kokAl(81,4)
"""
"""
def kokAl(sayi,derece =3):
    kok = sayi**(1/derece)
    return kok
girilen = float(input("Karekökü alınacak bir sayı giriniz: "))    
k = kokAl(girilen)

print(k)
"""

# UYGULAMA ÖRNEK

#1.SORU CEVABI
"""
def yazdir(kelime , adet):
    print(kelime * adet)
yazdir('merhaba\n', 10)
"""

#2.SORU CEVABI 
"""
def listeyecevir(*params):
    liste = []
    for param in params:
        liste.append(param)
    return liste
result = listeyecevir(10,20,30,'merhaba')
print(result)
"""


#3.SORU CEVABI
"""
sayi1 = int(input("sayı 1: "))
sayi2 = int(input("sayi 2: "))
def asalsayilaribul(sayi1 , sayi2):
    for sayi in range(sayi1 ,sayi2+1 ):
        if sayi > 1:
            for i in range(2, sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)



asalsayilaribul(sayi1 , sayi2)               
"""


#4.SORU CEVABI
"""
def tambolenleribul(sayi):
    tambolenler = []
    for i in range(2,sayi):
        if (sayi % i == 0):
            tambolenler.append(i)
    return tambolenler
print(tambolenleribul(20))            
"""























