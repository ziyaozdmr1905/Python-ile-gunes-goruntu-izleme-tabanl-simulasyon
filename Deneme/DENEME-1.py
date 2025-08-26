# TEKRAR
"""
print("Programdan çıkmak için [ç] harfi giriniz...")

while True:
    i = input("Kareköküalınacak sayıyı giriniz: ")
    if i == "ç":
        print("[ç] girdiniz programdan çıkılıyor...")
        break
    if int(i)<0:
        print("Karmaşık şimdilik hesaplayamıyorum...")
        continue
    k = int(i) **(1/2)
    print("Girdiğiniz sayının karekökü: ", k)
"""



"""
print("Ülkemizin en güney ili hangisidir..")
print("Sadece iki şansınuız var...")

i = 1

while i <= 2:
    print(i,". şans ")
    girilen = input("Bir il giriniz: ")
    if girilen == "Hatay":
        print("Tebrikler en güney ilimiz hataydır..")
        break
    i += 1
else:
    print("Üzgünüm iki şansınızıda denediniz ve kaybettiniz..")
"""


# pi hesaplama
"""
n = 0
toplam = 0
son = 1000

while n < son:
    toplam += (((-1)**n) / (2*n+1))
    n += 1
print("Pi sayısının değeri: ", 4 *toplam)
"""

# KİTAPTAN ALIŞTIRMALAR

# BÜYÜK OLAN SAYIYI BULMA
"""
while True:
    sayi1 = int(input("Bir sayı girniz: "))
    sayi2 = int(input("Bir sayı giriniz: "))
    if (sayi1 < sayi2):
        print(f"Büyük olan sayı : {sayi2}")
        break
    elif (sayi2 < sayi1):
        print(f"Büyük olan sayı {sayi1}")
        break
    else:
        print("Sayılar eşittir")       
        break
"""

# boy endex sorusu
"""
while True:
    isim = input("Bir isim giriniz(Dögüden çıkmak için [q] basın): ")
    if (isim == "q"):
        print("Program sonlandırılıyor...")
        break
    
    kilo  = int(input("Kilonuzu giriniz:")) 
    boy = float(input("Boyunuzu giriniz: "))
    
    endex = (kilo / (boy**2))
    print(endex)
    
    if (0 < endex < 18.5):
        print(f"Sayın {isim}, kilo endexsiniz: {endex}, Zayıfsınız")
    elif (18.5 <= endex <= 24.9):
        print(f"Sayın {isim}, kilo endexsiniz: {endex}, Normalsiniz")
    elif (25.0 <= endex <= 29.9):
        print(f"Sayın {isim}, kilo endexsiniz: {endex}, Fazla kilolusunuz")
    elif (30.0 <= endex <= 39.9):
        print(f"Sayın {isim}, kilo endexsiniz: {endex}, Şişmansınız")
    elif (40.0 <= endex <= 50.0):
        print(f"Sayın {isim}, kilo endexsiniz: {endex}, Obezsiniz")
    else:
        print(f"Sayın {isim} Yanlış girdiniz")    
"""    

"""
for i in range(10 , 0 , -1):
    print(i)
"""

"""
for i in range(100 , 0 , -5):
    print(i)
"""

"""
sayi = input("Bir sayı giriniz ama 100 e kadar: ")

while 1:
    if (sayi == "q"):
        break
    if (0 <= int(sayi) <= 100):
        print(f"Girilen sayı {sayi}")
        break
    else:
        print(  "Hatalı giriş yapıldı...")    
        break
"""

# önemli istediğin sayıyı gir çarpım tablosunu bul
"""
print("1 ile 10 arasında bir sayı giriniz....")

sayi = int(input("Bir sayı giriniz: ")) 

sayac = 0
while sayac < 10:
    sayac += 1
    print(sayi , "x" , sayac , "=" , sayac*sayi)
"""


"""
for a in range(1, 10):
    print("-" *20)
    print(a , "ler")
    for b in range(1,10):
        print(b,'*',a,'=',b*a)
"""



"""
sayi = int(input("Bir sayı girinz (0 ile 100 arası):"))

while 1:
    if 0 < sayi <100:
        print(sayi)
        break
    else:
        print("Hatalı giriş")
        break
"""

"""
for i in range(1 , 11):
    print("-" * 20)
    for k in range(1 , 11):
        print(i , "x" , k , "=" , i * k)
"""

