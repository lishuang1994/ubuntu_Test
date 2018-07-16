class cat:
    def eat(self):
        print("猫吃鱼")
    def drink(self):
        print("猫喝牛奶")
    def introduce(self):
        print("猫的颜色是%s,猫的产地是%s,猫的身价是%s"%(self.color,self.type,self.price))
fadou = cat()
fadou.eat()
fadou.drink()
fadou.color = "黄色"
fadou.type = "法国"
fadou.price ="8888"
fadou.introduce()
