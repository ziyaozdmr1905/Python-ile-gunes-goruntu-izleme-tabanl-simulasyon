# modüller



"""
# Bu gmtime() modülü içinde bulunduğumuz zamanı her ayrıntısı ile bize söylüyor
import time

zaman = time.time()

print(time.gmtime(zaman))


#yukardaki ile aynı
import time 

zaman = time.localtime()

print(zaman)
"""



"""
import time 

zaman = time.asctime()

print((zaman))


# Bu da time modülünün asctime() ile aynı

import time 

zaman = time.ctime()

print(zaman)
"""


"""
import time 


print("Büyük cevaba son 10 saniye..")

for i in range(10 , 0 , -1):
    
    print(i)
    time.sleep(2)

print("Sayma işlemi sona erdi...")
"""



# hesap makinesi
"""
import math , time

def hesap_makinesi():
    
    print('''**********
    Toplama(+):         1
    Çıkartma(-):        2
    Çarpma(*):          3
    Bölme(/):           4
    Faktöriyel(!):      5
    Mod(%):             6
    Logaritma(log):     7
    Kuvvet alma(**):    8
    Karekök:            9
    **********''')

    while True:
        islem= input("Bir işlem belirtin: ")
        sayi1 = int(input("Bir sayı girinz: "))
        sayi2 =  int(input("Bir sayı girinz: "))
        if (islem == "1"):
            print("Hesaplanıyor...")
            time.sleep(1)
            return sayi1 + sayi2
        elif (islem == "2"):
            print("Hesaplanıyor...")
            time.sleep(1)
            return sayi1 - sayi2
        elif (islem == "3"):
            print("Hesaplanıyor...")
            time.sleep(1)
            return sayi1 * sayi2
        elif (islem == "4"):
            print("Hesaplanıyor...")
            time.sleep(1)
            return sayi1 / sayi2
        elif (islem == "5"):
            birinci = math.factorial(sayi1)
            ikinci = math.factorial(sayi2)
            print("Hesaplanıyor...")
            time.sleep(1)
            return birinci , ikinci
        elif (islem == "6"):
            birinci = math.fmod(sayi1 , sayi2)
            ikinci = math.fmod(sayi2 , sayi1)
            print("Hesaplanıyor...")
            time.sleep(1)
            return birinci , ikinci
        elif (islem == "7"):
            log = math.log(sayi1 , sayi2)
            print("Hesaplanıyor...")
            time.sleep(1)
            return log
        elif (islem == "8"):
            birinci = math.pow(sayi1)
            ikinci = math.pow(sayi2)
            print("Hesaplanıyor...")
            time.sleep(1)
            return birinci , ikinci
        elif (islem == "9"):
            birinci = math.sqrt(sayi1)
            ikinci = math.sqrt(sayi2)
            print("Hesaplanıyor...")
            time.sleep(1)
            return birinci , ikinci
        else:
            print("Hatalı giriş yapıldı..")
                
print(hesap_makinesi())
"""



# SINIFLAR

"""
class Araba():

    def __init__(self , model , renk = "Bilgi yok" , beygir_gücü = "bilgi yok" , silindir = "bilgi yok"):
        print("İnit fonksiyonu çağrıldı..")
        self.model = model
        self.renk = renk
        self.beygir_gücü = beygir_gücü
        self.silindir = silindir


araba1 = Araba(model= "BMW")

araba2 = Araba("Mazda" , "Mavi" , 90 , 4)

print(araba1.renk)
print(araba1.model)
"""



"""
class Person:
    addres = "Kocaeli"
    def __init__(self, name , surname , year , age):
        self.name = name
        self.surname = surname
        self.year = year
        self.age = age
        print("İnit çalıştı..")



a1 = Person("Ziya" , "Öz" , 1997 , 25)
a2 = Person("Musto" , "Taş" , 1998 , 24)


print(f"A1: Name: {a1.name} Surname: {a1.surname} Year: {a1.year} Age: {a1.age} Address: {a1.addres} ")

print(f"A2: Name: {a2.name} Surname: {a2.surname} Year: {a2.year} Age: {a2.age} Address: {a2.addres} ")
"""


"""
class Person:
    def __init__(self, name , surname , age, year):
        self.name = name
        self.surname = surname
        self.age = age
        self.year = year
        print("İnit çalıştı...")

a1 = Person("davut" , "öz" , 23 , 2000)
a2 = Person("ayşe","er" , 22 , 2001)

print(f"a1: name: {a1.name} surname: {a1.surname} age: {a1.age} year: {a1.year}")

print(f"a2: name: {a2.name} surname: {a2.surname} age: {a2.age} year: {a2.year}")
"""


