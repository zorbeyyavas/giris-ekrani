#break komutu döngüyü sona erdirmek için kullanılır genellikle döngüde if yada wwhile ile kullanılır
#klavyeden girilen kullanıcı adı carsamba sifre myo olduğunda giriş başarılı aksi durumda kullanıcı adı veya şifre hatalı diyen mesaj 
#while kullanarak 1. yönetem
kullaniciadi="carsamba"
sifre="myo"
while True:
    a=input("kullanıcı adi giriniz")
    b=input("sifre giriniz")
    if(a==kullaniciadi and b==sifre):
        print("giris başarili")
    else:
        print("kullanıcı adı veya şifre hatalı")
#if kullanarak 2. yönetem
kullaniciadi="carsamba"
sifre="myo"
a=input("kullanıcı adi giriniz")
b=input("sifre giriniz")
if(a==kullaniciadi and b==sifre):
        print("giris başarili")
else:
        print("kullanıcı adı veya şifre hatalı")