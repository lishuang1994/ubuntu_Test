def w1(fun):
    def inner():
        print("验证登录")
        fun()
    return inner
@w1 #test = w1(test)
def test():
    print("------------支付--------------")
#test()
#test = w1(test)
test()
