# Konu: Karar yapıları (if-elif-else).
# Görev:
# · Kullanıcının girdiği bir sayının tek mi çift mi olduğunu bulan bir Python programı yazın.
number=int(input("Bir sayi gir : "))
if (number % 2==0) :
    print("Sayi ciftdir")
else: print("Sayi tektir")

# · Kullanıcının notunu alarak aşağıdaki not sistemine göre harf notunu hesaplayın:
# 90-100 -> A
# 80-89 -> B
# 70-79 -> C
# 60-69 -> D
# 0-59 -> F
note=int(input("Notunuzu giriniz : "))
if(note>=90 & note<=100) :
    print(f"{note} : A")
elif(note>=80 & note<=89) :
    print(f"{note} : B")  
elif(note>=70 & note<=79) :
    print(f"{note} : C") 
elif(note>=60 & note<=69) :
    print(f"{note} : D") 
elif(note>=0 & note<=59) :
    print(f"{note} : F")
else: print("Yanlis not girişi yaptiniz lütfen tekrar deneyiniz") 

# · Kullanıcının yaşına göre hangi yaş grubunda olduğunu bulan bir program yazın:
# 0-12 yaş: Çocuk
# 13-19 yaş: Genç
# 20-59 yaş: Yetişkin
# 60 ve üzeri: Yaşlı

yas=int(input("Yasinizi giriniz : "))
if(yas>=60) :
    print(f"{yas} : Yasli")
elif(yas>=20 & yas<=59) :
    print(f"{yas} : Yetiskin")  
elif(yas>=13 & yas<=19) :
    print(f"{yas} : Genc") 
elif(yas>=0 & yas<=12) :
    print(f"{yas} : Cocuk") 
else: print("Yanlis yas girişi yaptiniz lütfen tekrar deneyiniz") 