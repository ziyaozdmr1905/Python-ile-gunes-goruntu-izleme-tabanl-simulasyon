# MODÜL

"""
Bu modül matematik işlemlerini kolaylaştırmak için yazılımıştır..
"""


def toplama(a , b):
    return a+b

def cikarma(a , b):
    return a - b


def carpma(a , b):
    return a * b


def bölme(a , b):
    return a / b


def mod(a , b):
    return a % b

def üsAlma(a , b):
    return a ** b

def karekök(a):
    return a ** 0.5

def kareAlma(a):
    return a ** 2

def logaritma(sayi , taban):
    
    '''
    Burada b taban a üs logritma rolündedir..
    '''
    for i in range(1 , sayi):
        if (taban ** i == sayi):
            return i




def faktorial(sayi):
    faktoriyel = 1
    i = 1

    if (sayi >= 0):
        while (i <= sayi):
            faktoriyel *= i
            i += 1
        return faktoriyel




def tamsayi(sayi):
    sayi = int(sayi)
    return sayi








pi = [3,1415926535]
radyan = 1
def radyancevir(sayi):
    
    for i in pi:
        radyan = sayi * (i / 180)
        return radyan









































