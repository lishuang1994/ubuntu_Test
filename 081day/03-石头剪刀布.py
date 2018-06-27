#1----石头
#2----剪刀
#3----布
import random
pc = random.randint(1,3)
player = int(input("请输入1:石头2:剪刀3:布"))
if (pc == 1 and player == 3) or (pc == 2 and player == 1) or (pc == 3 and player == 2):
    print("玩家赢了")
elif pc == player:
    print("平局")
else:
    print("电脑赢了")
