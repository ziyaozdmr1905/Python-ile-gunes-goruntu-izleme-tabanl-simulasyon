# tekrar
"""
kuruyemisler = ["badem","fındık","fıstık"]

kuruyemisler.append("ceviz")

kuruyemisler[-1] = 'iğde'
"""

"""
elemansayisi = len(kuruyemisler)
i = 0
while i < elemansayisi:
    print(kuruyemisler[i])
    i += 1
"""

#print(kuruyemisler)

"""
# fıtığın index inin bulduk
i = 0

while i < len(kuruyemisler):
    if kuruyemisler[i] == 'fıstık':
        print(i)
    i += 1    
"""

"""
komsuiller = ["Kırıkkale","Kırşehir","Nevşehir","Kayseri","Sivas","Tokat","Amasya","Çorum"]
print("Yozgat ilinin komşularını öğrenelim ")

girilne = input("Lütfen ilk harfi büyük giriniz: ")
i = 0
while i < len(komsuiller):
    if komsuiller[i] == girilne:
        print('Tebrikler! ', girilne, ' Yozgat iline komşudur.')
        break
    i += 1
else:
    print("Üzgünüm ", girilne,' Yozgat iline komşu değildir')    
"""


"""
k = 'elma' in ["Armut","elma","erik"]
print(k)
"""


"""
komsuiller = ["Kırıkkale","Kırşehir","Nevşehir","Kayseri","Sivas","Tokat","Amasya","Çorum"]
print("Yozgat ilinin komşularını öğrenelim ")

girilne = input("Lütfen ilk harfi büyük giriniz: ")

if girilne in komsuiller:
    print('Tebrikler! ', girilne , ' Yozgat iline komşudur')
else:
    print('Üzgünüm ', girilne , " Yozgat iline komşu değildir")
"""

"""
canta = ["kalem","silgi"]

s = 0
while True:
    x =input("Çanta da ne yok?")
    if x in canta:
        print(f"Çanta da {x} var. ")
    else:
        canta.append(x)
        break
print(canta)        
"""

"""
meyvalar = ["armut","elma","erik"]

for meyva in meyvalar:
    print(meyva)
"""
"""
for u in range(0,24,3):
    print(u)
"""
"""
u = 0

while u < 24:
    print(u)
    u += 3
"""



"""
myevalar = ["erik","elma","armut","muz","elma"]

u = "elma"

myevalar.remove(u)

print(myevalar)
"""

"""
kitaplar = [
    [45623 , 'Python' , 'Mustafa' , 'Başer' , 23],
    [99878 , 'Linux Ağ Servisleri' , 'Mustafa' , 'Başer' , 26],
    [98938 , 'İşletim Sistemleri' , 'Ali' , '   Saatçi' , 17],
    [98947 , 'PHP ve AJAX' , 'Haydar' , 'Tuna' , 25]
]

while 1:
    kitapNo = input('Kitap numarası giriniz: ')
    if kitapNo not in ['ç','Ç']:
        for k in kitaplar:
            if int(kitapNo) == k[0]:
                print(f" {k[1]} Kitabın yazarı: {k[2]} {k[3]} Fiyatı: {k[4]} TL ") 
                break
            else:
                print(f" {kitapNo} numaralı kitap arşivde yok. ")
    else:
        break            

"""

"""
kutuphane = [
    [ 123 , 'Beyoğlunun En Güzel Abisi' , 'Ahmet' , 'Ümit' , 23 ],
    [ 456 , 'Hayat Güzeldir' , 'Esra' , 'Ezmeci' , 24],
    [ 789 , 'İstanbul Hatırası' , 'Ahmet' , 'Ümit' , 30],
    [ 369 , 'Beyoğlu Rapsodisi' , 'Ahmet' , 'Ümit' , 31],
    [ 258 , 'Börü' , 'Çağlayan' , 'Yılmaz' , 28],
    [ 147 , 'Çalıkuşu' , 'Reşat Nuri' , 'Gültekin' , 27],
    [ 301 , 'Karantina' , 'Beyza' , 'Alkoç' , 25],
    [ 624 , 'Asansör' , 'Beyza' , 'Alkoç' , 29],
    [ 957 , 'Dönüşüm' , 'Fransz' , 'Kafka' , 31]
]


while 1:
    fiyat =(input("Bir kitap fiyatı giriniz: "))
    if fiyat not in ["a" , "A"]:
        for k in kutuphane:
            if k[4] < int(fiyat):
                print(f"Girilen fiyattan düşük olan kitaplar.")
                print(k)
                continue
        yazarAd = input("Bir yazar ismi giriniz: ")
        if yazarAd == k[2]:
            print(f" {k[0]} numaralı kitaplar karşımıza çıktı. kitap ismileri {k[1]}")
            print(k)
            continue
        kitapAd = input("Kitabın ismini giriniz: ")
        if kitapAd == k[1]:
            print(f"Aradığınız kitap {k[0]} numaralı olup {k[2]} {k[3]} adlı yazara aittir.")
        else:
            print('Yanlış isim girdiniz')
    else:
        break                 

"""



