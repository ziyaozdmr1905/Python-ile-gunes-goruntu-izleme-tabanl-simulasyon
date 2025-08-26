#string tekralarıları

"""
while True:
    sor = input("Şehir giriniz. çıkmak için 'q' ya basınız..")
    if (sor == "ankara"):
        print("Plaka numarası 06 dır. Başkenttir ve soğuk kurak bir iklimi vardır..")
    elif (sor == "istanbul"):
        print("Plaka numarası 34 tür. denize kısı olan mükemmel bir şehirdir..")    
    elif (sor == "adana"):
        print("Plaka numarası 01 dir. kebabı ile ünlüdür..")
    elif(sor == "q"):
        print("Program sonlanıyooor..")
        break
    else:
        print("Yanlış girdiniz..")       
        

"""
"""
kknlr = []
kanal = input("Kanalları virgül ',' ile giriniz: ")

kanal_listesi = kanal.split(',')

for eklenecekler in kanal_listesi:
    kknlr.append(eklenecekler)
print(kknlr)    """


"""
seirler = ['kocaeli' , 'istanbul' , 'ankara' , 'izmir' , 'rize']

for sehir in seirler:
    if (len(sehir) <= 5):
        print(sehir)
"""


"""
print("Çorum , Sivas , Kayseri ile komşu olan ilimiz hangisidir?")

girilen = input("Bir il giriniz: ")

if (girilen == 'Yozgat') or (girilen == 'yozgat'):
    print("Evet cevabınız doğru..")
else:
    print("Maalesef cevap yanlış..")    """

"""
girilen = int(input("3 ile tam bölünen bir sayı giriniz: "))

if (girilen % 3 == 0):
    print("Girdiniz sayı 3 ile tam bölünen bir sayıdır..")
else:
    print("Bu sayı 3 ile bölünmez..")
"""

"""
# Bu soruyu böyle yapınca i 1,2,3,4,5 değerlerini aldı.
i = 0

while (i < 5):
    i += 1
    print(i)    
"""

"""
# Aynısını böyle yaptık bu sefer i 0,1,2,3,4 değerlerini aldı.
i = 0

while (i < 5):
    print(i)
    i += 1
"""        
    
"""
# BU defa da böyle yaptık i sadece 5 oldu..
i = 0

while (i < 5):
                  # Burada i nin 5 olamsının nedeni i sürekli arttı artık durduğu sayı yı ekrana bastı..
    i += 1
print(i)
"""


"""
girilen = ''

while girilen != 'ç':  #Burada ki mevzu, girilen ç ye eşit değil ise program devam etsin
    girilen = input("Bir sayı giriniz, Çıkmak için [ç]: ")
    if (girilen == 'ç'):
        print('Program sonlandı..')
    else:
        print("Belirttiğiniz sayını karekökü: ",(float(girilen)**0.5))
"""

"""
x = 10

if not (x == 3 or x > 9):
    print("Sayı belirtilen aralıkta..")
else:
    print("Bu sayıyı istememiştik..")    
"""

"""
x = 10

if not x == 3 or x > 9:
    print("Sayı belirtilen aralıkta..")
else:
    print("Bu sayıyı istememiştik..")    
"""


"""
i = 1
while i < 6:
    j = 1
    while j < 6:
        print(i , j , i*j*'*')
        j += 1
    i += 1    
"""
"""
ogrenci = ['dilek' , 'ismail' , 'fatih' , 'kuddisi' , 'melike']

ogrenci.extend(['selim' , 1998])

print(ogrenci)

"""
"""
ogrenci = ['dilek' , 'ismail' , 'fatih' , 'kuddisi' , 'melike']

ogrenci = ogrenci + ['bedir' , 'emel']

print(ogrenci)
"""

"""
kitapalr = [
    [45 , 'python' , 'mustafa' , 23],
    [99 , 'linux' , 'mustafa' , 26],
    [98 , 'işletim' , 'ali' , 30],
    [48 , 'php' , 'haydar' , 36]
]

while 1:
    kitapno = input('Kitap numarsı giriniz: ')
    if kitapno not in ['ç' , 'Ç']:
        for k in kitapalr:
            if (int(kitapno) == k[0]):
                print(k[1] , 'kitabın yazarı' , k[2] , 'fiyatı: ', k[3])
                break
        else:
            print(kitapno , 'nolu kitap arşivde yok..')
    else:
        break        
"""



