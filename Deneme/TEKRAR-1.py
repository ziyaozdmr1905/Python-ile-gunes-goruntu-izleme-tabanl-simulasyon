#EN BAŞTAN TEKRAR
"""
pi = 3.14
r = 2
x = 2*pi*r
print("DAİRENİN ÇEVRESİ: ", x)
"""
"""
x = 7
y = (x+13)/4
z = x+13/4
v = 2*x+9
b = (7+x)/2**2
n = ((7+x)/2)**2
print(y)
print(z)
print(v)
print(b)
print(n)
"""
"""
x = "9" + "9"
print(x)
"""
"""
u = 20
k = 3
p = u-18
p = str(p)
y =3*p
print(y)
"""
"""
vi = 100
sin53 =0.8
cos53= 0.6
g = 10
vix = vi*cos53
viy = vi*sin53
tcik = viy/9
tuc = 2*tcik
r = vix*tuc

print(vix)
print(viy)
print(tcik)
print(tuc)
print(r)
"""
#def kullanımı
"""
def f(x):
    print("x paremetresini aldığı değer: ",x)
f(3)
"""
"""
girilen = input("bir sayı giriniz: ")
if int(girilen) < 10:
    print("girdiniz sayı 10 dan daha küçük")
else:
    print("girilen sayı 10 dan büyük")
"""

"""
print("Çorum,Sivas ve Kayseri ile komşu olan ilimiz hangisidir ?")
girilen = input("bir şehir giriniz: ")

if (girilen == "Yozgat") or (girilen == "nevşehir"):
    print("Tebrikler cevabınız doğru") 
else:
    print("Maalesef cevabınız yanlış")
"""
"""
girilen = int(input("sayı: "))
if (girilen % 2 == 0):
    print("sayı çift sayıdır")
elif(girilen == 0):
    print("sayı sıfırdı")
else:
    print("sayı tek sayıdır")
"""
"""
i = 1
while (i <= 5):
    print(i)
    i += 1
"""
"""
i = 5
c = 1
while (i > 0):
    c = i * c
    i -= 1
print(c)    
"""
"""
i = 1
while (i < 11):
    print(i, "* 5 = ", i*5)
    i += 1
"""
"""
girilen = ""
while ( girilen != "ç"):
    girilen = input('bir sayı giriniz. çıkmak için [ç]: ')
    if (girilen == "ç"):
        print("Çıkmak istediniz program sonlandı")
    else:
        girilen = float(girilen)
        print("Girdiğiniz sayının karakökü: ", girilen**(1/2))
"""
"""
x = 10
if not (x == 3 or x > 9):
    print("Sayı belirtilen aralıkta")
else:
    print("Bu sayıyı istememiştik")
"""
"""
x = 10
if not x == 3 or x > 9:
    print("Sayı belirtilen aralıkta")
else:
    print("Bu sayıyı istememiştik")
"""
"""
i = 1
while i < 6:
    j = 1
    while j < 6:
        print(i , j , i*j*'*')
        j = j + 1
    i += 1    
"""

"""
x = 0

while x < 5:
    if x == 2:
        continue
    print(x)
    x += 1
"""


"""
markalar = []

marka =input("Marka: ")
markalar.append(marka)

marka =input("Marka: ")
markalar.append(marka)

marka =input("Marka: ")
markalar.append(marka)

print(markalar)
"""



# eksik çalıştı
"""
marka = input("Marka: ")
marka1 = input("Marka: ")
marka2 = input("Marka: ")
marka3 = input("Marka: ")

def listeOlustur(*artı):  # '*' yıldızı koymadğım için bir saaat uğraştım. sebebi aşağıda yazılı
    liste = []
    if (len(artı) < 6):
        liste.append(artı)
        return liste
    
print(listeOlustur(marka,marka1,marka2,marka3)) #SEBEBİ: çünkü burada 4 tane bileşeni yan yana yazamıyorduk izin vermiyordu. * sınırsız parametre yazmamızı sağlar
"""


# eksik çalıştı
"""
marka = input("Marka: ")
marka1 = input("Marka: ")
marka2 = input("Marka: ")
marka3 = input("Marka: ")

def listeOlustur(*artı):  # '*' yıldızı koymadğım için bir saaat uğraştım. sebebi aşağıda yazılı
    liste = []
    if (len(liste) < 4): 
        liste.append(artı)
    return liste
    
print(listeOlustur(marka,marka1,marka2,marka3)) #SEBEBİ: çünkü burada 4 tane bileşeni yan yana yazamıyorduk izin vermiyordu. * sınırsız parametre yazmamızı sağlar
"""

