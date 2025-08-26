#pythın sets listeleri


fruits={'orange','apple','banana','banana','orange'}
#print(fruits)

#for x in fruits:
#    print(x)


#fruits.add('cherry')               eleman ekleme

#fruits.update(['mango','grape'])   bu metot listeleme yöntemi ile ekleme yapar

#fruits.remove('banana')            daha önceden gördüştük silme işlemi yapıyor

#fruits.discard('banana')           remove gibi silme işlemi yapıyor

#print(set(fruits))                 set metodu aynı elemandan birden fazla var ise teke düşürüp öyle yazar



#KARAKTER DİZİLERİ STRİNG İFALERİ EN BAŞTAN BAŞLIYORUZ

# name='sadık'
# surname='turan'
# age= 36

#print("My name is " + name + " " + surname + " I'm "+  str(age) + " years old.")

"""
deneme="My name is "
deli=" I'm "
ful= " years old."
print(deneme + name + " " + surname + deli + str(age) + ful)


cümle= " My name is " + name + " " + surname + " and\n I'm " + str(age) + " years old."
print(cümle[3:7])
"""

"""
#STRİNG FORMATLAMA 
name='çınar'
surname='turan'
age=36
"""
#print("My name is {n} {s}".format(n=name, s=surname))

#result=200/700

#print('The result is {r:1.4}'.format(r=result))

# f STRİNGİ VAR DAHA KOLAY
#print(f"My name is {name} {surname} and I'm {age} years old ")

#UYGULAMA
website="http://www.sadıkturan.com"

course="Python kursu: Baştan sona kadar python programlama rehberimiz(40 saat) "

"""
#1.SORU CEVABI
print(len(course))
print(len(website))

#2.SORU CEVABI
print(website[7:10])

#3.SORU CEVABI
print(website[22:])
print(website[-3:])

#4.SORU CEVABI
print(course[:15])
print(course[-15:])
print(website[:15])
print(website[-15:])

#5.SORU CEVABI
print(course[::-1])
print(website[::-1])

#6.SORU CEVABI
name, surname, age, job="Bora", "Yılmaz", 36 , "mühendis" 
sel=f"Benim adım {name} soyadım {surname}. Yaşım {age} ve mesleğim {job} "
print(sel)

#7.SORUNUN CEVABI
sel="Hello world"
sel=sel[0:6] + " W" + sel[-4:] 
print(sel)

#8.SORUNUN CEVABI
w='abc'*3
print(w)
"""

#STRİNG METOTLARI

#message="Hello There. My name is sadık turan"

#UPPER MOTODU
#message=message.upper()

#LOWER METODU
#message=message.lower()

#TİTLE METODU
#message=message.title()

#CAPİTALİZE METODU
#message=message.capitalize()

#STRİP METODU
#message=message.strip("turan")

#SPLİT METODU
#message=message.split()

#JOİN METODU
#message=message.split()
#message="*".join(message)

#FİND METODU
#message=message.find("sadık")

#İNDEX METODU
#message=message.index("a")

#STARTSWİTH METODU
#message=message.startswith("H")


#ENDSWİTH METODU
#message=message.endswith("n")

#REPLACE METODU
#message=message.replace("turan","taş")

#CENTER METODU
#message=message.center(150)

#CASEFOLD METODU
#message=message.casefold()

#COUNT METODU
#message=message.count("My")

#İSHALPHA METODU
#message=message.isalpha()

#İSALNUM METODU
#message=message.isalnum()

#İSDİGİT METODU
#message=message.isdigit()

#İSİDENTİFİER METODU
#message=message.isidentifier()

#İSLOWER METODU
#message=message.islower()

#İSNUMERİC METODU
#message=message.isnumeric()


#İSPRİNTABLE METODU
#message=message.isprintable()

#İSTİTLE METODU
#message=message.istitle()

#İSUPPER METODU
#message=message.isupper()

#PARTİTİON METODU
#message=message.partition("My name")

#RFİND METODU
#message=message.rfind("My")

#SWAPCASE METODU
#message=message.swapcase()

#print(message)


#STRİNG METOT UYGULAMASI

website="http://www.sadıkturan.com"

course="Python kursu: Baştan sona kadar python programlama rehberimiz(40 saat) "

#1.SORU CEVABI
# sel=" Hello world "
# sel=sel.strip()
# print(sel)

#2.SORU CEVABI
# sel="www.sadıkturan.com"
# sel=sel.rstrip(".com")
# sel=sel.lstrip("www.")
# print(sel)

#3.SORU CEVABI
# course=course.lower()
# print(course)

#4.SORU CEVABI
# website=website.count("a")
# print(website)

#5.SORU CEVABI
#website=website.endswith(".com")
# website=website.startswith("www")
# print(website)

#6.SORU CEVABI
#website=website.find(".com")
#website=website.index(".com")
#website=website.find(".com",0,30)    0 ile 30. index aralığında var mı diye bakar
#print(website)

#7.SORU CEVABI
# course=course.isnumeric()
# print(course)

#8.SORU CEVABI
# x="countents"
# x=x.center(50)
# x=x.replace(" ","*")
# print(x)

#9.SORU CEVABI
# course=course.replace(" ", "-" )
# print(course)

#10.SORU CEVABI
# x="Hello world"
# x=x.replace("Hello","There")
# print(x)

#11.SORU CEVABI
# course=course.split(" ")
# print(course)

