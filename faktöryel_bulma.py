print("""
*****************************************
Faktöryel Bulma Programı

Çıkmak İçin q ya Basınız
*****************************************
""")

while True:
    sayı = input("Sayı:")
    if (sayı == "q"):
        print("program Sonlandırılıyor.")
        break

    else:
        sayı = int(sayı)

        faktöryel = 1

        for i in range(2,sayı+1):
            faktöryel *=  i
        print("Faktöryel ",faktöryel)