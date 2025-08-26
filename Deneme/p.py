# FOR DÖNGÜSÜ (RANGE) FONKİSYONU 



#sayilar = [1,2,3,4,5]

"""
for sayi in range(5):
    print("Merhaba")

for i in range(5):
    print(i)
"""

#WHİLE DÖNGÜLERİ
"""
x = 0
while True:
    print()
"""
"""
x = 0
while x < 100:
    print(x)
    x = x + 1
print("biti...")    
"""

#x +=1 dedik çünkü x in bir arması lazım ki 100 e ulaşalım. while döngüsü içinde yazdık ki çünkü koşul 100 olması wihile içinde
"""
x = 1
while x <= 100:
    if x % 2 == 0:
        print(f"çift sayı: {x}")
    else:
        print(f"tek sayı: {x} ")
    x += 1        
print("biti...")
"""
"""
name = '' #false
while not name.strip():
    name = input('isminizi giriniz: ')
print(f'merhaba, {name}')
"""

sayilar = [1,3,5,7,9,12,19,21]

#1.SORU CEVABI
"""
while sayilar:
    print(sayilar)
"""
#2.SORU CEVABI
"""
x = 1
while x <= 21:
    if x % 2 == 1:
        print(x)
    x += 1
print("bitti...")    
"""
#3.SORU CEVABI
"""
x = 100
while 0 <= x:
    print(x)
    x -= 1
print("bitti...")
"""
#4.SORU CEVABI
"""
x0 = int(input("sayı: "))
x1 = int(input("sayı: "))
x2 = int(input("sayı: "))
x3 = int(input("sayı: "))
x4 = int(input("sayı: "))

y = [x0,x1,x2,x3,x4]

while y:
    print(y)

print("bitti...")    
"""

#5.SORU CEVABI
"""
urunler = {}
urun_sayısı = int(input("sayi giriniz: "))

name = input("Ürün ismi: ")
price = int(input("fiyat: "))

while urunler:
    urunler.update({
        'ürün ismi': name,
        'fiyat bilgisi': price
    })
price(urunler)
"""

#break ve continue ifadeleri
"""
name = 'sadık turan'

for let in name:
    print(let)
"""

"""
name = 'sadık turan'
# break ifadesi 'a' ya kadar git sonra koşulu durdur. 
for let in name:
    if let == 'a':
        break
    print(let)
"""
"""
name = 'sadık turan'
for let in name:
    if let == ' ':
        break
    print(let)
"""
"""
name = 'sadık turan'
# continue ifadesi isteidğimiz harfi es geçer ve devam eder
for let in name:
    if let == 'a':
        continue
    print(let)
"""
"""
#break ifadesi 2 olmadan koşulu sağladı va dur durdu
x = 0
while x<5:
    if x == 2:
        break
    print(x)
    x += 1

"""
"""
#continue ifadesi 2 yi es geçti ve yolunadevam etti
x = 0
while x <5:
    x += 1
    if x == 2:
        continue
    print(x)
"""    

"""
# 1-100 arası sayılarım toplamı 
x = 1
result = 0

while x < 100:
    result += x
    x += 1
print(f"toplam: {result} ")    
"""
"""
#burada çift sayıların toplamını bulduk çünkü continue ifadesi tek sayıları atma anlamıma gelen koşul oluşturduk
x = 0
result = 0

while x < 100:
    x += 1
    if x % 2 == 1:
        continue
    result += x
print(f"toplam: {result} ")    
"""
"""
x = 0
result = 0

while x < 100:
    x += 1
    if x % 2 == 0:
        continue
    result += x
print(f"toplam: {result} ")    
"""


#******DÖNGÜ METOTLARI*******#
#------------------------------------RANGE() METODU--------------------------------#
# bu metot bir liste tanımlanmasına gerek kalmadan sayı yı direk bize veriyor
# range(10) yazamak demek 0 dan 10 a kadar olan sayıları yazmak demektir
"""
for sel in range(10):
    print(sel)
"""

"""
for sel in range(50,100,10):
    print(sel)
"""

#range metonunu listelemek için kullandık bu örnekte
"""
for item in range(50,100,20):
    print(item)
print(list(range(50,100,20)))
"""

#-----------------------ENUMERATE METODU-----------------------#
# görüldüğü gibi index numarları ve harfler tek tek karşılarına yazıldı.
"""
index = 0
greaating = 'hello'

for let in greaating:
    print(f"index {index} let {let} ")
    index += 1
"""

# yine aynı sonuca ulaştım yukardaki ile
"""
greatting = "hello"

for index,letter in enumerate(greatting):
    print(f"index {index} letter: {letter} ")
"""

"""
greeting = 'hello'

for item in enumerate(greeting):
    print(item)
"""

#----------------------------ZİP() METODU------------------------------#
# sonucu liste halinde verir
"""
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']

print(list(zip(list1,list2)))
"""

"""
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500]

print(list(zip(list1,list2,list3)))
"""

#daha kısa bir yoldur for döngüsü
"""
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500]

for item in zip(list1,list2,list3):
    print(item)
"""
"""
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500]

for a,b,c in zip(list1,list2,list3):
    print(a,b)
"""

#FOR VE WHİLE DÖNGÜLERİNİN DAHA KOLAY BİR KULLANIM YOLU VAR 
""" #BU YOL UZUN OLAN
for let in range(10):
    print(let)
"""
# kısa yol şu şekilde olur
"""
numbers = [x for x in range(10)] 
print(numbers)
"""
# aynısını aşağıda yazık ama uzun olan halini
"""
numbers = []

for x in range(10):
    numbers.append(x)
print(numbers)    
"""

"""
for x in range(10):
    print(x**2)
"""

"""
numbers = [x**2 for x in range(10)]
print(numbers)
"""
#koşulu for döngüsünden sonra kullandık
"""
numbers = [x*x for x in range(10) if x % 3 == 0]
print(numbers)
"""
"""
years = [1983,1999,2008,1956,1986]
ages = [2019-year for year in years]

print(ages)
"""













