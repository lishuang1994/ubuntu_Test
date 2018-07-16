class person():#人类
    def __init__(self,name):
        self.name = name
        self.hp = 100
    def naiqang(self,gun):#持枪
        self.gun = gun
    def zhuangzidan(self,danjia,zidian):
        danjia.list.append(zidian)#装子弹
    def zhuangdanjia(self,gun,danjia):#装弹夹
        gun.danjia = danjia
    def opengun(self,diren):#开枪
        zidan = self.gun.danjia.tanzidan()
        zidan.kill(diren)
    #count---伤害量
    def diaoxue(self,count):
        self.hp -= count
        print("还剩多少%d"%self.hp)
        if self.hp <= 0:
            print("死翘翘")
class gun():#枪类
    def __init__(self,name):
        self.name = name
        self.danjia = None#假设没有弹夹
class danjia():#弹夹类
    def __init__(self,name,count):
        self.name = name
        self.count = count
        self.list = []
    def tanzidan(self):#弹子弹
        zidan = self.list.pop()
        return zidan
class zidan():#子弹
    def __init__(self,name,kill_count):
        self.name = name
        self.kill_count = kill_count#子弹伤害
    def kill(self,diren):#子弹杀人
        diren.diaoxue(self.kill_count)
laowang = person("老王")#创建老王
ak47 = gun("ak47")#创建枪
danjia = danjia("快速扩容,40")#创建弹夹
laowang.naqiang(ak47)#让老王持枪
for i in range(40):#创建一些子弹
    zidan = zidan("5.56",20)
    laowang.zhuangzidan(danjia,zidan)
laowang.zhuangdanjia(ak47,danjia)#装弹夹
laosong = person("老宋")
laowang.opengun(laosong)
laowang.opengun(laosong)
laowang.opengun(laosong)
laowang.opengun(laosong)
laowang.opengun(laosong)
laowang.opengun(laosong)
laowang.opengun(laosong)













