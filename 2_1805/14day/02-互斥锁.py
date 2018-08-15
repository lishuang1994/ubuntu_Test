from threading import Thread,Lock
import time


num = 0
flag = 1
def work():
    global num
    #mutex.acquire(True)#阻塞上锁
    for i in range(1000000):
        mutex.acquire(True)#阻塞上锁
        num+=1
        mutex.release()#释放锁
    print("线程一%d"%num)
def work1():
    global num #在函数内部修改全局变量要加global声明

    for i in range(1000000):
        mutex.acquire(True)
        num+=1
        mutex.release()
    print("线程二%d"%num)
mutex = Lock()
t = Thread(target=work)#创建一个线程
t1 = Thread(target=work1)
t.start()#创建启动
t1.start()
