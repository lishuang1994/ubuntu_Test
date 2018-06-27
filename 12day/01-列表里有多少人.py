list = ["laowang","laoli","laogao","laowang"]
name = input("请输入您要查询的名字")
count = 0
for i in list:
    if name == i:
        print("找到的索引是%d"%count)
    count +=1
for position,i in enumerate(list):
    if name == i:
        print(position,i)
