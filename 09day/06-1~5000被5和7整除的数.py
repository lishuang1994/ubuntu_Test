#打印出1~5000之间能同时被5和7整除的数
for i in range(1,5000):
    if i %5 == 0 and i %7 == 0:
        print(i)