"""
import time

class Person:
    def __init__(self, name , surname , age, year):
        self.name = name
        self.surname = surname
        self.age = age
        self.year = year
        print("İnit çalıştı...")

a1 = Person("davut" , "öz" , 23 , 2000)
a2 = Person("ayşe","er" , 22 , 2001)

time.sleep(1)
print(f"a1: name: {a1.name} surname: {a1.surname} age: {a1.age} year: {a1.year}")
time.sleep(1)
print(f"a2: name: {a2.name} surname: {a2.surname} age: {a2.age} year: {a2.year}")
"""

"""
import time
kitaplar = []
kitaplar2 = []
while 1:
    sayi = input("Sayı giriniz: ")
    if (sayi == "q"):
        print("Program sonlandı..")
        break
    if (int(sayi) % 2 == 0):
        kitaplar.append(sayi)
        time.sleep(1)
        print(f"Çift sayılar: {kitaplar}")
            
    else:
        kitaplar2.append(int(sayi))
        time.sleep(1)
        print(f"TEK SAYILAR: {kitaplar2}")
        
"""

"""
class Person:
    
    address = "Kocaeli"
    def __init__(self, kitaplar1 , kiyaplar2):
        self.kitaplar1 = kitaplar1
        self.kitaplar2 = kiyaplar2


a1 = Person("PHP" , "CSS")
a2 = Person("PYTHON" , "C++")

print(f"kitaplar1: {a1.kitaplar1} kitaplar2: {a1.kitaplar2} adres: {a1.address}")
print(f"kitapalr1: {a2.kitaplar1} kitaplar2: {a2.kitaplar2} adres: {a2.address}")
"""


#import math

#res = math.ceil(4.6)
#res = math.floor(5.7)

#import random

#res = random.random()

#res = random.random()*100

#res = random.randint(10, 100)
#res = random.uniform(10 , 100)

#names = ['ali' , 'yağmur' , 'deniz' , 'cenk']


#res = names[random.randint(0 , len(names)-1)]
#res = random.choice(names)
"""
liste = list(range(10))
random.shuffle(liste)
res = liste"""

"""
liste = range(100)
res =  random.sample(liste , 3)
"""

#import time

#res = time.time()
"""
res = time.time()
print(time.gmtime(res))
"""

#res = time.localtime()
#res = time.asctime()
#res = time.strftime
#res = time.strftime('%a')
#res = time.strftime('%B')
#res = time.strftime('%c')
#res = time.strftime('%d')
#res = time.strftime('%j')
#res = time.strftime('%m')
#res = time.strftime('%U')
#res = time.strftime('%Y')
#res = time.strftime('%y')
#res = time.strftime('%x')
#res = time.strftime('%X')

"""
res = 'ayşe'
res2 = 'ali'
print(res)
time. sleep(2)

print(res2)
"""

#import turtle


#res = turtle.forward(100)
#res = turtle.left(90)
#res = turtle.right(90)
#res = turtle.pensize(10)
#res = turtle.circle(100)

#res = turtle.backward(100)
#res = turtle.color("red" , "yellow")
#res = turtle.goto(100,200)
#res = turtle.clear()
#print(res)

"""
class Araba():
    model = 'Megane Renault'
    renk = 'Gümüş'
    beygir_gucu = 110
    silindir = 4



araba1 = Araba()
res = araba1.model
#print(res)


araba2 = Araba()

res = araba2.renk
print(res)
"""

# yazılımcı
"""
class Yazılımcı():
    def __init__(self,isim,soyisim,numara,maas,yas,diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maas = maas
        self.yas = yas
        self.diller = diller

    def bilgilerigöster(self):
        print('''
        Yazılımcı objesinşn özellikleri

        İsim : {}
        Soyisim : {}
        numara :{}
        maaş : {}
        yaş : {}
        Bildiği diller : {}
        '''.format(self.isim , self.soyisim , self.numara , self.maas , self.yas, self.diller))



    def zamyap(self , zam_miktari):
        print("Zam yapılıyor..")
        self.maas += zam_miktari
    def dil_ekle(self, yeni_dil):
        print("Dil ekleniyor...")
        self.diller.append(yeni_dil)


yazılımcı = Yazılımcı("Murat" , "Coşkun" , 123456 , 3000 , '25' , ["PHP , PYTHON , C++ , JAVA"])

yazılımcı.dil_ekle("MATLAP")
yazılımcı.zamyap(300)

yazılımcı.bilgilerigöster()

"""


