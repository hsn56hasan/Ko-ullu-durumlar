print("""**********************************************
      
 Hesap Makinesi 

 İşlemler;

   Toplama = 1
   Çıkarma = 2
   Çarpma = 3
   Bölme = 4
   Üslü Sayı Almak = 5
   Sayının Kare Kökünü Almak = 6
   Sayının Logaritmasını Almak = 7
   Derceyi Radyana Çevirmek = 8
   Radyanı Dereceye Çevirmek = 9
   Sin üsü bulmak = 10
   Cos ü bulmak = 11
   Tanjantı Bulmak = 12
   Cotanjantı Bulmak = 13
   Çıkmak için q ya basınız

**********************************************""")
      



import time 
import math

while True:
    işlem = int(input("İşlem giriniz:"))

    if (işlem == "q"):
        print("İşleminiz Sonlandırılıyor...")
        time.sleep(2)
        print("Tekrar Bekleriz...")
        break

    elif (işlem == 1):
        sayı1 = int(input("1. Sayıyı Giriniz:"))
        sayı2 = int(input("2. Sayıyı Giriniz:"))
        print("İşleminiz Yapılıyor...")
        time.sleep(1)
        print("{} + {} = {} toplamıdır".format(sayı1,sayı2,sayı1 + sayı2))

    elif (işlem == 2):
        sayı1 = int(input("1. Sayıyı Giriniz:"))
        sayı2 = int(input("2. Sayıyı Giriniz:"))
        print("İşleminiz Gerçekleştiriliyor...")
        time.sleep(1)
        print("{} - {} = {} farkıdır".format(sayı1,sayı2,sayı1 - sayı2))

    elif (işlem == 3):
        sayı1 = int(input("1. Sayıyı Giriniz:"))
        sayı2 = int(input("2. Sayıyı Giriniz:"))
        print("İşleminiz Gerçekleştiriliyor...")
        time.sleep(1)
        print("{} * {} = {} çarpımıdır".format(sayı1,sayı2,sayı1 * sayı2))

    elif (işlem == 4):
        sayı1 = int(input("1. Sayıyı Giriniz:"))
        sayı2 = int(input("2. Sayıyı Giriniz:"))
        print("İşleminiz Gerçekleştiriliyor...")
        time.sleep(1)
        print("{} / {} = {} bölümüdür".format(sayı1,sayı2,sayı1 / sayı2))

    elif (işlem == 5):
        sayı1 = int(input("Sayının Tabanını Giriniz:"))
        sayı2 = int(input("Sayının Üs sünü Giriniz:"))
        print("İşleminiz Gerçekleştiriliyor...")
        x = math.pow(sayı1, sayı2)
        print("{} üssü {} = {} budur".format(sayı1,sayı2,math.pow(sayı1, sayı2)))

    elif (işlem == 6):
        sayı1 = int(input(" sayıyı giriniz : "))

        print("işleminiz yapılıyor...")
        time.sleep(1)
        x= math.sqrt(sayı1)
        print("{} sayısının karekökü = {} ".format(sayı1,math.sqrt(sayı1)))

    elif(işlem == 7):
        sayı1 = int(input(" sayıyı giriniz : "))
        sayı2 = int(input(" logaritmanın tabanını giriniz : "))
        print("işleminiz yapılıyor...")
        time.sleep(1)
        print("{} sayısının {} tabanında logaritması = {} ".format(sayı1,sayı2,math.log(sayı1,sayı2)))

    elif(işlem == 8):
        sayı1 = int(input(" Dereceyi giriniz : "))
        print("işlemniz yapılıyor...")
        time.sleep(1)
        print("{} derece = {} radyandır.".format(sayı1,math.degrees(sayı1)))

    elif(işlem == 9):
        sayı1 = int(input(" radyanı giriniz : "))
        print("işleminiz yapılıyor...")
        time.sleep(1)
        print("{} radyan {} derecedir.".format(sayı1,math.radians(sayı1)))

    elif(işlem == 10):
        a = input( "radyan için = R , derce için = D")
        if(a == "r" or a == "R"):
            sayı1 = int(input(" sayıyı giriniz : "))
            x = math.sin(sayı1)
            print("işleminiz yapılıyor...")
            time.sleep(1)
            print("sin {} = {} ".format(sayı1,x))
        elif(a == "d" or a == "D"):
            sayı1 = int(input(" Dereceyi giriniz : "))
            x = math.sin(sayı1)
            y = math.radians(x)
            print("işleminiz yapılıyor...")
            time.sleep(1)
            print("sin {} = {} ".format(sayı1,y))


    elif(işlem == 11):
        sayı1 = int(input(" dereceyi giriniz : "))
        print("işleminiz yapılıyor...")
        time.sleep(1)
        print("cos {} = {} ".format(sayı1,math.cos(sayı1)))

    elif(sayı1 == 12):
        sayı1 = int(input(" Dereceyi giriniz : "))
        print("işleminiz yapılıyor...")
        time.sleep(1)
        print("tanjant {} = {} ".format(sayı1,math.tan(sayı1)))

    elif(sayı1 == 13):
        sayı1 = int(input(" Dereceyi giriniz : "))
        print("işleminiz yapılıyor...")
        time.sleep(1)
        x = math.cos(sayı1)/math.sin(sayı1)
        print("cotanjant {} = {} ".format(sayı1,x))

