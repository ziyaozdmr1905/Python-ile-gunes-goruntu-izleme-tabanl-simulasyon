


"""
sayi = int(input("Sayı: "))
taban = int(input("Taban: "))

def logaritma(sayi , taban):
    
    '''
    Burada b taban a üs logritma rolündedir..
    '''
    for i in range(1 , taban):    
        if (sayi == 1):
            return 0
        elif ( sayi == taban):
            return 1
        elif (sayi > taban):
            sayi = taban ** i
        i += 1    
        return i        
    else:
        sonuc = (sayi == taban ** i)
        return sonuc

print(logaritma(sayi, taban ))
"""

"""
def logaritma():
    sayi = int(input("Sayı: "))
    taban = int(input("Taban: "))
    '''
    Burada b taban a üs logritma rolündedir..
    '''
    sonuc=[x for x in range(1 , sayi) if taban ** x == sayi]
    
    return sonuc 

print(logaritma())
"""




"""
def faktorial():
    faktoriyel = 1
    i = 1
    sayi = int(input("Sayı: "))
    if (sayi >= 0):
        while (i <= sayi):
            faktoriyel *= i
            i += 1
        return faktoriyel

print(faktorial())
"""



"""
def tamsayi():
    sayi = float(input("Sayı: "))
    sayi = int(sayi)
    return sayi
print(tamsayi())
"""

"""
def logaritma():
    sayi = int(input("Sayı: "))
    taban = int(input("Taban: "))
    '''
    Burada b taban a üs logritma rolündedir..
    '''
    for i in range(1 , sayi):
        if (taban ** i == sayi):
            return i
print(logaritma())
"""

"""
pi = [3,1415926535]
sin = 1
def sinus(sin , pi):
    
    sayi = int(input("Sayı: "))
    if (sayi == 30):
        sin = 0.5
        return sin
    elif (sayi == 90):
        sin = 1
        return sin
    elif (sayi == 0):
        sin = 0
        return sin
    else:
        for i in pi:
            if (float(i)):
                sin = sayi * ( i / 180)
            return sin       

print(sinus(sin , pi))
"""

"""
pi = [3,1415926535]
radyan = 1
def radyancevir():
    sayi =  int(input("Sayı: "))
    for i in pi:
        radyan = sayi * (i / 180)
        return radyan

print(radyancevir())
"""




"""
def faktorial(sayi):
    faktoriyel = 1
    i = 1
    if (sayi >= 0):
        while (i <= sayi):
            faktoriyel *= i
            i += 1
        return faktoriyel



def sinus(x):
    toplam = 0
    for n in range(1 , 20):
        toplam += ((((-1)**n) * ((x ** (2*n+1)) / (faktorial( 2*n + 1)))))
        return toplam

x = int(input("Bir açı giriniz: "))

sayi = int(x)
sayi = sayi % 360
radyan = sayi * (3.1415926535 / 180)
x = radyan

print(radyan)
print("sin({}): {} ".format(sayi , sinus(radyan)))
#print(f"sin{x}: {radyan}" , sayi , sinus(x))
"""



"""
def faktorial(sayi):
    faktoriyel = 1
    i = 1
    if (sayi >= 0):
        while (i <= sayi):
            faktoriyel *= i
            i += 1
        return faktoriyel

print(faktorial(5))

def sinus(x,):
    toplam = 0
    #x = float(x)
    for n in range(0 , 30):
        toplam += (((-1)**n) * ((x ** (2*n+1)) / (faktorial( 2*n + 1))))
        print(toplam)
        return toplam

    
x = int(input("Bir açı giriniz: "))      
sayi = x
x = x % 360
radyan = x * (3.1415926535 / 180)


print(sinus(radyan))
"""


# Hesap makinesi


import matematik as mat
import time


def hesap_makinesi():
    
    print('''**********
    Toplama(+):         1
    Çıkartma(-):        2
    Çarpma(*):          3
    Bölme(/):           4
    Faktöriyel(!):      5
    Mod(%):             6
    Logaritma(log):     7
    Kuvvet alma(**):    8
    Karekök:            9
    Tam sayı:           10
    radyan:             11
    **********''')

    while True:
        islem= input("Bir işlem belirtin: ")
        sayi1 = (input("Bir sayı girinz: "))
        sayi2 =  (input("Bir sayı girinz: "))
        if (islem == "1"):
            sayi1 = int(sayi1)
            sayi2 =  int(sayi2)
            print("Hesaplanıyor...")
            time.sleep(1)
            sonuc = mat.toplama(sayi1 , sayi2)
            return sonuc
        elif (islem == "2"):
            sayi1 = int(sayi1)
            sayi2 =  int(sayi2)
            print("Hesaplanıyor...")
            time.sleep(1)
            sonuc = mat.cikarma(sayi1 , sayi2)
            return sonuc
        elif (islem == "3"):
            sayi1 = int(sayi1)
            sayi2 =  int(sayi2)
            print("Hesaplanıyor...")
            time.sleep(1)
            sonuc = mat.carpma(sayi1 , sayi2)
            return sonuc
        elif (islem == "4"):
            sayi1 = int(sayi1)
            sayi2 =  int(sayi2)
            print("Hesaplanıyor...")
            time.sleep(1)
            sonuc = mat.bölme(sayi1 , sayi2)
            return sonuc
        elif (islem == "5"):
            sayi1 = int(sayi1)
            sayi2 =  int(sayi2)
            birinci = mat.faktorial(sayi1)
            ikinci = mat.faktorial(sayi2)
            print("Hesaplanıyor...")
            time.sleep(1)
            return birinci , ikinci
        elif (islem == "6"):
            sayi1 = int(sayi1)
            sayi2 =  int(sayi2)
            birinci = mat.mod(sayi1 , sayi2)
            ikinci = mat.mod(sayi2 , sayi1)
            print("Hesaplanıyor...")
            time.sleep(1)
            return birinci , ikinci
        elif (islem == "7"):
            sayi1 = int(sayi1)
            sayi2 =  int(sayi2)
            log = mat.logaritma(sayi1 , sayi2)
            print("Hesaplanıyor...")
            time.sleep(1)
            return log
        elif (islem == "8"):
            sayi1 = int(sayi1)
            sayi2 =  int(sayi2)
            birinci = mat.üsAlma(sayi1)
            ikinci = mat.üsAlma(sayi2)
            print("Hesaplanıyor...")
            time.sleep(1)
            return birinci , ikinci
        elif (islem == "9"):
            sayi1 = int(sayi1)
            sayi2 =  int(sayi2)
            birinci = mat.karekök(sayi1)
            ikinci = mat.karekök(sayi2)
            print("Hesaplanıyor...")
            time.sleep(1)
            return birinci , ikinci
        elif(islem == "10"):
            sayi1 = float(sayi1)
            sayi2 = float(sayi2)
            birinci = mat.tamsayi(sayi1)
            ikinci = mat.tamsayi(sayi2)    
            print("Hesaplanıyor...")
            time.sleep(1)
            return birinci , ikinci        
        elif(islem == "11"):
            sayi1 = int(sayi1)
            sayi2 =  int(sayi2)
            birinci = mat.radyancevir(sayi1)
            ikinci = mat.radyancevir(sayi2)    
            print("Hesaplanıyor...")
            time.sleep(1)
            return birinci , ikinci   
        else:
            print("Hatalı giriş yapıldı..")


print(hesap_makinesi())








