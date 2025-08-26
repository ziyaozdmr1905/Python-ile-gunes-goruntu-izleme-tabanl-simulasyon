#LİSTE METOTLARI

#MİN VE MAX DEĞERLERİ
numbers=[1,10,5,16,4,9,10]
letters=["a","g","s","b","y","a","s"]


#val=max(numbers)
#val=min(numbers)
#val=min(letters)
#val=max(letters)

#val=numbers[:4]
#numbers[4] = 40


#numbers.append(45) kullanımına dikkat et stringlerde ki gibi değil

#numbers.insert(3,78)   3.index e sayı eklemek demektir


#numbers.pop(0)
#letters.pop()

#letters.remove("a")
#numbers.remove(1)


#numbers.sort()
#letters.sort()


#numbers.reverse()
#letters.reverse()

#n=numbers.count(10)
#l=letters.count("a")



#print(n)
#print(l)


#UYGULAMA ÖRNEK

names=["Ali","Yağmur","Hakan","Deniz"]
years=[1998,2000,1998,1987]


#1.SORU CEVABI

#names.append("Cenk")
#print(names)

#2.SORU CEVABI

#names.insert(0,"Sena")
#print(names)

#3.SORU CEVABI
#names.pop(3)
#names.remove("Deniz")
#print(names)

#4.SORU CEVABI
#n=names.index("Deniz")
#print(n)

#5.SORU CEVABI
#n="Ali" in names
#print(n)

#6.SORU CEVABI
#print(names[::-1])
#print(years[::-1])

#7.SORU CEVABI
#numbers.sort()
#years.sort()
#print(numbers)
#print(years)

#8.SORU CEVABI
#years.sort()
#print(years)


#9.SORU CEVABI
#stra="Chevrolet, Daica"
#a=stra.split()
#print(a)

#10.SORU CEVABI
#y=min(years)
#a=max(years)
#print(y)
#print(a)


#11.SORU CEVABI
#y=years.count(1998)
#print(y)

#12.SORU CEVABI
#years.clear()
#print(years)

#13.SORU CEVABI
markalar=[]
marka=input("Marka ismi gir:  " )
markalar.append(marka)

marka=input("Marka ismi gir:  " )
markalar.append(marka)

marka=input("Marka ismi gir:  " )
markalar.append(marka)

#print(markalar)