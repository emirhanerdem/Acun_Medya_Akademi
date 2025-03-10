# Konu: Değişkenler, veri tipleri (int, float, string, boolean), kullanıcıdan veri alma.
# Görev:
# · Kullanıcıdan adını, yaşını ve doğum yılını alarak ekrana aşağıdaki gibi yazdıran bir Python programı yazın:
# Merhaba Ali! 25 yaşındasın ve 1998 yılında doğmuşsun.
# · Kullanıcıdan iki sayı alarak bu sayıların toplamını, farkını, çarpımını ve bölümünü ekrana yazdırın.

ad=input("Adinizi giriniz : ")
soyad=input("Soyadinizi giriniz : ")
yas=input("Yasinizi giriniz : ")
dogumYili=input("Doğum yilinizi giriniz : ")
print(f"Merhaba {ad + " "+ soyad}! {yas} yasindasin ve {dogumYili} yilinda dogmussun ")

#--------------------------------------------------------------------------------------------------

x=int(input("ilk sayiyi giriniz : "))
y=int(input("ikinci sayiyi giriniz : "))

print(f"iki sayinin toplami : {x+y} ")
print(f"iki sayinin farki : {x-y}")
print(f"iki sayinin carpimi : {x*y}")
print(f"iki sayinin bolumu : {x/y} " )