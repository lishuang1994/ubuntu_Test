def register(account,pwd):
    a = isphone(account)
    if a :
        print("呵呵呵")
def login(account,pwd):
    result = isphone(account)
    if result:
        print("哈哈哈")
def isphone(account):#判断手机号合不合法
    if len(account) == 11 and account.startswith("1"):
        return True
    else:
        return False
register(12345678912)
login(123456)
