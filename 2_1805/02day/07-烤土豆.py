class SweetTuDou():
    def __init__(self):
        self.status = "生的"
        self.time = 0
        self.list = []
    def cook(self):
        self.time+=1
        if self.time < 3:
            self.status = "生的"
        elif self.time >= 3 and self.time < 10:
            self.status = "半生不熟"
        elif self.time >=10 and self.time < 15:
            self.status = "熟了"
        elif self.time > 15:
            self.status = "糊了"
    def tellStatus(self):
        print(self.status)
        print("佐料有%s"%str(self.list))
    def addZuoLiao(self,s):
        self.list.append(s)
digua = SweetTuDou()
for i in range(16):
    digua.cook()
    if i == 1:
        digua.addZuoLiao("盐")
    elif i == 3:
        digua.addZuoLiao("糖")
    elif i == 5:
        digua.addZuoLiao("辣椒酱")
    digua.tellStatus()

