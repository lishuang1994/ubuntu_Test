import time
time.time
print("欢迎来到如家酒店".center(56,"*"))
list = []
def register():
    while True:
        account = input("请输入账号")
        pwd= input("请输入密码") 
        user = {}#初始化字典
        if len(account) == 11 and account.startswith("1")and len(pwd) > 6:
            #保存账号和密码
            user["account"] = account
            user["pwd"] = pwd
            list.append(user)
            print("注册成功")
            login()
            break
        else:
            print("注册失败,请重新输入")
def login():#登录函数
    while True:
        acc = input("请输入账号")
        pwd = input("请输入密码")
        for i in list:
            if acc == i["account"] and pwd == i["pwd"]:
                print("登录成功")
                zong()
                break
                
            else:
                print("登录失败请重新输入")


list1 = []
def gongneng():
    while True:
        print("1:入住".center(56,"*"))
        print("2:查找".center(56,"*"))
        print("3:删除".center(56,"*"))
        print("4:统计".center(56,"*"))
        print("5:退出".center(56,"*"))
        num = int(input("请选择功能"))
        if num  == 1:
            d = {}
            while True:
                name = input("请输入要登记的用户名字")
                if len(name) > 4:
                    print("太长，请重新输入")
                    continue
                sex = input("请输入要添加用户的性别")
                if len(sex) > 1:
                    print("请输入男，或者女")
                    continue
                phone = input("请输入添加的用户的手机号")
                if len(phone) != 11 or  phone.startswith("1") == False:
                    print("手机号输入有误，请重新输入")
                    continue
                d["name"] = name
                d["sex"] = sex
                d["phone"] = phone

                list1.append(d)
                print("添加成功")
                break
                count = people*time
        elif num == 2:
            name = input("请输入要查找离店人的名字")
            flag = False
            for i in list1:
                if name == i["name"]:
                    print("姓名:%s\n性别:%s\n电话:%s"%(i["name"],i["sex"],i["phone"]))
                    flag = True#找到了
                    break

            if flag == False:
                print("查无此人")                
        elif num  == 3:
            name = input("请输入你要删除的用户的名字")
            flag = False
            for position,i in enumerate(list1):
                if name == i["name"]:
                    flag = True
                    print("1:确认删除")
                    print("2:取消删除")
                    num_2 = int(input("请选择序号"))
                    if num_2 == 1:
                        list1.pop(position)#直接删除
                    break
            if flag == False:
                print("查无此人") 
        elif num == 4:
            money = count*10
                if people in list1():
                    print("今日的收益额是%d 总入住人数是%d 离店人数是%d"%(money,count,people))
        elif num == 5:
            print("您已经退出系统,欢迎下次光临")
register()G
