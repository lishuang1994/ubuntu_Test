class Person(object):
    def __init__(self,name,age,taste):
        self.name = name
        self._age = age
        self.__taste = taste
    def showperson(self):
        print(self.name)
        print(self._age)
        print(self.__taste)
    def dowork(self):
        self._work()
        self.__away()
    def _work(self):
        print("my_work")
    def __away(self):
        print("my_away")

