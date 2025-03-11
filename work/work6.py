# Ödev: Listeler ve Tuple'lar
# Konu: Listeler, Tuple'lar, listelerde döngü.
# Görev:
# · Kullanıcıdan 5 adet sayı alarak bir listeye ekleyin ve bu listenin toplamını, ortalamasını, en büyük ve en küçük elemanını bulun.
list = []
for i in range(5):
    num=int(input("Bir sayi giriniz : "))
    list.append(num)
toplam = sum(list)

ortalama = toplam / len(list)

en_buyuk = max(list)
en_kucuk = min(list)

print(f"Liste : {list}")
print(f"Toplam : {toplam}")
print(f"Ortalama : {ortalama}")
print(f"En Büyük Eleman : {en_buyuk}")
print(f"En Küçük Eleman : {en_kucuk}")

# · Kullanıcıdan aldığı kelimeleri bir listeye ekleyerek ters sıralayan bir program yazın.
kelime = []
for i in range(5):
    kel = input("Bir kelime giriniz : ")
    kelime.append(kel)
kelime.reverse()
for i in kelime:
    print(i)

# · Bir liste içindeki tekrar eden elemanları kaldıran bir program yazın.
liste = (2,4,9,10,3,17,7,8,4,3,17)
benzersiz_list=[]

for eleman in liste:
    if eleman not in benzersiz_list:
        benzersiz_list.append(eleman)

print(liste)
print(benzersiz_list)