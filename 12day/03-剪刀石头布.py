import random
computer = random.randint(1,3)
player = int(input("请输入1:剪刀2:石头3:布"))
if (computer == 1 and player == 2) or (computer == 2 and player == 3) or (computer == 3 and player == 1):
    print("玩家赢了")
elif computer == player:
    print("平局")
else:
    print("电脑赢了")
