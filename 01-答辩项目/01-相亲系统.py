print('\n'.join([''.join([('Love'[(x-y)%4]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))
print("欢迎来到万里挑一注册相亲系统".center(56,"*"))
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
def zong():
    while True:
        print("1:添加用户".center(56,"*"))
        print("2:查找用户".center(56,"*"))
        print("3:修改信息".center(56,"*"))
        print("4:删除用户".center(56,"*"))
        print("5:输出用户".center(56,"*"))
        print("6:配对成功".center(56,"*"))
        num = int(input("请选择功能"))
        if num  == 1:
            d = {}#空字典
            while True:
                name = input("请输入要添加用户的名字")
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

                #添加到列表
                list1.append(d)
                print("添加成功")
                break
             
        elif num == 2:
            name = input("请输入要查找的用户名")
            flag = False#假设没有咱们要找的人
            for i in list1:
                if name == i["name"]:
                    print("姓名:%s\n性别:%s\n电话:%s"%(i["name"],i["sex"],i["phone"]))
                    flag = True#找到了
                    break

            if flag == False:
                print("查无此人")                
        elif num == 3:
            #要改之前，你得先查到你要找的那个
            name = input("请输入你要改的人的姓名")
            flag = False
            for i in list1:
                if name == i["name"]:
                    print("1:修改名字")
                    print("2:修改性别")
                    print("3:修改电话")
                    num_1 = int(input("请选择功能"))
                    if  num_1 == 1:
                        new_name = input("请输入新的名字")
                        i["name"] = new_name
                    elif num_1 == 2:
                        new_sex = input("请输入新的性别")
                        i["sex"] = new_sex
                    elif num_1 == 3:
                        new_phone = input("请输入新的电话")
                        i["phone"] = new_phone
                    flag = True
                    break
            if flag == False:
                print("查无此人")
        elif num  == 4:
            name = input("请输入你要删除的用户的名字")
            flag = False
            for position,i in enumerate(list1):#把索引遍历出来
                if name == i["name"]:
                    flag = True#找到了
                    print("1:确认删除")
                    print("2:取消删除")
                    num_2 = int(input("请选择序号"))
                    if num_2 == 1:
                        list1.pop(position)#直接删除
                    break
            if flag == False:
                print("查无此人") 
        elif num == 5:#打印名片
            print("名字\t性别\t电话")
            for i in list1:
                print(" "+i["name"]+"\t "+i["sex"]+"\t "+i["phone"])
        elif num == 6:
            print("恭喜你已经注册成功，希望您早日找到终生伴侣!".center(50,"*"))        
            exit()
register()
