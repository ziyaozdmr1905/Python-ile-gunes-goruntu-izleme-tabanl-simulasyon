#PYTHON OPERATÖRLERİ

#ATAMA OPERATÖRÜ
"""
x=5
y=8
z=4
print(x,y,z)
"""

x , y , z = 5 , 10 , 20

# x,y=y,x  DEĞİŞKENLERDE DEĞİŞKİNLİK OLDU

# x = x + 2   BU YÖNTEM UZUN YÖNTEM DAHA KISA YÖNTEMLER VAR
 
###     x += 5     ###  KISA YÖNTEM 

# y -= 4   ÇIKARMA İŞLEMİ
# z /= 5   BÖLME İŞLEMİ
# x *= 8   ÇARPMA İŞLEMİ
# x %= 3   MOD ALMA 
# x //= 3  TAM BÖLME
# x **= 2  ÜS ALMA 
# y **= x

# values = (1,2,3)   # LİSTE OLUYORDU TUBLE LİSTESİ
# values = 1,2,3     # LİSTEDE OLUYORDU TUBLE İSTESİ

# values = 1,2,3,5,7,8,9

# print(values)
# print(type(values))

# x,*y,z = values

# print(x,y,z)


#UYGULAMA ÖRNEK

x,y,z = 2, 5, 10
number = 1, 7, 10, 6

#1.SORU CEVABI
"""
v = float(input("Bir sayı giriniz: "))

r = float(input("Bir sayı giriniz: "))
ret = (v*r)-(x+y+z)
"""

#2.SORU CEVABI
"""
y //= x
print(y)
"""

#3.SORU CEVABI
"""
v = x+y+z
v %= 3 
print(v)
"""
#4.SORU CEVABI
"""
y **= x
print(y)
"""

#5.SORU CEVABI
"""
x, *y, z = number  
v = z * z * z
print(v)
"""

#6.soru cevabı
"""
x, *y, z = number  
v = y[0] + y[1]
print(v)
"""

#KARŞILAŞTIRMA OPERATÖRLERİ

#  (== ) OPERATÖRÜ



a, b, c, d=5, 5, 10, 4
#r= (a==b)

#r= (a==c)

"""
password = '1234'

username = 'sadikturan'

r= ('sadikturan'== username)
"""

# (!=) OPERATÖRÜ

#r = (a != b)
#r = (a != c)

# (>) OPERATÖRÜ
#r = (a > b)
#r = (d > b )

# (<) OPERATÖRÜ
#r= (a<b)

# (>=) OPERATÖRÜ
#r = (a >= b)
#print(r)

# UYGULAMA ÖRNEK

#1.SORU CEVABI
"""
v = int(input('v: ' ))
t = int(input('t: '))
r = (v > t)
print(f'v: {v} t: {t} den büyüktür: {r}')
"""
#2.SORU CEVABI
"""
vize1 = float(input('vize1: '))
vize2 = float(input('vize2: '))
final = float(input('final: '))

ort =float(((vize1+vize2)/2)*0.6) + float(final*0.4)

print(f"Not ortalamanız: {ort} ve dersten geçme durumunuz {ort >= 50}")
"""
#3.SORU CEVABI
"""
sayi = int(input('sayı: '))
tekcift = float(sayi % 2 == 0)

print(f"Girilen sayı çift olma durumu: {tekcift}")
"""
#4.SORU CEVABI
"""
sayi = int(input('sayı: '))
negatif = (sayi < 0)
print(f'sayının negatif olma durumu: {negatif}')
"""
#5.SORU CEVABI
"""
email = 'sadıkturan@gmail.com'
passport = '12345678'

e = input('Email adresi giriniz: ')
p = input('şifrenizi giriniz: ')

isr = (email == e.lower().strip())
isp = (passport == p.lower())

print(f'email bilgisi doğru mu {isr} parola bilgisi doğru mu {isp}')
"""