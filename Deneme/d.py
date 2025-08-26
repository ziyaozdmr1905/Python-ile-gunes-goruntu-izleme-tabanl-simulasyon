course=" His name is john. He's 40 years old. His from TORONTO. He is a student."
family=" My sister goes to bed late. My father speak angry with her"

#course=course.format("23")
"""
#UPPER
course=course.upper()
family=family.upper()
"""
"""
#LOWER
course=course.lower()
family=family.lower()
"""
"""
#TİTLE
course=course.title()
family=family.title()
"""
"""
#CAPİTALİZE
course=course.capitalize()
family=family.capitalize()
"""
"""
#STRİP
course=course.rstrip("dent.")
family=family.rstrip("her.")
"""
"""
#SPLİT
course=course.split()
family=family.split()
print(course[2:5])
print(family[3:6])
"""
"""
#JOİN
course=course.split()
family=family.split()
X="*".join(course)
Y="--".join(family)
print(course)
print(X)
print(family)
print(Y)
"""
"""
#FİND
course=course.find("years")
family=family.find("her")
"""
"""
#STARTSWİTH
course=course.startswith(" ")
family=family.startswith(" ")
"""
"""
#ENDSWİTH
course=course.endswith(".")
family=family.endswith("her")
"""
"""
#REPLACE
course=course.replace("john", "ziya")
family=family.replace("father","mother")
"""
"""
#CENTER
course=course.center(100)
family=family.center(100)


# course=course.replace(" ","*")
# family=family.replace(" ","*")
"""
"""
#COUNT
course=course.count("is")
family=family.count("My")
"""
"""
#İNDEX
index=course.index("is")
index=family.index("My")
print(index)
"""
"""
#İSNUMERİC
course=course.isnumeric()
family=family.isnumeric()
"""
#print("123 4".isdigit())          #İSDİGİT

#print("as1245_".isidentifier())   #İSİDENTİFİER
"""
#İSTİTLE
course=course.istitle()
family=family.istitle()
"""
"""
#LJUST
family=family.ljust(20)
print(family, "banana")
"""
"""
#PARTİTİON
family=family.partition("My father")
course=course.partition("years old.")
"""

"""
#RFİND
family=family.rfind("f")
course=course.rfind("y")
"""
"""
#swapcase
family=family.swapcase()
course=course.swapcase()
"""
"""
#ZFİLL
family=family.zfill(65)
course=course.zfill(80)
"""
print(family)
print(course)