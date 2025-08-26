"""#stirng metotları

class Sorular():
    def __init__(self, soru , secenekler , cevap):
        self.soru = soru
        self.secenekler = secenekler
        self.cevap = cevap
    def girilen_cevap(self, cevap):
        return self.cevap == cevap

class Quiz:
    def __init__(self, sorular):
        self.sorular = sorular
        self.skor = 0
        self.soru_index = 0

    
    def soru_yeri(self):
        return self.sorular[self.soru_index]

    def ekran_sorusu(self):
        text = self.soru_yeri()
        print(f"soru {self.soru_index + 1} : {self.text}")

        for q in text.secimler:
            print('-' + q)

        cevap = input('cevap: ')
        self.tahmin(cevap)
        self.soruyukle()
    def tahmin(self, cevap):
        text = self.soru_yeri()
        if text.girilen_cevap(cevap):
            self.skor += 1
        self.soru_index += 1  



s1 = Sorular('En iyi programlama dili hangisidir ?' , ['PHP' , 'CSS' , 'PYTHON' , 'MATLAP' , 'C++'] , 'PYTHON')

print(s1.girilen_cevap('PYTHON'))

"""


# en eskiler tekraraalr stringler




mes  = 'Sting bir ifade yazılırken çift tırnak arasına yada tek tırnaklar arasına yazılabilir.'


# print(mes.capitalize())
# print(mes.casefold())
# print(mes.center(100 , '*'))
# print(mes.count('s'))
# print(mes.upper())
# print(mes.lower())
# print(mes.title())
# print(mes.strip("r."))
# print(mes.split())
# print('*'.join(mes))
# print(mes.join("--"))
# print(mes.find('a'))
# print(mes.index('s'))
# print(mes.replace('a','e'))
# print(mes.count('e'))
# print(mes.partition('tırnak'))

# for i in mes.partition('tırnak'):
#     print(i)


# for i in mes.split():
#     print(i)

# LİSTELER

num = [1,2,6,89]

#er = min(num)
#er = max(num)


"""
num.insert(2,4)
# eğer for i in num.insert(2,4) deseydim none type hatası geliyor
for i in num:
    print(i)
"""


# python tuple listeleri

# llis = [1,2,3]



# print(llis)

# bu = (12,5,6,8,'ali')


# print(bu.index(8))

# al = (1,2,3,4,5)

# beni = (6,7,8,9)

# print(al + beni)



# sehirler = ['kocaeli' , 'istabul']
# plkalr = [41 , 34]

# print(plkalr[sehirler.index('kocaeli')])


# ev = ['eren' , 'atem' , 'tel']

# nu = [1 , 2 , 6]

# print(nu[ev.index('tel')])


#        plakar = {'key': 'value'}



# plakalr = {'kocaeli': 41 , 'istanbul' : 34}

# print(plakalr['istanbul'])

"""
bilgi = {
    'cinar': {
        'age': 12,
        'address': 'Kocaeli',
        'roles': ['admin', 'user'],
        'phone': 123456789
    }

}"""

#print(bilgi['cinar']['age'])

# for i in (bilgi['cinar']['roles']):
#     print(i)





#fruit = {'elma' , 'armut' , 'muz', 'elma','elma'}

#fruit.add('portakal')
#fruit.clear()
#fruit.update(['portakal' , 'erik'])


#fruit.difference()


# ar = 'erik' , 'elma'

# for i in ar:
#     print(i)


# print(ar)


# x , y , z = 1 , 2 , 3

# print(x , y , z)

# val = 1 , 2, 3,  (4, 5, 6)

# x ,y , *z = val

# for i in z:
#     print(i)

#print(x ,y ,z )

"""
er = ('armetur geldi işte')

print('a' not in er)

"""

# tup = ([1,2] , [3,4])

# for x,y in tup:
#     print(x,y)



# tup = [(1,2,3) , (4,5,6)]

# for x,y,z in tup:
#     print(x,y , z)

"""
tup = {
    'a': 1,
    'b': 2,
    'c': 3
}


for i,t in tup.items():
    print(t)

"""


"""
ay = int(input('Ay giriniz: '))

gun = int(input('gün giriniz: '))


burc = {
    'akrep': (24 , 10 , 22 , 11), 
    'yay': (23 , 11 , 21 , 12)

}


for burc,(baslangic_gun , ilk_ay , sonraki_gun , son_ay) in burc.items():
    if (gun >= baslangic_gun  and ay == ilk_ay) or (gun <= sonraki_gun and ay == son_ay):
        print(burc)


"""

"""
#kelime =  input('kelime girin: ')
sozluk = {
    'compiter': 'bilgisayar',
    'driver': 'sürücü', 
    'memory': 'hafıza',
    'output': 'çıktı',
    'software': 'yazılım',
    'printer': 'yazıcı'

}


print(sozluk.keys())
print(sozluk.values())
print(sozluk.items())
#print(sozluk.get(kelime, 'aradığınız kelime yok.'))
#sozluk.clear()
#del sozluk
sozluk.pop('driver')
print(sozluk)
sozluk.popitem()
print(sozluk)
print(sozluk.setdefault('city'  ,'şehir'))
#sozluk.update()
print(sozluk)

"""