"""# sayı tahmin oyunu

import random

sayi = random.randint(1,100)

can = int(input("Kaç hak kullanmak istersiniz: "))

hak = can

sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("Tahmin: "))
    if (sayi == tahmin):
        print(f"Tebrikler {sayac}. defa da bildiniz. Toplam puan : {100 - (100 /can) * (sayac-1)}")
    elif (sayi > tahmin):
        if (sayi - tahmin <= 10):
            print("Biraz yukarı")
        else:
            print("Yukarı")
    elif (tahmin > sayi):
        if (tahmin - sayi <= 10):
            print("Biraz aşağı")    
        else:
            print("Aşağı")
    if hak == 0:
        print(f"Hakkınız bitti, tutulan sayı {sayi}")    
        break    

"""
"""
class Araba():
    def __init__(self,renk):
        self.renk = renk
    def start(self):
        print("Araç çalıştırıldı..")
    def stop(self):
        print("Araç durduruldu..")        


a1 = Araba('sarı')


a1.start()
a1.stop()
"""


"""
class Person():
    def __init__(self , name ,year):
        self.name = name
        self.year = year
        print("İnit metodu çalıştı..")

p1 = Person('ali' , 23)

p2 = Person('yağmur' , 25)

print(f"Benim adım {p1.name} ve yaşım {p1.year}..")

print(f"Benim adım {p2.name} ve yaşım {p2.year}..")
"""


"""
class Person():
    def __init__(self, name , surname , year):
        self.name = name
        self.surname = surname
        self.year = year

        print("İnit metodu çalıştı..")
    def calcu(self):
        return 2023 - self.year    
    def bilgileri_göster(self):
        print(f"Merhaba, ismim {self.name} soysimim {self.surname} ve doğum yılım {self.calcu()} ")


p1 = Person('Ali' , 'Taş' , 1995)

p2 = Person('Yağmur' , 'Er' , 1998)

p1.bilgileri_göster()

p2.bilgileri_göster()

p1.calcu()
p2.calcu()

"""

"""
class Ogrenci():
    def __init__(self, isim , numara , yil):
        self.isim = isim
        self.numara = numara
        self.yil = yil

        print("İnit fonksiyonu çalıştı..")
    def hesap(self):
        return 2023 - self.yil   
    def bilgilerigöster(self):
        print(f"Benim; adım: {self.isim} okul numaram: {self.numara} ve yaşım {self.hesap()} ")


o1 = Ogrenci('Halil' , 456 , 1997)
o2 = Ogrenci('Ece' , 123 , 1998)


o1.bilgilerigöster()

o2.bilgilerigöster()

"""



