"""class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self, answer):
        return self.answer == answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def get(self):
        question = self.getQuestion()
        print(f'soru: {self.questionIndex + 1} : {question.text}')
        
        for q in question.choices:
            print('-' + q) 
        answer = input('cevap: ')
        self.ques(answer)
        self.loadQuestion()    




q1 = Question('en iyi programlama dili hangisidir ?', ['C#','python','javascript','java'], 'python')
q2 = Question('en popüler programlama dili hangisidir ?', ['python','javascript','C#','java'], 'python')
q3 = Question('en çok kazandıran programlama dili hangisidir ?', ['C#','javascript','java','python'], 'python')
q4 = Question('en çok sevilen programlama dili hangisidir ?', ['C#','javascript','java','python'], 'python')
q5 = Question('en kolay programlama dili hangisidir ?', ['C#','javascript','java','python'], 'python')

questions = [q1,q2,q3,q4,q5]

quiz = Quiz(questions)

q6 = Quiz([1,2,3,4])
print(q6.getQuestion())
quiz.get()
"""

# HATA VE HATA YÖNETİMİ


"""
try:
    x = int(input('x: '))  
    y = int(input('y: '))
    print(x/y)
except ZeroDivisionError:
    print('y için 0 girilmez')
except ValueError:
    print('x ve y için sayısal değer girmelisiniz')

"""

"""
try:
    x = int(input('x: '))  
    y = int(input('y: '))
    print(x/y)
except (ZeroDivisionError, ValueError) as e:
    print('yanlış bilgi girdiniz')
    print(e)

"""


"""
while True:
        
    try:
        x = int(input('x: '))  
        y = int(input('y: '))
        print(x/y)
    except Exception as e:
        print('yanlış bilgi girdiniz',e) 
    else:
        break       
"""

"""
x = 10

if x > 5:
    raise Exception ('x 5 den büyük değer alamaz')

"""


"""
def chec(psw):
    import re
    if len(psw) < 8:
        raise Exception ('Parola en az 7 karakter olmalıdır.')
    elif not re.search ("[a-z]" , psw):
        raise Exception ('parola küçük harf içermelidir.')
    elif not re.search ("[A-Z]", psw):
        raise Exception ('paralo büyük harf içermelidir')
    elif not re.search ("[0-9]",  psw):
        raise Exception ('parola rakam içermelidir') 
    elif not re.search ("[_@£", psw):
        raise Exception ('parola alpha numerik karakter içermelidir')
    elif re.search ("\s",psw):
        raise Exception ('parola boşluk içermemelidir')

password = '12345678aA'


try :
    chec(password)
except Exception as ex:
    print(ex)
else:
    print('geçerli parola : else')
finally:
    print('validation tamamlandı')            

"""


"""class Person:
    def __init__(self, name , year):
        if len(name) > 10:
            raise Exception ('name alanı fazla karakter içeriyor')
        else:
            self.name = name
p = Person('Aliiiiiiiiiiiiiii' , 1989)                
"""




liste = ['1' , '2' , '5a' , '10b' , 'abc' , '10' , '50']


#1.SORU-Liste elemanları içinde sayısal değerleri bulun
"""
for x in liste:

    try:
        res = int(x)
        print(res)
    except ValueError:
        continue    
"""

#2.SORU-Kullanıcı 'q' değerini girmedikçe aldığınız her imputun sayı olduğundan 
# emin olunuz aksi takdirde hata mesajı veriniz
"""
while 1 :
    giris = input('Sayı girin çıkmak için(q): ')
    if (giris == 'q'):
        print('program sonlandı..')
        break
    else:
        try:
            int(giris) 
            print(giris)
        except Exception as ex:
            print('yanlış girildi..',ex) 
                    
"""

#3.SORU-Girilen paralo içinde Türkçe karakter hatası veriniz

"""
def sifre(prl):
    import re

    if len(prl) < 8:
        raise Exception('parola 8 karakterli olmalıdır')
    elif not re.search('[a-z]',prl):
        raise Exception('parola harf içermelidir')    
    elif re.search('[ıöüş]',prl):
        raise Exception('parola Türkçe karakter içermemelidir')
    elif re.search('[1-9]',prl):
        raise Exception('parola rakam içermemelidir')     

parola = input('Parola giriniz: ')
try:
    sifre(parola)
except Exception as ex:
    print(ex)    
"""


