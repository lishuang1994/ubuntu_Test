class Tool():
    count = 0
    def __init__(self):
        Tool.count+=1
        self.name = "liandao"
    def fuzi(self):
        print("咔咔")
    @classmethod
    def getCount(cls):
        return cls.count
chuizi = Tool()
chuizi.fuzi()
chuizi1 = Tool()
chuizi1.fuzi()
print(chuizi.getCount())
print(chuizi1.getCount())
