class Cat(object):
    __instance = None
    __flag = False
    def __new__(cls,*args,**kwargs):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance
    def __init__(self,name):
        if Cat.__flag == False:
            self.name = name
            Cat.__flag = True
maomao = Cat("maomao")
print(id(maomao))    
maomao1 = Cat("maomao1")
print(id(maomao1))

print(maomao.name)
