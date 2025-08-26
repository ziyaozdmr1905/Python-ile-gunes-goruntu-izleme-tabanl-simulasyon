# tekrar

"""
kitaplar = [
    [45623 , "Python" , "Mustafa" , "Başer" , 23],
    [99878 , "Linux Ağ Servisleri" , "Mustafa" , "Başer" , 26],
    [98938 , "İşletim Sistemleri" , "Ali" , "Saatçi" , 17],
    [98947 , "PHP ve AJAX" , "Haydar" , "Tuna" , 25]
]
while 1:
    kitapno = input("Kitap numarasını giriniz: ")
    if kitapno not in ['ç' , 'Ç']:
        for k in kitaplar:
            if (int(kitapno) == k[0]):
                print(f"{k[1]}, kitabının yazarı: {k[2]} {k[3]}, fiyatı: {k[4]} ")
                break
        else:
            print(kitapno, " numaralı kitap arşivde yok")
    else:
        break

"""

"""
while True:
    sayi = input("sayı giriniz (çıkmak için q basın):")
    
    if (sayi == "q"):
        print("Program sonlandırılıyor")
        break
    else:
        sayi = int(sayi)
        faktoriyel = 1
        for i in range(2 , sayi+1):
            faktoriyel *= i
        print("faktoriyel: " , faktoriyel)
"""


"""
def square(num): return num**2

res = square(9)
print(res)
"""
"""
def square(num): return num**2
numers = [1,2,3,9]

res = list(map(square,numers))
print(res)
"""

"""
numbers = [1,3,5,9]
res = list(map(lambda x: x ** 2, numbers))
print(res)
"""


"""
numbers = [1,3,5,9]
s = lambda num:num**2
res = list(map(s,numbers))

print(res)
"""


"""
numbers = [1,3,5,9,10,14]
#def cet(num): return (num % 2 == 0)

res = list(filter(lambda num: num % 2 == 0, numbers))
print(res)
"""



"""
numbers = [1,3,5,9,10,4]

cet = lambda num : num % 2 == 0
res = list(filter(cet, numbers))

print(res)
"""


"""
name = "çınar"
def chnage(new):
    global name
    name = new
    print(name)

chnage("ada")
print(name)    
"""

"""
def toplama(sayi1 , sayi2 ):
    return (sayi1 + sayi2)

print("Toplama:", toplama(3,4))
"""


# Fonksiyonlarda hesap makinesi
"""
def toplama(sayi1 , sayi2):
    return (sayi1 + sayi2)

def cikarma(sayi1 , sayi2):
    return (sayi1 - sayi2)

def carpma(sayi1 , sayi2):
    return (sayi1 * sayi2)

def bolme(sayi1 , sayi2):
    return (sayi1 / sayi2)


print("*******************\nToplama:1\nÇıkarma:2\nÇarpma:3\nBölme:4\nÇıkış:q\n********************")

while True:
    secim = input("Bir seçim yapın(çıkış: q): ")
    if (secim == "q"):
        exit()

    sayi1 = int(input("1.Sayı: "))
    sayi2 = int(input("2.Sayı: "))
    if (secim == "1"):
        print("Sonuç: ", toplama(sayi1 , sayi2))
    elif (secim == "2"):
        print("Sonuç: ", cikarma(sayi1 , sayi2))
    elif (secim == "3"):
        print("Sonuç: ", carpma(sayi1 , sayi2))
    elif (secim == "4"):
        print("Sonuç: ", bolme(sayi1 , sayi2))
    else:
        print("Yanlış seçim yapıldı.")
        exit()
"""

"""
sayi1 = int(input("1.Sayı: "))

sayi2 = int(input("2.Sayı: "))

def buyukolan(sayi1 , sayi2):
    
    while True:
        if (sayi1 < sayi2):
            print("2. sayı 1.sayıdan büyük")
            exit()
        elif (sayi1 > sayi2):
            print("1.sayı 2.sayıdan büyük")
            exit() 
        else:
            print("sayılar eşit")
            exit()       
        
buyukolan(sayi1 , sayi2)
"""

"""
def buyukOlan(x , y):
    if x > y:
        return x
    return y

number1 = int(input("Birinci sayıyı giriniz: "))
number2 = int(input("İkinci sayıyı giriniz: "))

biggernumber = buyukOlan(number1 , number2)
print(f"büyük olan sayı {biggernumber}")
"""

"""
def buyukOlan(x , y):
    if x > y:
        return x
    return y

def buyuk(a , b , c):
    aAndB = buyukOlan(a , b)
    return (aAndB , c)

number1 = int(input("Birinci sayıyı giriniz: "))
number2 = int(input("İkinci sayıyı giriniz: "))
number3 = int(input("Ücüncü sayıyı giriniz: "))

biggernumber = buyuk(number1 , number2 , number3)
#print(f"Büyük olan sayı: {biggernumber}")
print(biggernumber)
"""



"""
def maxOfTwo (x, y):
    if x > y:
        return x
    return y
 
def maxOfThree (a, b, c):
    aAndB = maxOfTwo(a, b)
    return maxOfTwo(aAndB, c)
 
number1 = int(input("Birinci sayıyı giriniz..."))
number2 = int(input("İkinci sayıyı giriniz..."))
number3 = int(input("üçüncü sayıyı giriniz..."))
 
biggerNumber = maxOfThree(number1, number2, number3)
print(biggerNumber)

"""
"""
liste = [1,4,5,6,7]

def carp(liste):
    total = 1
    for i in liste:
        total *= i
    return total    


newtotal = carp([1,4,5,6,7])
print(f"Çarpımları: {newtotal} ")
"""

