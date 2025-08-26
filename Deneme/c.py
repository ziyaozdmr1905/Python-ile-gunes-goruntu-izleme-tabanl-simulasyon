
# name="sadık"
# surname="Turan"
# age=36

# x= "My name is " + name + " " + surname + " and \nı am " + str(age) + " years old" 


# print(x[5:15:2])
#print(len(x))
# print(x[-15:])

#x="benim adım turan çınar ve ben 36 yaşındayım"

#lenget= len(x)
#print(x[lenget-1])

#print(x[2:5])

#string formatlama
"""
name="çınar"
surname="Turan"
age=36
job="mühendis"
"""
#print("My name is {} {}".format(name, surname))
#print("My name is {0} {1}".format(name, surname))
#print("My name is {1} {0}".format(name, surname))
#print("My name is {s} {n}".format(n=name, s=surname))
#print("My name is {} {} and ı am {} years old".format(name, surname, age))
#print("My name is {} {} and ı am {} years old".format(name, name, name))

#result= 200/700
#print("the result is {}".format(result))
#print("the result is {r:10.3}".format(r=result))
#print("the result is {r:5.5}".format(r=result))

#f stringi önemli çünkü uzun dğil veçok iyi bir metot#

#print(f"My name is {name} {surname} and ı'm {age} years old")

website= "http://www.sadikturan.com"
course="python kursu: Baştan sona python programlama rehberiniz (40 saat)"

#1    print(len(course))
#2    print(website[7:10])
#3    print(website[-3:])
#4    print(course[:15])
#4-2  print(course[-15:])
#5    print(course[::-1])    tersten yazdırma
#6    print(f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}")
#7    print("Hello World".replace("W", "w"))  replace isteğimiz harfi değiştiriyoruz
#8    print("abc"*3)

#------STRİNG METOTLARI-----#

message="Hello There. My name is sadık Turan"


""""
UPPER METODU BÜTÜN HRFLERİ BÜYÜK YAPAR
message="Hello There. My name is sadık Turan"
message=message.upper()
print(message)
"""
"""
CASEFOLD METODU LAWER METODU İLE AYNIDIR BÜTÜN HARFİ KÜÇÜK YAPAR
message=message.casefold()
message=message.lower()
print(message)
"""
"""
BU METOT KELİMELRİN BAŞ HERFİNİ BÜYÜK YAZAR
message=message.title()
print(message)
"""
"""
SADECE CÜMLENİN EN BAŞINDAKİNİ BÜYÜK YAPAR
message=message.capitalize()
print(message)
"""

"""
CÜLENİN BAŞINDA YADA SONUN DA BOŞLUK VARSA SİLER
message=message.strip()
print(message)
"""

"""
CÜMLEYİ LİSTELER HALİNE GETİRİF
message=message.split()
print(message)
"""
"""
CÜMLEYİ 2 YE BÖLDÜ VE LİSTELEDİ
message=message.split(".")
print(message)
"""
"""
BU METOTLA KELİMELERİN ARASINA İSTEDİĞİMİZ ŞEYLERİ KOYARIZ
message=message.split()
print(message)
message="*".join(message)
print(message)

message=message.split()
message="----".join(message)
print(message)
"""
"""
BU METOT KELİMENİN CÜMLE İÇİNDE OLUP OLMADIĞINI BELİRLİYOR
index=message.find("sadık")
print(index)

index=message.find("sadıkk")
print(index)
"""
"""
BU METOT CÜMLE HANGİ HARF İLE BAŞLAIYORSA ONU DOĞRULAR YADA YANLIŞ CEABINI VERİR
x=message.startswith("H")
print(x)
"""
"""
BU METOT DA HNAGİ HARF İLE BİTİYORSA    
x=message.endswith("n")
print(x)
"""
"""
BU METOT CÜMLE İÇİNDEN HARF YADA KELİME Yİ DEĞİŞTİRMEY YARIYOR
message=message.replace("sadık", "ziya")
print(message)
"""
"""
BU METOT CÜMLENİN SAĞINDA VE SOLUNDA BOŞLUK BIRAKIR
message=message.center(55)
print(message)
"""
"""
BU METOT CÜMLE İÇİNDE KELİMENİN KAÇ DEFA GEÇTİĞİNİ SÖYLER
x=message.count("name")
print(x)
"""

"""
BU METOT KELMENİN KAÇINCI İNDEXTE OLDUNUĞU BİZE SÖYLER
message=message.index("name")
print(message)
"""
"""
BU METOT SADECE KELİMELERDEN OLUŞUYORSA TRUE DEĞERİ DÖNDERİR
x="bizimevinönüyasmaa"
y="bok mu var"
#z=y.isalpha()
#z=x.isalpha()
print(z)
"""
"""
BU METOT SADECE SAYI DEĞERİ DÖNDÜRÜR
x="12334555"
z=x.isdigit()
print(z)
"""
"""
BU METOT TÜM HARFLER KÜÇÜKSE TRUE DEĞERİNİ DÖNDÜRÜR
x="sadfghtybnmges"
z=x.islower()
print(z)
"""
"""
BU METOT CÜMLENİN BÜYÜK HARFLE BAŞLARSA TRUE DEĞERİ DÖNDÜRÜR
x=input("Bir şifre giriniz ve büyük harfle başmasına dikkat ediniz: ")
x=x.istitle()
print(x)
"""
"""
BU METOT İLGİLİ KELİMEYİ SEÇER VER ÖCEKİ SONRAKİ KISMI LİSTE HALİNDE 3 E BÖLER
x=message.partition("name")
print(x)
"""

