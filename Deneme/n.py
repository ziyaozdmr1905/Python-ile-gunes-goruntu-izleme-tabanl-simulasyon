# FOR DÖNGÜLERİ
"""
number = [1,2,3,4,5]
for x in number:
    print(x)
"""
"""
number = [1,2,3,4,5]

for x in number:
    print("merhaba")
"""

#names = ["çınar","sadık","sena"]
"""
for a in names:
    print(f"my name is {a}")
"""
"""
for a in names:
    print(f"my name is {a}")
"""
"""
name = "sadık turan"

for x in name:
    print(x)
"""
"""
tuple = [(1,2),(1,3),(3,5),(5,7)]

for a,b in tuple:
    print(a,b)
"""
"""
tuple = [(1,2),(1,3),(3,5),(5,7)]

for a in tuple:
    print(a)
"""

"""
meyvalar = ["armut", "elma", "erik"]
for m in meyvalar:
    print(m)
"""
"""
for m in [0,1,2,3,4]:
    print(m)
"""
"""
for i in range(0, 30,3):
    print(i)
"""
#***********UYGULAMA ÖRNEK*************#

sayilar = [1,3,5,7,9,12,19,21]
# Bir döngü var diyelim mesela 15 tane öğrenci var bunların spora katılsın döngü (FOR WHİLE ) en başa kadar gelsin ama bir koşul (İF ELİF ELSE) var en kısadan uzuna doğru sıralansın 

#1.SORU CEVABI
"""
for sayi in sayilar:
    if (sayi % 3 == 0):
        print(sayi)
"""






#2.SORU CEVABI

"""
toplam = 0
for x in sayilar:
    toplam += x
print(toplam)    
"""








#3.SORU CEVABI
"""
for sayi in sayilar:
    if (sayi % 2 == 1):
        print(sayi**2)
"""







#4.SORU CEVABI
"""
sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

for sehir in sehirler:
    if (len(sehir) <= 5):
        print(sehir)
"""



urunler = [
  {'name':'samsung S6', 'price': '3000' },
  {'name':'samsung S7', 'price': '4000' },
  {'name':'samsung S8', 'price': '5000' },
  {'name':'samsung S9', 'price': '6000' },
  {'name':'samsung S10', 'price': '7000' }
]

#5.SORU CEVABI
"""
toplam = 0
for urun in urunler:
    fiyat = int(urun['price'])
    toplam += fiyat
print(toplam)    
"""



#6.SORU CEVABI
"""
for urun in urunler:
    if (int(urun['price']) <= 5000):
        print(urun['name'])
"""

