"""
class Ogrenci():
    def __init__(self , adi , soyadi , numarasi, okul_No , subesi):
        self.adi = adi
        self.soyadi = soyadi
        self.numarasi = numarasi
        self.okul_No = okul_No
        self.subesi = subesi


    def ogrencibilgisi(self):
        print(f'''
        Öğrenci bilgileri 
        Adı : {self.adi}
        Soyadı : {self.soyadi}
        Numarası : {self.numarasi}
        Okul No = {self.okul_No}
        Şubesi = {self.subesi}
        ''')
    def ogrenci_Ekleme(self , yeni_Adi , yeni_soyadi , yeni_num , yeni_okulno , yeni_sube):
        print('yeni öğrenci ekleniyor..')
        self.adi.append(yeni_Adi)
        self.soyadi.append(yeni_soyadi)
        self.numarasi.append(yeni_num)
        self.okul_No.append(yeni_okulno)
        self.subesi.append(yeni_sube)


bilgi = Ogrenci(['Can'] , ['Polat'] , [123456789] , [123] , ['A'])
bilgi.ogrencibilgisi()

bilgi.ogrenci_Ekleme('Osman' , 'Kan' , 987654321 , 456 , 'B')
bilgi.ogrencibilgisi()
"""

"""
class Araba():
    def __init__(self ):
        self.ismi = input("Arabanın ismini giriniz: ")
        self.rengi = input("Arabanın rengini giriniz: ")
        self.fiyati = int(input("Arabanın fiyatını giriniz: "))
        self.beygir_gücü = input("Arabanın beygir gücünü giriniz: ")
    def bilgilerigöster(self):
        print(f'''
        Arabının bilgileri gösteriliyor..

        Araç İsmi : [{self.ismi.capitalize().strip()}]
        Araç Rengi : [{self.rengi.capitalize().strip()}]
        Araç Fiyatı : [{self.fiyati}]
        Araç Beygir Gücü : [{self.beygir_gücü}]
        ''')
    def zamEkle(self, zam_miktarı):
        self.fiyati += zam_miktarı

araba = Araba()       
araba.bilgilerigöster()

araba.zamEkle(zam_miktarı= int(input("Zam miktarı giriniz: ")))

araba.bilgilerigöster()

"""

"""
class Calisan():
    def __init__(self, isim , maas , departman):
        self.isim = isim
        self.maas = maas
        self.departman = departman
    def bigilerigöster(self):
        print('Çalışan sınıfın bilgileri..')
        print(f'''
        Adı : {self.isim}
        Maaş : {self.maas}
        Departman : {self.departman}

        ''')    
    def deparman_degis(self , yeni_departman):
        self.departman = yeni_departman
class Yönetici(Calisan):
    def zam_yap(self, zam_miktari):
        print('Zam yapılıyor..')
        self.maas += zam_miktari

yönetici = Yönetici('Mustafa Murat' , 5000 , 'Bilişim')

yönetici.bigilerigöster()
yönetici.deparman_degis('İnsan kaynakları')
yönetici.zam_yap(500)
yönetici.bigilerigöster()


"""

"""
class Calisan():
    def __init__(self, isim , maas , departman):
        self.isim = isim
        self.maas = maas
        self.departman = departman
    def bilgilerigöster(self):
        print(f'''
        **********
        Çalışan sınıfının bilgileri...

        İsim : {self.isim}
        Maaş : {self.maas}
        Departman : {self.departman}
        **********
        ''')    
    def departman_degistir(self, yeni_departman):
        self.departman = yeni_departman

class Yönetici(Calisan):
    def __init__(self, isim, maas, departman, kisi_sayisi):
        self.isim = isim
        self.maas = maas
        self.departman = departman
        self.kisi_sayisi = kisi_sayisi
    def bilgilerigöster(self):
        print(f'''
        **********
        Yönetici sınıfının bilgileri...

        İsim : {self.isim}
        Maaş : {self.maas}
        Departman : {self.departman}
        Kişi Sayısı : {self.kisi_sayisi}
        **********
        ''') 

    def zam_yap(self, zam):
        self.maas += zam


yönetici = Yönetici('Mustafa' , 4000 , 'Bilişim' , 10)

yönetici.bilgilerigöster()

yönetici.zam_yap(3000)

yönetici.bilgilerigöster()

yönetici.departman_degistir('Üretim')

yönetici.bilgilerigöster()
"""