"""
ay = int(input('Ay giriniz: '))

gun = int(input('gün giriniz: '))


burc = {
    'Oğlak':      (22 , 12 , 20 , 1),
    'Kova':       (21 , 1 , 19 , 2),
    'Balık':      (20 , 2 , 20 , 3),
    'Koç':        (21 , 3 ,  20 , 4),
    'Boğa':       (21 , 4 , 20 , 5),
    'İkizler':    (21 , 5 , 21 , 6),
    'Yengeç':     (22 , 6 , 22 , 7),
    'Aslan':      (23 , 7 , 23 , 8),
    'Başak':      (24 , 8 , 23 , 9),
    'Terazi':     (24 , 9 , 23 , 10),
    'Akrep':      (24 , 10 , 22 , 11), 
    'Yay':        (23 , 11 , 21 , 12)

}


for burc,(baslangic_gun , ilk_ay , sonraki_gun , son_ay) in burc.items():
    if (gun >= baslangic_gun  and ay == ilk_ay) or (gun <= sonraki_gun and ay == son_ay):
        print(f'Burcunuz: {burc} ')
   


"""
"""
yas = int(input("Yaşınızı giriş: "))
isim = input("isim giriniz: ")
ücret = int(input("Paranız: "))


if (5 < yas <= 18):
    print('Bilet alabilirsiniz')
    if ücret > 10:
        print('''
        1- Kondol = 13 TL
        2- çarpışan araba = 15 TL
        3- korku treni = 10 TL
        4- adranalin = 15 TL
        ''')
        park = {
            1 : ('Kondol', 13 ), 
            2 : ('Çarpışan Araba', 15) ,
            3 : ('Korku Tüneli', 10),
            4 : ('Adranalin' , 15) 
        }
        alet = int(input("Alet seçin: "))

        if alet == 1:

            print(f'''
            **Luna park bileti**

            isim : {isim}
            yaş : {yas}
            alet : {park[1][0]}
            kalan : {ücret- park[1][1]}
            ''')
        elif (alet == 2):
            print(f'''
            Luna park bileti
            isim : {isim}
            yaş : {yas}
            alet: {park[2][0]}
            kalan : {ücret- park[2][1]}
            ''')

        elif (alet == 3):
            print(f'''
            Luna park bileti
            isim : {isim}
            yaş : {yas}
            alet: {park[3][0]}
            kalan : {ücret- park[3][1]}
            ''')
        elif (alet == 4):
            print(f'''
            Luna park bileti
            isim : {isim}
            yaş : {yas}
            alet: {park[4][0]}
            kalan : {ücret- park[4][1]}
            ''')
        else:
            print('Hatalı giriş..')           

    else:
        print("Maalesef ücret yetersiz..")
else:
    print("Yaşınız tutmamaktadır..")
"""




"""
print('''
Şimdi sıcaklık birim dönüşümleri için

1 - Celsius - Fahrenheit      Fahrenheit bulma

2 - Fahrenheit - Celsius      Celsius bulma

3 - Celsius - Kelvin          Kelvin bulma

4 - Kelvin - Celsius          Celsius bulma

''')


islem = input('İşlem seçin: ')
derece = float(input('Derece girini: '))

if (islem == '1'):
    F =  (derece * 1.8 ) + 32
    print('Fahrenheit: ',F)
elif (islem == '2'):
    C = (derece - 32) / 1.8
    print('Celsius: ',C)
elif (islem == '3'):
    K = derece + 273.15
    print('Kelvin: ',K)
elif (islem == '4'):
    C = (derece - 273.15)
    print('Celsius: ',C)
else:
    print('Yanlış girdi..')            
"""

"""
urunler = [
    {'name' : 'samsung s6' , 'price' : 5000},
    {'name' : 'samsung s7' , 'price' : 6000},
    {'name' : 'samsung s8' , 'price' : 7000},
    {'name' : 'samsung s9' , 'price' : 8000}
]


mevcut = int(input('Mevcut param: '))

#if int(urunler['price']) <= mevcut:
for urun in urunler:
    if (int(urun['price']) <= mevcut):
        print(urun['name'])


"""

# while döngüsü
"""
sayilar = [1,2,5,7,9]

i = -1

while i < len(sayilar):
    print(sayilar[i])
    i += 1

"""
"""
baslangic = int(input("Sayi: "))
bitis = int(input("Bitiş: "))

i = baslangic
while i < bitis:
    i += 1
    if (i % 2 == 1):
        print(i)

"""
"""
i = 100

while i > 0:
    i -= 1
    
    if (i % 2 == 0):
        print(i)
"""

"""    
num = []
sayac = 1
while sayac < 6:
    sayi = int(input(f"{sayac}.Sayı: "))
    num.append(sayi)
    sayac += 1
num.sort()    
print(num)
"""

"""urunler = []
adet = int(input('Kaç ürün eklemek istiyorsunuz: '))
i = 0

while (i < adet):
    name = input("Ürün ismi: ")
    price = input("Ürün fiyatı: ")
    urunler.append(
        {
            'name': name,
            'price': price
        }
    )

    i += 1
for urun in urunler:
    print(f"ürün adı: {urun['name']} ürün fiyatı: {urun['price']}")    
"""

# enumarete metodu



#bu öğrneğin uzun hali birde motodunu kullnalım
"""
index = 0

gre = 'hello'

for let in gre:
    print(f"index : {gre}  let : {let} ")
    index += 1
"""

"""
gre = 'hello'

for index , let in enumerate(gre):
    print(index , let)

"""

# zip metodu

"""
liste1 = [1,2,3,4,5]

liste2 = ['a' , 'b' , 'c' , 'd' , 'e']

print(list(zip(liste1, liste2)))
"""


liste1 = [1,2,3,4,5]

liste2 = ['a' , 'b' , 'c' , 'd' , 'e']

liste3 = [100 , 200 , 300 , 400, 500]

print(list(zip(liste1 , liste2 , liste3)))





