"""
sayi = int(input("Bir sayı girinz(1 ile 10 arası): "))

sayac = 0

while sayac < 10:
    sayac += 1
    print(sayi , "x" , sayac , "=" , sayi * sayac)

"""

"""
sayi = input("Bir sayı dizisi girin: ")

kat = 20

while 1:
    print(sayi , "*" , kat , "=" , sayi * kat)
    break
"""


"""
asalmi = True

sayi = int(input("Bir sayı giriniz (1 ile 500 arasında): "))
if sayi== 0 or sayi == 1:
    asalmi = False
    print("Sonuç asal değildir...")
if (sayi == 2):
    print(f"{sayi} Sayı asal sayıdır..")    
    
for i in range(2 , sayi):
    if (sayi % i == 0):
        asalmi = False
        break        
if (asalmi):
    print(f"{sayi} sayısı asal dır...")
        
else:
    print(f"{sayi} Sayı asal değildir..")
"""    






"""
asalmi = True

sayi = int(input("Bir sayı girini: "))

if (sayi == 1):
    asalmi = False
if (sayi == 2):
    print(f"{sayi} Sayı asaldır..")    
if (sayi > 2):
    for i in range(2 , sayi):
        if (sayi % i == 0):
            asalmi= False
    if (asalmi):
        print(f"{sayi} sayısı asaldır..")        
    else:
        print(f"{sayi} asal değildir")
"""



"""
sayi = int(input("Bir sayı giriniz 1 ile 500 arası: "))

asalmi = True

while sayi < 500:
    if (sayi == 1):
        asalmi = False
        print(f"{sayi} asal değildir.. ")
        break
    if (sayi == 2):
        print(f"{sayi} asaldır.. ")
        break
    if (sayi > 2):
        for i in range(2 , sayi):
            if (sayi % i == 0):
                asalmi = False
        if (asalmi):
            print(f"{sayi} sayısı asaldır.. ")
            break
        else:
            print(f"{sayi} asal değildir ")
            break
"""


"""
sayi = int(input("Bir sayı giriniz: "))
        
def faktorbul(n):
    faktoriyel = 1
    while True:

        if (sayi == 0) or (sayi == 1):
            print(f"{sayi}! faktöriyeli 1 dir...")
            break
        if (sayi > 1):
            #faktoriyel = 1
            for i in range(2 , sayi+1):
                faktoriyel *= i
            print("faktöriyeli: ",faktoriyel)
        
            break
        else:
            print("hatalı")

faktorbul(sayi)
"""




"""
sayi = int(input("Bir sayı giriniz: "))

toplam = 0

for k in range(1, sayi):
    if ( sayi % k == 0):
        toplam += k
if (toplam == sayi):
    print(sayi,"mükemmel sayı")
else:
    print(sayi,"mükemmel değil..")        
"""





#ebob

"""
sayi1 = int(input("Küçük-Sayı: "))
sayi2 = int(input("Büyük-Sayı-2: "))
bolen = 0
ebob = []

if (0 < sayi1) and (0 < sayi2):

    for i in range(1 , sayi1):

        if (sayi1 % i == 0) and (sayi2 % i==0):
            bolen = i
            ebob.append(bolen)
    print(ebob)
    print("EBOB: " , max(ebob))
else:
    print("Hatalı giriş yapıldı...")    
"""    


# fonksiyonlarla ebob yapımı returnsuz
"""
def ebob(sayi1 , sayi2):
    ebobliste = []
    if (0 < sayi1 ) and (0 < sayi2):
        for i in range(1 , sayi1):
            if (sayi1 % i == 0) and (sayi2 % i == 0):
                ebobliste.append(i)
        print(ebobliste)
        print("EBOB: " , max(ebobliste))      
              
    else:
        print("Hatalı giriş..")

sayi1 = int(input("Küçük-sayı: "))
sayi2 = int(input("Büyük-sayı: "))

ebob(sayi1 , sayi2)
"""


# ebob fonksiyon kullanarak yazdık returnlu
"""
ebobliste = []
    
def ebob(sayi1 , sayi2):
    if (0 < sayi1 ) and (0 < sayi2):
        for i in range(1 , sayi1):
            if (sayi1 % i == 0) and (sayi2 % i == 0):
                ebobliste.append(i)
                #print(ebobliste)
    return max(ebobliste)      
    
sayi1 = int(input("Küçük-sayı: "))
sayi2 = int(input("Büyük-sayı: "))

print("ebob: ", ebob(sayi1 , sayi2))
"""





