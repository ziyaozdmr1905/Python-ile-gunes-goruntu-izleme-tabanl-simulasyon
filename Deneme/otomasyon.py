
def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")
   
    ogrenci_adi = liste[0]
    notlari = liste[1].split(",")

    not1 = int(notlari[0])
    not2 = int(notlari[1])
    not3 = int(notlari[2])
    
    ortalama = (not1+not2+not3)/3
    son_not = ortalama

    if (son_not >= 90):
        harf = "AA"
    elif (son_not >= 80):
        harf = "BA"    
    elif (son_not >= 70):
        harf = "BB"    
    elif (son_not >= 60):
        harf = "CB"    
    elif (son_not >= 50):
        harf = "CC"    
    elif (son_not >= 40):
        harf = "DC"    
    else:
        harf = "FF"    

    return ogrenci_adi + "---------------------->" + harf + "\n"


def ortalamalari_oku():
    with open("sınav_notları.txt", "r" , encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))
            


def not_gir():
    ad = input("Öğrenci adı: ")
    soyad = input("Öğrenci soyadı: ")
    not1 = (input("Not1: "))
    not2 = (input("Not2: "))
    not3 = (input("Not3: "))

    with open("sınav_notları.txt", "a" , encoding="utf-8") as file:
        file.write(ad + " " + soyad + ":" + not1 + "," + not2 + "," + not3 + "\n") 


def notlari_kaydet():
    with open("sınav_notları.txt", "r" , encoding="utf-8") as file:
        liste = []

        for i in file:
            liste.append(not_hesapla(i))
    
    with open("sonuclar.txt", "w" , encoding="utf-8") as file2:
        for i in liste:
            file2.write(i)
        
def kalanlar(satir):

    satir = satir[:-1]
    liste = satir.split(":")
   
    ogrenci_adi = liste[0]
    notlari = liste[1].split(",")

    not1 = int(notlari[0])
    not2 = int(notlari[1])
    not3 = int(notlari[2])
    
    ortalama = (not1+not2+not3)/3
    

    if ortalama < 40:
        with open("sınav_notları.txt", "r" , encoding="utf-8") as file:
            liste = []

            for i in file:
                liste.append(not_hesapla(i))
       
        with open("sonuclar.txt", "w" , encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)        
            
            


while True:
    islem = input("1-Notları Oku\n2-Notları Gir\n3-Notları Kaydet\n4-Kalanlar\n5-Çıkış\nİşlem: ")

    if islem == '1':
        ortalamalari_oku()
    elif islem == '2':
        not_gir()
    elif islem == '3':
        notlari_kaydet()
    elif islem == '4':
        kalanlar()
    else:
        break    

