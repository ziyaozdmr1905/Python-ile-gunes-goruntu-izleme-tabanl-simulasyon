'''
x=5
y=2.5
name='çınar'
isOnline=False

# result= x + y
# print(result)
# print(type(result))

# isOnline = str(isOnline)
# print(isOnline)
# print(type(isOnline))

isOnline= int(isOnline)
print(isOnline)
print(type(isOnline))
'''

"""
r=float(input("Yarı çap giriniz: "))     #eğer float girmeseydik kesirli çıkıyo diye yani otomati int alıyo oyüzden hata verirdi.
Pi=3.14
alan=Pi*(r**2)
cevre= 2*Pi*r
print("Alan: ", alan)
print("Çevre: ", cevre)
"""

website= "http://www.sadikturan.com"
course="python kursu: Baştan sona python programlama rehberiniz (40 saat)"

"""
#1. SORU ÇÖZÜM 
# rstrip İLE SAĞ TARAFTAKİ KARAKTERLERİ SİLDİRİRİZ
# lstrip İLE SOL TARAFTAKİ KARAKTERLERİ SİLDİRİRİZ
x="Hello World"
#x=x.strip()
x=x.rstrip("d")
x=x.lstrip()
print(x)
"""
"""
#2. SORU ÇÖZÜMÜ
x="www.sadikturan.com"
x=x.rstrip(".com")
x=x.lstrip("www.")
print(x)
"""
"""
#3. SORU ÇÖZÜMÜ
x=course.lower()
print(x)
"""
"""
#4. SORU ÇÖZÜMÜ
x=website.count("a")
print(x)
"""
"""
#5. SORU ÇÖZÜMÜ
#x=website.startswith("www")
#x=website.endswith(".com")
print(x)
"""
"""
#6. SORU ÇÖZÜMÜ
index=website.index(".com")
print(index)
"""
"""
#7. SORU ÇÖZÜMÜ
x=course.isalpha()
print(x)
"""
"""
#8. SORU ÇÖZÜMÜ
x="countents"
x=x.center(50)
x=x.replace(" ", "*")
print(x)
"""
"""
#9. SORU ÇÖZÜMÜ
x=course.replace(" ","-")
print(x)
"""
"""
#10. SORU ÇÖZÜMÜ
x="Hello World"
x=x.replace("World", "There")
print(x)
"""
"""
#11. SORU ÇÖZÜMÜ
x=course.split(" ")
print(x)
"""