"""
kutuphane = [
    { 'no' : 123 , 'KitapAdı' : 'Beyoğlunun En Güzel Abisi' , 'YazarAdı' : 'Ahmet' , 'YazarSoy' : 'Ümit' , 'Fiyatı' : 23 },
    { 'no' : 456 , 'KitapAdı' : 'Hayat Güzeldir' , 'YazarAdı' : 'Esra' , 'YazarSoy' :'Ezmeci' , 'Fiyatı' : 24},
    { 'no' : 789 , 'KitapAdı' : 'İstanbul Hatırası' , 'YazarAdı' : 'Ahmet' , 'YazarSoy' : 'Ümit' , 'Fiyatı' : 30},
    { 'no' : 369 , 'KitapAdı' : 'Beyoğlu Rapsodisi' , 'YazarAdı' : 'Ahmet' , 'YazarSoy' : 'Ümit' , 'Fiyatı' : 31},
    { 'no' : 258 , 'KitapAdı' : 'Börü' , 'YazarAdı' : 'Çağlayan' , 'YazarSoy' : 'Yılmaz' , 'Fiyatı' : 28},
    { 'no' : 147 , 'KitapAdı' : 'Çalıkuşu' , 'YazarAdı' : 'Reşat Nuri' , 'YazarSoy' : 'Gültekin' , 'Fiyatı' : 27},
    { 'no' : 301 , 'KitapAdı' : 'Karantina' , 'YazarAdı' : 'Beyza' , 'YazarSoy' : 'Alkoç' , 'Fiyatı' : 25},
    { 'no' : 624 , 'KitapAdı' : 'Asansör' , 'YazarAdı' : 'Beyza' , 'YazarSoy' : 'Alkoç' , 'Fiyatı' : 29},
    { 'no' : 957 , 'KitapAdı' : 'Dönüşüm' , 'YazarAdı' : 'Fransz' , 'YazarSoy' : 'Kafka' , 'Fiyatı' : 31}
]

while 1:
    fiyat =(input("Bir kitap fiyatı giriniz: "))
    
    if fiyat not in ["a" , "A"]:
        for k in kutuphane:
            if k['Fiyatı'] < int(fiyat):
                print(f"Girilen fiyattan düşük olan kitaplar.")
                print(k)
                continue
            yazarAd = input("Bir yazar ismi giriniz: ")
            if yazarAd == k['YazarAdı']:
                print(f" {k['no']} numaralı kitaplar karşımıza çıktı. kitap ismileri {k['KitapAdı']}")
                print(k)
            continue
        kitapAd = input("Kitabın ismini giriniz: ")
        if kitapAd == k['KitapAdı']:
            print(f"Aradığınız kitap {k[0]} numaralı olup {k[2]} {k[3]} adlı yazara aittir.")
        else:
            print('Yanlış isim girdiniz')
    else:
        break                 
"""











"""
for i in kutuphane:
    if i['no'] < 500:
        print(i['no'])
"""
"""
for k in kutuphane:
    if k[4] > 30:
        continue
    print(k)
    if k[0] == 123:
        print(k)

"""

"""
kutuphane = [
    ['Beyoğlunun En Güzel Abisi' , 'Ahmet' , 'Ümit' , 23 ],
    ['Hayat Güzeldir' , 'Esra' , 'Ezmeci' , 24],
    ['İstanbul Hatırası' , 'Ahmet' , 'Ümit' , 30],
    ['Beyoğlu Rapsodisi' , 'Ahmet' , 'Ümit' , 31],
    ['Börü' , 'Çağlayan' , 'Yılmaz' , 28],
    ['Çalıkuşu' , 'Reşat Nuri' , 'Gültekin' , 27],
    ['Karantina' , 'Beyza' , 'Alkoç' , 25],
    ['Asansör' , 'Beyza' , 'Alkoç' , 29],
    ['Dönüşüm' , 'Fransz' , 'Kafka' , 31]
]
yazarAd = input("Bir kitap ismi giriniz: ")
for k in kutuphane:
    if (yazarAd == (k[0])):
        print(f" {(k[0])} numaralı kitaplar karşımıza çıktı. kitap ismileri {k[1]}")
        print(k)
        break
"""

