#从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
#电脑 随机 出拳 —— 先假定电脑只会出石头，完成整体代码功能
#比较胜负
#1:石头2:剪刀3:布
import random
computer = random.randint(1,3)
player = int(input("请输入1:石头2:剪刀3:布"))
if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
    print("玩家赢了")
elif player == computer:
    print("平局")
else:
    print("电脑赢了")
