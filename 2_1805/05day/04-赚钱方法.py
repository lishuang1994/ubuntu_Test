class father(object):
    def money(self):
        print("经商")
class mather(father):
    def money(self):
        print("下海")
class son(mather):
    def money(self):
        print("天上掉馅饼")
a = father()
a.money()
b = mather()
b.money()
c = son()
c.money()

