#  Merhaba arkadaşlar,
#  Bu hafta öğrendiğimiz değişkenler, döngüler ve fonksiyonlar konularını pekiştirmek için iki farklı problem üzerinde çalışacağız. Her iki problemi de fonksiyon kullanarak çözmelisiniz.

#  🔹 1. Asal Sayı Kontrolü
#  Bir sayının asal sayı olup olmadığını kontrol eden bir Python fonksiyonu yazın.
#  ✅ Kurallar:
#  Asal sayı, sadece kendisine ve 1’e bölünebilen 1’den büyük pozitif sayılardır.
#  Fonksiyon, kullanıcıdan bir sayı almalı ve asal olup olmadığını kontrol etmelidir.
#  🎯 Örnek Kullanım:
#  asal_mi(7) # Çıktı: 7 bir asal sayıdır.
#  asal_mi(10) # Çıktı: 10 bir asal sayı değildir.

def asal_mi(a):
    for i in range(2,a):
        if(a%i==0):
            return print(f"{a} bir asal sayi değildir")
    return print(f"{a} bir asal sayidir")

asal_mi(25)
asal_mi(17)
            
#  🔹 2. Basit Hesap Makinesi
#  Kullanıcıdan iki sayı ve bir işlem türü alarak sonucu döndüren bir fonksiyon yazın.
#  ✅ Kurallar:
#  Kullanıcı +, -, *, / işlemlerinden birini seçmelidir.
#  Bölme işleminde, ikinci sayı 0 olursa "Bölme işlemi için ikinci sayı 0 olamaz!" şeklinde uyarı verin.
#  Kullanıcı geçersiz bir işlem girerse, "Geçersiz işlem türü!" mesajı gösterin.
#  🎯 Örnek Kullanım:
#  hesap_makinesi(5, 3, '+') # Çıktı: 5 + 3 = 8
#  hesap_makinesi(10, 2, '/') # Çıktı: 10 / 2 = 5.0
#  hesap_makinesi(4, 0, '/') # Çıktı: Bölme işlemi için ikinci sayı 0 olamaz!
#  hesap_makinesi(6, 2, '%') # Çıktı: Geçersiz işlem türü!

def hesap_makinesi(a,b,c):
    if(c=="+"):
        print(f"{a+b}")
    elif(c=="-"):
        print(f"{a-b}")
    elif(c=="*"):
        print(f"{a*b}")    
    elif(c=="/"):
        if(b==0):
            print("Bölme işlemi için ikinci sayi 0 olamaz lütfen tekrar deneyiniz")
        else:
            print(f"{a/b}")
n=int(input("Birinci Sayiyi Giriniz: "))
m=int(input("İkinci sayiyi giriniz: "))
p=input("Lütfen işlem seçiniz : '+' , '-' , '*' , '/' ")
hesap_makinesi(n,m,p)



