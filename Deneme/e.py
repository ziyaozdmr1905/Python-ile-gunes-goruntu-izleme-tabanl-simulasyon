#PYTHON LİSTELER

"""
my_list=[1,2,3,]
print(my_list)
"""

# list1=["one", "two", "there"]
# list2=["four","five","six"]

#print(list1+list2)  toplama

"""
lists= list1+list2
print(lists[2])
"""
"""
userA=["sadık", 36]
userB=["çınar",2]
#users=userA+userB

users=[userA, userB]
print(users[1][0])
"""

#LİSTE METOTLARI

numbers=[1,10,5,16,4,9,10]
letters=["a","g","s","b","y","a","s"]

#val=min(numbers)
#val=max(numbers)
#val=min(letters)
#val=max(letters)

# val=numbers[:4]
#numbers[4]=50

"""
numbers.append(12)
letters.append("w")
"""

#numbers.insert(4,45)

#numbers.pop(1)     1.İNDEX DEKİ SAYIYI SİLDİ YANİ 10 U
#numbers.remove(1)   REMOVE METODU İÇİNDE YAZDIĞIMIZ SAYIYI SİLİYOR
"""
numbers.sort()
letters.sort()
"""
#numbers.reverse()    TERSİNE ÇEVİRİR


# print(numbers)
# print(letters)



names=["Ali", "Yağmur", "Hakan", "Deniz"]
years=[1998, 2000,1998,1987]

"""
#1.SORU CEVABI
names.append("Cenk")
2#.SORU CEVABI
names.insert(0,"Sena")
"""
"""
#3.SORU CEVABI
names.remove("Deniz")
names.pop(3)
"""
#4.SORU CEVABI


#5.SORU CEVABI
"""
val="Ali" in names
print(val)

"""

#6.SORU CEVABI
"""
names.reverse()
years.reverse()
"""

#7.SORU CEVABI
"""
names.sort()
years.sort()
"""


#8.SORU CEVABI
"""
years.sort()
"""

#9.SORU CEVABI
"""
str="Chevrolet,Dacia"
str=str.split(",")
print(str)
"""

#10.SORU CEVABI
"""
years=min(years)
years=max(years)
"""


#11.SORU CEVABI
"""
print(years.count(1998))
"""

#12.SORU CEVABI
"""
years.clear()
"""
#13.SORU CEVABI
"""
markalar=[]

marka=input("marka: ")
markalar.append(marka)

marka=input("marka: ")
markalar.append(marka)

marka=input("marka: ")
markalar.append(marka)

print(markalar)
"""
# print(years)
# print(names)