import random

while True:
    soru = input("Zar atmak istermisiniz ?(cevabınız evetse herhangi bir tuşa, hayırsa q'ya basın.): ")
    if soru == "q":
        print("İyi günler.")
        break
    s1 = random.randint(1,6)
    s2 = random.randint(1,6)
    if ((s1 == 1 and s2 == 2) or (s1 == 2 and s2 == 1)):
        print(s1)
        print(s2)
        print("Ortam kızına zar at demişler. 1, 2 atmış.")
    elif(s1 == 3 and s2 == 1):
        print(s1)
        print(s2)
        print("SJ")
    else:
        print(s1)
        print(s2)
    
    