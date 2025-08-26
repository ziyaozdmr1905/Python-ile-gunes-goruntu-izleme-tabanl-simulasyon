
"""
name = "sadık"
surname = "turan"
print("benşm adım {} ve soyadım {}".format(name,surname))
"""
"""
name = "sadık"
surname = "turan"
age = 36

print(f"beni madım {name} {surname} ve yaşım {age}")
"""

#message = "Hello there. My name is sadık turan"
#message = message.upper()
#message = message.lower()
#message = message.title()
#message = message.capitalize()
#message = message.strip("Hle")
#message = message.split(' ')
#message = message.split()
#message = "*".join(message)
#message = message.find("m")
#message = message.startswith("H")
#message = message.endswith("n")
#message = message.replace("Hello","Hi")
#message = message.center(70)
#message = message.count("e")


#************LİSTELER***********#

#degis = "Benim adım ziya özdemir. elelktrik elektronik mühendisiyim. osmaniyede oturuyorum".split(" ")

#print(degis)
"""
list1 = [1,2,3]
list2 = [4,5,6,7]
lists = list1 + list2
print(lists)
"""
"""
userA = ["sadık", 36]
userB = ["çkınar", 2]
users = userA , userB

print(users[1][1])
"""

#list1 = ["Bmw", "Mercedes", "Opel","Mazda"]

#print(len(list1))

#print(list1[0])
#print(list1[1])
"""
list1[-1] = "Toyota"
list1[2] = "Tofaş"
list1[1] = "Nissan"
list1[0] = "Audi"
"""
"""
res = list1  
#res = "Mercedes" in list1

res = "Mazda" in list1
"""
"""
list1[-2:] = ["Toyota","Renault"]
res = list1
print(res)
"""

#res = list1 + ["Audi","Nissan"]
#del list1[-4]

#print(list1)

"""
studentA = ["Yiğit","Bilgi",2010,[70,60,70]]
studentB = ["Sena","Turan",1999,[80,80,70]]
studentC = ["Ahmet","Turan",1998,[80,70,90]]


res = studentA
res = studentB
res = studentC

res1 = f"{studentA[0]} {studentA[1]} {2022-studentA[2]} yaşında ve not ortalaması {((studentA[3][0] + studentA[3][1] + studentA[3][2])/3)}"
res2 = f"{studentB[0]} {studentB[1]} {2022-studentB[2]} yaşında ve not ortalaması {((studentB[3][0] + studentB[3][1] + studentB[3][2])/3)}"
res3 = f"{studentC[0]} {studentC[1]} {2022-studentC[2]} yaşında ve not ortalaması {((studentC[3][0] + studentC[3][1] + studentC[3][2])/3)}"

print(res1)
print(res2)
print(res3)


"""


# LİSTE METOTLARI

numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a','g','s','b','y','a','s']

#val = max(numbers)
#val = min(numbers)
#val = max(letters)
#val = min(letters)
#val = numbers[4:]

#numbers.append(49)
#numbers.insert(3,78)
#numbers.pop(2)
#numbers.remove(10)
#numbers.sort()
#numbers.reverse()
#print(numbers.count(10))
#numbers.clear()
#print(numbers)

#UYGULAMA ÖRNEK

names = ["Ali","Yağmu","Hakan","Deniz"]
years = [1998, 2000, 1998, 1987]

#names.append("cenk")
#names.insert(0,"Sena")
#names.pop(-1)
#names = names.index("Ali")
#names = names.count("Ali")
#names.reverse()
#names.sort()
#years.reverse()
#years.sort()
#ser = "Chevrolet,Dacia".split()
#araba[0] = "Chevrolet, Dacia"
#ser = min(years)
#ser = max(years)
#ser = years.count(1998)
#ser = years.index(1998)
#years.clear()
#print(years)
"""
marka = []

girilen = input("Marka: ")
marka.append(girilen)
girilen = input("Marka: ")
marka.append(girilen)
girilen = input("Marka: ")
marka.append(girilen)

print(marka)
"""

# python tuple listeleri


#list = (1,"iki",3)
#print(list)


#list = ["Ali","Veli","Kemal"]
#tuple = ("Ayşe", "Damla","Elif")

#list[:] = "Ömer"   ömer adını harflerşne ayırdı
#list = list + ["Ömer"]
#tuple[1] = "Nur"

#print(list)
#print(tuple)
"""
name = ("Ayşe","Nur","Ece") + tuple

res = name.count("Ayşe")
print(name)
print(res)
"""


# LİSTE TİPİ DİCTİONARY 
"""
sehirler = ["Kocaeli","İstanbul"]
plakar = [41,34]

print(plakar[sehirler.index("Kocaeli")])
"""

"""
plakalar = {"Kocaeli" : 41, "İstanbul": 34}
print(plakalar['İstanbul'])
"""

"""
users = {
    "sadıkturan": {
        "email" : "sadık@gmail",
        "address" : "Kocaeli",
        "age" : 36
},
    "çınarturan" : {
        "email" : "çınar@gmail",
        "address" : "Kocaeli",
        "age" : 2
    }
}

print(users["çınarturan"])
"""


# PYTHON SETS LİSTELERİ

fruits = {"Orange", "Apple", "Banana"}
#print(fruits)
"""
for x in fruits:
    print(x)
"""

#fruits.add("cherry")
#****fruits.update("cherry")**** böyle yaparsak "CHERRY" nin harflerini tek tek kendine göre ekler
#fruits.update(["Mango"])

myList = [1,1,2,2,3,1,5,4,8,7,9,5,6,5]
#res = set(myList)
#print(res)
#myList.remove(1)
 
#fruits.discard("Apple")
"""
a = ["Apple","Banana"]
b = ["Apple","Banana"]
"""
#************ATAMA OPERATÖRLERİ************#
#x , y , z = 5 , 4 , 14
#x, y = y ,x 

#x *= y 
#y *= x 
#x += z

#res = 1,2,3,5
#print(type(res))

#res = (x == y+1)
#res = (x != y)
#res = x > y
username = "ziyaozdmr"
password = "123456789"

#print(username == "ziyaozdmr")
"""
x = int(input("Sayi giriniz: "))
y = int(input("Sayi giriniz: "))

ıslem = (x > y)
print(f"x: {x} sayısı, y : {y} sayısından daha büyük mü: {ıslem}.")
"""

"""
vize1 = int(input("Vize 1 : "))
vize2 = int(input("Vize 2 : "))
final = int(input("Final: "))
ort = ((vize1 + vize2)*0.6) + (final * 0.4)
gecti = (ort >= 50)
print(ort)

print(f"Öğreninin vize1 notu: {vize1}, vize2 notu: {vize2} ve final notu: {final} olup ortlaması: {ort} şeklindedir dersten geçme dururmu: {gecti} ")

"""
"""
girilen = int(input("Sayı: "))

res = (girilen % 2 == 0)
print(f"Girilen sayı {girilen} bu sayının çift olma durumu: {res} ")

girilen = int(input("Sayı: "))

res = (girilen > 0)
print(f"Girilen sayı: {girilen} pozitif olma durumu: {res} ")
"""
"""
Email = "ziya@gmail"
parola = 123456

girilenEmail =input("Email: ")
girilenParola = int(input("Parola: "))

res = (Email == girilenEmail.lower())
res2 = (parola == girilenParola)

print(f"Email bilisi: {Email}, parola bilgisi: {parola} ve email doğru mu: {res}, parola doğru mu: {res2} ")
"""

#x = 4
#res = 4 <= x < 12

"""
hak = 0
devam= 'e'
res = (hak > 0) and (devam == 'e')
"""































