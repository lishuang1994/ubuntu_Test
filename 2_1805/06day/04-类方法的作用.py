class Dog(object):
    def __init__(self):
        print("init")
        self.name = "tom"
    def __str__(self):
        print("str")
        return "哈哈"
    def __del__(self):
        print("del")
    def __new__(cls):#创建对象的方法
        print("new")
        return object.__new__(cls)
dog = Dog()
print(dog)
