"""
import time

#HAYVANLARIN SINIFI

class Hayvan():

    def __init__(self, hayvan_grubu = 'omurgalı' , solunum = 'Oksijenli Solunum', beslenme = 'Hem Ototrof Hem Heterotrof Beslenme' , ureme = 'Eşeyli Üreme' , bosaltim = 'atık madde' , buyume_gelisme = 'kütle ya da hacim artışı' , hareket = ' yer değiştirme'  , adaptasyon = 'uyum sağlama'):
        self.hayvan_grubu = hayvan_grubu
        self.solunum = solunum
        self.beslenme = beslenme
        self.ureme = ureme
        self.bosaltim = bosaltim
        self.buyume_gelisme = buyume_gelisme
        self.hareket = hareket
        self.adaptasyon = adaptasyon

    def hayvanlarda_grup(self, sec , bil):
        '''
        HAYVANLAR İKİYE AYRILIR

        1.OMURGALI HAYVANLAR: Genel olarak ise sırtlarında omurga bulunan canlılara omurgalılar denmektedir.
        Omurga içerisinde sinir ve kemik ile beraber kıkırdak doku yer almaktadır.
        Bu organizmalar ortak şekilde ve senkronize olarak çalışarak, 
        canlının çok daha aktif bir yaşam sürmesine olanak vermektedir.

        OMURGALILAR BİR GRUBA AYRILIR
        A.MEMELİLER
        B.SÜRÜNGENLER
        C.KUŞLAR
        D.KURBAĞALAR
        E.BALIKLAR 

        2.OMURGASIZ HAYVANLAR: omurga yapısı bulunmayan canlılara verilen genel bir isimdir.
        Omurgasız olarak bilinen canlıların yapısında herhangi bir iskelet sistemi yoktur. 

        OMURGASIZLAR BİR GRUBA AYRILIR
        A.SOLUCAN
        B.YENGEÇ
        C.DENİZ ANALARI
        D.KELEBEKLER VS..

        '''
           
        if (sec == '1'):
            print("Omurgalılar grubunun bir üyesidir")
            if (bil == 'A') or (bil == 'a'):
                print('''
                MEMELİLER: 
                ✔  Vücutları deri ve tüylerle kaplıdır.
                Bu, onları iklim şartları ve zorlu yaşam koşullarına karşı korur.
                Bu tüyler zaman zaman dökülür, yerine yenileri çıkar.
                ✔  Memeliler sıcakkanlı ve omurgalı canlılardır.
                ✔  Dişileri yeni doğan yavrularını meme bezlerinin salgıladığı sütle besler.
                ''')
            elif (bil == 'B') or (bil == 'b'):
                print('''
                SÜRÜNGENLER:
                ✔  Vücutlarının pul ya da benzer levhalarla kaplı olması nem kaybını en az düzeyde tutmalarını sağlar,
                bu sayede kurak ortamlara oldukça iyi uyum sağlarlar.
                ''')   
            elif (bil == 'C') or (bil == 'c'):
                print('''
                KUŞLAR:
                ✔  Kuşlar; tüyleri, dişsiz gagaları, yumurtladıkları sert kabuklu yumurtalar yoluyla üreyen, 
                ✔  yüksek metabolizma hızına sahip, 
                ✔  dört odacıklı kalpleri ve hafif ama güçlü bir iskelet yapısına sahip, 
                ✔  Aves sınıfını oluşturan sıcakkanlı omurgalı hayvanlar grubudur.
                
                ''')
            elif (bil == 'D') or (bil == 'd'):
                print('''
                KURBAĞALAR:
                ✔  Erişkinlerinin uzun arka bacaklar, tıknaz gövde, araları zarlı parmaklar, 
                çıkık gözler ve kuyruksuzluk gibi özellikleri bulunan kurbağaların 
                büyük çoğunluğu yarı sucul bir yaşam sürer ama 
                tırmanarak ya da zıplayarak karada da rahatça hareket edebilirler.
                ''')    
            elif (bil == 'E') or (bil == 'e'):
                print('''
                BALIKLAR:
                ✔  Balıklar (Latince: pisces) poikloterm olan, neredeyse sadece suda yaşayan ve 
                solungaçları ile solunum yapan, soğuk kanlı, yürekleri çift gözlü, çoğunun vücudu pullu, 
                genellikle yumurta ile üreyen omurgalı hayvanlardır.
                ''')        
        elif (sec == '2'):
            print("Omurgasızlar da kendi içinde gruba ayrılır. şu anlık bu bilgilere ihtiyaç yoktur. ")




    def hayvanlarda_solunum(self,sec):
        
        '''
        Solunum: Canlılar hayatlarına devam edebilmek için gerekli olan enerjiyi besinlerden karşılar.\nBesinin yapısında bulunan enerjiyi kullanılabilir hale getirmek için de hücresel solunum yaparlar.\nHücresel solunum temel olarak üç şekilde gerçekleşir.

        1.Oksijenli Solunum

        2.Oksijensiz Solunum

        3.Fermantasyon

        '''
        if (sec == '1'):
            print('''
        OKSİJENLİ SOLUNUM: Besinin parçalanması sürecinde oksijenin kullanıldığı hücresel solunumdur.
        Diğer hücresel solunumlara göre daha fazla enerji üretilir.
        
        ''')
        elif (sec == '2'):
            print("2.OKSİJENSİZ SOLUNUM:\nBesinin parçalanma sürecinde oksijen dışında bir inorganik maddenin kullanıldığı\nhücresel solunumdur(N ve S gibi).\nSadece prokaryot hücreli canlıların bazılarında görülür.")
        elif (sec == '3'):
            print("3.FERMANTASYON:\nBesinin parçalanma sürecinde herhangi bir inorganik madde kullanılmadan,\nbesinin kısmen parçalanmasıdır.Enerji üretimi çok düşüktür.")
        else:
            print("Hatalı giriş..")        
    def hayvanlarda_beslenme(self, sec):
        '''

        Beslenme: Canlılar hayatsal faaliyetleri için gerekli olan enerjiyi elde edebilmek için beslenmek zorundadır.\nBeslenme açısından canlılar üç gruba ayrılır.

        1.Ototrof Beslenme

        2.Heteretrof Beslenme

        3.Hem Ototrof Hem Heterotrof Beslenme
        
        '''

        if (sec == '1'):
            print('''
            
        OTOTROF BESLENME: Besinini kendi üreten canlıların yapmış olduğu beslenmedir.
        Bu canlılar besini dışarıdan hazır almazlar sadece besini üretmek için
        gerekli olan ham maddeyi (inorganik madde) dışarıdan alırlar.

        ✔ Ototrof beslenme de iki farklı mekanizma ile besin üretilir.
        Bu mekanizmalar fotosentez ve kemosentezdir.
        Fotosentez yaparak besin üreten canlılarda klorofil bulunur.

            ''')
        
        elif (sec == '2'):
            print("HETERETROF BESLENME: Besinini dışarıdan hazır alan canlıların yaptığı beslenmedir.\nHeterotrof beslenme çok çeşitlidir.")
        elif (sec == '3'):
            print('''

        HEM HETERETROF HEM OTOTROF: Gerektiğinde besinini dışarıdan hazır alan gerektiğinde besinini
        üretebilen canlıların yapmış olduğu beslenmedir.
        Bu canlıların ototrof beslenme mekanizması fotosentez ile olur.
        
        ''')
        else:
            print("Hatalı giriş..")
    def hayvanlarda_ureme(self,sec):
        '''

        Üreme: Canlılar nesillerini devam ettirebilmek için kendilerine benzer yavrular meydana getirirler.\nÜreme canlının ortak özelliğidir. Ancak yaşam için zorunlu değildir.\nÜreme temel olarak iki çeşittir. 
        
        1.Eşeyli Üreme

        2.Eşeysiz Üreme
        
        '''
        
        if (sec == '1'):
            print('''
            
        EŞEYLİ ÜREME: İki canlının beraberce yavru meydana getirdiği üremedir.
        Genetik çeşitlenmeye neden olduğundan, değişen çevre şartlarına dayanıklı bireyler meydana gelir.
            
            ''')
        elif (sec == '2'):
            print('''
            
        EŞEYSİZ ÜREME: Canlının üreme için başka bir canlıya ihtiyacı olmadan yaptığı üremedir.
        Genellikle gelişmemiş canlılarda görülür.
        Genellikle genetik çeşitlenmeye neden olmadığından değişen çevre şartlarına dayanamayan 
        bireyler meydana gelir.
            
            ''')
        else:
            print("Hatalı giriş..")    

    def hayvanlarda_bosaltim(self):
        '''

        Boşaltım: Canlıların metabolizma sonucu oluşan atık maddelerini vücudundan uzaklaştırılmasıdır.

        ✔ Her canlı atık madde oluşturmak zorundadır.
        Ancak bu atık maddelerin vücuttan uzaklaştırılması farklı mekanizmalar ile gerçekleşebilir.

        ✔ Tatlı suda yaşayan tek hücreliler kontraktil 
        kofullarını kullanarak vücutlarındaki fazla suyu dışarı atarlar.

        ✔ Bitkiler yaprak dökerek boşaltım yaparlar. 
        Ayrıca farklı mekanizmaları da kullanırlar (terleme, gutasyon).

        ✔ Hayvanlar farklı mekanizmalar kullanarak boşaltım yaparlar.
        Bu mekanizmalar; karbondioksit solunum sistemi ile su ve suda çözünmüş atık maddeler 
        böbrekler ve ter ile sindirilmemiş besinler ise dışkı halinde sindirim sisteminden uzaklaştırılır.
        Ayrıca bazı gelişmemiş hayvanlarda vücut yüzeyinden atık maddeler vücut dışına atılır.

        ✔ Canlıların hepsi metabolizması sonucu azotlu boşaltım atığı oluşturarak,
        kendilerine uygun boşaltım mekanizması ile bu maddeleri uzaklaştırır.
            
            '''

    def hayvanlarda_buyume(self):
        print('''

        Büyüme ve Gelişme: Büyüme, bir canlıda görülen kütle ya da hacim artışıdır.
        Tek hücrelilerde sitoplazma miktarının artması ve çekirdeğin büyümesi şeklinde olabilirken, 
        çok hücrelilerde mitoz bölünme ile sağlanır.

        ''')
    def hayvanlarda_hareket(self):
        print('''

        Hareket: Tüm canlılar hareket edebilir. 
        Bu hareket mekanizması bütün canlılarda aynı şekilde olmaz. 
        Bazı canlılar yer değiştirme hareketi yaparken bazıları sadece belirli yapılarını 
        hareket ettirebilir ya da yaşadığı çevrenin hareketi sayesinde yer değiştirebilir. 
 
        ''')

    def hayvanlarda_adaptasyon(self):
        print('''

        Adaptasyon: Canlılar bulundukları ortamdaki yaşama şanslarını artırabilmek ve 
        nesillerini devam ettirebilmek için kalıtsal özelliklere sahiptirler.

        ✔ Kaktüslerde su kaybını minimuma indirmek için yapraklar diken halini almıştır.

        ✔ Kutup ayılarının postu soğuktan korumak amacı ile diğer ayıların postlarına göre daha kalındır.
        ''')

h1 = Hayvan()

class Atlar(Hayvan):
    def __init__(self, solunum , beslenme , ureme , bosaltim , buyume_gelisme , hareket  , adaptasyon , hayvan_grubu, at_listesi = ['Yarış Atı'] ):
        super().__init__(solunum , beslenme , ureme , bosaltim , buyume_gelisme , hareket  , adaptasyon , hayvan_grubu)
        self.at_listesi = at_listesi
    def at_biyolojik_ozellikleri(self):
        print("Atların Biyolojik Unsurları")
        time.sleep(2)
        self.hayvan_grubu = h1.hayvanlarda_grup('1' , 'a')
        time.sleep(2)
        self.solunum = h1.hayvanlarda_solunum('1')
        time.sleep(2)
        self.beslenme = h1.hayvanlarda_beslenme('1')
        time.sleep(2)
        self.ureme = h1.hayvanlarda_ureme('1')
        time.sleep(2)
        self.bosaltim = h1.hayvanlarda_bosaltim()
        time.sleep(2)
        self.buyume_gelisme = h1.hayvanlarda_buyume()
        time.sleep(2)
        self.hareket = h1.hayvanlarda_hareket
        time.sleep(2)
        self.adaptasyon = h1.hayvanlarda_adaptasyon()

    def at_bakim_yili(self):
        time.sleep(2)
        print('''
        Yetiştirme, bakım ve çevreye bağlı olarak modern atların ömrü ortalama 25 ila 30 yıl  arasındadır.

        Tay: Bir yaşından küçük olan her iki cinsten bir tay. Tayların çoğu beş ila yedi aylıkken sütten kesilir, ancak taylar dışarıdan bir etki olmaksızın dört ayda da sütten kesilebilir.
        
        Genç At: Bir ya da iki yaşında olan her iki cinsiyetten bir at.
        
        Aygır: Dört yaşında ve daha büyük hadım edilmemiş bir erkek at. “At” terimi bazen aygır anlamında da kullanılmaktadır.
        
        Kısrak: Dört veya daha büyük yaşında olan dişi at.
        
        İğdiş: Her yaştan hadım edilmiş erkek at.
        ''')
    def at_turu(self):
        while True:
            kop = input("Listeye eklemek istiğiniz at türü var mı (E, e): evet , (H,h): hayır : ")
            time.sleep(2)
            if (kop == 'e') or (kop == 'E'):
                tur = input("At türü giriniz: ")
                time.sleep(2)
                self.at_listesi.append(tur)
                print(self.at_listesi)
            else:
                print("Ekleme olayacak çıkılıyor..")
                print(self.at_listesi)
                break 

    def at_sayisi(self):
        return len(self.at_listesi)    

class Kopek(Hayvan):
    def __init__(self, solunum , beslenme , ureme , bosaltim , buyume_gelisme , hareket  , adaptasyon , hayvan_grubu , kopek_listesi = ["AV köpeği"]):
        super().__init__(solunum , beslenme , ureme , bosaltim , buyume_gelisme , hareket  , adaptasyon , hayvan_grubu)        
        self.kopek_listesi = kopek_listesi

    def kopek_biyolojik_ozellikler(self):
        print("Köpeklerin Biyolojik Unsurları")
        time.sleep(2)
        self.hayvan_grubu = h1.hayvanlarda_grup('1' , 'a')
        time.sleep(2)
        self.solunum = h1.hayvanlarda_solunum('1')
        time.sleep(2)
        self.beslenme = h1.hayvanlarda_beslenme('3')
        time.sleep(2)
        self.ureme = h1.hayvanlarda_ureme('1')
        time.sleep(2)
        self.bosaltim = h1.hayvanlarda_bosaltim()
        time.sleep(2)
        self.buyume_gelisme = h1.hayvanlarda_buyume()
        time.sleep(2)
        self.hareket = h1.hayvanlarda_hareket
        time.sleep(2)
        self.adaptasyon = h1.hayvanlarda_adaptasyon()
    
    def kopek_bakim_yili(self):
        time.sleep(2)
        print('''
        İnsanlarla binlerce yıldır beraber yaşayan köpeklerin en faydalı oldukları konu herhalde 
        çobanlara yaptıkları yardım ve korumadır.

        Soğuk iklime sahip bölgelerde köpekler, insanlara kızakları çekerek yardımcı olur. 
        Bu tür soğuk iklim köpekleri bir günde 150 km yol katedebilir.

        Köpeklerin Yaşadığı yerler: Evcil ve vahşi olarak dünyanın hemen hemen her yerinde.

        Özellikleri: Keskin koku alma ve işitme kabiliyetli etçil bir memeli. 
        Sahibine bağlılığı ile şöhret bulmuştur.

        Ömrü: 15-20 yıl.

        Çeşitleri: Görünüş ve büyüklükleri farklı 100’den fazla köpek ırkı vardır. 
        Çoban köpeği, av köpeği, bulldog, polis köpeği, Saint Bernard köpekleri Ünlüdür.
        
        ''')    

    def kopek_turu(self):
        while True:
            kop = input("Listeye eklemek istiğiniz köpek türü var mı (E, e): evet , (H,h): hayır : ")
            time.sleep(2)
            if (kop == 'e') or (kop == 'E'):
                tur = input("Köpek türü giriniz: ")
                time.sleep(2)
                self.kopek_listesi.append(tur)
                print(self.kopek_listesi)
            else:
                print("Ekleme olayacak çıkılıyor..")
                print(self.kopek_listesi)
                break 
    def kopek_sayisi(self):
        return len(self.kopek_listesi)        

class kuslar(Hayvan):
    def __init__(self ,  solunum , beslenme , ureme , bosaltim , buyume_gelisme , hareket  , adaptasyon , hayvan_grubu , kus_turlari_liste = ['Papağan']):
        super().__init__( solunum , beslenme , ureme , bosaltim , buyume_gelisme , hareket  , adaptasyon , hayvan_grubu)
        self.kus_turlari_listesi = kus_turlari_liste

    def kuslarin_biyolojik_ozellikleri(self):
        print("Kuşların Biyolojik Unsurları")
        time.sleep(2)
        self.hayvan_grubu = h1.hayvanlarda_grup('1' , 'c')
        time.sleep(2)
        self.solunum = h1.hayvanlarda_solunum('1')
        time.sleep(2)
        self.beslenme = h1.hayvanlarda_beslenme('3')
        time.sleep(2)
        self.ureme = h1.hayvanlarda_ureme('1')
        time.sleep(2)
        self.bosaltim = h1.hayvanlarda_bosaltim()
        time.sleep(2)
        self.buyume_gelisme = h1.hayvanlarda_buyume()
        time.sleep(2)
        self.hareket = h1.hayvanlarda_hareket
        time.sleep(2)
        self.adaptasyon = h1.hayvanlarda_adaptasyon()

    def kus_bakim_yili(self):
        time.sleep(2)
        print('''
        
        Yuva yapma ve yavru bakımı görülür.
        Kış uykusu görülmez.
        Bir çok kuş kış gelince sıcak bölgelere göç eder.
        Penguen,tavuk,kaz,ördek,devekuşu,serçe,kanarya,kartal,doğan,şahin örnek olarak verilebilir.
        
        ''')    

    def kus_turu(self):
        while True:
            time.sleep(2)
            kus = input("Listye eklemek istiğiniz kuş türü var mı (E, e): evet , (H,h): hayır : ")
            time.sleep(2)
            if (kus == 'e') or (kus == 'E'):
                tur = input("Kuş türü giriniz: ")
                time.sleep(2)
                self.kus_turlari_listesi.append(tur)
                print(self.kus_turlari_listesi)
            else:
                print("Ekleme olayacak çıkılıyor..")
                print(self.kus_turlari_listesi)
                break 
    def kus_sayisi(self):
        return len(self.kus_turlari_listesi)


a1 = Atlar('ok' , 'il' , 'w' , 'e' , 'q' , 'r', 'a' , 'd')


k1 = Kopek('ok' , 'il' , 'w' , 'e' , 'q' , 'r', 'a' , 'd')

ku = kuslar('ok' , 'il' , 'w' , 'e' , 'q' , 'r', 'a' , 'd')


'''
İŞLEM SEÇİN

1.ATLARIN ÖZELLİKLERİ

2.KÖPEKLERİN ÖZELLİKLERİ

3.KUŞLARIN ÖZELLİKLERİ


'''
while True:
    islem = input("Bir sayı seçiniz: ")

    if (islem == '1'):
        a1.at_biyolojik_ozellikleri()
        a1.at_bakim_yili()
        a1.at_turu()
        time.sleep(2)
        print('At türleri sayısı: ',len(a1.at_listesi))
        
        
    elif (islem == '2'):
        k1.kopek_biyolojik_ozellikler()
        k1.kopek_bakim_yili()
        k1.kopek_turu()
        print('Köpek türleri sayısı: ',len(k1.kopek_listesi))
    elif (islem == '3'):
        ku.kuslarin_biyolojik_ozellikleri()
        ku.kus_bakim_yili()
        ku.kus_turu()
        print('Kuş türleri sayısı: ',len(ku.kus_turlari_listesi))
    else:
        print("Yanlış işlem..")
        break    

"""






