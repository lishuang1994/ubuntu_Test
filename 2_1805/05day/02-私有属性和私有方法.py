class animal(object):
    def sleep(self):
        print("我们一起睡觉觉")




class Cat(animal):
    def eat(self):
        print("吃小鱼")
class Dog(animal):
    def wark(self):
        print("喵喵叫")
jiafeimao = Cat()
xiaobai = Dog()

jiafeimao.eat()
jiafeimao.sleep()
xiaobai.wark()
xiaobai.sleep()
