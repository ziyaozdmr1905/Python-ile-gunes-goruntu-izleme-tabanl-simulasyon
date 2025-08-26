#MANTIKSAL OPERATÖRLER
"""
x = 5
res = 5 < x < 10
print(res)
"""
#*******AND OPERATÖRÜ*******#
#true , true => true
#true , false => false  sadece bir true olması lazım 
"""
x = 6
result = (x > 5) and (x < 10)
print(result)
"""
"""
hak = 0
devam = "e"
res = (hak > 0) and (devam == "e")
print(res)
"""


#********OR OPERATÖRÜ********#
#true , false => true
#true , true => true
#false , false => false
"""
x= 5
res = (x > 0) or (x % 2 ==0)
print(res)
"""

#**********NOT OPERATÖRÜ**********#
#tam tersini alır
"""
x = 5 
res = not(x > 0 )
print(res)
"""
"""
x = 7
res = ((x > 5) and (x < 10) or (x % 2 == 0))
print(res)
"""

#*********UYGULMA ÖRMEK*********#

#1.SORU CEVABI
"""
x = int(input("sayı giriniz: "))
res = (x > 0 ) and (x < 100)
print(res)
"""

#2.SORU CEVABI
"""
x = int(input("sayı giriniz: "))
res = (x > 0) and (x % 2 == 0)
print(res)
"""

#3.SORU CEVABI
"""
Email = "email@sadikturan.com"
parola = "abc123"

girilenEmail  = input("Email: ")
girilenParola = input("Parola: ")

res = (girilenEmail == Email.lower().strip()) or (girilenParola == parola.lower())
print(res)
"""
#4.SORU CEVABI
"""
x = int(input("1.sayıyı gir: "))
y = int(input("2.sayıyı gir: "))
z = int(input("3.sayıyı gir: "))
bir = (x > y) and (x > z)
iki = (y < x) and (y > z)
üc = (z < x) and (z < y)
res = f"1.sayı en büyüktür x:{bir}, 2.sayı ortancadır y:{iki}, 3. en küçük sayı z:{üc}"
print(res)
"""

#5.SORU CEVABI
""" 
vize1 = float(input("1.vize notu : "))
vize2 = float(input("2.vize notu: "))
final = float(input("final notu: "))

ort = ((vize1 + vize2)/2)*(0.6) + (final*(0.4))

gecti = ((ort >= 50) and (final > 50)) or (final >= 70)
print(ort)
print(gecti)
"""

#6.SORU CEVABI

name = input("isminizi giriniz: ")
boy = float(input("boyunuzu giriniz : "))
kilo = float(input("kilonuzu giriniz: "))

formul = (kilo / boy**2)

zayıf = (formul >= 0) and (formul <= 18.4)
normal = (formul >= 18.5) and (formul <= 24.9)
kilolu = (formul >= 25.0) and (formul <= 29.9)
sisman = (formul >= 30.0) and (formul <= 34.9)


print(formul)
print(f"{name} kilo indexsin : {formul} ve kilo değerlendirmen zayıf: {zayıf}")
print(f"{name} kilo indexsin : {formul} ve kilo değerlendirmen normal: {normal}")
print(f"{name} kilo indexsin : {formul} ve kilo değerlendirmen kilolu: {kilolu}")
print(f"{name} kilo indexsin : {formul} ve kilo değerlendirmen şişman: {sisman}")








































