list = []
def play_game():
    pass


def print_card():
    print("名字\t职位\t电话")
        for i in list:
            print(" "+i["name"]+"\t "+i["job"]+"\t "+i["phone"])



def del_card():
 name = input("请输入你要删除的名字")
        flag = False
        for position,i in enumerate(list):#把索引遍历出来
            if name == i["name"]:
                flag = True#找到了
                print("1:确认删除")
                print("2:取消删除")
                num_2 = int(input("请选择序号"))
                if num_2 == 1:
                    list.pop(position)#直接删除
                break


def fix_card():
    name = input("请输入你要改的人的姓名")
    flag = False
    for i in list:
        if name == i["name"]
            print("1:修改姓名")
            print("2:修改职位")
            print("3:修改电话")
            num_1 = int(input("请选择功能"))
                if  num_1 == 1:
                    new_name = input("请输入新的名字")
                    i["name"] = new_name
                elif num_1 == 2:
                    new_job = input("请输入新的职位")
                    i["job"] = new_job
                elif num_1 == 3:
                    new_phone = input("请输入新的电话")
                    i["phone"] = new_phone
                flag = True


def find_card():
    name = input("请输入你要查找的姓名")
    flag = False
    for i in list:
        if name == i["name"]
            print("姓名:%s\n职位%s\n电话%s\n"%(i["name"],i["job"],i["phone"]))
            flag = True
        if flag == False:
            print("查无此人")
def add_card():
    if num == 1:
        d = {}
        while True:
            name = input("请输入要添加的名字")
            job = input("请输入要添加的工作")
            phone = input("请输入要添加的电话")
            d["name"] = name
            d["job"] = job
            d["phone"] = phone
            list.append(d)
            print("添加成功")

    pass
print("欢迎来到名片输入系统".center(44,"*"))
print("1:添加名片".center(50,"*"))
print("2:添加地址".center(50,"*"))
print("3:查找名片".center(50,"*"))
print("4:更改名片".center(50,"*"))
print("5:删除名片".center(50,"*"))
print("6:添加游戏".center(50,"*"))
