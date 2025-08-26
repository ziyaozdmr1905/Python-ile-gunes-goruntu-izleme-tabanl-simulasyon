# continue ve break ifadeleri
"""
i = 1
while True:
    print(i)
    print("şimdi i sayının 5 olup olmadığını sınayalım")
    if i == 5:
        break
    print("karşılaştırma yapıldı ve döngü durmadı")    
    i += 1
"""

"""
print("programdan çıkmak için [ç] harfi girin.")
while True:
    i = (input("karakök alınacak bir sayı giriniz: "))
    if i == 'ç':
        print("[ç] girdiniz programdan çıkılıyor.")
        break
    if int(i) < 0:
        print("karmaşık şimdilik hesapayamıyorum")
        continue
    k = int(i) ** (1/2)
    print("girdiğiniz sayının karakökü: ",k)
"""


"""
print("programdan çıkmak için [ç] harfi girin.")
while True:
    i = (input("karakök alınacak bir sayı giriniz: "))    
    if i == 'ç':
        print("[ç] girdiniz programdan çıkılıyor.")
    elif int(i) < 0:
        print("karmaşık şimdilik hesaplayamıyorum")
    else:
        k = int(i) ** (1/2)
        print("girdiğiniz sayının karakökü: ",k)
"""

"""
print("ülkemizin en güney ili hangisidir")
print("sadece iki şansınız var.")
girilen = ""
i = 1
while i <= 2:
    print(i,'.şans')
    girilen = input("Bir il giriniz: ")
    if girilen == "Hatay":
        print("tebrikler en güney ilimiz hatay dır.")
        break
    i += 1
else:
    print("üzgünüm ki şansınızıda denediniz ve kaybettiniz.")     
"""

"""
girilen = ""

while (girilen != "ç"):
    girilen = input("Bir sayı giriniz. Çıkmak için [ç]: ")
    if (girilen == "ç"):
        print("çıkmak istediniz program sonlandı")
    else:
        girilen = float(girilen)
        print("Girdiniz sayının karekökü: ",girilen**(1/2))
"""

"""
a = 10
while (a<14):
    print("a nın değeri: ",a)
    a +=1
"""
"""
a = 1
while (a < 13):
    print(a,". sınıf")
    a += 1
"""
"""
while True:
    sayi = int(input("1-5 arasında bir sayı giriniz: "))
    if( sayi == 3):
        break
print("3 sayısı girildi ve döngü sona erdi")    
"""

"""
while True:
    sifre = input(" En az 8 karakterli şifre giriniz: ")
    if(len(sifre) == 8):
        print("Şifreniz kaydedildi")
        break
    print("Şifreniz 8 karakterli olmalıdır")
"""

#girilen metni alt alta yazdıran program
"""
girilen = input("Bir metin giriniz: ")
for x in girilen:
    print(x)

"""

"""
isim = input("Adınızı giriniz: ")
sayac = 0
while sayac < len(isim):
    print(isim[sayac])
    sayac += 1
else:
    print("Adının harflerini listeledim")    
"""

"""
a = 1
while a <= 100:
    if a%2==0:
        print(a, end =",")
        a += 1
"""

"""
toplam = 0
a = 0
while a<=100:
    toplam = toplam + a
    a += 1
print("sayıların toplamı: ",toplam)
"""
"""
# q harfi girince dögüden çık demekttir break kullandık çünkü. ve liste karşımıza çıkar
liste = []
while True:
    urun = input("ürün adı giriniz: ")
    if urun =='q':
        break
    liste.append(urun)
print("girdiniz meyveler: ",liste)    
"""

#while döngüleri
# yan yana yazdırmak için end komutu kullamılır
"""
x = 0
while x < 50:
    print(x , end= ",")
    x += 1
"""

# 0-100 arası tek sayılar yazdırdık
"""
x = 0
while x < 100:
    if (x % 2 == 1):
        print(x , end=",")
    x += 1
print("bitti..")    
"""
# 0-100 arası çift sayıların toplamını yapalım
"""
x = 0
toplam = 0

while x <= 100:
    x += 1    #bunu hemen while döngüsünün altına yazdık ki x artsın ve döngü devam etsin
    if (x % 2 == 1):   #koşulu buraya yazdık bilerek ki altına continue ifadesi geldi yani devam et dedi
        continue     # tek sayıları atsın diye koşulu tek sayılara ekledik
    toplam += x
print(f"toplam {toplam}")
"""

"""
toplam = 0
x = 0
while x <= 100:
    toplam += x
    x += 1
print(f"toplam {toplam}")
"""        

"""
x = 1 
while x <= 100:
    if (x % 2 == 1):
        print(f"Sayı tek: {x}")
    else:
        print(f"Sayı çift: {x}")
    x += 1
print("Bitti...")    
"""


name = 'sadık turan'
"""
for nam in name:
    print(nam , end=",")
"""
"""
for x in name:
    if x == 'u':
        break
    print(x, end="/")
"""
"""
for x in name:
    if x == 'u':
        continue
    print(x,end=',')
"""
"""
x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1
"""
# bu iafde yanlış bir ifade 
"""
x = 0
while x < 5:
    if x == 2:
        continue
    print(x)
    x += 1
"""
# x += 1 ifadesini continue ifadesinden önceye getirdim ki program çalışsın
"""
x = 0
while x < 5:
    x += 1
    if x == 2:
        continue
    print(x)
"""    

"""
for item in range(10):
    print(item,end=',')
"""
"""
for x in range(50,100,20):
    print(x,end=',')
"""


# enumarate metodu
"""
index = 0
gree = 'hello'

for x in gree:
    print(f"index: {index} x : {x}")
    index += 1

#enumarate
gree = 'hello'
for index,x in enumerate(gree):
    print(f"index : {index} x : {x} ")
"""
"""
gree = 'Hello'
for x in enumerate(gree):
    print(x,end=',')

"""

# zip metodu
"""
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
print(list(zip(list1,list2)))
"""

"""
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']

for a,b in zip(list1,list2):
    print(a,b)
"""
"""
num = [x for x in range(10)]
print(num)
"""
"""
num = [x*x for x in range(10) if x % 3 == 0]
print(num)
"""
"""
num = [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(num)
"""

"""
import random

hak = int(input("Kaç defada bilebilirsin: "))
i = 1
puan = 100
x = random.randint(0,100)

while i <= hak:
    girilen = int(input("Tahmin ettiğiniz sayıyı giriniz: "))
    print(i,". Hakkınız: ")
    if (girilen == x):
        print("Tebrikler doğru bildiniz")
        print(x,puan)
        break 
    i += 1
    puan -= (puan/hak)
    if (girilen != x):
        print(f"Maalesef yeniden deneyin ve puanınız: {puan}")
        continue
else:
    print("Bilemediniz sayı: ",x)
    print(f"puanınız: {puan}")
"""

"""
import random

hak = int(input("Kaç defada bilebilirsin: "))
i = 1
puan = 100
x = random.randint(0,100)

while i <= hak:
    girilen = int(input("Tahmin ettiğiniz sayıyı giriniz: "))
    print(i,". Hakkınız: ")
    if (girilen == x):
        print("Tebrikler doğru bildiniz")
        print(x,puan)
        break 
    elif (x > girilen):
        print("Yukarı")
    else:
        print("Aşağı")   
    i += 1
    puan -= int(puan/hak)
else:
    print("Bilemediniz sayı: ",x)
    print(f"puanınız: {puan}")
"""

#asal sayı bulma

sayi = int(input("Bir sayi giriniz: "))




