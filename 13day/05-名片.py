list = []
print("名片管理系统".center(50,"*"))
while True:
    print("1:添加名片".center(50,"*"))
    print("2:查找名片".center(50,"*"))
    print("3:修改名片".center(50,"*"))
    print("4:删除名片".center(50,"*"))
    print("5:打印名片".center(50,"*"))
    num = int(input("请选择功能"))
    if num == 1:
        d = {}
        while True:
            name = input("请输入要添加的名字")
            if len(name) > 4:
                print("太长请重新输入")
                continue
            job = input("请输入要添加的职位")
            if len(job) > 4:
                print("太长请重新输入")
                continue
            phone = input("请输入要添加的电话")
            if len(phone) !=11 or phone.startswith("1") == False:
                print("手机号输入有误，请重新输入")
                continue
            d["name"] = name
            d["job"] = job
            d["phone"] = phone
            list.append(d)
            print("添加成功")
            break
    elif num == 2:
        name = input("请输入要查找的姓名")
        flag = False
        for i in list:
            if name == i["name"]:
                print("姓名:%s\n职位:%s\n电话:%s"%(i["name"],i["job"],i["phone"]))
                flag = True
                break
        if flag == False:
            print("查无此人")
    elif num == 3:
        name = input("请输入你要改的人的姓名")
        flag = False
        for i in list:
            if name == i["name"]:
                print("1:修改姓名")
                print("2:修改职位")
                print("3:修改电话")
                num_1 = int(input("请选择功能"))
                if num_1 == 1:
                    num_name = input("请输入新的名字")
                    i["name"] = new_name
                elif num_1 == 2:
                    new_job = input("请输入新的职位")
                    i["job"] = new_job
                elif num_1 == 3:
                    new_phone = input("请输入新的电话")
                    i["phone"] = new_phone
                flag = True
                break
        if flag == False:
            print("查无此人")
    elif num == 4:
        name = input("请输入你要删除的名字")
        flag = False
        for position,i in enumerate(list):
            if name == i["name"]:
                flag = True
                print("1:确认删除")
                print("2:取消删除")
                num_2 = int(input("请选择序号"))
                if num_2 == 1:
                    list.pop(position)
                break
            if flag == False:
                print("查无此人")
            elif num == 5:
                print("名字\t职位\t电话")
                for i in list:
                    print(" "+i["name"]+"\t"+i["job"]+"\t"+i["phone"])

















        














            
