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
        print(f"{self.hesapNo} nolu hesabınızda bulunan bakiye : {self.bakiye_bilgi} TL")
        time.sleep(1)
        cekilecek_miktar = int(input("Çekmek istediğiniz miktarı giriniz: "))
        if (cekilecek_miktar < self.bakiye_bilgi):
            güncel_paraa = self.bakiye_bilgi - cekilecek_miktar
            time.sleep(1)
            print(f"{self.hesapNo} nolu hesabınızda bulunan son bakiye: {güncel_paraa} TL")
            self.bakiye_bilgi = güncel_paraa
            print("Ana sayfaya geçiş yapılıyor..")
            time.sleep(3)
        elif (cekilecek_miktar > self.bakiye_bilgi):
            ek_bakiye = (input("Ek hesap kullanılsın mı? Evet ise [E] , Hayır ise [H] yazın: "))
            time.sleep(1)
            if (ek_bakiye == 'E'):
                güncel_paraa = (self.ek_hesap + self.bakiye_bilgi) - cekilecek_miktar 
                self.ek_hesap = güncel_paraa
                time.sleep(1)
                print(f"Ek hesap kullanılmıştır, bakiyeniz: {self.ek_hesap} TL")
                print("Ana sayfaya geçiş yapılıyor..")
                time.sleep(3)
            else:
                time.sleep(1)
                print("Maalesef bakiyeniz yetersizdir.")
                print("Ana sayfaya geçiş yapılıyor..")
                time.sleep(3)  
    
    def para_transfer(self):
        print(f"{self.hesapNo} nolu hesabınızda bulunan bakiye : {self.bakiye_bilgi} TL")
        transfer_edilecek_miktar = int(input("Transfer edilecek para miktarını giriniz: "))
        time.sleep(1)
        if (transfer_edilecek_miktar < self.bakiye_bilgi):
            güncel_paraa = self.bakiye_bilgi - transfer_edilecek_miktar
            time.sleep(1)
            print(f"Hesabınızda bulunan mevcut bakiye: {güncel_paraa} TL")
            self.bakiye_bilgi = güncel_paraa
            print("Ana sayfaya geçiş yapılıyor..")
            time.sleep(3)
        elif (transfer_edilecek_miktar > self.bakiye_bilgi):
            ek_bakiye = (input("Ek hesap kullanılsın mı? Evet ise [E] , Hayır ise [H] yazın: "))
            time.sleep(1)
            if (ek_bakiye == 'E'):
                güncel_paraa = (self.ek_hesap + self.bakiye_bilgi) - transfer_edilecek_miktar 
                self.ek_hesap = güncel_paraa
                time.sleep(1)
                print(f"Ek hesap kullanılmıştır, ek hesap bakiyeniz: {self.ek_hesap} TL")
                print("Ana sayfaya geçiş yapılıyor..")
                time.sleep(3)
            else:
                time.sleep(1)
                print("Maalesef bakiyeniz yetersizdir.")
                print("Ana sayfaya geçiş yapılıyor..")
                time.sleep(3)
 
    
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
                print("Ana sayfaya geçiş yapılıyor..")
                time.sleep(3)
            else:
                print("Kredi kartı borcunuz ödenmemiştir..")
                print("Ana sayfaya geçiş yapılıyor..")
                time.sleep(3)   
        elif (self.bakiye_bilgi < self.kredi_kartı):
            kullan = input("kredi kartı borcu için Ek hesap kullanılsın mı ? Evet ise [E] , Hayır ise [H] diyin: ")
            if (kullan == 'E'):
                kalan = (self.bakiye_bilgi + self.ek_hesap) - self.kredi_kartı
                time.sleep(1)
                print(f"Kredi kartı borcunuz ödenmiştir. Mevcut bakiye {kalan} TL")
                self.ek_hesap = kalan
                time.sleep(1)
                print(f"Ek hesaptaki mevcut bakiyeniz {self.ek_hesap} TL")
                print("Ana sayfaya geçiş yapılıyor..")
                time.sleep(3)

            else:
                print("Kredi kartı borcunuz ödenmemiştir..")
                print("Ana sayfaya geçiş yapılıyor..")
                time.sleep(3)

    def sifre_islemleri(self):
        i = 0
        while i < 3:
            once = input("Şifre değişirmek için, Önce mevcut şifrenizi doğrulayın: ")
            time.sleep(1)
            if (self.sifre == once):
                istiyormusun = input("Şifre değiştirmek istiyor musunuz ? Evet ise [E] , Hayır ise [H] diyin: ")
                time.sleep(1)
                if (istiyormusun == 'E'):
                    yeni_sifre = (input("4 haneli şifre belirleyin: "))
                    time.sleep(1)
                    if (len(yeni_sifre) == len(self.sifre)):
                        time.sleep(1)
                        print("Şifreniz değiştiriliyor..")
                        time.sleep(1)
                        print(f"Mevcut şifreniz {yeni_sifre} olarak değiştirilmiştir..")
                        self.sifre = yeni_sifre
                        print("Ana sayfaya geçiş yapılıyor..")
                        time.sleep(3)
                        break
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
        print(f'''
        BAKİYE - BİLGİ
        
        1.BAKİYE ÖĞREN

        2.KAYITLI TELEFON NUMARASI

        3.HESAP NUMARASI

        4.EK HESAP ÖĞREN

        5.MEVCUT ŞİFRENİZİ ÖĞRENİN

        ''')
        gir = input("İşlem belirtin: ")
        time.sleep(1)

        if (gir == '1'):
            print(f"{self.hesapNo} nolu hesabınızda ki mevcut bakiye: {self.bakiye_bilgi}")
            print("Ana sayfaya geçiş yapılıyor..")
            time.sleep(3)
        elif (gir == '2'):
            print(f"{self.hesapNo} nolu hesabınızda ki kayıtlı telefon numarası: {self.telNo}")
            print("Ana sayfaya geçiş yapılıyor..")
            time.sleep(3)  
        elif (gir == '3'):
            print(f"Hesap numaranız: {self.hesapNo}")
            print("Ana sayfaya geçiş yapılıyor..")
            time.sleep(3)
        elif (gir =='4'):
            print(f"{self.hesapNo} nolu hesabınızda ki mevcut ek bakiye: {self.ek_hesap}")
            print("Ana sayfaya geçiş yapılıyor..")
            time.sleep(3)
        elif (gir == '5'):
            print(f"{self.hesapNo} nolu hesabınızın mevcut şifre: {self.sifre}")
            print("Ana sayfaya geçiş yapılıyor..")
            time.sleep(3)

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
            onay= input("Elektrik faturası ödemesini onaylıyor musunuz? Evet ise [E] , Hayır ise [H] diyin: ")
            if (onay == 'E'):
                fatura = self.bakiye_bilgi - elektrik
                time.sleep(1)
                print(f"Elektirik faturanız ödendi. mevcut bakiyeniz {fatura} TL")
                self.bakiye_bilgi = fatura
                print("Ana sayfaya geçiş yapılıyor..")
                time.sleep(5)
            else:
                print("Faturanız ödenmemiştir..")
                print("Ana sayfaya geçiş yapılıyor..")
                time.sleep(3)
        
        elif (ode == '2'):
            onay= input("Su faturası ödemesini onaylıyor musunuz? Evet ise [E] , Hayır ise [H] diyin: ")
            if (onay == 'E'):
                fatura = self.bakiye_bilgi - su
                time.sleep(1)
                print(f"Su faturanız ödendi. mevcut bakiyeniz {fatura} TL")
                self.bakiye_bilgi = fatura
                print("Ana sayfaya geçiş yapılıyor..")
                time.sleep(5)
            else:
                print("Faturanız ödenmemiştir..")
                print("Ana sayfaya geçiş yapılıyor..")
                time.sleep(3)
        elif (ode == '3'):
            onay= input("Meb ödemesini onaylıyor musunuz? Evet ise [E] , Hayır ise [H] diyin: ")
            if (onay == 'E'):
                fatura = self.bakiye_bilgi - meb
                time.sleep(1)
                print(f"Meb borcunuz ödendi. mevcut bakiyeniz {fatura} TL")
                self.bakiye_bilgi = fatura
                print("Ana sayfaya geçiş yapılıyor..")
                time.sleep(5)
            else:
                print("Faturanız ödenmemiştir..")
                print("Ana sayfaya geçiş yapılıyor..")
                time.sleep(3)

        elif (ode == '4'):
            onay= input("Doğal gaz faturası ödemesini onaylıyor musunuz? Evet ise [E] , Hayır ise [H] diyin: ")
            if (onay == 'E'):
                fatura = self.bakiye_bilgi - dogal_gaz
                time.sleep(1)
                print(f"Doğal gaz faturanız ödendi. mevcut bakiyeniz {fatura} TL")
                self.bakiye_bilgi = fatura
                print("Ana sayfaya geçiş yapılıyor..")
                time.sleep(5)
            else:
                print("Faturanız ödenmemiştir..") 
                print("Ana sayfaya geçiş yapılıyor..")
                time.sleep(3)
        elif (ode == '5'):
            onay= input("Telefon faturası ödemesini onaylıyor musunuz? Evet ise [E] , Hayır ise [H] diyin: ")
            if (onay == 'E'):
                fatura = self.bakiye_bilgi - telefon
                time.sleep(1)
                print(f"Telefon faturanız ödendi. mevcut bakiyeniz {fatura} TL")
                self.bakiye_bilgi = fatura
                print("Ana sayfaya geçiş yapılıyor..")
                time.sleep(5)
            else:
                print("Faturanız ödenmemiştir..")    
                print("Ana sayfaya geçiş yapılıyor..")
                time.sleep(3)
        else:
            print("Yanlış işlem belirttiniz..")                  
            print("Ana sayfaya geçiş yapılıyor..")
            time.sleep(3)
    
    
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
                break
            else:
                if (len(sifre) < len(self.sifre)):
                    print("Eksik tuşlama yaptınız. Tekrar deneyin. 3 kere bilemezseniz blok olur.")
                else:
                    print("Şifre hatalı. Tekrar deneyin. 3 kere bilemezseniz blok olur.")
            i += 1
            print("Kartınız Blok olmuştur. Lütfen Müşteri hizmetleri ile iletişime geçin..")       
                
    def kart_iste(self):
        print("Lütfen kartınızı bekleyin..")
      
       
        

banka = BankaYazılım()
banka.bilgilerigöster()

while 1:
    print('''
            BİP BANKASI

            1.PARA ÇEKME

            2.PARA TRANSFERİ

            3.ŞİFRE İŞLEMLERİ

            4.ÖDEME İŞLEMLERİ

            5.BAKİYE-BİLGİ

            6.KREDİ KARTI İŞLEMLERİ

            7.KARTI İSTEYİN
            ''')
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

    elif (islem == '6'):
        banka.kredi_karti()   

    elif ( islem == '7'):
        banka.kart_iste()
        break
    
    else:
        print("Yanlış seçim")     

         



