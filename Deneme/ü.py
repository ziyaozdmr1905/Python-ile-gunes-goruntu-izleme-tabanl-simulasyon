"""class Kitap():
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
    def __new__(self):
        return 



kitap = Kitap('İstanbul Hatırası' , 'Ahmet Ümit' , 561 , 'Polisiye')"""





class X():
    def __init__(self ,x):
        self.x = x

    def __repr__(self):
        return self.x

test = X("Hello")

print(test)



"""
class Araba():
    def __init__(self, x , y):
        self.x = x
        self.y = y
    def __ne__(self):
        return self.x + self.y
   
a = Araba(2,3)

#print(a.__dict__)"""



"""
class kisi():
    kisi_sayisi = 0
    def __init__(self, isim , yas):
        self.isim = isim
        self.yas = yas

        kisi.kisi_sayisi += 1
    
    @classmethod
    def kisi_sayisini_soyle(cls):
        return cls.kisi_sayisi

    @classmethod
    def string_ile_olustur(cls, str_):
        isim,yas = str_.split("-")
        return cls(isim , yas)



kisi1 = kisi("Ali" , 20)

kisi2 = kisi("Veli" , 23)

kisi3 = kisi.string_ile_olustur("Ayşe-25")

print(kisi3.isim)

print(kisi.kisi_sayisini_soyle())

"""

"""
class Calisan:
    zam_oranı = 1.1

    def __init__(self, isim , soyisim, maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim + soyisim + "@sirket.com"
    
    def bilgileri_göster(self):
        return f"Ad: {self.isim} Soyad: {self.soyisim} Maaş: {self.maas} Email: {self.email} "




calisan1 = Calisan("Ali","Çalışkan" , 5000)

calisan2 = Calisan("Ayşe","Kan" , 7000)


# print(calisan1.bilgileri_göster())
# print(calisan2.bilgileri_göster())


class Yazilimci(Calisan):
    zam_oranı = 1.2
    def __init__(self, isim , soyisim , maas , bildigi_dil):
        super().__init__(isim , soyisim , maas)
        self.bildigi_dil = bildigi_dil
    def bilgileri_goster(self):
        return f"Ad: {self.isim} Soyad: {self.soyisim} Maaş: {self.maas} Email: {self.email} Dil: {self.bildigi_dil} "

    def dilini_soyle(self):
        return f"Bildiğim dil: {self.bildigi_dil}"

class Yonetici(Calisan):

    def __init__(self , isim , soyisim , maas , calisanlar = None):
        super().__init__(isim , soyisim , maas)
        if (calisanlar == None):
            self.calisanlar = []
        else:
            self.calisanlar = calisanlar

    def calisan_ekle(self , calisan):
        if calisan not in self.calisanlar:
            self.calisanlar.append(calisan)

    def calisan_sil(self, calisan):
        if calisan in self.calisanlar:
            self.calisanlar.remove(calisan)

    def calisanlari_goster(self):
        for calisan in self.calisanlar:
            print(calisan.bilgileri_göster())


yazilimci1 = Yazilimci("Sıla" , "Yıldız" , 8000 , "Python")

yazilimci2 = Yazilimci("Fatma" , "Ay" , 9000 , "Java")


yonetici1 = Yonetici("Metin" , "Ali" , 10000)

yonetici1.calisan_ekle(calisan1)

yonetici1.calisan_ekle(yazilimci1)

yonetici1.calisanlari_goster()

print("**************")
yonetici1.calisan_sil(calisan1)

yonetici1.calisanlari_goster()

"""

