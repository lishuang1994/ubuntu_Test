class people():
    def __init__(self,name,height,weight):
        self.name = name
        self.heght = height
        self.weight = weight
    def introduce(self):
        print("我的名字是%s 我的身高是%s 我的体重是%s"%(name,height,weight))


name = "李爽"
height = 165
weight = 110
woman = people(name,height,weight)

woman.introduce()
