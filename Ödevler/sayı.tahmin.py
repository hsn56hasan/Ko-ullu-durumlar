import random
import time

rastgele_sayı = random.randint(1,40)
tahmin_hakkı = 7

while True:

    tahmin = int(input("Tahmininiz:"))

    if (tahmin < rastgele_sayı):
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)

        print("Daha yüksek sayı söyleyin...")

        tahmin_hakkı -= 1
    elif (tahmin > rastgele_sayı):
        print("Bilgiler Sorgulanılıyor...")
        time.sleep(1)

        print("Daha küçük bir sayı söyleyin...")

        tahmin_hakkı -= 1
    else:
        print("Bilgiler Sorgulanılıyor...")
        time.sleep(1)
        print("Tebrikler sayınız",rastgele_sayı)
        break
    if (tahmin_hakkı == 0 ):
        print("Tahmin hakkınız bitti")
        break