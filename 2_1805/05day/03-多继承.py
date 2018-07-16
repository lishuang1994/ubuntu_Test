class cat():
    def eat(self):
        print("吃猫粮")
class dog():
    def sleep(self):
        print("睡觉觉")
class animal(cat,dog):
    pass
a = animal()
a.eat()
a.sleep()
print(animal.__mro__)
