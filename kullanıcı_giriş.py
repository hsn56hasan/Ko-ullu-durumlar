print(""""
******************************
Kullanıcı Girişi
******************************""")

sys_kullanıcı_adı = "Hasan"
sys_parola = "123456"

kullanıcı_adı = input("Kullanıcı Adı:")
parola = input("Parola:")

if (kullanıcı_adı == sys_kullanıcı_adı and sys_parola != parola ):
    print("Parola hatalı...")

elif (kullanıcı_adı != sys_kullanıcı_adı and sys_parola == parola):
    print("Kullanıcı adı hatalı...")

elif(kullanıcı_adı != sys_kullanıcı_adı and sys_parola != parola):
    print("Kullanıcı adı ve Parola hatalı...")

else:
    print("Sisteme başarıyla giriş yapıldı...")
