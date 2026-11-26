# import string

# parola= input("parola gir: ")

# if len(parola) >=12:
#     print("uzunluk yeterli")

# else:
#     print("çok kısa")

# puan=0

# if any(c.isupper() for c in parola):
#     puan+=25

# else:
#     print("en az 1 büyük harf olmalı")

# if any(c.islower() for c in parola):
#     puan+=25
# else:
#     print("en az 1 küçük harf olmalı")

# if any(c.isdigit() for c in parola):
#     puan+=25
# else:
#     print("en az bir rakam olmalı")

# if any(c in string.punctuation for c in parola):
#     puan+=25
# else:
#     print("en az bi özel karakter olmalı")

# print("Toplam puan", puan)






















import string

sifre = input("şifrenizi giriniz:")

if len(sifre) >=12 :
    print("yetersiz karakter")

sayac=0

if any(c.isupper() for c in sifre):
    sayac+=20
else:
    print("büyük harf eksik")

if any(c.islower() for c in sifre):
    sayac+=20
else:
    print("küçük harf eksik")

if any(c.isdigit() for c in sifre):
    sayac+=20
else:
    print("rakam eksik")

if any(c in string.punctuation for c in sifre):
    sayac+=20
else:
    print("özel karakter eksik")

print("toplam puan" , sayac)