class student():#学生类
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
        #属性
    def upclass(self):
        print("听听课")
    def __str__(self):
        return "我的名字是%s 我的性别是%s"%(self.name,self.sex)
class manager():#管理类
    def __init__(self):
        self.list = []
    def add(self,student):
        self.list.append(student)
        for i in self.list:
            print(i)
    def remove(self):
        pass
    def update(self):
        pass
    def find(self):
        pass

class Menu():#菜单类
    def __init__(self):
        self.m = Manager()#让菜单持有管理类对象的引用
    def print_men(self):
        print("欢迎来到学生管理系统")
        while True:
            fun = int(input("请选择功能"))
            if fun == 1:
                name = input("请输入学生姓名")
                sex = input("请输入学生性别")
                s = student(name,sex)
                self.m.add(s)# m = Manager() m.add()
