class Home():
    
    def __init__(self,name,size):
        self.name = name
        self.size = size
        self.list = []
    def __str__(self):
        msg = "房子的地址是%s 房子的大小是%d"%(self.name,self.size)
        return msg
    def zhuangjiazhu(bingxiang)
        if self.size < jiaju.price:
            print("不能在装了")
        else:
            self.size = self.area-jiazhu.size
            self.list.append(bingxiang)
beijing = Home("碧桂园",150)
print(beijing)

class bed():
    def __init__(self,color,area):
        self.color = color
        self.area = area
    def __str__(self):
        msg = "床的颜色是%s 床的面积是%s"%(self.color,self.area)
        return msg
huangchao = bed("红色",15)
print(huangchao)
