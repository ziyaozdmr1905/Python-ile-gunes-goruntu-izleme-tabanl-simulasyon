#UYGULAMA ÖRNEK#
"""
girilen = int(input("Sayı: "))
res  = (0 < girilen < 100)
print(res)
"""
"""
girilen = int(input("Sayı: "))
res = (girilen > 0) and (girilen % 2 == 0)
print(res)
"""
"""
Email = "ziya@gmail"
parola = 123456
girilenEmail =input("Email: ")
girilenParola = int(input("Parola: "))
res = (Email == girilenEmail) and (parola == girilenParola)
print(f"Email:{Email} , parola: {parola} olacaktı ve doğrulukları: {res} ")
"""
"""
x  = y = [1,2,3,4]
z = [1,2,3,4]
print(x is z)
print(x is y)
"""
"""
x = ["Apple", "Banana", "Cherry","Mango"]
print("Mango" in x)
"""

#if (3 > 3):
#    print("Hoş geldiniz")
"""
username = "ziyaözdemir"
passport = "123abc"

res = (username == "Ziyaözdemir".lower()) and (passport == "123abc")
if res:
    print("Hoş geldiniz")
"""
"""
username = "ziyaözdemir"
passport = "123abc"

res = (username == "Ziyaözdemir".lower()) 
if res:
    if ((passport == "123abc")):
        print("Hoş geldiniz")
    else:
        print("Parola yanlış")
else:
    print("Email yanlış")    
"""
"""
x = 80
y = 70
if x > y:
    print("x ' y den büyük ")
elif x == y:
    print("x y eşit")
else:
    print("y x den büyük")
"""

"""
name = input("İsim: ")
surname = input("Soyisim: ")
age = int(input("Yaş: "))
school = input("Eğitim durumu: ")


if age > 18:
    if (school == "lise") or (school == "üniversite"):
        print(f"Sayın {name} {surname} bir sikime yaramayan ehliyeti kazandınız. artık siktirip gidebilirsiniz ")
    else:
        print(f"Sayın {name} {surname} okuduğunuz okulu sikim, bir sikime yetmiyo ehliyet alamıyosunuz siktir git şimdi ")
else:
    print(f"Sayın {name} {surname} yaşınız bir sikime yetmiyo şimdi siktir git yaşını büyüt gel GÖT ")
"""

"""
name = input("İsim: ")
surname = input("Soyisim: ")
yazılı1 = float(input("1. Yazılı: "))
yazılı2 = float(input("2.Yazılı: "))
sozlu = float(input("Sözlü: "))


print(f"Sayın {name} {surname} 1.yazılı notonuz: {yazılı1}, 2.sayılı notunuz: {yazılı2} ve sözlü notunuz: {sozlu} bu şekildedir.")

ort = (yazılı1 + yazılı2 + sozlu)/3
if (0 <= ort) and (ort <= 24):
    print("Ortalamaya karşılık gelen notunuz: 0 kaldınız")
elif (25 <= ort) and (ort <= 44):
    print("Ortalamaya karşılık gelen notunuz: 1 kaldınız")
elif (45 <= ort) and (ort <= 54):
    print("Ortalamınza karşılık gelen Notunuz: 2 ")
elif (55 <= ort) and (ort <= 69):
    print("Ortalmanıza karşılık gelen notonuz: 3")
elif (70 <= ort) and (ort <= 84):
    print("Ortalamanıza karşılık gelen notunuz: 4")
elif (85 <= ort) and (ort <= 100):
    print("Ortalamaya karşılık gelen notunuz: 5")
else:
    print ("sınava girmemiş")
"""
"""
days = int(input("Araç kaç gündür trafikte: "))

if days <= 365:
    print("1.servis aralığı")
elif days > 365:
    print("2.servis aralığı")
elif days > 365:
    print("3.servis aralığı")
else:
    print("Htalı süre")
"""

#FOR DÖNGÜLERİ#
"""
numbers = [1,2,3,4,5,6]

for num in numbers:
    print(num)

names = ["çınar","sadık","sena"]

for a in names:
    print(f"my name is {a}")

name = "sadık turan"
for n in name:
    print(n)
"""


#TUBLE LİSTELERİ
"""
tuple  = [(1,2), (1,3), (3,5), (5,7)]

for t in tuple:
    print(t)


for a,b in tuple:
    print(a,b)


for a,b in tuple:
    print(a)
"""

"""
d = {"k1": 1 , "k2": 2 , "k3": 3}
for a in d:
    print(a)

for a in d.items():
    print(a)
"""
#UYGULAMA ÖRNEK 
sayilar = [1,3,5,7,9,12,19,21]

#1.soru : sayılar listesindeki hangi sayılar 3 ün katıdır.
"""
for sayi in sayilar:
    if (sayi % 3 == 0):
        print(sayi)
"""
#2.soru : sayılar listesinde ki sayıların toplamı kaçtır ? 
"""
toplam = 0
for sayi in sayilar:
    toplam += sayi
print("toplamı: ", toplam) 
"""
#3.soru
"""
for sayi in sayilar:
    if (sayi % 2 == 1):    
        print(sayi**2)
"""

sehirler = ["kocaeli","istnabul","ankara","izmir","rize"]

#4.soru
"""
for ser in sehirler:
    if (len(ser) < 7):
        print(f"en fazla 5 karakter barındıran şehirler: {ser}")
"""

urunler = [
    {'name' : 'samsung s6' ,'price' : "3000"},
    {'name' : 'samsung s7' ,'price' : "4000"},
    {'name' : 'samsung s8' ,'price' : "5000"},
    {'name' : 'samsung s9' ,'price' : "6000"},
    {'name' : 'samsung s10' ,'price' : "7000"}
]


#5.soru
"""
for urun in urunler:
    print(urun['price'])
"""
"""
toplam = 0
for urun in urunler:
    fiyat = int(urun['price'])
    toplam += fiyat
print(toplam)    
"""

#6.soru
"""
for urun in urunler:
    if (int(urun['price']) <= 5000 ):
        print(urun['name'])
"""

















