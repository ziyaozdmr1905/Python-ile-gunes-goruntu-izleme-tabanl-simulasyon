
"""
def toplam(a , b):
    return a + b

print(toplam(1 , 2))    
"""
"""
def yasHesapla(dogum):
    return 2023 - dogum

agecınar = yasHesapla(2002)
ageeda = yasHesapla(1997)
agetimur = yasHesapla(2010)


print(agecınar , ageeda , agetimur)
"""
"""
def sehir(n):
    n[0] = 'istanbul'
sehirler = ["ankara" , "izmit"]

sehir(sehirler)
print(sehirler)
"""
"""
sehirler = ["ankara" , "izmit"]
n = sehirler[:]

n[0] = "istanbul"


print(sehirler)
print(n)
"""
"""
def add(a , b):
    return sum((a , b))

print(add(10 , 20))    
"""

"""
def add(a, b, c ):

    return sum((a , b , c))

print(add(10 , 20 , 30))
"""
"""
def add(*params):
    return sum((params))


print(add(10 ,20 , 30, 40))

print(add(50 ,10 , 60, 40))

print(add(10 ,220 , 70, 140))

"""

"""
def add(*params):
    arti = 0
    for n in params:
        arti = arti + n
    return arti

print(add(10, 20, 50))
print(add(10, 30, 70))
print(add(15, 55, 50, 45 , 65))
"""

"""
def add(**user):
    for key, value in user.items():
        print("{} is {}".format(key , value))


add(name = 'çınar' , age = 2 , city = 'istanbul') 


"""
"""
def listeyecevir(*params):
    liste = []
    for param in params:
        liste.append(param)
    return liste

res = listeyecevir(10 , 20 , 30 , 'merhaba')
print(res)
"""

"""
sayi1 = int(input("Sayı 1 :"))

sayi2 = int(input("Sayı 2 :"))

def asalsayilaribul(sayi1 , sayi2):
    for sayi in range(sayi1 , sayi2 + 1):
        if sayi > 1:
            for i in range(2 , sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)

asalsayilaribul(sayi1 , sayi2)

"""

"""
def tambolenelribul(sayi):
    tambolenelr = []
    for i in range(2 , sayi):
        if (sayi % i == 0):
            tambolenelr.append(i)
    return tambolenelr

print(tambolenelribul(20))            
"""


# lambda , map , filter
"""
def deri(num): return num**2
numbers = [1 , 3 , 5 , 9]

res = list(map(deri , numbers))

print(res)

"""


"""
numbers = [1, 3, 5, 9]

res = list(map(lambda num: num**2 , numbers))

print(res)
"""

"""
numbers = [1, 3, 5, 9]

sq = lambda num: num**2

res = list(map(sq , numbers))
print(res)
"""
"""
sq = lambda num: num**2
res = sq(3)
print(res)
"""

"""
sayi = int(input("Bir sayı giriniz: "))

sq = lambda num: num**3
res = sq(sayi)
print(res)
"""

"""
numbers = [1, 2, 3, 6, 5, 8, 9]
def say(num): 
    return num % 2 == 0

res = list(filter(say , numbers))
print(res)
"""
"""
numbers = [1, 2, 3, 6, 5, 8, 9]

res = list(filter(lambda num: num % 2 == 0 , numbers))
print(res)
"""
"""
numbers = [1, 2, 3, 6, 5, 8, 9]

cehc = lambda num: num%2==0
res = list(filter(cehc , numbers))
print(res)
"""




"""
SadıkHesap = {
    'Ad' : 'Sadık turan',
    'HesapNo' : '123456',
    'Bakiye' : 3000,
    'EkHesap' : 2000
}



AliHesap = {
    'Ad' : 'Ali turan',
    'HesapNo' : '456789',
    'Bakiye' : 2000,
    'EkHesap' : 1000
}



def  paracek(hesap , miktar):
    print(f"Merhaba {hesap['Ad']}")

    if(hesap['Bakiye'] >= miktar):
        hesap['Bakiye'] -= miktar
        print("Paranızı alabilirsiniz..")
        #bakiyesorgula(hesap)
    else:
        toplam = hesap['Bakiye'] + hesap['EkHesap']
        if toplam >= miktar:
            ekhesapkullanımı = input("Ek hesap kullanıldı mı (E / H): ")

            if ekhesapkullanımı == 'E':
                ekhesapkullanılacakmiktar = miktar - hesap["Bakiye"]
                hesap['Bakiye'] = 0
                hesap['EkHesap'] -= ekhesapkullanılacakmiktar
                print('paranızı alabilirsiniz..')
                #bakiyesorgula(hesap)
            else:
                print(f"{hesap['HesapNo']} nolu hesabınızda {hesap['Bakiye']} bulunmaktadır.")
        else:
            print("Üzgünüz bakiye yetersiz.")
            #bakiyesorgula(hesap)

#def bakiyesorgula(hesap):

paracek(AliHesap, 3000)
paracek(SadıkHesap , 3000)

"""