"""
urunler = [
    {'name' : 'samsung s6' , 'price' : '3000'},
    {'name' : 'samsung s7' , 'price' : '4000'},
    {'name' : 'samsung s8' , 'price' : '5000'},
    {'name' : 'samsung s9' , 'price' : '6000'},
    {'name' : 'samsung s10' , 'price' : '7000'}
]

for i in urunler:
    print(i['name'])
"""







"""
while 1:
    fiyat =(input("Bir kitap fiyatı giriniz: "))
    if fiyat not in ["a" , "A"]:
        for k in kutuphane:
            if k[4] < int(fiyat):
                #print(f"Girilen fiyattan düşük olan kitaplar.")
                print(k)
                continue
            yazarAd = input("Bir yazar ismi giriniz: ")    
            if yazarAd == k[2]:
                print(f" {k[0]} numaralı kitaplar karşımıza çıktı. kitap ismileri {k[1]}")
                print(k)
                kitapAd = input("Kitabın ismini giriniz: ")
                if kitapAd == k[1]:
                    print(f"Aradığınız kitap {k[0]} numaralı olup {k[2]} {k[3]} adlı yazara aittir.")
                else:
                    print('Yanlış isim girdiniz')
            else:
                print("Böyle bir yazar yoktur")                   
    else:
        break
"""











# KÜTÜPHANE

"""
kutuphane = [
    { 'no' : 123 , 'KitapAdı' : 'Beyoğlunun En Güzel Abisi' , 'YazarAdı' : 'Ahmet' , 'YazarSoy' : 'Ümit' , 'Fiyatı' : 23 },
    { 'no' : 456 , 'KitapAdı' : 'Hayat Güzeldir' , 'YazarAdı' : 'Esra' , 'YazarSoy' :'Ezmeci' , 'Fiyatı' : 24},
    { 'no' : 789 , 'KitapAdı' : 'İstanbul Hatırası' , 'YazarAdı' : 'Ahmet' , 'YazarSoy' : 'Ümit' , 'Fiyatı' : 30},
    { 'no' : 369 , 'KitapAdı' : 'Beyoğlu Rapsodisi' , 'YazarAdı' : 'Ahmet' , 'YazarSoy' : 'Ümit' , 'Fiyatı' : 31},
    { 'no' : 258 , 'KitapAdı' : 'Börü' , 'YazarAdı' : 'Çağlayan' , 'YazarSoy' : 'Yılmaz' , 'Fiyatı' : 28},
    { 'no' : 147 , 'KitapAdı' : 'Çalıkuşu' , 'YazarAdı' : 'Reşat Nuri' , 'YazarSoy' : 'Gültekin' , 'Fiyatı' : 27},
    { 'no' : 301 , 'KitapAdı' : 'Karantina' , 'YazarAdı' : 'Beyza' , 'YazarSoy' : 'Alkoç' , 'Fiyatı' : 25},
    { 'no' : 624 , 'KitapAdı' : 'Asansör' , 'YazarAdı' : 'Beyza' , 'YazarSoy' : 'Alkoç' , 'Fiyatı' : 29},
    { 'no' : 957 , 'KitapAdı' : 'Dönüşüm' , 'YazarAdı' : 'Fransz' , 'YazarSoy' : 'Kafka' , 'Fiyatı' : 31}
]

"""







"""
while 1:
    fiyat =(input("Üst fiyat limitini belirleyin: "))
    if fiyat not in ("a","A"):
        for k in kutuphane:
            if k['Fiyatı'] < int(fiyat):
                print(f"Girilen fiyattan düşük olan kitaplar")
                print(k)
            continue
"""
            
