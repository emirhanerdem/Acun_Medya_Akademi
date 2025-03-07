# f = open("deneme.txt","r")
# icerik = f.read()
# print(icerik)
# f.close()

#----------------------------------------------------------------

#dosyayı manuel olarak kapatmaya gerek kalmayan with open yapısı
# with open("deneme.txt","r") as f:  #2. parametreye "r" yazmasak bile default read modunda çalışır
#     # icerik = f.read()
#     # icerik = f.readlines() #satır satır okuma yapar ve her elemanı bir diziye yazar dönen şey dizidir
#     icerik = f.readline()
#     pozisyon = f.tell() #pozisyonun yerinin söyler
#     print(pozisyon)
#     f.seek(0) #pozisyonu 0 a getirir
#     # for satir in f: 
#     #     print(satir,end="")

#     print(icerik)
#---------------------------------------------------------------------------------
#w modu
# with open("deneme2.txt","w") as f: #her seferinde yeniden yazar
#     f.write("deneme")

# #---------------------------------------------------------------------------------
# # a modu
# with open("deneme2.txt","a") as f: #sonradan yazı ekler
#     f.write(" sinavi")

#------------------------------------------------------------------------------------
#deneme.txt dosyasının içeriğini deneme2.txt dosyasına yazma
# with open("deneme.txt") as okunacak:
#     with open("deneme2.txt","w") as yazilacak:
#         for satir in okunacak:
#             yazilacak.write(satir)
#------------------------------------------------------------------------------------
#Ödev : Kullanıcının girdiği metni bir .txt dosyasına yazan daha sonra bu dosyayın içeriği ekrana yazan program

# text = input("Bir metin giriniz : ")
# with open("deneme3.txt","w") as yazilacak:
#     yazilacak.write(text)

# with open("deneme3.txt","r") as okunacak:
#     oku = okunacak.read()
#     print(oku)

#------------------------------------------------------------------------------------
#Ödev : Kullanıcıdan alınan 5 farklı satır verisini bir dosyaya kaydedin ve 
# ardından bu dosyadaki verileri satır satır okuyarak ekrana yazdırın
dizi = []
for i in range(5):
    texts=input(f"{i+1}. metni giriniz : ")
    dizi.append(texts)
#dosyaya yazma işlemi    
with open("deneme4.txt","w") as yaz:
    for i in dizi:
        yaz.write(i + "\n")
#dosyadaki verileri satır satır yazma işlemi
with open("deneme4.txt") as oku:
    for satir in oku:
        print(satir, end="")
