# HESAP MAKİNESİ
"""
islem = input("İşlem belirtiniz(+ = 1, - = 2, * = 3, / = 4, // = 5, % =6 ): ")

sayi1 = int(input("1.Sayi: "))

sayi2 = int(input("2.Sayi: "))

if islem == "1" :
    sonuc = (sayi1 + sayi2)
    print("Sonuç: ",str(sonuc))
elif islem == "2":
    sonuc = (sayi1 - sayi2)
    print("Sonuç: ",str(sonuc))
elif islem == "3":
    sonuc = (sayi1 * sayi2)
    print("Sonuç: ",str(sonuc))
elif (islem == "4"):
    sonuc = (sayi1 / sayi2)
    print("Sonuç: ",str(sonuc))
elif (islem == "5"):
    sonuc = (sayi1 // sayi2)
    print("Sonuç: ",str(sonuc))
elif(islem == "6"):
    sonuc = (sayi1 % sayi2)
    print("Sonuç: ",str(sonuc))
"""



#SINIF YOKLAMA
"""
a_sınıfı = ["Ahmet","Mehmet","Ayşe"]
b_sınıfı = ["Veli", "Ali", "Emel"]
isim = input("Bir isim giriniz: ")

if isim in a_sınıfı:
    print("Kişi A sınıfındadır")
elif isim in b_sınıfı:
    print("Kişi B sınıfındadır")
else:
    print("Böyle bir kişi yoktur")    
"""

# TEK ÇİFT SAYI
"""
sayi = int(input("Sayi: "))

if (sayi > 0):
    if (sayi % 2 == 0):
        print("Sayı çift bir sayıdır.")
    else:
        print("Sayı tek bir sayıdır.")
elif (sayi == 0):
    print("Sayı 0 a eşitir")
else:
    print("Sayı negatif bir sayıdır")
"""

# USERNAME-PAROLA
"""
userName = "ziya"
parola = 3346

girilenUserName = input("UserName giriniz: ")
girilenParola = int(input("Parola giriniz: "))

if (userName == girilenUserName.lower()) and (parola == girilenParola):
    print("Bilgileriniz doğru.")
else:
    print("Girilne bilgiler yanlış, tekrardan deneyiniz")    
"""

# WHİLE ÇİFT YAZDIRMA
"""
sayi = int(input("Sayı yı kaça kadar yazdırmak istiyorsanı giriniz: "))
sayici = 0
while (sayi > sayici):
    if sayici % 2 == 0:
        print(sayici)
    sayici += 1
"""

# FAKTORİYEL 
"""
sayi = int(input("Faktöriyeli alınacak sayı yı giriniz: "))

faktoriyel = 1
sayici = 1

while sayi +1 > sayici:
    faktoriyel *= sayici
    sayici += 1
print(faktoriyel)
"""

# TOPLAM
"""
sayi = int(input("Sayi: "))
toplam = 0
sayici = 1
while sayi > sayici:
    toplam += sayici
    sayici += 1
print("TOPLAM: ",(toplam))
"""


# ASAL SAYI ARALIĞI
"""
sayi = int(input("Kaça kadar asal sayıları yazdıracağınızı belirtiniz:  "))
print(2)

for i in range(3,sayi,1):
    kontrol = False
    for j in range(2,i):
        if i%j==0:
            kontrol = True
    if kontrol == False:
        print(i)        
"""


# ÇİFT SAYI YAZDIRMA ARALIĞI
"""
sayi = int(input("Çift sayıları kaça kadar yazdrımak istediğinizi belirleyin: "))
for i in range(1,sayi,1):
    if i % 2 == 0:
        print(i)
"""
"""
sayi = int(input("Çift sayıları kaça kadar yazdrımak istediğinizi belirleyin: "))
for i in range(0,sayi,2):
    print(i)
"""


# HARF RAKAM SAYICI
"""
veri = "eğitim 101"
egitim = list(veri)
harf_sayici = 0
rakam_sayici = 0

for i in egitim:
    if i.isdecimal():
        rakam_sayici += 1
    else:
        harf_sayici += 1
print("Rakam sayısı: ", rakam_sayici)            

print("Karakter sayısı: ",harf_sayici)
"""


# FAKTÖRİYEL
"""
sayi = int(input("Sayi: "))

faktoriyel = 1
for i in range(1,sayi+1,1):
    faktoriyel *= i
print(faktoriyel)    
"""


# SAYILARIN TOPLAMI
"""
sayi = int(input("Kaça kadar sayıların toplamını alacağını belirleyin: "))
toplam = 0
for i in range(1,sayi,1):
    toplam += i
print(toplam)    
"""

# ÜS ALMA
"""
sayi = int(input("ÜS: "))
taban = int(input("Taban: "))

sonuc = 1
for i in range(1,sayi+1,1):
    sonuc *= taban
print(sonuc)
"""








