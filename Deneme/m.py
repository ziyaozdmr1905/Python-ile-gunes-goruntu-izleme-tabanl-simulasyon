"""
x = 6

if (x < 5): 
    print("x'in değeri 5 den küçük")
else:
    print("değer yanlış")
"""
"""
girilen = (input("Veri giriniz : "))

if (girilen):
    print("klavyeden bir veri girdiniz. Girdiğiniz veri:",girilen)
"""
"""
print("Çorum,Sivas ve Kayseri ile komşu olan ilimiz hangisidir?")

girilen = input("cevabınız: ")


if (girilen == "Yozgat") or (girilen == "yozgat"):
    print("tebrikler cevabınız doğru")
else:
    print("maalesef cevabınız yanlış.")
"""

"""
girilen = int(input("bir sayı giriniz: "))
if girilen < 0:
    print("girilen sayı negatiftir")
elif girilen == 0:
    print("sayı sıfıra eşittir")    
else:
    print("girilen sayı pozitiftir")
"""

"""
a = 3
if a > 1:
    print("a sayısı 1 den büyüktür")
elif a > 2:
    print("a sayısı 2 den büyüktür")
elif a > 3:
    print("a sayısı 3 den büyüktür")
elif a > 4:
    print("a sayısı 4 den büyüktür")
"""
"""
a = 3
if a > 1:
    print("a sayısı 1 den büüyktür")
if a > 2:
    print("a sayısı 2 den büüyktür")
if a > 3:
    print("a sayısı 3 den büüyktür")
if a > 4:
    print("a sayısı 4 den büüyktür")
"""
"""
odaİsisi = int(input("oda sıcaklığını giriniz: "))

if odaİsisi < 23:
    print("içerisi soğuk olur")
elif (odaİsisi >= 23) and (odaİsisi <= 25):
    print("içerisi iyi")
else:
    print("içerisi çok sıcak")
"""
"""
girilen = int(input("bir sayı giriniz: "))

if ((girilen % 2) == 0):
    print("girdiğiniz sayı çift bir sayıdır")
elif (girilen == 0):
    print("girilen sayı sıfırdır")
else:
    print("girilen sayı tek sayıdır")
"""

"""
girilen = float(input("Bir sayı giriniz: "))
if (girilen > 0):
    if (girilen % 3 == 0):
        print("Girdiğiniz sayı 3 ile tam bölünebilir")
    else:
        print("Girdiniz sayı 3 ile tam bölünemez")
else:
    print("Negatif bir sayı girdniz")            
"""



#********UYGULAMA ÖRNEK*******#

#1.SORU CEVABI
"""
girilen = int(input("Bir sayı giriniz: "))

if girilen >= 0:
    if  0 <= girilen <= 100:
        print("girdiğiniz sayı 0-100 aralındadır")
else:
    print("girilen sayı 0-100 değer aralığı dışındadır")
"""

"""
girilen = int(input("Bir sayı giriniz: "))

if 0 <= girilen <= 100:
    print("Girilen sayı 0-100 aralığndadır")
else:
    print("Girilen sayı 0-100 değer aralığnda değildir")
"""


#2.SORU CEVABI
"""
girilen = int(input("Bir sayı giriniz: "))

if girilen > 0:
    if (girilen % 2 == 0):
        print("Girilen sayı pozitif çift sayıdır")
    else:
        print("Girilen sayı pozitif tek sayıdır")
elif (girilen == 0):
    print("Girilen sayı sıfır dır")        
else:
    print("Sayı negatiftir")
"""


#3.SORU CEVABI
"""
girilen = input("Bir email adresi griniz: ")
girilenSifre = input("Bir parola giriniz: ")
Email = "email@sadıkturan.com"
parola = "abc123"

if (girilen == Email):
    if girilenSifre == parola:
        print("Hoş geldiniz")
    else:
        print("Parolayı yanlış girdiniz")
else:
    print("Email adresini yanlış girdiniz")            
"""

#4.SORU CEVABI
"""
girilen1 = int(input("1.sayıyı giriniz: "))
girilen2 = int(input("2.sayıyı giriniz: "))
girilen3 = int(input("3.sayıyı giriniz: "))

if (girilen1 > girilen2) and (girilen2 > girilen3):
    print("sayı sıralaması = 1.sayı > 2.sayı > 3.sayı")
elif (girilen2 > girilen3) and (girilen3 > girilen1):
    print("sayı sıralaması = 2.sayı > 3.sayı > 1.sayı")
elif (girilen1 > girilen3) and (girilen3 > girilen2):
    print("Sayı sıralaması = 1.sayı > 3.sayı > 2.sayı")
elif (girilen3 > girilen1) and (girilen1 > girilen2):
    print("Sayı sıralamsı = 3.sayı > 1.sayı > 2.sayı")
elif (girilen2 > girilen1) and (girilen1 > girilen3):
    print("Sayı sıralaması = 2.sayı > 1.sayı > 3.sayı ")
elif (girilen3 > girilen2) and (girilen2 > girilen1):
    print("Sayı sırlaması = 3.sayı > 2.sayı > 1.sayı")
else:
    print("hatalı girdiniz")
"""

#5.SORU CEVABI

"""
vize1 = int(input("1.Vize notunuzu giriniz: "))
vize2 = int(input("2.Vize notunuzu giriniz: "))
final = int(input("Final notunuzu giriniz: "))

ort = ((vize1 + vize2)*0.6) + (final*0.4)
print(ort)

if final >= 70:
    print("Tebrikler geçtiniz")
elif (ort >= 50):
    print("Tebrikler geçtiniz")    
else:
    print("Maalesef kaldınız")
"""

#6.SORU CEVABI




print("************KİLO BOY İNDEX HESAPLAMA*************")
name = input("İsminizi giriniz: ")
kg = float(input("Kilo değerinizi giriniz: "))
boy = float(input("Boy değerinizi giriniz: "))

index = (kg) / (boy**2)

if (10 < index <= 18.4):
    print(f"SAYIN {name}, KİLO İNDEXSİNİZ: {index} GURU TAHTA MI SİKSİN BU MİLLET AMINAGOYİM AZ KİLO AL")    
elif (18.5 <= index <= 24.9):
    print(f"SAYIN {name}, KİLO İNDEXSİNİZ: {index} KİLONUZ ÇOK GÜZEL TAM SİKİLECEK KIVAMDASINIZ, YALARIM")    
elif (25 <= index <= 29.90):
    print(f"SAYIN {name}, KİLO İNDEXSİNİZ: {index} YEYİP YEYİP SIÇMAMIŞSIN AMINAGOYİM")        
elif (30 <= index <= 34.9):
    print(f"SAYIN {name}, KİLO İNDEXSİNİZ: {index} GURBAN OLDUĞUM MİDENİ ALDIR, AMINA YİTELEDİĞİM")    
else:
    print(f"SAYIN {name} ÖLMÜŞSÜNÜZ AMINAGOYİM")







































