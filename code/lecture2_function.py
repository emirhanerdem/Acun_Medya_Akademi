
#calculate_tax()
def calculate_tax(price,rate=20):
    total_price=price+(price*rate/100)
    print(total_price)

calculate_tax(50,50)
calculate_tax(100)
calculate_tax(100,60)
calculate_tax(500)

print("******")

def calculate_tax2(price,rate=30):
    total_price=price+(price*rate/100)
    return total_price

price1 = calculate_tax2(50,50)
price2 = calculate_tax2(100)
price3 = calculate_tax2(100,60)
price4 = calculate_tax2(500)

print(price1+50) #kargo ücreti
print(price2+100)
print(price3*5)

print("****")


#gelecek argüman sayısı belirsiz??
def sum(*a):
    result=0
    for i in a:
        result+=i
    return result
print(sum(1,5))
print(sum(5,10,7))

print("******")

#lambda fonksiyonlar
topla = lambda a,b:a+b
print(topla(10,20))