#ebob - ekok aynı soruda
"""
sayi1 = int(input("Küçük-sayı: "))
sayi2 = int(input("Büyük-sayı: "))


if (0 < sayi1) and (0 < sayi2):
    for i in range(1 , sayi1):
    
        if (sayi1 % i == 0) and (sayi2 % i == 0):
            ebob = i
    print(ebob)    
    ekok = (sayi1 * sayi2)// ebob
    print(ekok)
"""            
 




"""
sayi1 = int(input("Küçük-sayı: "))
sayi2 = int(input("Büyük-sayı: "))

if sayi1 > sayi2:
    kucuksayi = sayi2
else:
    kucuksayi = sayi1
for i in range(1 ,kucuksayi + 1):
    if (sayi1 % i == 0) and (sayi2 % i == 0):
        ebob = i
        ekok = (sayi1 * sayi2)// ebob
print(ebob)
print(ekok)        
"""


# fonksiyon ile ebob ekok bulma
"""
def ebob_bulma(sayi1 , sayi2):
    for i in range(1 , sayi1+1):
        if (sayi1 % i == 0) and (sayi2 % i == 0):
            ebob = i
           
    return ebob
def ekok_bulma(sayi1 , sayi2):
    return (sayi1 * sayi2)// ebob_bulma(sayi1 , sayi2)            

sayi1 = int(input("Küçük sayı: "))
sayi2 = int(input("Büyük sayı: "))

print("Ebob: ",ebob_bulma(sayi1,sayi2))
print("Ekok: ",ekok_bulma(sayi1,sayi2))
"""


"""
birler = ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","DOkuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Atmış","Yetmiş","Seksen","Doksan"]


def harfcevir(sayi):
    birinci = sayi % 10
    ikinci = sayi // 10
    
    return onlar[ikinci] + " " + birler[birinci] 

sayi = int(input("2 basamaklı Sayı: "))

print(harfcevir(sayi))

"""


"""
sayi1 = int(input("Sayı1: "))
sayi2 = int(input("Sayı2: ")) 

i = 1
pisagor = 0
while (sayi1 < 100) and (sayi2 < 100):
    if pisagor < 100:
        pisagor = (((sayi1**2) + (sayi2**2))**0.5)
    
    print(pisagor)
    break
else:
    print("Hatalı giriş")

for t in range(1 , 100):
    if ( pisagor % t == 0):

        print(t)
"""

"""
a = 12
b = 5
c = 0
p = 0
while (a < 100) and (b < 100):
    if (c > a) and ( c > b):
        p = ((a**2) + (b**2) == (c**2))
    a += 1
    b += 1
"""


"""
for i in range(1 , 101):
    a = ((2*i+1)**2)
    b = ((2*(i**2)) ** 2)
    c = (((2*i)**2) + (2*i) + 1)
    if (((2*i+1)**2) + ((2*(i**2)) ** 2)) == (((2*i)**2) + (2*i) + 1):

        print(c)
"""        
    
"""    
c = 1
pisagor= []
for i in range(1 ,101):
    for k in range(1 , 101):
        c = (((i ** 2) + (k **2))** 0.5)
        if ( c == int(c)):
            pisagor.append((i , k ,int(c)))
for t in pisagor:
    print(t)
"""

"""
for i in range(1 ,11):
    print("******************")
    for j in range(1 ,11):
        print(i , "x" , j , "=" , i*j)
"""


"""
sayi = int(input("Sayı: "))
for i in range(1 ,11):
    if(sayi == i):
        print("****************")
        for j in range(1 , 11):
            print(i , "x" , j , "=" , i*j)
"""


"""
def pisagor_bulma():
    
    pisagor = []
    for i in range(1 ,101):
        for j in range(1 ,101):
            c = ((i**2) + (j**2)) ** 0.5
            if ((c == int(c))):
                pisagor.append((i , j, (int(c))))
    return pisagor

for i in pisagor_bulma():
    print(i)
"""

"""
n = 1
def faktor(n):
    faktorbulduk = 1
    
    if (n >= 0):
        for i in range(1 , n+1):
            faktorbulduk *= i
        return faktorbulduk    
    else:
        print("Girdiğiniz sayı negatif bir sayıdır..")

print(faktor(n))
"""


"""
import math

x = 2
e = x**0/math.factorial(0) + x**1/math.factorial(1) + x**2/math.factorial(2) + x**3/math.factorial(3) + x**4/math.factorial(4)

print(e)
"""

