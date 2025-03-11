# Konu: For ve while döngüleri.
# Görev:

# · 1’den 100’e kadar olan sayıları ekrana yazdırın.
for i in range(1,101):
    print(i)

# · 1’den 100’e kadar sadece çift sayıları ekrana yazdıran bir program yazın.
for i in range(1,101):
    if(i%2==0):
        print(i)

# · Kullanıcıdan bir sayı alıp, bu sayının faktöriyelini hesaplayan bir program yazın.
# Örnek: 5! = 5 * 4 * 3 * 2 * 1 = 120
num=int(input("Faktoriyeli alinicak sayiyi giriniz : "))
total=1
temp=1
while(temp<=num):
    total*=temp
    temp=temp+1
print(total)

# · 1’den 100’e kadar olan tüm asal sayıları bulan bir program yazın.
for sayi in range(2,101) : 
    bolen = 2
    while bolen * bolen <=sayi and sayi%bolen!=0:
        bolen+=1
    if bolen * bolen > sayi:
        print(sayi, end=" ")
    