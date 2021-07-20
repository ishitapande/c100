class Car(object):
   
    def __init__(self, model, color, company, speed):
        self.color = color
        self.company = company
        self.speed = speed
        self.model = model

    def start(self):
        print("Wrommm Start")
     
    def stop(self):
        print("STOPP")

    def acce(self):
        print("Accelarating forward")

    def gear(self,gear_type):
        print("gear is changed")

audi=Car("A6","red","audi",80)
print(audi.color)
print(audi.start())