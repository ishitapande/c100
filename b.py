class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def  start(self):
        print("HOw are you")

    def stop(self):
        print("I am fine")


ishi = Person("ishita", 12)


print(ishi.stop())