"""
class Calisan():
    def __init__(self , isim , maas,  departman):
        print('Çalışan sınıfının init fonksiyonu..')
        
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgileriGöster(self):

        print(f'''
        **********
        Çalışan sınıfının Bilgileri gösteriliyor...

        İsim : {self.isim}
        Maaş : {self.maas}
        Departman : {self.departman}
        
        **********
        ''')    
    def yeni_Departman(self, yeni_departman):
        self.departman = yeni_departman    

class Yonetici(Calisan):
    def __init__(self, isim , maas , departman , kisi_sayisi):

        super().__init__(isim , maas , departman)

        print('Yönetici sınıfının init fonksiyonu...')
        self.kisi_sayisi = kisi_sayisi

    def bilgileriGöster(self):
        print(f'''
        **********
        Yönetici sınıfının Bilgileri gösteriliyor...

        İsim : {self.isim}
        Maaş : {self.maas}
        Departman : {self.departman}
        Kişi sayısı : {self.kisi_sayisi}
        **********
        ''')    

    def zam_yap(self, zam):
        self.maas += zam

yonetici = Yonetici('Ayşe' , 5000 , 'Tüketim' , 38)

yonetici.bilgileriGöster()

yonetici.yeni_Departman('Bilişim')

yonetici.bilgileriGöster()

yonetici.zam_yap(750)

yonetici.bilgileriGöster()
"""

"""
class Kitap():
    def __init__(self, isim , yazar , sayfa_sayisi , tur):
        print('İnit fonksiyonu')
        self.isim=isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tur = tur
    def __str__(self):
        return f'İsim : {self.isim}\nYazar : {self.yazar}\nSayfa sayısı : {self.sayfa_sayisi}\nTür : {self.tur} '
    def __len__(self):
        return self.sayfa_sayisi


kitap = Kitap('İstanbul Hatırası' , 'Ahmet Ümit' , 561 , 'Polisiye')

print(kitap)

print(len(kitap))

"""






"""
# KUMANDA YAZILIMI


import time
import random


class Kumanda():
    def __init__(self , Tv_Durum = 'KAPALI' , TV_Ses = 0 , kanal_listesi = ['TRT'] , kanal = 'TRT'):
        self.Tv_Durum = Tv_Durum
        self.TV_Ses = TV_Ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
    def TV_ac(self):
        if (self.Tv_Durum == 'AÇIK' ):
            print('Televizyon zaten açık')
        else:
            print('Televizyon açılıyor.....')
            self.Tv_Durum = 'AÇIK'
    def Tv_kapat(self):
        if(self.Tv_Durum == 'KAPALI'):
            print('Televizyon zaten kapalı..')
        else:
            print('Televizyon kapanıyor.....')
            self.Tv_Durum = 'KAPALI'    
    def ses_ayarları(self):
        while True:
            cevap = input("Sesi Azalt : '<'\nSesi Artır: '>'\nÇıkış: çıkış ")
            if (cevap == '<'):
                if (self.TV_Ses != 0):

                    self.TV_Ses -= 1
                    print('Ses: ', self.TV_Ses)
            elif (cevap == '>'):
                if(self.TV_Ses != 31):
                    
                    self.TV_Ses += 1
                    print('Ses: ', self.TV_Ses)
            elif(cevap == 'çıkış'):
                print('Ses güncellendi..' , self.TV_Ses)
                break
            else:
                print('Hatalı girdi..')        
    def kanal_ekle(self, kanal_ismi):       
        
        print('Kanal ekleniyor...')
        time.sleep(1)      
        self.kanal_listesi.append(kanal_ismi)

        print('Kanal eklendi....')
    def rastgele_kanal(self):
        rastgele = random.randint(0 , len(self.kanal_listesi) - 1) 

        self.kanal = self.kanal_listesi[rastgele]
        print('Şu anki kanal: ', self.kanal)
# buyarda özel fonksiyonlarda kullanıalbilir o yüzden onlarıda tanımlıyoruz..
    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return f"Tv durumu : {self.Tv_Durum}\nTv ses: {self.TV_Ses}\nKanal listesi: {self.kanal_listesi}\nŞuan ki kanal: {self.kanal}\n "


'''
Televiyon Uygulaması

1. Tv Aç

2. Tv Kapat

3. Ses Ayarları

4. Kanal Ekle

5. Kanal Sayısını Öğrenme

6. Rastgele Kanala Geçme

7. Telvizyon bilgileri

Çıkmak için 'q' ya basın..
'''


kumanda = Kumanda()

while True:
    islem = input("İşlem seçiniz: ")

    if(islem == 'q'):
        print('Program sonlandırlıyor..')
        break

    elif (islem == '1'):
        kumanda.TV_ac()
    elif (islem == '2'):
        kumanda.Tv_kapat()
    elif (islem == '3'):
        kumanda.ses_ayarları()
    elif ( islem == '4'):
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak girin..")
        kanal_listesi = kanal_isimleri.split(',')

        for eklenecekeler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekeler)        
    elif ( islem == '5'):
        print('Kanal sayısı: ', len(kumanda))
    elif(islem == '6'):
        kumanda.rastgele_kanal()
    elif(islem == '7'):
        print(kumanda)
    else:
        print('Geçersiz işlem.')            

"""