"""
class Futbolcu():

    def __init__(self, isim , soyisim , yas):
        self.isim = isim
        self.soyism = soyisim
        self.yas = yas

    def __str__(self):
        return f'Ad: {self.isim}  Soyad: {self.soyism} ve yaş: {self.yas}'
    
    def __lt__(self, x ,y):   # Bu operatör metotları yani demektir ki : x < y eğer doğru ise true çıkar ek.çık
        return x.__lt__(y)    # print(f1.__lt__(2,3)) ekran çıktısı için kullanım böyle
    def __le__(self, x , y):  # x <= y demektir
        return x.__le__(y)  
    def __eq__(self, x ,y):   # x == y demektir
        return x.__eq__(y)
    def __ne__(self,x,y):     # x != y demektir
        return x.__ne__(y)
    def __gt__(self, x, y):   # x > y demektir
        return x.__gt__(y)
    def __ge__(self, x, y):   # x >= y demektir
        return x.__ge__(y)
    def __bytes__(self):
        return f'{self.isim}'
    


f1 = Futbolcu("ALİ" , "Dal" , 32)

print(f1.__lt__(2,3))

print(f1.__le__(2,3))

print(f1.__eq__(2,3))

print(f1.__ne__(2,3))

print(f1.__gt__(2,3))

print(f1.__ge__(2,3))

print(f1.__bytes__())
"""


"""
#Kumanda

import time
import random


class Kumanda():
    def __init__(self , Tv_Durum = 'KAPALI' , TV_Ses = 0 , kanal_listesi = ['TRT'] , kanal = 'TRT', Bluetooth_baglantisi = 'KAPALI', Wifi = 'KAPALI'):
        self.Tv_Durum = Tv_Durum
        self.TV_Ses = TV_Ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
        self.Bluetooth_baglantisi = Bluetooth_baglantisi
        self.wifi = Wifi
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
    def bluetooth_ac(self):
        if (self.Bluetooth_baglantisi == 'AÇIK'):
            print("Bluetooth zaten açık..")
        else:
            print("Bluetooth açılıyor..")
            self.Bluetooth_baglantisi = 'AÇIK'    
    def bluetooth_kapat(self):
        if (self.Bluetooth_baglantisi == 'KAPALI'):
            print("Bluetooth bağlantısı zaten kapalı..")
        else:
            print("Bluetooth bağlantısı kapanıyor..")
            self.Bluetooth_baglantisi = 'KAPALI'            

    def wifi_ac(self):
        if (self.wifi == 'AÇIK'):
            print("Wifi zaten açık..")
        else:
            print("Wifi açılıyor..")
            self.wifi = 'AÇIK'        
    def wifi_kapat(self):
        if (self.wifi == 'KAPALI'):
            print('Wifi zaten kapalı..')
        else:
            print("Wifi kaoanıyor..")
            self.wifi = 'KAPALI'    
    def kanal_sil(self):
        knalsil = input("Silmek isteiğiniz kanalı yazın: ")
        self.kanal_listesi.remove(knalsil)
        print ("kanal siliniyor..")
        time.sleep(2)
        print(self.kanal_listesi)



'''
Televiyon Uygulaması

1. Tv Aç

2. Tv Kapat

3. Ses Ayarları

4. Kanal Ekle

5. Kanal Sayısını Öğrenme

6. Rastgele Kanala Geçme

7. Telvizyon bilgileri

8.Wifi aç

9.Wifi Kapat

10.Bluetooth Aç

11.Bluetooth Kapat

12.Kanal Sil

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
    elif (islem == '8'):
        kumanda.wifi_ac()
    elif (islem == '9'):
        kumanda.wifi_kapat()
    elif (islem == '10'):
        kumanda.bluetooth_ac()
    elif (islem == '11'):
        kumanda.bluetooth_kapat()
    elif(islem == '12'):
        kumanda.kanal_sil()
    else:
        print('Geçersiz işlem.')            

"""



# bilgisayar sınıfı 

"""
import pygame
import time


from pygame import mixer
mixer.init()
mixer.music.load('D:\ZİYA\MÜZİK\yirmi7 - Sokak Lambası (Official Video).mp3') # örnek: C:/Deneme.mp3
mixer.music.play()
time.sleep(60)"""


"""
# bu daha güzel çaldırıyor müziği
from playsound import playsound
playsound("D:\ZİYA\MÜZİK\yirmi7 - Sokak Lambası (Official Video).mp3")
"""



