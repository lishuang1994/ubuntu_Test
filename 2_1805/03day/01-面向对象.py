import random
class Tool():
   def faf(self):
        list = []
        n = 0
        while len(list)<10:
            a = random.randint(1,101)
            list.append(a)
            c = list[n]
            n+=1
            if list.count(c)>1:
                list.pop()
                n=n-1
        print(list)
aa = Tool()
aa.faf()
