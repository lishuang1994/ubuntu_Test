class Cat():

    def __init__(self,color,size):
        self.name = "汤姆"
        self.color = color
        self.size = size
    def introduce(self):
        print("我的颜色是%s 我的大小是%d"%(self.color,self.size))
c = Cat("红色",12)
c.introduce()
