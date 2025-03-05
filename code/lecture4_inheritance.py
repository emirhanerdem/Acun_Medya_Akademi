#inheritance(kalıtım,miras)
class Vehicle():
    def __init__(self,model):
        self.model=model
    def start(self):
        print(f"{self.model} Arac baslatiliyor")

class Car(Vehicle):
    def __init__(self,model):
        #self.model #car classındaki modeli işaret eder
        super().__init__(model)

        pass
class Truck(Vehicle):   
    def __init__(self,model):
        super().__init__(model)
    def start(self):  #method overriding
        print(f"{self.model} kamyoneti baslatiyor.")

class Motocyle(Vehicle):
    def __init__(self,model):
        super().__init__(model)


car1 = Car("Hyundai")
car1.start()

truck1 = Truck("Mercedes")
truck1.start()