#4.SORU-Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin

"""
def faktoriyel(x):

    x = int(x)
    if x < 0:
        raise ValueError('Negatif sayı')
    res = 1

    for i in range(1 , x+1):
        res *= i
        return res

for x in [3, 12 , 20, -4 , '2e']:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
"""
"""
liste = ["345","sadas","324a","14","kemal"]

for i in liste:
    try:
        i = int(i)
        print(i)
    except ValueError:
        continue"""


"""
turkce_karakterler = 'şçğüöıİ'
parola = input('şifre: ')

for i in parola:
    if i in turkce_karakterler:
        raise TypeError('Parola türkçe karakter içeremez')
    else:
        pass    
print('geçerli parola', parola)

"""




"""
def cift(x):
    x = int(x)
    if x % 2 == 0:
        return x
    else:
        raise ValueError('Sayı tek sayıdır')

print(cift(3))
"""
"""
liste = [1,3,4,6,7,8,24]

for x in liste:
    try :
        print(cift(x))
    except ValueError:
        continue    
"""



# dosya açma işlemleri
"""
file = open("test.txt","w",encoding= "utf-8")
file.write('ahmet ziya')
file.close()

file = open("test.txt","w",encoding= "utf-8")
"""

"""
file = open("test.txt","a",encoding= "utf-8")
file.write("Ahmet Ziya Özdemir\n")
file.close()
"""
"""
file = open("test.txt","a",encoding= "utf-8")
file.write("Ayşe Nur Ay\n")
file.close()
"""

"""
file = open("C:/Users/Ziya/Desktop/dos","a",encoding="utf-8")
file.write('sıınıf açma işlemi')
file.close()
"""
"""
file = open("C:/Users/Ziya/Desktop/dos","a",encoding="utf-8")
file.write('neresi burası')
file.close()
"""

"""
file = open("C:/Users/Ziya/Desktop/dosta.txt","a",encoding="utf-8")
file.write('neresi burası')
file.close()
"""

"""
try:
    file = open("bilgiler2.txt","r")
except FileNotFoundError:
    print('Dosya bulunamadı..')
"""

"""
file = open("test.txt", "a", encoding= 'utf-8')

file.write('Ahmet')
file.write('Mehmet')
file.write('Samet')

file.close()


file = open("test.txt", "r", encoding= 'utf-8')


for i in file:
    print(i)

file.close()
"""


"""
file = open("test.txt", "a", encoding= 'utf-8')

file.write('Ahmet\n')
file.write('Mehmet\n')
file.write('Samet\n')

file.close()

"""

"""
file = open("test.txt", "r", encoding= 'utf-8')
conten = file.read()
print(conten)
file.close()
"""

"""
file = open("test.txt", "r", encoding= 'utf-8')
conten = file.readline()
print(conten)
file.close()
"""

"""
file = open("test.txt", "r", encoding= 'utf-8')
conten = file.readlines()
print(conten[1])
file.close()
"""

"""
with open("test.txt", "r" , encoding= "utf-8") as file:
    conten = file.read()
    file.seek(3)
    print(conten)
    print(file.tell())

"""

""" # şu an bu kod dosya okuma işlemi için kullanılır 
with open("test.txt", "r+" , encoding= "utf-8") as file:
    print(file.read())
"""


"""
# bu kod satırı güncelleme yapmak için
with open("test.txt", "r+" , encoding= "utf-8") as file:
    file.write("denme")


with open("test.txt", "r+" , encoding= "utf-8") as file:
    print(file.read())

"""



# sayfa sonu güncelleme
"""
with open("test.txt", "a" , encoding= "utf-8") as file:
    file.write("\nEMEL")

with open("test.txt", "r" , encoding= "utf-8") as file:
    print(file.read())

"""

# sayfa başı güncelleme

