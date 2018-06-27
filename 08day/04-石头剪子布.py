'''
while True:
    print("石头,剪子,布")
'''
import random
computer = random.randint(1,3)
player = int(input("请输入1:石头2:剪子3:布"))
computer #!=0<=3
player #!=0<=3
if (computer==1 and player==3) or (computer==2 and player==1) or (computer==3 and player==2) :
    print("玩家赢了")
elif computer == player:    
    print("平局")
else:
    print("电脑赢了")

