print("-------欢迎来到学生管理系统-------")
l = []
while True:
    user=input("1,添加\n2,删除\n3,修改\n4,查找\n0,退出")
    if user == "1":
        use = input("请输入您要添加的姓名:")
        l.append(use)
        print("-------添加成功-------")
        print(l)
    elif user == "2":
        us = input("请输入您要删除的姓名:")
        if us in l:
            l.remove(us)
            print("-------删除成功-------")
            print(l)
        else:
            print("-------查无此人-------")
    elif user == "3":
        f = input("请输入您要修改的姓名:")
        if f in l:
            b = l.index(f)
            n = input("请输入您的新姓名:")
            l[b]=n
            print("-------修改成功-------")
            print(l)
        else:
            print("-------查无此人-------")
    elif user == "4":
        m = input("请输入您要查找的姓名:")
        if m in l:
            print(m)
        else:
            print("-------查无此人-------")
    elif user == "0":
        print("-------退出成功-------")
        break