# fiyat isteniyo        
"""
kutuphane = [
    ['Beyoğlunun En Güzel Abisi' , 'Ahmet' , 'Ümit' , 23 ],
    ['Hayat Güzeldir' , 'Esra' , 'Ezmeci' , 24],
    ['İstanbul Hatırası' , 'Ahmet' , 'Ümit' , 30],
    ['Beyoğlu Rapsodisi' , 'Ahmet' , 'Ümit' , 31],
    ['Börü' , 'Çağlayan' , 'Yılmaz' , 28],
    ['Çalıkuşu' , 'Reşat Nuri' , 'Gültekin' , 27],
    ['Karantina' , 'Beyza' , 'Alkoç' , 25],
    ['Asansör' , 'Beyza' , 'Alkoç' , 29],
    ['Dönüşüm' , 'Fransz' , 'Kafka' , 31]
]

while 1:
    fiyat = input("Bir fiyat giriniz: ")
    if fiyat not in ["a", "A"]:
        for k in kutuphane:
            if k[3] < int(fiyat):
                print("Girilen fiyattan düşük olan kitaplar")
                print(k)
                continue
"""        
            


# kitap ismi istensin 
"""
kutuphane = [
    ['Beyoğlunun En Güzel Abisi' , 'Ahmet' , 'Ümit' , 23 ],
    ['Hayat Güzeldir' , 'Esra' , 'Ezmeci' , 24],
    ['İstanbul Hatırası' , 'Ahmet' , 'Ümit' , 30],
    ['Beyoğlu Rapsodisi' , 'Ahmet' , 'Ümit' , 31],
    ['Börü' , 'Çağlayan' , 'Yılmaz' , 28],
    ['Çalıkuşu' , 'Reşat Nuri' , 'Gültekin' , 27],
    ['Karantina' , 'Beyza' , 'Alkoç' , 25],
    ['Asansör' , 'Beyza' , 'Alkoç' , 29],
    ['Dönüşüm' , 'Fransz' , 'Kafka' , 31]
]

while 1 :
    kitapAdı = input("Kitap ismi giriniz: ")
    if kitapAdı not in ["a","A"]:
        for k in kutuphane:
            if kitapAdı == k[0]:
                print(k)
                continue
"""





"""
kutuphane = [
    ['Beyoğlunun En Güzel Abisi' , 'Ahmet' , 'Ümit' , 23 ],
    ['Hayat Güzeldir' , 'Esra' , 'Ezmeci' , 24],
    ['İstanbul Hatırası' , 'Ahmet' , 'Ümit' , 30],
    ['Beyoğlu Rapsodisi' , 'Ahmet' , 'Ümit' , 31],
    ['Börü' , 'Çağlayan' , 'Yılmaz' , 28],
    ['Çalıkuşu' , 'Reşat Nuri' , 'Gültekin' , 27],
    ['Karantina' , 'Beyza' , 'Alkoç' , 25],
    ['Asansör' , 'Beyza' , 'Alkoç' , 29],
    ['Dönüşüm' , 'Fransz' , 'Kafka' , 31]
]


while 1 :
    soyadi = input("Soyisimini giriniz: ")
    if soyadi not in ["a","A"]:
        for k in kutuphane:
            if soyadi == k[2]:
                print(k)
                break
        else:
            print("Bu kitap arşivde yok")            
    else:
        break
"""
"""
kutuphane = [
    ['Beyoğlunun En Güzel Abisi' , 'Ahmet' , 'Ümit' , 23 ],
    ['Hayat Güzeldir' , 'Esra' , 'Ezmeci' , 24],
    ['İstanbul Hatırası' , 'Ahmet' , 'Ümit' , 30],
    ['Beyoğlu Rapsodisi' , 'Ahmet' , 'Ümit' , 31],
    ['Börü' , 'Çağlayan' , 'Yılmaz' , 28],
    ['Çalıkuşu' , 'Reşat Nuri' , 'Gültekin' , 27],
    ['Karantina' , 'Beyza' , 'Alkoç' , 25],
    ['Asansör' , 'Beyza' , 'Alkoç' , 29],
    ['Dönüşüm' , 'Fransz' , 'Kafka' , 31]
]

kitaplar = []
while 1 :
    fiyat = input("Kitap için bir fiyat belirtin: ")
    if fiyat not in ["j","J"]:
        for a,b,c,d in kutuphane:
            if d > int(fiyat):
                #print("Girilen kitaptan düşük kitaplar")
                
                continue
            print(a,b,c,d)
        # kitaplar.append(d)
    
        # print(kitaplar)
    else:
        print("Program sonlandı")
        break
        
"""      
