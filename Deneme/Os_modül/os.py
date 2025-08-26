import os

import datetime

"""
# .name metodu hangi işletim sistemi varsa onu söyler
res = os.name

print(res)
"""

"""
# .getcwd() metodu ilgili klasörün hmagi konumda olduğunu bize söyler
res = os.getcwd()
"""

"""
# dosya oluşturmak için mkdir metodu kullanılır..
os.mkdir("newdosya")

"""

"""
# .chdir metodu konum belirtir yani o konuma gider ve mkdir metodu ise  o konuma dosya oluşturur
os.chdir('c:\\')
os.mkdir("yeni")
"""

"""
# listeleme yapmak için .listdir metodu kullanılır
res  = os.listdir('C:/Users/Ziya/Desktop/python örnekleri')


for dosya in res:
    if dosya.endswith("txt"):
        print(dosya)
"""
"""
# os isimli dosyanın tam olarak konumunu bize verir
res = os.path.abspath("os.py")
"""

"""
# dosyanın dizin ismini almak için bu metot kullanılır
res = os.path.dirname("C:/Users/Ziya/Desktop/python örnekleri/os.py")

"""

"""
#dosya var mı yok mu ona göre false veya true verilir
res = os.path.exists("os.py")
"""





"""
# mevcut dosyanın uzantısı i,le ismini ayırır
res = os.path.splitext("os.py")
"""





#               REGULAR EXPRESSİON MODÜLÜ

import re

str = "Python Kursu: Python Programlama Rehberiniz | 40 saat"

"""
# str ifadesi içinde kaç tane varsa pytohn dan o kadar yazdırır
res = re.findall("Python",str)
"""



"""
# Boşluklardan ayırdık
res = re.split(" " , str)
"""

"""
# Boşluklara - koy diyoruz..
res =re.sub(" ","-",str)
"""

"""
# konumu bulmak istersek bu metodu kullanırız..
res = re.search("Python" , str)
#res = res.span()
"""

"""
# köşeli parantez içinde ki bütün karakterler aranır ve onlarlar liste halinde yazdırılır
res = re.findall("[abc]" , str)
"""


"""
# a-o arası ne kadar harf varsa str ifadesi içinde olanalrı bul ve yazdır
res = re.findall("[a-o]" , str)
"""

"""
# bu metot ise 0 ile 5 arası bütün rakamlara bakar olanları yazdırır
res = re.findall("[0-5]", str)
"""

"""
# ^abc demek abc harflaeri dışındaki bütün harflere bak demektir
res = re.findall("[^abc]", str)
"""

"""
# bütün str ifadesini üçlü şekilde böler ve yazdırır
res = re.findall("..." , str)
"""


#res = re.findall("\APython" , str)
#res = re.findall("saat\Z",str)

import json


"""
# Bu string ifadesini tek tırnak içinde alırız yoksa hata mesajı veriyor..
person_stringi = '{"name": "Ali" , "langues" : ["pytohn","C#"]}'

res = json.loads(person_stringi)
"""






#print(res)















