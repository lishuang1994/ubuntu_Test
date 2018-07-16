from random import randint
n = randint(1,100)
print("随机生成的数字是%d"%n)
i = 0
while True:
    num = int(input("请输入你要猜的数字"))
    i+=1
    if (num>n):
        print("输入的数字太大了")
    elif(num<n):
        print("输入的数字太小了")
    else:
        print("恭喜你猜对了")
        break
print("输入的次数是%d"%i)
if i<=5:
    print("你太聪明了")
else:
    print("方法还需要改进")
