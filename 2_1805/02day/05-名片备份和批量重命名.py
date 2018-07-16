import os
def gn():
    while True:
        print("1:写")
      　print("2:读")
        print("3:备份")
        print("4:重命名")
        print("5:退出系统")
        a = int(input("请选择功能"))
        if a == 1:
            xie()
        elif a == 2:
            du()
        elif a == 3:
            bf()
        elif a == 4:
            cmm()
        elif a == 5:
            print("退出系统")
            break
def xie():
    l = input("请输入你要写的内容")
    b = open("1.txt","w")
    b.write("我爱学习，学习使我快乐")
    b.close()
def du():
    l = input("请输入你要读的文件")
    c = open("1.txt","r")
    d = c.read()
    print(d)
def bf():
    l = input("请输入你要备份的文件名字")
    s = open(l,"r")
    new = input("请输入备份后的文件名")
    s1 = open(l,"w")
    s1 = write(new)
    while True:
        y = s.read(1024)
        if y == "":
            break
        s.close()
        s1.close()
def cmm():
    name = input("请输入文件的名字")
    content = os.listdir(name)
    os.chdir(name)
    for i in content:
        position = i.rfind(".")
        new_name = i[:position]+"学习"+i[position:]
        os.rename(i,new_name)