# SINIFLAR 

"""
class Person:
    pass
    address = 'no information'
    def __init__(self, name, year):
        self.name = name
        self.year = year
        print("init metodu çalıştı")
        #print(f"benim adım {name} ve yaşım {2022 - year} ")
p1 = Person(name="ali", year= 1997)
p2 = Person(name="yağmur",year=2000)

p1.address = "kocaeli"
p2.address = "adana"

print(f"p1: name: {p1.name} year: {p1.year} address: {p1.address} ")

print(f"p2: name: {p2.name} year: {p2.year} address: {p2.address} ")
"""
"""
class person:
    address = "information"
    def __init__(self,name,year):
        self.name = name
        self.year = year
    def intro(self):
        print("Hello There")    

p1 = person(name="Ali", year= 1998)
p2 = person(name="Yağmur",year= 1997)

p1.intro()  #parantezler önemli, yazılmazsa kod çalışmaz
p2.intro()
"""



"""
class person:
    address = "information"
    def __init__(self,name,year):
        self.name = name
        self.year = year
    def intro(self):
        print("Hello There. I am " + self.name)
    def calculateAge(self):
        return 2020 - self.year        

p1 = person(name="Ali", year= 1998)
p2 = person(name="Yağmur",year= 1997)


print(f"Adım {p1.name} ve yaşım {p1.calculateAge()} ")

print(f"Adım {p2.name} ve yaşım {p2.calculateAge()} ")

p1.intro()  #parantezler önemli, yazılmazsa kod çalışmaz
p2.intro()
"""


"""
class circle:
    pi = 3.14
    def __init__(self, yaricap = 1):
        self.yaricap = yaricap
    def cevre_hesapla(self):
        return 2 * self.pi * self.yaricap
    def alan_hesapla(self):
        return self.pi * (self.yaricap ** 2)        
c1 = circle()
c2 = circle(5)  # yarı çap belirttim belirtmezsek 1 olrak alır

print(f"c1: alan: {c1.alan_hesapla()} çevre: {c1.cevre_hesapla()} ")

print(f"c2: alan: {c2.alan_hesapla()} çevre: {c2.cevre_hesapla()} ")
"""


# mirasalma (kalıtım)
"""
class person():
    def __init__(self):
        print("Person created")

class student(person):

    def __init__(self):
        person.__init__(self)
        print("Student created")


p1 = person()
s1 = student()

"""


"""
class person():
    def __init__(self, fname , lname):
        self.firstName = fname
        self.lastName = lname
        print("Person created")

class student(person):

    def __init__(self ,fname , lname):
        person.__init__(self, fname , lname)
        print("Student created")


p1 = person("Ali","Yılmaz")
s1 = student("Çınar","Turan")


print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName)
"""



"""
class person():
    def __init__(self, fname , lname):
        self.firstName = fname
        self.lastName = lname
        print("Person created")
    def who_am_i(self):
        print("I am a person")
    def eat(self):
        print("I am a eating")

class student(person):

    def __init__(self ,fname , lname , number):
        person.__init__(self, fname , lname)
        self.studentnumber = number
        print("Student created")

class Teacher(person):
    def __init__(self,fname,lname,branch):
        super().__init__(fname, lname)
        self.branch = branch
    def who_am_i(self):
        print(f"I am a {self.branch} teacher")    


t1 = Teacher("Serkan", "Yılmaz", "Math")
t1.who_am_i()


p1 = person("Ali","Yılmaz")
s1 = student("Çınar","Turan" , 256)



print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName + ' ' + str(s1.studentnumber))

p1.who_am_i()
s1.who_am_i()

p1.eat()
s1.eat()
"""



"""
mylist = [1,2,3]

class movie():
    def __init__(self,title, director,duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Movie objesi oluşturuldu.")
    def __str__(self):
        return f" {self.title} by {self.director} "

m = movie("Film adı","Yönetmen adı","Filmin süresi")
print(str(mylist))
print(str(m))
"""


















