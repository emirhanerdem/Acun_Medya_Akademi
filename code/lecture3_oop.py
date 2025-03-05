#object-priented-p

class Car():
    
    model = ""

    #constructor - yapıcı metod
    def __init__(self,model,year=2025):
        self.year=year
        self.__model=model
        print("Car nesnesi oluşturuldu")

    def start(self,a):
        model = "Fonksiyon içi değişken"
        print(f"{self.__model} {a} araba calistiriliyor")
        self.startEngine()

    def startEngine(self):
        print("Motor başlatiliyor")

    def set_model(self,model):
        if len(model) < 3 :
            print("Model ismi en az 3 hane olmalidir")
            return
        self.__model=model
    def get_model(self):
        return self.__model

car1 = Car("Toyota",2020)
car1.set_model="acccc"
print(car1.get_model())
car1.start(1)

car2=Car("Hyundai")
car2.start(2)