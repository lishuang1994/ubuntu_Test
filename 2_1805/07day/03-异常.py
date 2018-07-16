class num(object):
    def one(self):
        n = int(input("请输入一个数字"))
        try:
            print(n+1)

        except (NameError,ValueError,FileNotFoundError):
            print("输入的不对")
        except Exception as ret:
            print(ret)
            print("不对")
        else:
            print(n+1)
a = num()
a.one()
