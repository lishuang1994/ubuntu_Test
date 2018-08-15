import os
rpid = os.fork()
if reid < 0:
    print("fork调用失败.")
elif reip == 0:
    print("我是子进程(%s),我的父进程是(%s)"%(os.getpid(),os.getppid()))
    x+=1
else:
    print("我是父进程(%s),我的子进程是(%s)"%(os.getpid(),os.getppid()))