"""
import time

class BankaYazılım():
    def __init__(self , kredi_kartı = 6000 , isim = 'Ziya', soyisim = 'Özdemir', sifre = '1234' , hesapNo = 987654321 , telNo = 5478946321 , bakiye_bilgi = 12500 ,ek_hesap= 9000):
        self.isim = isim
        self.soyisim = soyisim
        self.sifre = sifre
        self.hesapNo = hesapNo
        self.telNo = telNo
        self.bakiye_bilgi = bakiye_bilgi
        self.kredi_kartı = kredi_kartı
        self.ek_hesap = ek_hesap
    
    def para_cekme(self):
        print(f"Hesabınızda bulunan bakiye : {self.bakiye_bilgi} TL")
        time.sleep(1)
        cekilecek_miktar = int(input("Çekmek istediğiniz miktarı giriniz: "))
        if (cekilecek_miktar < self.bakiye_bilgi):
            güncel_paraa = self.bakiye_bilgi - cekilecek_miktar
            time.sleep(1)
            print(f"Hesabınızda bulunan son bakiye: {güncel_paraa} TL")
        elif (cekilecek_miktar > self.bakiye_bilgi()):
            ek_bakiye = (input("Ek hesap kullanılsın mı? Evet ise [E] , Hayır ise [H] yazın: "))
            time.sleep(1)
            if (ek_bakiye == 'E'):
                güncel_paraa = (self.ek_hesap + self.bakiye_bilgi) - cekilecek_miktar 
                self.ek_hesap = güncel_paraa
                time.sleep(1)
                print(f"Ek hesap kullanılmıştır, bakiyeniz: {self.ek_hesap} TL")
            else:
                time.sleep(1)
                print("Maalesef bakiyeniz yetersizdir.")    
    
    def para_transfer(self):
        print(f"Hesabınızda bulunan bakiye : {self.bakiye_bilgi} TL")
        transfer_edilecek_miktar = int(input("Transfer edilecek para miktarını giriniz: "))
        time.sleep(1)
        if (transfer_edilecek_miktar < self.bakiye_bilgi):
            güncel_paraa = self.bakiye_bilgi - transfer_edilecek_miktar
            time.sleep(1)
            print(f"Hesabınızda bulunan son bakiye: {güncel_paraa} TL")
        elif (transfer_edilecek_miktar > self.bakiye_bilgi):
            ek_bakiye = (input("Ek hesap kullanılsın mı? Evet ise [E] , Hayır ise [H] yazın: "))
            time.sleep(1)
            if (ek_bakiye == 'E'):
                güncel_paraa = (self.ek_hesap + self.bakiye_bilgi) - transfer_edilecek_miktar 
                self.ek_hesap = güncel_paraa
                time.sleep(1)
                print(f"Ek hesap kullanılmıştır, bakiyeniz: {self.ek_hesap} TL")
            else:
                time.sleep(1)
                print("Maalesef bakiyeniz yetersizdir.")
 
    
    def kredi_karti(self):
        print(f"Hesabınızda bulunan bakiye : {self.bakiye_bilgi} TL")
        time.sleep(1)
        print(f"Mevcut kredi kartı borcunuz {self.kredi_kartı} TL")
        borc = input("kredi kartını ödemek istiyormusunuz ? Evet ise [E] , Hayır ise [H] diyin: ")
        time.sleep(1)
        if(self.kredi_kartı < self.bakiye_bilgi):
            if(borc == 'E'):

                kalan = self.bakiye_bilgi - self.kredi_kartı   
                time.sleep(1)
                print(f"Kredi kartı borcunuz ödenmiştir. Mevcut bakiye {kalan} TL")
                self.bakiye_bilgi = kalan
                time.sleep(1)
                print(f"Mevcut bakiyeniz {self.bakiye_bilgi} TL")
            else:
                print("Kredi kartı borcunuz ödenmemiştir..")    
        elif (self.bakiye_bilgi < self.kredi_kartı):
            kullan = input("kredi kartı borcu için Ekhesap kullanılsın mı ? Evet ise [E] , Hayır ise [H] diyin: ")
            if (kullan == 'E'):
                kalan = (self.bakiye_bilgi + self.ek_hesap) - self.kredi_kartı
                time.sleep(1)
                print(f"Kredi kartı borcunuz ödenmiştir. Mevcut bakiye {kalan} TL")
                self.ek_hesap = kalan
                time.sleep(1)
                print(f"Ek hesaptaki mevcut bakiyeniz {self.ek_hesap} TL")

            else:
                print("Kredi kartı borcunuz ödenmemiştir..")

    def sifre_islemleri(self):
        i = 0
        while i < 3:
            once = input("Şifre değişrmek için, Önce mevcut şifrenizi doğrulayın.")
            time.sleep(1)
            if (self.sifre == once):
                istiyormusun = input("Şifre değiştirmek istiyor musunuz ? Evet ise [E] , Hayır ise [H] diyin")
                time.sleep(1)
                if (istiyormusun == 'E'):
                    yeni_sifre = (input("4 haneli şifre belirleyin: "))
                    time.sleep(1)
                    if (len(yeni_sifre) == len(self.sifre)):
                        time.sleep(1)
                        print("Şifreniz değiştiriliyor..")
                        time.sleep(1)
                        yeni_sifre = self.sifre
                        print(f"Mevcut şifreniz {yeni_sifre} olarak değiştirilmiştir..")
                    elif (len(yeni_sifre) <= len(self.sifre)):
                        print("Eksik rakam girdiniz.. lütfen tekrar deneyiniz.")
                    else:
                        print("Fazla rakam girdiniz. lütfen tekrard deneyiniz.")
                    
                else:
                    print("Şifreniz değiştiril memiştir..")      
            else:
                print("Şifrenizi yanlış girdiniz. Tekrar deneyiniz")   
            i += 1               

    def bakiye_ogrenme(self ):
        return self.bakiye_bilgi

    def odeme_islemleri(self, elektrik = 550 , su = 800 , meb = 250 , telefon = 300 , dogal_gaz = 1500):
        print('''
        1.Elektrik Faturası Ödemesi

        2.Su Fatura Ödemesi

        3.Meb Ödemeleri

        4.Doğal Gaz Fatua Ödemeleri 

        5.Telefon Fatura Ödemeleri
        ''')
        ode = input("Bir işlem berlitin: ")
        time.sleep(1)
        if (ode == '1'):
            onay= input("Elektrik faturası ödemesini onaylıyor musunuz? Evet ise [E] , Hayır ise [H] diyin.")
            if (onay == 'E'):
                fatura = self.bakiye_bilgi - elektrik
                time.sleep(1)
                print(f"Elektirik faturanız ödendi. mevcut bakiyeniz {fatura} TL")
            else:
                print("Faturanız ödenmemiştir..")
        
        elif (ode == '2'):
            onay= input("Su faturası ödemesini onaylıyor musunuz? Evet ise [E] , Hayır ise [H] diyin.")
            if (onay == 'E'):
                fatura = self.bakiye_bilgi - su
                time.sleep(1)
                print(f"Su faturanız ödendi. mevcut bakiyeniz {fatura} TL")
            else:
                print("Faturanız ödenmemiştir..")

        elif (ode == '3'):
            onay= input("Meb ödemesini onaylıyor musunuz? Evet ise [E] , Hayır ise [H] diyin.")
            if (onay == 'E'):
                fatura = self.bakiye_bilgi - meb
                time.sleep(1)
                print(f"Meb borcunuz ödendi. mevcut bakiyeniz {fatura} TL")
            else:
                print("Faturanız ödenmemiştir..")

        elif (ode == '4'):
            onay= input("Doğal gaz faturası ödemesini onaylıyor musunuz? Evet ise [E] , Hayır ise [H] diyin.")
            if (onay == 'E'):
                fatura = self.bakiye_bilgi - dogal_gaz
                time.sleep(1)
                print(f"Doğal gaz faturanız ödendi. mevcut bakiyeniz {fatura} TL")
            else:
                print("Faturanız ödenmemiştir..") 

        elif (ode == '5'):
            onay= input("Telefon faturası ödemesini onaylıyor musunuz? Evet ise [E] , Hayır ise [H] diyin.")
            if (onay == 'E'):
                fatura = self.bakiye_bilgi - telefon
                time.sleep(1)
                print(f"Telefon faturanız ödendi. mevcut bakiyeniz {fatura} TL")
            else:
                print("Faturanız ödenmemiştir..")    
        else:
            print("Yanlış işlem belirttiniz..")                  

    def bilgilerigöster(self):
        i = 0
        while i < 3:
            sifre = (input("Şifre giriniz: "))
            time.sleep(1)
            if (self.sifre == sifre):
                if (self.isim == 'ziya'.capitalize() or self.isim == 'ali'.capitalize() or self.isim == 'veli'.capitalize()):
                    print(f"Bankamıza Hoş geldiniz. Sayın {self.isim} bey.")
                elif (self.isim == 'yagmur'.capitalize() or self.isim == 'ayse'.capitalize() or self.isim == 'ece'.capitalize()):    
                    print(f"Bankamıza Hoş geldiniz. Sayın {self.isim} hanım.")
                time.sleep(2)
                print('''
            BİP BANKASI

            1.PARA ÇEKME

            2.PARA TRANSFERİ

            3.ŞİFRE İŞLEMLERİ

            4.ÖDEME İŞLEMLERİ

            5.BAKİYE-BİLGİ

            6.KREDİ KARTI İŞLEMLERİ
            ''')
                break
            else:
                if (len(sifre) < len(self.sifre)):
                    print("Eksik tuşlama yaptınız. Tekrar deneyin. 3 kere bilemezseniz blok olur.")
                else:
                    print("Şifre hatalı. Tekrar deneyin. 3 kere bilemezseniz blok olur.")
            i += 1
            print("Kartınız Blok olmuştur. Lütfen Müşteri hizmetleri ile iletişime geçin..")       
                


banka = BankaYazılım()
banka.bilgilerigöster()

while 1:
    islem = input("İşlem seçiniz: ")
    time.sleep(1)
    if (islem == '1'):
        banka.para_cekme()

    elif (islem == '2'):
        banka.para_transfer()

    elif (islem == '3'):
        banka.sifre_islemleri()    

    elif (islem == '4'):
        banka.odeme_islemleri()

    elif (islem == '5'):
        banka.bakiye_ogrenme()

         
"""



















