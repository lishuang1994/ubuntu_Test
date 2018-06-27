'''
猜数字
和电脑比赛大小
随机十次
'''
import random
computer = random.randint(1,100)
i=0
while i<10:
    user = int(input("请输入一个数字"))
    if computer > user:
        print("输入小了")
    elif computer < user:
        print("输入大了")
    else:
        print("猜对了")
        i=10
    i+=1
