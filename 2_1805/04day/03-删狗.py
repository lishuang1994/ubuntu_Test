class dog():
    def __init__(self,name):
        self.name = name
    def __del__(self):
        print("我要快乐")
    def wark(self):
        print("汪汪叫")
tom = dog("tom")#会执行__init__()
tom1 = tom
del tom
print("啦啦啦啦啦啦")