"""
liste = [1, 2, 3, 4, 5, 6, 7]

def ikikat(liste):
    i = 0
    while i < len(liste):
        liste[i] = liste[i] * 2
        i += 1
    return liste    

newliste = ikikat([1, 2, 3, 4, 5, 6, 7])
print(f"İki katı alınırsa: {newliste} ")
"""

# asal mi
"""
def asalmi(sayi):
    if (sayi == 1):
        return False
    elif (sayi == 2):
        return True
    else:
        for i in range(2, sayi): #tam bölüyorsa asasl bir sayı değildir.
            if (sayi % i == 0):
                return False
            return True

while True:
    sayi = input("Bir sayı giriniz: ")
    if (sayi == "q"):
        print("Program sonlandı...")
        break
    else:
        sayi = int(sayi)

        if (asalmi(sayi)):
            print(sayi, "Sayı asal bir sayıdır...")
        else:
            print(sayi, "Sayı asal bir sayı değildir...")    
"""

#tam bölen bulma
"""
def tambolenbul(sayi):
    tambolen = []

    for i in range(2 , sayi):
        if (sayi % i == 0):
            tambolen.append(i)
    return tambolen
while True:
    sayi = (input("Bir sayı giriniz: "))
    if (sayi == "q"):
        print("Program sonlandırılıyor...")
        break
    else:
        sayi = int(sayi)
        print("Tam bölenleri: ", tambolenbul(sayi))
"""


"""
def mukemmel(sayi):

    toplam = 0
    for i in range(1 , sayi):
        if (sayi % i == 0):
            toplam += i
    return toplam == sayi # ÇOK ÇOK ÇOK ÇOK ÖNEMLİ DİKKAT ET RETURN İFADESİ YANLIŞ YERDE OLURSA PRO ÇALIŞMAZ

        # buraya kadar olan kısmında tam bölenlerin toplamı ve eşitliği yaptık

for i in range(1, 1001):

    if(mukemmel(i)):
        print("Mükemmel sayı: ", i)    
"""
        





"""
# MÜKEMMEL SAYİI ÖRNEĞİ
# for döngüsü ile mükemmel sayı yapımı
sayi = int(input("Bir sayı giriniz: "))
toplam = 0
for i in range(1,sayi):
    if (sayi % i == 0):
        toplam += i
    i += 1
if (toplam == sayi):
    print(sayi , "Mükemmel bir sayıdır...")

else:
    print(sayi , "Mükemmel bir sayı değildir...")
"""

# while döngüsü ile mükemmel bir sayı yapımı
"""
sayi = int(input("Bir sayı giriniz: "))

i = 1
toplam = 0

while i < sayi:
    if (sayi % i == 0):
        toplam += i
    i += 1
if (toplam == sayi):
    print(sayi , "Mükemmel bir sayıdır...")
else:
    print(sayi , "Mükemmel bir sayı değildir...")
"""         



"""
sayi = int(input("Bir sayı giriniz: "))

toplam = 0
for k in range(1, sayi):
    if (sayi % k ==0 ):
        toplam += k
    k += 1
if toplam == sayi:
    print(sayi , " sayısı mükemmel bir sayıdır...")
else:
    print(sayi ," sayısı mükemmel bir sayı değildir...")    
"""

"""
def mukemmel(sayi):
    toplam =  0
    for i in range(1, sayi):
        if (sayi % i == 0):
            toplam += i
    return toplam == sayi

for k in range(1 , 1001):
    if (mukemmel(k)):
        print(k ,"Sayı mükemmel bir sayıdır...")             
"""

"""
sayi = int(input("Bir sayı giriniz: "))
def tambol(sayi):
    tambolen = []
    for i in range(2 ,sayi):
        if (sayi % i == 0):
            tambolen.append(i)
    return tambolen

print(tambol(sayi))
"""


# EBOB BULMA SORUSU
"""
def ebob_bulma(sayi1 , sayi2):
    i = 1
    ebob = 1
    while (i <= sayi1 and i <= sayi2):
        
        if (not (sayi1 % i) and not (sayi2 % i)):
            ebob = i
        i += 1
    return ebob     
sayi1 = int(input("Sayi-1: "))
sayi2 = int(input("Sayi-2: "))

print("Ebob: ", ebob_bulma(sayi1 , sayi2))
"""


#EKOK BULMA SORUSU
"""
def ekok_bul(sayi1 , sayi2):
    ekok = 1
    i = 2
    while True:

        if (sayi1 % i == 0) and (sayi2 % i == 0):
            ekok *= i
           
            sayi1 //= i
            sayi2 //= i
        elif (sayi1 % i == 0 ) and (sayi2 % i != 0):
            ekok *= i
            sayi1 //= i
        elif ( sayi1 % i != 0) and (sayi2 % i == 0):
            ekok *= i
            sayi2 //= i
        else:
            i += 1
        
        if (sayi1 == 1 and  sayi2 == 1):
            break                     
    return ekok


sayı1 = int(input("Sayı-1:"))
sayı2 = int(input("Sayı-2:"))

print("Ekok:",ekok_bul(sayı1,sayı2))
"""

"""
birler = ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar = ["","on","yirmi","otuz","kırk","elli","atmış","yetmiş","seksen","doksan"]

def okunusu(sayi):
    birinci = sayi % 10
    ikinci = sayi // 10

    return onlar[ikinci]+ " " + birler[birinci]

sayi = int(input("Bir sayı girinz: "))

print(okunusu(sayi))
"""


