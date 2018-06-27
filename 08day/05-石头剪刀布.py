'''
石头剪刀布
电脑玩家
普通玩家
'''
import random
i=1
while i<4:
    py=random.randint(1,3)
    pc=int(input("请输入1:石头2:剪刀3:布"))
    if (py==1 and pc==3) or (py==2 and pc==1) or (py==3 and pc==2):
        print("玩家赢了")
    elif py==pc:
        print("平局")
    else:
        print("电脑赢了")
    i+=1
