sayi = int(input("Asal olup olmadığını kontrol etmek üzere bir sayı giriniz: "))
asalmi = True

if (sayi == 1):
    asalmi = False

for i in range(2,sayi):
    if (sayi % i == 0):
        asalmi = False
        break

if asalmi:
    print(F"{sayi} asal bir sayıdır.")
else:
    print(F"{sayi} asal bir sayıdır.")