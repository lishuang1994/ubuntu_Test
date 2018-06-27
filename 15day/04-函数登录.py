import time
def print_words():
    while True:
        i = 0
        time.sleep(1)
        print("我喜欢玩游戏")
        i+=1
        if i%2!=0:
            j()
def j():
    time.sleep(1)
    print("我喜欢打代码")
print_words()
