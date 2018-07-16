dir = []
def money(kn,month,day):
    all_money = 0
    for i in range(30):
        for j in range(day):
            if km <= 6:
                all_money = 3
            elif km > 6 and km <= 12:
                all_money = 4
            elif km > 12 and km <= 22:
                all_money = 5
            elif km > 22 and km <= 32:
                all_money = 6
            elif km > 32:
                if (km-32)%20 == 0:
                    all_money = 6+(km-32)/20
                else:
                    all_money = 6+int((km-32)/20)+1
            if all_money>= 100 and all_money<150:
                all_money=all_money*0.8
            elif all_money>=150 and all_money<400:
                all_money= all_money=all_money*0.5
    dir["month"]=all_money
    list.append(dir)
    print(list)
def count():
    for i in list:
        for j,k in i.items():
            print("%d月份花了%.02f元"%(j,k))
while True:
    print("菜单\t1:乘坐\t2:计算")
    cai = ("请输入功能")
    if cai == 1:
        km = int(input("请输入距离"))









else:
                price = 6+int((km-32)/20)+1
        #打折逻辑
        if all_money > 100 and all_money <= 150:
                price = price*0.8
        elif all_money > 150 and all_money <=400:
                price = price *0.5
    
        all_money = all_money + price

print("总钱%.02f"%all_money)
