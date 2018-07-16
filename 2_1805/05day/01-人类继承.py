class person():
    def sleep(self):
        print("睡觉觉")
class woman(person):
    def eat(self):
        print("吃水果")
class man(person):
    def eat(self):
        print("吃烧烤")
laowang = woman()
laosong = man()
laowang.eat()
laowang.sleep()
laosong.eat()
laosong.sleep()
