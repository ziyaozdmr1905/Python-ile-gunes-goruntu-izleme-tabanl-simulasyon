# İF-ELİF-ELSE KOŞULLARI

"""
if 3>=3:
    print("hoş geldiniz")
"""
"""
name = "sadıkturan"
parola = "235"
#res = (name == "sadıkturann") and (parola == "235")
"""

"""
if (name == "sadıkturan"):
    if (parola == "235"):

    print("Hoş geldiniz")

    else:
        print("parola yanlış")
else:
    print("name yanlış")
"""

"""
if (name == "sadıkturan"):
    if (parola == "235"):
        print("hoş geldiniz")
    else:
        print("parola yanlış")
else:
    print("name yanlış")        
"""

"""
x = 20
y = 20
if x>y:
    print("x y den büyük")
elif x == y:
    print("x y eşit")
else:
    print("y x den büyük")
"""

"""
num = int(input("sayı: "))

if num>0:
    print("pozitif bir sayı")
elif num<0:
    print("negatif bir sayı")
else:
    print("sayı sıfır")
"""

#***********UYGULAMA ÖRNEK**********#

#1.SROU CEVABI
"""
name = input("İsiminiz: ")
age = int(input("Yaşınız: "))
school = input("Eğitim durumunuz: ")

res = (school == "lise") or (school == "üniversite")

if (age > 18) and res:
    print("ehliyet alabilir")
    else:
        print("ehliyet alamazsınız eğitim durumunuz yetersiz)
else:
    print("ehliyet alamazsınız yaşınız tutmuyor")    
"""

#2.SORU CEVABI
"""
yazili1 = int(input("1.yazılı: "))
yazili2 = int(input("2.yazılı: "))
sozlu = int(input("sözlü: "))
ort = ((yazili1 + yazili2 + sozlu)/3)
print(ort)

if (0 < ort <24 ):
    print("sınav ortalamanız 0")
elif (25 <= ort <= 44):
    print("sınav ortalamanız 1")
elif (45 <= ort <= 54):
    print("sınav ortalamanız 2")
elif (55 <= ort <= 69):
    print("sınav ortalamanız 3")
elif (70 <= ort <= 84):
    print("sınav ortalamanız 4")
elif (85 <= ort <= 100):
    print("sınav ortalamanız 5")
else:
    print("sınava girilmemiştir")
"""

#3.SORU CEVABI
"""
days = int(input("aracınız kaç gündür trafikte: "))

if days <= 365:
    print("1. servis aralığı")
elif days > 365 and days <= 365*2:
    print("2. servis aralığı")
elif days > 365*2 and days <= 365*3:
    print("3. servis aralığı")
else:
    print("hatalı süre")
"""

"""
import datetime

tarih = input("aracınız hangi trafikte trafiğe çıktı (2019/8/9): ")
tarih = tarih.split('/')

trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()

fark = simdi - trafigeCikis
days = fark.days

if days <= 365:
    print("1. servis aralığı")
elif days > 365 and days <= 365*2:
    print("2. servis aralığı")
elif days > 365*2 and days <= 365*3:
    print("3. servis aralığı")
else:
    print("hatalı süre")
"""




import datetime

tarih = input('aracınız hangi tarihte trafiğe çıktı (2019/8/9): ')
tarih = tarih.split('/')
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))

simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days = fark.days

if days<=365:
     print('1.servis aralığı')
elif days>365 and days<=365*2:
     print('2.servis aralığı')
elif days>365*2 and days<=365*3:
    print('3.servis aralığı')
else:
    print('hatalı süre.')







































