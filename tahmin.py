import random

sayi = random.randint(1,100)

can = int(input("Kaç hakkınız olsun istersiniz: "))
hak = can
sayac = 0

while hak > 0:
    sayac += 1
    hak -= 1
    tahmin = int(input("Tahmin: "))

    if sayi == tahmin:
        print(F"Tebrikler {sayac}. defada bildiniz. Toplam puanınız: {(100) - (100/can)*(sayac-1)}")
        break
    elif sayi > tahmin:
        print("Yukarı")
    else:
        print("Aşağı")

    if hak == 0:
        print(F"Hakkınız bitti sayi: {sayi}")