"""
girilen1 = input("Bir meyve yazınız: ")

meyve = []

if (len(girilen1) < 5):
    meyve.append(girilen1)
else:
    print("Harf fazla")

print(meyve)
"""

"""
girilen = input("Meyve: ")

def listeolustur(girilen):
    liste = []
    if (len(girilen) < 5):

        liste.append(girilen)
        return liste          # return komutunu koymadığım için çalışmadı önemli bir konudur unutma
    else:
        print("Harf fazla")
        return liste
print(listeolustur(girilen))

"""



# hatalı çalışmıyor
"""
girilen = input("Meyve: ")
girilen1 = input("Meyve: ")
girilen3 = input("Meyve: ")


def listeolustur(girilen ,girilen1 , girilen3):
    liste = []
    for i in (girilen, girilen1, girilen3):
        if (len(i) < 5):

            liste.append(i)
            return liste          # return komutunu koymadığım için çalışmadı önemli bir konudur unutma
        else:
            print("Harf fazla")
            return liste
print(listeolustur(girilen, girilen1, girilen3))
"""

"""
def tambolenleribul(sayi):
    tambolenler = []
    for item in range(2 , sayi):
        if (sayi % item == 0):
            tambolenler.append(item)
    return tambolenler    # önemli return ifadesi for döngüsünğn bittiğini gösterecek yoksa program yanlış çalışıyor
print(tambolenleribul(20))
"""


# girilen iki sayı arasında kalan asal sayıları ekrana yazdıran kod
"""
sayi1 = int(input("Sayı: "))
sayi2 = int(input("Sayı: "))
def asalsayilariBul(sayi1 , sayi2):
    for sayi in range(sayi1, sayi2):
        if sayi >1:
            for i in range(2, sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)
asalsayilariBul(sayi1 , sayi2)                     
"""

"""
def toplama(a,b):
    return a+b

def ortalama(a,b):
    t = toplama(a,b)
    return t/2
print(ortalama(8,9))    
"""

"""
def kareal(a,b,c):
    return b**2
def delta(a,b,c):
    d = kareal(a,b,c)
    return d-4*a*c
print(delta(2,4,7))        
"""


"""
A = int(input("Sayı: "))
B = int(input("Sayı: "))
C = int(input("Sayı: "))

def kareal(A,B,C):
    return B**2
def islem(A,B,C):
    k = kareal(A,B,C)    
    return k -4*A*C
def toplma(A,B,C):
    d = islem(A,B,C)
    return toplma
def delta(A,B,C):
    X1 = (- k - toplma**(1/2))/(2*A)    
    X2 = (k - toplma**(1/2))/(2*A) 
    
    print(X1)
    print(X2)

print(delta(A,B,C))    
"""
"""
x = int(input("Birinci sayıyı giriniz: "))
y = int(input("İkinci sayıyı giriniz: "))
z = int(input("Üçüncü sayıyı giriniz: "))

t = x * y * z
print("Çarpımları: {0} ".format(t))
"""
"""
x = int(input("Kilo değerini giriniz: "))
y = float(input("Boy değerini giriniz: "))

indexi = x / (y * y)
print(f"Bende kilo boy indexsiniz: {indexi}")
"""


"""
px = input("DÖRTGEN mi bulmak istiyorsunuz yoksa ÜÇGEN mi?: ")


if (px == 'üçgen'):
    x = int(input("1. kenar : "))
    y = int(input("2. kenar : "))
    z = int(input("3. kenar : "))
    if ((x + y > z) and (x + z > y) and (z + y > x)):
        if (x == y != z):
            print("Bu üçgen bir ikizkenar üçgendir")
        elif (x == y == z):
            print("Bu üçgen bir eşkenar üçgendir")
        else:
            print("Normal bir üçgendir")
    else:
        print("Bu koşullar bir üçgen belirtmiyor")                

elif (px == 'dörtgen'):
    x = int(input("1. kenar : "))
    y = int(input("2. kenar : "))
    z = int(input("3. kenar : "))
    v = int(input("4. kenar : "))
    if (x == y == z == v):
        print("Bu bir karedir")
    elif (x == y) != (z == v):
        print("Bu bir Dikdörtgendir")
    elif (x != y != z != v):
        print("Bu bir dörtgendir")
    else:
        print('hatalı giriş')            
else:
    print("Htalı giriş")        
"""