"""
with open("test.txt", "r+" , encoding= "utf-8") as file:
    con = file.read()
    con = "EMEL\n" + con
    file.seek(0)
    file.write(con)


with open("test.txt", "r" , encoding= "utf-8") as file:
    print(file.read())
"""

"""
file = open("test.txt" , "w" , encoding="utf-8")
file.write("Ayşe")
file.close()

"""

"""
with open("test.txt" , "r" , encoding="utf-8") as file:
    con = file.read()
    print(con)
    file.seek(20)
    print(file.tell())
    con2 = file.read(10)
    print(con2)
"""



"""
with open("test.txt" , "r+" , encoding="utf-8") as file:
    file.write("deneme")

with open("test.txt" , "r" , encoding="utf-8") as file:
    print(file.read())
"""

#sonuna ekleme yaptık
"""
with open("test.txt" , "a" , encoding="utf-8") as file:
    file.write("\nBengü")
with open("test.txt" , "r" , encoding="utf-8") as file:
    print(file.read())
"""


#başına ekleme
"""
with open("test.txt" , "r+" , encoding="utf-8") as file:
    con = file.read()
    con = "Fatma\n" + con
    file.seek(0)
    file.write(con)

with open("test.txt" , "r" , encoding="utf-8") as file:
    print(file.read())
"""


"""
with open("test.txt" , "r+" , encoding="utf-8") as file:
    liste = file.readlines()
    liste.insert(1, "Ali\n")
    file.seek(0)
    for i in liste:
        file.write(i)

with open("test.txt" , "r" , encoding="utf-8") as file:
    print(file.read())
"""



"""
with open("test.txt" , "r+" , encoding="utf-8") as file:
    liste = file.readlines()
    liste.insert(4, "Alper\n")
    file.seek(0)
    file.writelines(liste)
with open("test.txt" , "r" , encoding="utf-8") as file:
    print(file.read())
"""


"""
file = open("sebze.txt" , "a" , encoding= "utf-8")
file.write("Domates\n")
file.write("Salatalık\n")
file.close()


file = open("sebze.txt" , "r" , encoding= "utf-8")
print(file.read())
file.close()
"""

"""
file = open("sebze.txt" , "r" , encoding= "utf-8")
for i in file:
    print(i , end= "")
file.close()    """



"""
file = open("tez.txt","w",encoding="utf-8")
file.write("otomasyon\n")
file.write("Elektrik\n")
file.close()

file = open("tez.txt","r",encoding="utf-8")
print(file.read())"""
"""
file = open("tez.txt","r",encoding="utf-8")

for i in file:
    print(i,end="")

file.close()
"""


"""
file = open("tez.txt","r",encoding="utf-8")
e = file.readlines()
print(e)
e.insert(2,"Elektronik")
print(e)
file.close()

"""
"""
with open("tez.txt","r",encoding="utf-8") as file:
    con = file.read()
    print(con)
    file.seek(10)
    print(file.tell())
    con2 = file.read(10)
    print(con2)
"""


# dosya sonu güncelleme
"""
with open("tez.txt","a",encoding="utf-8") as file:
    file.write("Gömülü yazılım\n")

with open("tez.txt","r",encoding="utf-8") as file:
    con = file.read()
    print(con)
"""

#dosya başında güncelleme
"""
with open("tez.txt","r+",encoding="utf-8") as file:
    con = file.read()
    con = "Elektronik\n" + con
    file.seek(10)
    file.write(con)
with open("tez.txt","r",encoding="utf-8") as file:
    con = file.read()
    print(con)"""



# dosya ortsında güncelleme
"""
with open("tez.txt","r+",encoding="utf-8") as file:
    liste = file.readlines()
    liste.insert(3,"Yazılım\n")
    file.seek(0)
    for i in liste:
        file.write(i)

with open("tez.txt","r",encoding="utf-8") as file:
    print(file.read())

"""

"""
with open("tez.txt","r+",encoding="utf-8") as file:
    liste = file.readlines()
    liste.insert(2,"Güç sistemleri\n")
    file.seek(0)
    file.writelines(liste)

with open("tez.txt","r",encoding="utf-8") as file:
    print(file.read())
"""



