sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

yuzde = (sayi1 / 100) * sayi2

print("{0} sayısının {1} sayısına oranı %{2} olarak hesaplandı.".format(sayi1, sayi2, yuzde))