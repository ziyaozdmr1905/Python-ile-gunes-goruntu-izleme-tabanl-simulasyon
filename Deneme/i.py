#PYTHON TUBLE LİSTE

"""
list=[1,2,3]

tuble=(1,"iki",3)
print(type(list))
print(type(tuble))

print(list[2])

print(tuble[2])

print(len(list))

print(len(tuble))
"""
"""
list=["Ali","Veli"]
tuble=("Damla","Ayşe")

list[0]="Ahmet"

#tuble[0]="Deniz"



#print(tuble)

print(list)
"""


#list=["Ali","Veli"]
#tuble=("Damla","Ayşe")


#t=tuble.count("Ayşe")
#print(t)

"""
tuble=("Damla","Ayşe","Ayşe")
names=("Demet","Emel","Ayşe") + tuble

print(names)
"""


#LİSTE TİPİ DİCTİONARY

#key-value şeklinde çalışıyor


#sehirler=["Kocaeli","İstanbul"]
#plakalar=[41,34]

#print(plakalar[sehirler.index("Kocaeli")])
#print(plakalar[sehirler.index("İstanbul")])
#BU yol bizim için uzun daha kısası var ve daha çok şey yapıyoruz

#MESELA

# PLAKALAR={"KEY" : "VALUE"} #
# -KEY- YERİNE *KOCAELİ* , -VALUE- YERİNE *41* YAZILIR



plakalar={"Kocaeli" : 41 , "İstanbul" : 34}
"""
print(plakalar["İstanbul"])
print(plakalar["Kocaeli"])


plakalar["Ankara"]= 6

print(plakalar)
print(plakalar["Ankara"])
"""

#plakalar["Kocaeli"]="New value"

#print(plakalar)


#NOT# = LİSTELERİ DAHA DETAYLI OLUŞTURABİLİRİZ.

users={
    "sadıkturan" : {
        "age" : 36,
        "roles" : ["user"],
        "email" : "sadık@gmail.com",
        "address" : "kocaeli",
        "phone" : "213456798" 
    },
    "çınarturan" : {
        "age" : 2,
        "roles" : ["admin","user"],
        "email" : "cınar@gmail.com",
        "address" : "Kocaeli",
        "phone" : "123645789"
    }
}


#print(users["sadıkturan"])

#print(users["çınarturan"])

#print(users["sadıkturan"]["email"])

#print(users["çınarturan"]["age"])

#print(users["sadıkturan"]["roles"][0])

#print(users["çınarturan"]["roles"][1])

#PYTHON DA SETS LİSTLERİ
fruits = {"orange", "apple", "banana"}
#print(fruits)

#for x in fruits:
#    print(x)




#ADD METODU ELEMAN EKLEME
#fruits.add("mango")
#print(fruits)

#UPDATE METODU DA İÇİNDE LİSTE OLUŞTURUP ATIYORUZ
#fruits.update({"cherry","mango"})

#SET KOMUTU TEKRARLANAN ELEMANLARI BİR DEFA YAZDIRIR
#numbers = [1,2,3,4,4,5,5,6,1,2,]
#print(set(numbers))

#DİSCARD İLE SİLME İŞLEMİ YAPILIR
#fruits.discard("apple")

#POP METODU İSTEDİĞİ ELEMANI KENDİ SİLER BİZ SEÇEMEYİZ
#fruits.pop()


print(fruits)



















