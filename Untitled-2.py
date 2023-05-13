ondalikli_sayi = float(input("Ondalıklı sayıyı girin: "))

# Ondalık kısmı ve tam sayı kısmını ayırın
tam_sayi = int(ondalikli_sayi)
ondalik_kisim = ondalikli_sayi - tam_sayi

# Kesir halini hesaplayın
pay = int(ondalik_kisim * (10 ** len(str(ondalik_kisim))))
payda = 10 ** len(str(ondalik_kisim))

# Kesir halini basın
print("Ondalıklı sayının kesir hali: {}/{}".format(pay, payda))
