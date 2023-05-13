print("""
******************************

Atm Makinesine Hoşgeldiniz...

İşlemler;

1. Bakiye Sorma

2. Para Yatırma

3. Para Çekme

Programdan çıkmak için q ya basınız.
******************************
""")

bakiye = 1000

while True:
    işlem = input("İşlem seçiniz:")

    if (işlem == "q"):
        print("Yine bekleriz")
        break
    elif (işlem == "1"):
        print("Bakiyeniz {} TL".format(bakiye))
    elif (işlem == "2"):
        miktar = int(input("miktarı Giriniz:"))

        bakiye += miktar
    elif (işlem == "3"):
        miktar = int(input("Miktar Giriniz:"))

        if (bakiye - miktar < 0):
            print("Yetersiz Bakiye")
            continue
        bakiye -= miktar
        
    else:
        print("Geçersiz İşlem ...")