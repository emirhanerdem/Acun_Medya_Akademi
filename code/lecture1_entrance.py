print("Hello World")


#değişkenler
#python type-safe(tip güvenilir) değildir.
#geçici hafızada (ram) age ismine 50 değeri olduğunu atadım
age=50 #int-integer

print(age)

age = "Merhaba" #str-string
print(age)

#c#-java type safe
#python-js type safe değil

print(type(age))

#operatörler

#aritmatik operatörler(matematiksel işlem)
print(1+1) #2 int
print(5-1) #4 int
print(5*2) #10 int
print(25/5) #5.0 float olarak bölme işlemi yapar
print(25//5) #5 iki tane bölme işlemi kullanırsak cevabı int olarak yazar
print(7//2) #3
print(3**3) #27 üs alma işlemidir
print(100%3) #1 mod operatörü

#atama operatörleri
name="emirhan"
number=50
number+=10 #number = number + 10
number-=5 #nunber = number - 5
print(number)

number2=3
number2 **=2 #number2 = number2 **2  >> 3 ** 2 
print(number2)

#bool-boolean >> 2 değere sahiptir true - false

#karşılaştırma operatörleri
print(1==1) #true döner
print(1!=1) #false döner
print(10>5) #true
print(10>=5) #true
print(10<=10) #true

print("emirhan"=="emirhan")
#genelde stringlerde bu operatörler tercih edilmez
##stringlerde büyük küçüktür operatörleri sözlük sırasına göre UNICODE değerine göre sıralanır
print("car">"bus")
print("Apple">"apple") #'A' >65 , 'a' >97
print("apple">"Apple")

#mantıksal operatörler >>and,or,not
print(1==1 and 10>5)
print(1==1 or 5<3)

students = ["Emir","Yasin","Emirhan","Barış",5,True,10.1,2]
print(students)

a=5
b=a
b+=4
print(a) #5
print(b) #9

students2 = students
students2.append("Ahmet")
students2.append(100)

print(students)
print(students2)

#döngüler
#for
for i in range(5):
    print(i)
    print("hello")
print("for bitti")

for i in range(5,10):
    print(i)

for i in range(5,100,5):
    print(i)

students3 = ["ali","ayşe","kerem","emir"]
for student in students3:
    print(student)

print("*****")

for student in students3:
    if student=="kerem":
        continue #döngüye sonraki elemeandan devam et
    print(student)

print("*****")

for student in students3:
    if student=="kerem":
        break #döngüyü kır
    print(student)

#while
#koşul ile çalışıyor
x=100
while x>50:
    print(x)
    x-=1
    
user_input=input("Lutfen bir deger giriniz ve cikmak için q tuşuna basiniz")
while user_input!="q":
    print(user_input)
    user_input=input("Lutfen bir deger giriniz ve cikmak için q tuşuna basiniz")

#fonksiyonlar

