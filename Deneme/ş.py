# FONKSİYONLARDA MAP VE FİLTER METOTLARI

"""
def square(num): return num**2

result = square(2)
print(result)
"""
"""
def square(num): return num**2

numbers = [1,3,5,9]

res = list(map(square, numbers))
print(res)
"""

"""
numbers = [1,3,5,9]
def square(num): return num**2

for item in map(square , numbers):
    print(item)
"""


"""
numbers = [1,3,5,9]

res = list(map(lambda num: num**2 , numbers))

print(res)

"""

"""
numbers = [1,3,5,9]

square = lambda num: num**2
res = list(map(square , numbers))

print(res)
"""

"""
square = lambda num: num**2
res = square(4)

print(res)
"""


"""
numbers = [1,3,5,9,4,8,10,14]

def check_even(num): return num % 2 == 0
res = list(filter(check_even, numbers))

print(res)
"""


"""
numbers = [1,3,14,5,10,9,4]

res = list(filter(lambda num: num % 2 == 0, numbers))
print(res)
"""

# GLOBAL VE LOCAL DEĞİŞKENLER

"""
x = "global x"

def function():
    x = "local x"
    print(x)

function()
print(x)
"""

"""
x = "global x"

def function():
#    x = "local x"
    print(x)

function()
print(x)
"""


"""
name = "çınar"

def changeName(new_Name):
    name = new_Name
    print(name)

changeName("Ada")
print(name)
"""

"""
name = "global string"

def greeting():
    name = "Çınar"
    
    def hello():
        name = "Ada" 
        print(name)
    hello()    

greeting()
"""

"""
name = "global string"

def greeting():
    #name = "Çınar"
    
    def hello():
        print(name)
    hello()    

greeting()

"""



"""
name = "global string"

def greeting():
    global name
    name = "Çınar"
    
    def hello():
        name = "Ada" 
        print(name)
    hello()    

greeting()
print(name)  # global name durumu def fonksiyonu dışında yazılan print ifadesi için geçerli
"""

"""
x = 50
def test(x):
    print(f"x : {x}")
    x = 100
    print(f"change x to {x} ")
test(x)
"""

"""
x = 50
def test(x):
    global x # hata veriyor test(x) değişkenin içindeki x i silmemiz lazım

    print(f"x : {x}")
    x = 100
    print(f"change x to {x} ")
test(x)
print(x)
"""


"""
x = 50
def test():
    global x
    print(f"x : {x}")
    x = 100
    print(f"change x to {x} ")
test()
print(x)
"""


"""
def fonk(*cocuklar):
    print("En genç çocuk: " + cocuklar[2])

fonk("Emel","Ali","Ayşe","Ömer")
"""

"""
def fonk(cocuk0,cocuk2,cocuk1):
    print("En genç çocuk: " + cocuk0)

fonk(cocuk2 = "Yağmur", cocuk1  = "Emel", cocuk0 = "Ali")
"""

"""
def meyveler(food):
    for x in food:
        print(x)

meyveIsimleri = ["elma","armut","karpuz","muz"]
meyveler(meyveIsimleri)
"""


#faktöriyel
"""
def fonks(n):
    if n==1: return n
    else: return n*fonks(n-1)

print(fonks(4))
"""
"""
def topla(k):
    if(k > 0):
        result = k + topla(k - 1)
        print(result)
    else:
        result = 0
        return result

topla(6)        
"""
"""
users  = {
    'adı' : 'veli',
    'soyadı' : 'taşkıran',
    'yası' : 30,
    'sehir' : 'adana'
}
print(f"Öğrencinin adı: {users['adı']}\nSoyadı: {users['soyadı']}\nYaşı : {users['yası']}\nVe yaşadığı şehir: {users['sehir']}")
"""
"""
listemeyve = []
def meyve(x):
    listemeyve.append(x)

meyve('muz')
print(listemeyve)
"""

"""
girilensifre = int(input("ŞİFRENİZİ GİRİNİZ: "))


ziyahesap = {
    'sifre' : 6161 ,
    'adı' : 'ziya',
    'soyadı' : 'Özdemir',
    'yaşı' : 25,
    'kartNo' : 123456789,
    'bakiye' : 6000,
    'ekhesap' : 3000
}


sülohesap = {
    'sifre' : 3131,
    'adı' : 'Sülümen',
    'soyadı' : 'GÖTÜGÜZEL',
    'yaşı' : 26,
    'kartNo' : 987654321,
    'bakiye' : 2000,
    'ekhesap' : 1500
}


def paracek(hesap , miktar):
    print(f"Hoş geldiniz sayın {hesap['adı']}  {hesap['soyadı']}")

    if (hesap['bakiye'] >= miktar):
        print("Paranızı alabilirsiniz.")
    else:
        toplam = hesap['bakiye'] + hesap["ekhesap"]
        if (toplam >= miktar):
            ekhesapkullanimi = input("Ekhesap kullanılsın mı [evet ise: e, hayır ise: h]: ")
            
            if ekhesapkullanimi == 'e':
                print("Paranızı alabilirsiniz")
            elif ekhesapkullanimi == 'h':
                print(f"{hesap['kartNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
            else:
                print("Yanlış giriş yaptınız. lütfen tekrar deneyiniz")
        else:
            print("Üzgünüz bakiye yetersiz")        








paracek(ziyahesap , 6000 )



"""

"""

def paracek(hesap , miktar):
    print(f"Hoş mu geldiniz yoksa Yarraglara mı geldiniz bilmiyorum sayın {hesap['adı']}  {hesap['soyadı']}")
    
    if (hesap['sifre'] == girilensifre):
        
        if (hesap['bakiye'] >= miktar):
            print("En fakir sizsiniz aq, Paranızı alabilirsiniz.")
            bakiyesorgulama(hesap)
        else:
            toplam = hesap['bakiye'] + hesap["ekhesap"]
            if (toplam >= miktar):
                ekhesapkullanimi = input("Fakirlikten geberecen götveren, Ekhesap kullanılsın mı [evet ise: A, (AM) hayır ise: M]: ")
            
                if ekhesapkullanimi == 'A':
                    ekhesapkullanılacakmiktar = miktar - hesap['bakiye']
                    hesap['bakiye'] = 0
                    hesap['ekhesap'] -= ekhesapkullanılacakmiktar 
                    print("Paranızı verirken yanlışlıkla elinize vermeyelim, tabi ona para denirse Amınakoyim")
                    bakiyesorgulama(hesap)
                elif ekhesapkullanimi == 'M':
                    print(f"{hesap['kartNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Bu para göt bile siktirilmez")
                    bakiyesorgulama(hesap)
                else:
                    print("Yanlış giriş yaptınız. lütfen tekrar deneyiniz")
            else:
                print("Fakirsiniz amına goyim")
                bakiyesorgulama(hesap)
    else:
        print(f"Sikicem şimdi, şifreyi yanlış girdiniz {hesap['adı']} bey")                    


def bakiyesorgulama(hesap):
    print(f" {hesap['kartNo']} nolu hesabınız da {hesap['bakiye']} TL (yani bir sikim bulunmamaktadır) bulunmaktadır, Ek hesap limitiniz ise {hesap['ekhesap']} TL bulunmaktadır. ")




paracek(sülohesap, 3500

"""



















