print("""
**************************************

Geometri Hesaplama Programı

İşlemler;

1. Dikdörtgen Alanı

2. Üçgen Alanı

3. Kare Alanı
 
4. Dikdörtgen Çevre

5. Üçgen Çevre

6. Kare Çevre

**************************************
""")

işlem = input("İşlem giriniz:")

if işlem == "1":
    a = float(input("Uzun Kenar:"))
    b = float(input("Kısa Kenar:")) 
    print("{} ile {} çarpımı {} dır".format(a,b,a  *  b))



if işlem == "2":
    c = float(input("Taban:"))
    d = float(input("Yükseklik:"))
    print("{} çarpı {} bölümü {} dır".format(c,d,c * d / 2))
    print(" %{} ".format(c * d / 2 * c * d / 2 / 100))

if işlem == "3":
    e = float(input("1. Kenar:"))
    karesi = e * e
    print("{} sayının karesi {} dır".format(e,karesi))

if işlem == "4":
    f = float(input("Uzun Kenar:"))
    g = float(input("Kısa Kenar:"))
    print("{} ile {} toplamı {}".format(f * 2,g * 2,f * 2 + g * 2))

if işlem == "5":
    h = float(input("1. Kenar:"))
    i = float(input("2. Kenar:"))
    j = float(input("3. Kenar:"))
    print("{} ile {} ile {} toplamı {}".format(h,i,j,h+i+j))

if işlem == "6":
    k = float(input("1 Kenar CM:"))
    print("{} 4 ile çarpım {}".format(k,k * 4))