"""
from playsound import playsound

import time


class Bilgisayar():

    def __init__(self, bilgisayar_durum = 'KAPALI', bilgisayar_ses = 0 , bilgisayar_ekran_parlak = 0 , bilgisayar_program = ["PYTHON"]  , bilgisayar_sifre = 'abc123' ):
        self.bilgisayar_durum = bilgisayar_durum
        self.bilsayar_ses = bilgisayar_ses
        self.bilsayar_ekran_parlak = bilgisayar_ekran_parlak
        self.bilsayar_program = bilgisayar_program
        self.bilsayar_sifre = bilgisayar_sifre
    
    def bilgisayar_ac(self):
        if (self.bilgisayar_durum == 'AÇIK'):
            print("Bilgisayar zaten açık..") 
        else:
            print("Bilgisayar açılıyor..")
            time.sleep(2)
            i = 0
            while i < 3:
                girilen_sifre = input("Kullanıcı parola: ")
                
                if (self.bilsayar_sifre == girilen_sifre.lower()):
                    time.sleep(3)
                    print("Parola doğru bilgisayar açılıyoor...")
                    self.bilgisayar_durum = 'AÇIK'
                    break
                else:
                    if (i < 2):
                        print("Parola yanlış.Toplam 3 hakkınız vardı. Tekrar deneyin..")    
                    else:
                        print("Parola yanlış. Hakknız bitti. Bilgisayar kitlendi.")
                i += 1
            time.sleep(2)
            
    
    def bilgisayar_kapat(self):
        if (self.bilgisayar_durum == 'KAPALI'):
            print("Bilgisayar zaten kapalı..")
        else:
            time.sleep(2)
            print("Bilgisayar kapanıyor..")                   
            self.bilgisayar_durum = 'KAPALI'
    
    def bilgisaray_sesacma(self):
        while True:
            cevap = input("Sesi Azalt : '<'\nSesi Artır: '>'\nÇıkış: çıkış : ")
            if (cevap == '<'):
                if (self.bilsayar_ses != 100):
                    self.bilsayar_ses += 1
                    time.sleep(2)
                    print('Ses seviyesi: ',self.bilsayar_ses)
            elif (cevap == '>'):
                if (self.bilsayar_ses != 0):
                    self.bilsayar_ses -= 1 
                    time.sleep(2)
                    print('Ses seviyesi: ', self.bilsayar_ses)
            elif(cevap == 'çıkış'):
                time.sleep(2)
                print('Ses güncellendi..' , self.bilsayar_ses)
                break
            else:
                print('Hatalı girdi..')     
   
    def ekran_parlakligi(self):
        while True:
            cevap = input("Ekran parlaklığını Azaltır : '<'\nEkran parlaklığını Artır: '>'\nÇıkış: çıkış : ").lower()
            if (cevap == '<'):
                if (self.bilsayar_ekran_parlak != 100):
                    self.bilsayar_ekran_parlak += 1
                    time.sleep(2)
                    print('Ekran parlaklık: ',self.bilsayar_ekran_parlak)
            elif (cevap == '>'):
                if (self.bilsayar_ekran_parlak != 0):
                    self.bilsayar_ekran_parlak -= 1 
                    time.sleep(2)
                    print('Ekran parlaklık seviyesi: ', self.bilsayar_ekran_parlak)
            elif(cevap == 'çıkış'):
                time.sleep(2)
                print('Ekran parlaklığı güncellendi..' , self.bilsayar_ekran_parlak)
                break
            else:
                print('Hatalı girdi..')     
    def pragram(self):
        while True:
            yukle = input("Bilgisaysara pragram yükle, çıkış için 'q' basın: ")
            if (yukle == 'q'):
                break
            else:
                print("Program ekleniyor..")
                time.sleep(1)
                self.bilsayar_program.append(yukle)
                print("Program yüklendi..")
                time.sleep(1)
                print(self.bilsayar_program)
    def sifre(self):
        i = 0
        while i < 3:
            girilen_sifre = input("Kullanıcı parola: ")
            
            if (self.bilsayar_sifre == girilen_sifre):
                time.sleep(3)
                print("Parola doğru bilgisayar açılıyoor...")
                break
            else:
                print("Parola yanlış.Toplam 3 hakkınız vardı. Tekrar deneyin..")    
            i += 1
        time.sleep(2)
        print("Maalesef bilemediniz, bilgisayar kitlendi")
    def sifre_degistir(self):
        evetmi = input("Şifre değiştirmek istiyorsanız 'E' istemiyorsanız 'A' tıklayın: " )
        if (evetmi == 'E'):
            i = 0 
            while i < 3:
                eski_sifre = input("Şuan ki şifrenizi giriniz: ")
                if (self.bilsayar_sifre == eski_sifre.lower()):
                    yeni_sifre = input("Yeni bir şifre belirleyin..").lower()
                    print("Şifre değiştiriliyor..")
                    time.sleep(2)
                    self.bilsayar_sifre = yeni_sifre
                    break
                else:
                    print("Yanlış girildi tekrar deneyin..")    
                i += 1    

    def muzik(self):
        print('''
        Sülo'nun playist listesi

        1.Sokak lambası1
        2.Adını sen koy
        3.Sen leyla ben mecnun
        4.Ah yar
        5.Gel bahtımın kar beyazı

        ''')
        islem = input("Müzik açmak için listeden sayı seçin: ")
        if (islem == '1'):
            playsound("D:\ZİYA\MÜZİK\yirmi7 - Sokak Lambası (Official Video).mp3")
        elif (islem == '2'):
            playsound("D:\ZİYA\MÜZİK\Yeni mp3\Adını Sen Koy (Müslüm Gürses) Official Audio - adınısenkoy - müslümgürses - Esen Müzik ( 256kbps cbr ).mp3")
        elif (islem == '3'):
            playsound("D:\ZİYA\MÜZİK\Yeni yeni müz\wasık kedi aşık ım aşık sen leyla ben mecnun seviyorum brsyld.mp3")
        elif (islem == '4'):
            playsound("D:\ZİYA\MÜZİK\Mmpp33\Ah Yar.mp3")
        elif (islem == '5'):
            playsound("D:\ZİYA\MÜZİK\Yepisyeniler\Müslüm Gürses - Gel Bahtımın Kar Beyazı - 2017 Remastered Versiyon ( 256kbps cbr ).mp3")

    def __str__(self):
        return f"Bilgisayar şifre: {self.bilsayar_sifre}\nBilgisayar Ses Düzeyi: {self.bilsayar_ses}\nBilgisayar Ekran Parlaklığı: {self.bilsayar_ekran_parlak}\nBilgisayar Proğram Listesi: {self.bilsayar_program}"
    def __len__(self):
        return len(self.bilsayar_program)

    def yeniden_baslat(self):
        sor = input("Bilgisayar yeniden başlatılsın mı ? (E/e) evet / (H/h) hayır : ")
        if(sor == 'E') or (sor == 'e'):
            bil.bilgisayar_kapat()
            time.sleep(10)
            print("Yeniden başlatılıyor..")
            time.sleep(2)
            bil.bilgisayar_ac()
        else:
            print("Yeniden başlatma iptal edildi..")    
            


bil = Bilgisayar()

'''
işlem seçin 

1.Bilgisayar Aç

2.Bilgisayar Kapat

3.Bilgisayar Ses Açma

4.Ekran Parlaklığı

5.Program

6.Şifre Değiştir

7.Müzik Listesi

8.Bilgisayar Özellikleri

9.Program Sayısı

10.Yeniden Başlat

'''
bil.bilgisayar_ac()

while True:

    hareket = input("Bir işlem seçin: ")
    if(hareket == 'q'):
        
        print('Program sonlandırlıyor..')
        time.sleep(2)
        break
    elif (hareket == '1'):
        bil.bilgisayar_ac()
    elif(hareket == '2'):
        bil.bilgisayar_kapat()
        break
    elif(hareket == '3'):
        bil.bilgisaray_sesacma()
    elif (hareket == '4'):
        bil.ekran_parlakligi()
    elif (hareket == '5'):
        bil.pragram()

    elif (hareket == '6'):
        bil.sifre_degistir()
    elif (hareket == '7'):
        bil.muzik()
    elif (hareket == '8'):
        print(bil)
    elif (hareket == '9'):
        print("Program sayısı: ", len(bil))    
    elif (hareket == '10'):
        bil.yeniden_baslat()     
    else:
        print("Geçersiz işlem..")            

"""