from multiprocessing import Process
import time

def work(arg):
    for i in range(10):
        time.sleep(3)
        print("他是儿子")
p = Process(target = work,args=("哈哈",))
p.start()
p.join()
print("我是爸爸")
